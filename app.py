from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Pequeno Principe',
        'autor': 'Antoine de Saint-Exupéry'
    },
    {
        'id': 2,
        'título': 'A Sutil Arte de Ligar o Foda-se',
        'autor': 'Mark Manson'
    },
    {
        'id': 3,
        'título': 'Por Lugares Incriveis',
        'autor': 'Jennifer Niven'
    },
]

#Função para consultar todos os livros armazenados
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Função Consulta
@app.route('/livros/<int:id>',methods=['GET'])
def consulta_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Função Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_por_id(id):
    livro_alt = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alt)
            return jsonify(livros[indice])

#Função para Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir um Livro
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)