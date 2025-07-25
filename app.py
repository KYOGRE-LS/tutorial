from flask import Flask, render_template, request, jsonify
from waitress import serve

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message", "")
    resposta = responder(user_input)
    return jsonify({"response": resposta})

# Dicionário com perguntas e respostas
perguntas_respostas = {
    "oi": "Olá! Como posso ajudar você?",
    "qual é o seu nome?": "Eu sou um chatbot criado para te ajudar!",
    "como você está?": "Estou bem, obrigado por perguntar! E você?",
    "o que você faz?": "Eu sou um assistente virtual. Posso responder perguntas e ajudar com várias coisas.",
    "qual é a sua cor favorita?": "Eu sou um bot, não tenho preferências, mas adoro todas as cores!",
    "quem é o criador de você?": "Fui criado por desenvolvedores usando Python e IA!",
    "qual é o significado da vida?": "Essa é uma pergunta profunda! Dizem que o significado é 42, mas a resposta depende de cada um!",
    "meu nome é [nome]": "Prazer em te conhecer, [nome]! Como posso te ajudar?",
    "qual é a capital do Brasil?": "A capital do Brasil é Brasília.",
    "como está o tempo?": "Eu não consigo acessar informações em tempo real, mas você pode conferir a previsão do tempo no seu navegador!",
}

# Função para responder de acordo com a pergunta
def responder(pergunta):
    # Converte a pergunta para minúsculas para garantir que a comparação funcione
    pergunta = pergunta.lower()
    
    # Checa se a pergunta existe no dicionário
    resposta = perguntas_respostas.get(pergunta, "Desculpe, não entendi a sua pergunta. Pode reformular?")
    
    return resposta


if __name__ == '__main__':
    app.run()