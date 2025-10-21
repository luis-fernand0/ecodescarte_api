from flask import jsonify, make_response, request
import requests
import mysql.connector
from db_config.db_conection import create_conection

def get_pontos():
    try:
        conection = create_conection()
        if not conection:
            return jsonify({"message": "Não foi possivel se conectar com o banco"}), 500
        cursor = conection.cursor(dictionary=True)

        cep = request.args.get('cep')
        cep = cep.replace("-", "")

        url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
        response = requests.get(url)
        dados = response.json()

        if response.status_code != 200:
            return jsonify ({
                "message": f"Não encontramos nenhuma correspondecia com o CEP informado! {dados["message"]}",
                "erro": dados["type"] 
                }), response.status_code

        select_query = """
            SELECT * FROM pontos WHERE cidade = %s
        """
        values = dados["city"]

        cursor.execute(select_query, (values,))
        resultados = cursor.fetchall()

        if len(resultados) == 0:
            return jsonify({"data": [], "message": "Não encontramos nenhum ponto de descarte proximo ao CEP informado"}), 200

        return jsonify({"data": resultados}), 200
    except:
        return jsonify({"message": "Não foi possivel buscar os pontos de descarte"}), 500
    finally:
        if cursor:
            cursor.close()
        if conection:
            conection.close()
