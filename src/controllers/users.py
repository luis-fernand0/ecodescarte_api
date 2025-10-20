from flask import jsonify, make_response, request
import requests
import mysql.connector
from db_config.db_conection import create_conection

def get_users():
    try:
        cep = request.args.get('cep')
        cep = cep.replace("-", "")

        url = f"https://brasilapi.com.br/api/cep/v1/{cep}"

        response = requests.get(url)
        dados = response.json()

        conection = create_conection()

        if not conection:
            return jsonify({"message": "Não foi possivel se conectar com o banco"}), 500
        
        cursor = conection.cursor()

        select_query = """
            SELECT * FROM pontos WHERE cidade = %s
        """
        values = dados["city"]

        cursor.execute(select_query, (values,))
        resultados = cursor.fetchall()

        print(resultados)

        return jsonify({"message": "Cheguei aqui"}), 200
    except:
        return jsonify({"message": "Não foi possivel buscar os pontos de descarte"}), 500
    finally:
        if cursor:
            cursor.close()
        if conection:
            conection.close()
