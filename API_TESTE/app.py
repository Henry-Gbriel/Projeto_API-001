from flask import Flask, jsonify, request

app = Flask(__name__)

carros =[
    {
        'id': 1,
        'montadora': 'General Motors',
        'modelo': 'Onix'
        'ano': 2025
    },
    {
        'id': 2,
        'montadora': 'Volkswagen',
        'modelo': 'Polo',
        'ano': 2025
    },
    {
        'id': 3,
        'montadora': 'Hyundai',
        'modelo': 'HB20',
        'ano': 2026

    },
    {
        'id': 4,
        'montadora': 'Fiat',
        'modelo': 'Mobi',
        'ano': 2026
    },
    {
        'id': 5,
        'montadora': 'Volkswagen',
        'modelo': 'T-Cross',
        'ano': 2026
    },
    {
        'id': 6,
        'montadora': 'Fiat',
        'modelo': 'Argo',
        'ano': 2026
    },
]

# Vamos criar os endpoints
    # GET /carros - Retorna a lista de carros
    # GET /carros/<id> - Retorna um carro específico pelo ID
    # POST /carros - Adiciona um novo carro
    # PUT /carros/<id> - Atualiza um carro existente pelo ID
    # DELETE /carros/<id> - Remove um carro pelo ID

@app.route('/carros', methods=['GET']) # Consulta 
def obter_carros():
    return jsonify(carros)

@app.rout('/carros/<int:id>', methods=['GET']) # Consulta por ID
def obter_carros_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)
        
@app.route('/carros ', methods=['POST']) # Adiciona um novo carro
def adicionar_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)
    return jsonify(novo_carro)

@app.route('/carros/<int:id>', methods=['PUT']) # Atualiza um carro existente
def atualizar_carro(id):
    carros_alterados = request.get_json()
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carros_alterados)
            return jsonify(carros[indice])
    return jsonify({'mensagem': 'Carro não encontrado'}), 404

@app.route('/carros/<int:id>', methods=['DELETE']) # Remove um carro pelo ID
def deletar_carro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]
            return jsonify({'mensagem': 'Carro deletado com sucesso'})
    return jsonify({'mensagem': 'Carro não encontrado'}), 404


app.run(port=5000, host='localhost', debug=True)