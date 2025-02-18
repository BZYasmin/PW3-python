#Importando o Flask 
from flask import Flask

#Carregando o Flask na varável app
app = Flask(__name__)

#Criando aprimeira rota do site
@app.route('/')

#Criando função no python
def home():
    return'<h1>bem-vindo ao meu primeiro site em Flask!</h1>'


#iniciando o sevidor na localhost, porta 5000, modo de dpuração ativado
if __name__ == '__main__':
 app.run(host='localhost', port=5000, debug=True)
 
 