from flask import Flask, render_template, request, redirect, url_for, abort
import requests

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# search post route
@app.route('/post', methods = ['POST'])
def post():
    pokemon = request.form['nama_pokemon']
    pokemon = pokemon.lower()
    return redirect(url_for('hasil', nama = pokemon))

# show result route if success
@app.route('/hasil/<string:nama>')
def hasil(nama):
    url = 'https://pokeapi.co/api/v2/pokemon/'+nama
    pokemons = requests.get(url)
    if str(pokemons) == '<Response [404]>':
        abort(404)
    else:
        return render_template('hasil.html', x = pokemons)

# show error not found
@app.errorhandler(404)
def error(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True)

# due to my Mac Error, I need to run program with this:
# FLASK_APP=ujian_cari_pokemon.py FLASK_DEBUG=1 flask run