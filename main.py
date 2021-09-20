from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def erro(e):
	return render_template('erro.html')

@app.route('/')
def inicial():
	return render_template('index.html')

@app.route('/templates/<string:pagina>')
def mostrar_paginas(pagina):
	extensao = pagina.split('.')
	extensao = extensao[1]
	if extensao=='html':
		return render_template('{}'.format(pagina))
	else:
		return render_template('erro.html')

if __name__ == '__main__':
	app.run(Debug=True)