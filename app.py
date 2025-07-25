from flask import Flask, render_template, request, jsonify

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
      "o que é informática?": "É a ciência que estuda o processamento, armazenamento e transmissão de informações por meio de computadores.",
  "o que é um computador?": "É uma máquina capaz de processar dados de acordo com instruções pré-definidas.",
  "o que é hardware?": "É a parte física do computador, como monitor, teclado, mouse, placa-mãe, etc.",
  "o que é software?": "São os programas e sistemas que rodam no computador.",
  "qual a diferença entre hardware e software?": "Hardware é a parte física, e software é a parte lógica (os programas).",
  "o que é CPU?": "É a unidade central de processamento, o 'cérebro' do computador.",
  "para que serve a memória RAM?": "Serve para armazenar dados temporários enquanto o computador está ligado.",
  "o que é ROM?": "É a memória somente de leitura, onde ficam dados essenciais para o funcionamento inicial do computador.",
  "o que é disco rígido (HD)?": "É o dispositivo onde os dados são armazenados permanentemente.",
  "o que é SSD?": "É um tipo de armazenamento mais rápido que o HD tradicional.",
  "o que é sistema operacional?": "É o software que gerencia o hardware e os outros programas do computador.",
  "o que é Windows?": "É um sistema operacional criado pela Microsoft.",
  "o que é Linux?": "É um sistema operacional de código aberto.",
  "o que é macOS?": "É o sistema operacional dos computadores Apple.",
  "o que é um arquivo?": "É um conjunto de dados armazenados em disco com um nome e extensão.",
  "o que é uma pasta?": "É um local para armazenar e organizar arquivos.",
  "o que é extensão de arquivo?": "É o sufixo que indica o tipo de arquivo, como .txt, .jpg, .docx.",
  "o que é um navegador?": "É o programa usado para acessar sites na internet, como Chrome ou Firefox.",
  "o que é a internet?": "É uma rede mundial de computadores interligados.",
  "o que é WWW?": "Significa World Wide Web, é o sistema de navegação por sites e páginas.",
  "o que é URL?": "É o endereço de um site na internet.",
  "o que é Wi-Fi?": "É uma tecnologia de rede sem fio.",
  "o que é LAN?": "É uma rede local de computadores, geralmente usada em casas ou escritórios.",
  "o que é IP?": "É o número que identifica um dispositivo em uma rede.",
  "o que é antivírus?": "É um software que protege o computador contra vírus e malwares.",
  "o que é malware?": "É qualquer software malicioso, como vírus, trojans e ransomwares.",
  "o que é firewall?": "É um sistema de segurança que controla o tráfego de dados em uma rede.",
  "o que é backup?": "É uma cópia de segurança dos dados.",
  "o que é nuvem (cloud)?": "É um serviço que armazena dados na internet.",
  "o que é Google Drive?": "É um serviço de armazenamento em nuvem do Google.",
  "o que é processador?": "É o componente que executa as instruções dos programas.",
  "o que é placa-mãe?": "É a principal placa de circuito do computador, onde todos os componentes se conectam.",
  "o que é placa de vídeo?": "É responsável pelo processamento gráfico no computador.",
  "o que é resolução de tela?": "É a quantidade de pixels que compõem a imagem da tela.",
  "o que é pixel?": "É o menor ponto que compõe uma imagem digital.",
  "o que é HDMI?": "É um tipo de conexão de áudio e vídeo digital.",
  "o que é USB?": "É uma interface usada para conectar periféricos ao computador.",
  "o que é periférico?": "São os dispositivos conectados ao computador, como teclado e mouse.",
  "o que é um mouse?": "É um dispositivo de entrada usado para mover o cursor na tela.",
  "o que é um teclado?": "É um dispositivo de entrada usado para digitar textos e comandos.",
  "o que é impressora?": "É um dispositivo de saída que imprime documentos.",
  "o que é scanner?": "É um dispositivo que digitaliza documentos físicos para o computador.",
  "o que é monitor?": "É o dispositivo de saída que exibe as imagens do computador.",
  "o que é bit?": "É a menor unidade de informação digital, representando 0 ou 1.",
  "o que é byte?": "É um conjunto de 8 bits.",
  "quantos bytes tem 1 KB?": "1 KB tem 1.024 bytes.",
  "quantos KB tem 1 MB?": "1 MB tem 1.024 KB.",
  "quantos MB tem 1 GB?": "1 GB tem 1.024 MB.",
  "o que é programação?": "É o processo de escrever instruções para o computador executar.",
  "o que é algoritmo?": "É uma sequência de passos para resolver um problema.",
  "o que é linguagem de programação?": "É uma linguagem usada para criar programas de computador.",
  "o que é Python?": "É uma linguagem de programação simples e poderosa.",
  "o que é Java?": "É uma linguagem de programação muito usada em aplicativos e sistemas corporativos.",
  "o que é HTML?": "É a linguagem de marcação usada para criar páginas web.",
  "o que é CSS?": "É a linguagem usada para definir o estilo visual das páginas web.",
  "o que é JavaScript?": "É a linguagem de programação usada para deixar páginas web interativas.",
  "o que é banco de dados?": "É um sistema usado para armazenar e organizar informações.",
  "o que é SQL?": "É uma linguagem usada para manipular bancos de dados.",
  "o que é servidor?": "É um computador que fornece serviços para outros dispositivos em rede.",
  "o que é cliente?": "É o dispositivo que acessa serviços de um servidor.",
  "o que é rede de computadores?": "É o conjunto de dispositivos interligados para compartilhar dados.",
  "o que é domínio?": "É o nome de um site, como google.com.",
  "o que é DNS?": "É o sistema que traduz nomes de domínio em endereços IP.",
  "o que é HTTP?": "É o protocolo usado para acessar páginas da web.",
  "o que é HTTPS?": "É a versão segura do HTTP, com criptografia.",
  "o que é login?": "É o processo de entrar em uma conta com usuário e senha.",
  "o que é logout?": "É o processo de sair de uma conta ou sistema.",
  "o que é senha forte?": "É uma senha difícil de adivinhar, com letras, números e símbolos.",
  "o que é phishing?": "É uma tentativa de enganar o usuário para roubar dados pessoais.",
  "o que é spam?": "São mensagens eletrônicas indesejadas, geralmente com fins comerciais.",
  "o que é IoT?": "É a Internet das Coisas: dispositivos conectados entre si pela internet.",
  "o que é inteligência artificial?": "É a simulação da inteligência humana por máquinas.",
  "o que é criptografia?": "É a técnica de codificar dados para protegê-los.",
  "o que é um sistema embarcado?": "É um sistema computacional integrado em dispositivos específicos.",
  "o que é um bug?": "É um erro ou falha em um programa.",
  "o que é atualização de software?": "É uma nova versão do programa com melhorias ou correções.",
  "o que é um aplicativo?": "É um software criado para executar tarefas específicas.",
  "o que é mobile?": "É o termo usado para dispositivos móveis, como smartphones e tablets.",
  "o que é sistema binário?": "É o sistema numérico baseado em 0 e 1, usado pelos computadores.",
  "o que é multitarefa?": "É a capacidade de executar vários processos ao mesmo tempo.",
  "o que é formatação de disco?": "É o processo de preparar um disco para uso, apagando tudo nele.",
  "o que é overclock?": "É forçar o processador a trabalhar além de sua velocidade padrão.",
  "o que é código-fonte?": "É o conjunto de instruções escritas em linguagem de programação.",
  "o que é open source?": "É um software com código aberto, que pode ser modificado por qualquer um.",
  "o que é licença de software?": "É o contrato que define como um software pode ser usado.",
  "o que é drive?": "É o software que permite o funcionamento de dispositivos de hardware.",
  "o que é BIOS?": "É o sistema básico de entrada e saída do computador, ativado na inicialização.",
  "o que é boot?": "É o processo de inicialização do computador.",
  "o que é virtualização?": "É a criação de ambientes virtuais dentro de um computador real.",
  "o que é PDF?": "É um formato de documento portátil, que mantém o layout original.",
  "o que é compactação de arquivos?": "É o processo de reduzir o tamanho dos arquivos.",
  "o que é ZIP ou RAR?": "São formatos usados para compactar arquivos.",
  "o que é formatação de texto?": "É aplicar estilos como negrito, itálico e sublinhado.",
  "o que é planilha eletrônica?": "É um programa como Excel, usado para cálculos e gráficos.",
  "o que é apresentação de slides?": "É um conjunto de telas usadas para mostrar conteúdo, como no PowerPoint.",
  "obrigado": "De nada! Sempre à disposição.",
  "valeu": "Tamo junto! 😊",
  "tchau": "Até logo! Volte sempre!",
  "até mais": "Até mais! Cuide-se!",
  "bye": "Bye bye! 👋"
}

# Função para responder de acordo com a pergunta
def responder(pergunta):
    # Converte a pergunta para minúsculas para garantir que a comparação funcione
    pergunta = pergunta.lower()
    
    # Checa se a pergunta existe no dicionário
    resposta = perguntas_respostas.get(pergunta, "Desculpe, não entendi a sua pergunta. Pode reformular?")
    
    return resposta


if __name__ == '__main__':
    app.run()from flask import Flask, render_template, request, jsonify
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
