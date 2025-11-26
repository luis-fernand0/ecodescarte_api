from flask import jsonify, request
from db_config.db_conection import create_conection

def cadastrar():
    try:
        conection = create_conection()
        
        if conection:
            cursor = conection.cursor()

            data = request.form.to_dict()
            
            nome = data.get("nome")
            estado = data.get("estado")
            cidade = data.get("cidade")
            endereco = data.get("endereco")
            numero = data.get("numero")
            
            insert_query = """
                INSERT INTO pontos (nome, uf, cidade, endereco, numero)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (nome, estado, cidade, endereco, numero)

            cursor.execute(insert_query, values)
            conection.commit()

            return jsonify({"message": "Ponto de descarte cadastrado com sucesso!"}), 201

    except Exception as err:
        if err.errno == 1062:
            return jsonify({"message": f"Não foi possivel cadastrar o ponto de descarte! Já existe um ponto com esses dados"}), 409

        return jsonify({
            "message": f"Não foi possivel cadastrar o ponto de descarte! Erro: {err}"
        }), 500
    finally:
        if cursor:
            cursor.close()
        if conection:
            conection.close()