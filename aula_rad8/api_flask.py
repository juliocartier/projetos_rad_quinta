from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', nome="Maria", lista=["Maça", "Banana", "Uva"])

@app.route('/pagina_ast')
def pagina_ast():
    return render_template('pagina_astronomia.html')

@app.route("/inicio", methods=['GET'])
def index():
    return "Ola mundo!!!!"

@app.route("/usuarios", methods=['GET'])
def listar_usuarios():
    return jsonify([{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Cynthia"}])

@app.route("/usuarios", methods=['POST'])
def criar_usuario():
    dados = request.json
    return jsonify({"mensagem": "Usuario criado", "dados": dados}), 201

if __name__ == '__main__':
    #app.run(debug=True, host="127.0.1.27", port=9000)
    app.run(debug=True)