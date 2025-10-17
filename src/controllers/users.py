from flask import jsonify, make_response

pontos = [
    {
        'id': 1,
        'nome': 'Centro de reciclagem 1',
        'endereco': 'Rua exemplo, jardim exemplo, 000, EXEMPLO-EX',
        'funcionamento': 'Seg a Sab'
    },
    {
        'id': 2,
        'nome': 'Centro de reciclagem 2',
        'endereco': 'Rua exemplo, jardim exemplo, 000, EXEMPLO-EX',
        'funcionamento': 'Seg a Sex'
    },
    {
        'id': 3,
        'nome': 'Centro de reciclagem 3',
        'endereco': 'Rua exemplo, jardim exemplo, 000, EXEMPLO-EX',
        'funcionamento': 'Seg a Dom'
    }
]

def get_users():
    response = make_response(jsonify(pontos), 200)
    return response