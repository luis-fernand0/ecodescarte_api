from flask import jsonify, make_response, request
import mysql.connector
from db_config.db_conection import create_conection

def cadastrar():
    try:
        conection = create_conection()
        
        if conection:
            cursor = conection.cursor()

            data = request.form.to_dict()
            
            nome = data.get("nome")
            cnpj = data.get("cnpj")
            estado = data.get("estado")
            cidade = data.get("cidade")
            endereco = data.get("endereco")
            numero = data.get("numero")
            
            insert_query = """
                INSERT INTO pontos (nome, cnpj, estado, cidade, endereco, numero)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (nome, cnpj, estado, cidade, endereco, numero)

            cursor.execute(insert_query, values)
            conection.commit()

            return jsonify({"message": "Ponto de descarte cadastrado com sucesso!"}), 201

    except mysql.connector.Error as err:
        return jsonify({
            "message": f"Não foi possivel cadastrar o ponto de descarte! Erro: {err}"
        })
    finally:
        if cursor:
            cursor.close()
        if conection:
            conection.close()