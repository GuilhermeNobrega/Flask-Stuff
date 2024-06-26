from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/bemvindo')
def bemvindo():
  return render_template('bemvindo.html')

@app.route('/hora')
def hora():
   dh = datetime.now()
   saida_dh = dh.isoformat(" ", timespec='seconds')
   hora = dh.hour
   cumprimento = "Bom dia"
   if hora > 11 and hora < 19:
       cumprimento = "Boa tarde"
   elif hora > 18 and hora < 24:
       cumprimento = "Boa noite"

   return render_template('hora.html', data_hora=saida_dh, cumprimento=cumprimento)

if __name__ == '__main__':
	app.run(debug=1)

"""Comentários sobre o código da aplicação:

@app.route('/rota') é uma anotação, que informa ao flask, que no momento da chamada da URL com final /rota deverá rodar a função que esteja logo a seguir da anotação.
return render_template('arquivo.html') envia para o browser o conteúdo do arquivo HTML para ser interpretado.
return render_template('arquivo.html', rótulo=variável) indica que dentro do arquivo HTML existe um rótulo marcado com duas chaves {{ rótulo }}, que deve ser substituído pelo valor da variável.
"""