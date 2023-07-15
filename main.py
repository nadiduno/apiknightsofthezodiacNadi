import pandas as pd
from flask import Flask, jsonify

url = "https://raw.githubusercontent.com/nadiduno/apiknightsofthezodiac/main/DataBaseknightsofthezodiac.csv"

app = Flask(__name__)


@app.route('/')
def homepage():
  date_zodic = pd.read_csv(url)
  answer = {'date_zodic': date_zodic.to_json()}
  return (jsonify(answer))

# Criando Rota
# @app.route('/nadi')
# def api():
#   return ('API')


app.run(host='0.0.0.0')
