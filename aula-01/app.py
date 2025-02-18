#Importando o Flask 
from flask import Flask, render_template

#Carregando o Flask na varável app
app = Flask(__name__, template_folder='views')

#Criando aprimeira rota do site
@app.route('/')

#Criando função no python
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    título = 'CS-GO'
    ano = 2012
    categoria = 'FPS Online'
    jogadores = ['Julia' , 'eu']
    jogos = ['Minecraft', 'Freefire', 'Amongus', 'GTA', 'Pokemon', 'Roblox' ] 
    return render_template('games.html', título=título, ano=ano, categoria=categoria, jogadores=jogadores, jogos=jogos)


#iniciando o sevidor na localhost, porta 5000, modo de dpuração ativado
if __name__ == '__main__':
 app.run(host='localhost', port=5000, debug=True)
 
 