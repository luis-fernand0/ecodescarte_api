from flask import jsonify, request
from utils.buscar_cep import buscar_cep
from db_config.db_conection import create_conection

def get_pontos():
    try:
        conection = create_conection()
        if not conection:
            return jsonify({"message": "Não foi possivel se conectar com o banco"}), 500
        cursor = conection.cursor(dictionary=True)

        cep = request.args.get('cep')
        cep = cep.replace("-", "")

        dados = buscar_cep(cep)

        if not dados['success']:
            return jsonify(dados)
        
        cidade = ''
        if 'city' in dados['data']:
            cidade = dados['data']['city']
        else:
            cidade = dados['data']['localidade']
            
        select_query = """
            SELECT * FROM pontos WHERE cidade = %s
        """
        
        cursor.execute(select_query, (cidade,))
        resultados = cursor.fetchall()

        if len(resultados) == 0:
            return jsonify({"data": [], "message": "Não encontramos nenhum ponto de descarte proximo ao CEP informado"}), 200

        return jsonify({"data": resultados}), 200
    except Exception as err:
        return jsonify({
            "data": [],
            "message": f"Não foi possivel buscar os pontos de descarte! Erro: {err}"
            }), 500
    finally:
        if cursor:
            cursor.close()
        if conection:
            conection.close()
