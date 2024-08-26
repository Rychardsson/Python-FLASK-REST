from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo (simulando um banco de dados)
items = [
    {'id': 1, 'name': 'Item 1', 'description': 'Descrição do Item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'Descrição do Item 2'},
    {'id': 3, 'name': 'Item 3', 'description': 'Descrição do Item 3'}
]

# Rota para obter todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Rota para obter um item específico pelo ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item não encontrado'}), 404

# Rota para criar um novo item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        data = request.get_json()
        item.update(data)
        return jsonify(item)
    else:
        return jsonify({'error': 'Item não encontrado'}), 404

# Rota para deletar um item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deletado'}), 204

if __name__ == '__main__':
    app.run(debug=True)
