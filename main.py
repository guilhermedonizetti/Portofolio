from flask import Flask, render_template
from random import choice
from datetime import datetime
from pytz import timezone
from math import floor

app = Flask(__name__)

#Retorna a pagina de erro
@app.errorhandler(404)
def erro(e):
	return render_template('erro.html')

#Retorna a pagina inicial
@app.route('/')
def inicial():
	frase = frases()
	return render_template('index.html', frase=frase)

#Grencia as rotas das paginas
@app.route('/templates/<string:pagina>')
def mostrar_paginas(pagina):
	extensao = pagina.split('.')
	if extensao[1] == 'html':
		if extensao[0] == 'pessoal':
			foto = escolher_foto()
			tempo = tempo_de_experiencia()
			return render_template('{}'.format(pagina), foto=foto, tempo=tempo)
		else:
			return render_template('{}'.format(pagina))
	else:
		return render_template('erro.html')

#Seleciona randomicamente uma frase para ser exibida na pagina inicial
def frases():
	lista = [
				['O insucesso é apenas uma oportunidade para recomeçar com mais inteligência.', 'Henry Ford'],
				['Acredite que ainda não sorriu tudo e que seu coração ainda vai amar muito; acredite que o melhor da vida ainda vai chegar.', 'Desconhecido'],
				['O problema não é o problema, o problema é a sua atitude sobre o problema.','Capitão Jack Sparrow'],
				['Lute com determinação, abrace a vida com paixão, perca com classe e vença com ousadia, porque o mundo pertence a quem se atreve e a vida é muito para ser insignificante.', 'Charles Chaplin']
			]
	frase = choice(lista)
	return frase

#Seleciona rndomicamente uma foto para sre exibida na pagina de Sobre Mim
def escolher_foto():
	lista = ['eu_1', 'eu_2', 'eu_2', 'eu_3', 'eu_2', 'eu_2']
	foto = choice(lista)

	return foto

#Calcula a diferenca de datas para dizer automaticamente o tempo de experiencia
def tempo_de_experiencia():
	inicio_trabalho = datetime(2021, 12, 1)
	fuso = timezone('America/Sao_Paulo')
	data_atualmente = str(datetime.now().astimezone(fuso)).split(" ")
	data_atualmente = data_atualmente[0].split("-")
	data_atualmente =  datetime(int(data_atualmente[0]), int(data_atualmente[1]), int(data_atualmente[2]))
	dias = data_atualmente - inicio_trabalho
	dias = int(str(dias).split(" ")[0])

	if dias >= 30:
		mes = floor(dias / 30)
		tempo = "{} meses".format(mes)
	else:
		tempo = "{} dias".format(dias)

	return tempo

#Inicializa
if __name__ == '__main__':
	app.run()