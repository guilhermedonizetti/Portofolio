from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.errorhandler(404)
def erro(e):
	return render_template('erro.html')

@app.route('/')
def inicial():
	frase = frases()
	return render_template('index.html', frase=frase)

@app.route('/templates/<string:pagina>')
def mostrar_paginas(pagina):
	extensao = pagina.split('.')
	extensao = extensao[1]
	if extensao=='html':
		return render_template('{}'.format(pagina))
	else:
		return render_template('erro.html')

def frases():
	lista = [
				['O insucesso é apenas uma oportunidade para recomeçar com mais inteligência.', 'Henry Ford'],
				['Acredite que ainda não sorriu tudo e que seu coração ainda vai amar muito; acredite que o melhor da vida ainda vai chegar.', 'Desconhecido'],
				['O problema não é o problema, o problema é a sua atitude sobre o problema.','Capitão Jack Sparrow']
			]
	frase = choice(lista)
	return frase

if __name__ == '__main__':
	app.run()