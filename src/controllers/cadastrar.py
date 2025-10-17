from flask import jsonify, make_response, request

def cadastrar():
    data = request.form.to_dict()
    print(data.get("nome"))
    print(data.get("cnpj"))
    print(data.get("estado"))
    print(data.get("cidade"))
    print(data.get("endereco"))
    print(data.get("numero"))
    
    return jsonify({"msg": "cheguei"})