from flask import Flask, render_template, request, send_from_directory, redirect, url_for, jsonify
import requests

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# search route
@app.route('/post', methods = ['POST'])
def post():
    url_base = 'https://pokeapi.co/api/v2/pokemon/'
    database = requests.get(url_base)
    list_pokemons = database.json()['results']
    pokemon = request.form['nama_pokemon']

    i = 0
    while i <= len(list_pokemons)-1:
        if pokemon in list_pokemons[i]['name']:
            return redirect(url_for('hasil', nama = pokemon))
        # else: still can't figure out how to go to the next page
        #     i += 1
        #     limit = 20
        #     url_next = 'https://pokeapi.co/api/v2/pokemon/?offset='+limit+'&limit=20'
        #     database_next = requests.get(url_next)
        #     list_pokemons_next = database_next.json()['results']
            
        #     j = 0
        #     while j <= len(list_pokemons_next):
        #         if pokemon in list_pokemons[j]['name']:
        #             return redirect(url_for('hasil', nama = pokemon))
        #         else:
        #             j += 1
        #             limit += 20
        elif i == len(list_pokemons)-1:
            return render_template('error.html')
        else:
            i += 1

@app.route('/hasil/<string:nama>')
def hasil(nama):
    url = 'https://pokeapi.co/api/v2/pokemon/'+nama
    pokemons = requests.get(url)
    return render_template('hasil.html', x = pokemons)

if __name__ == '__main__':
    app.run(debug = True)

# due to my Mac Error, I need to run program with this:
# FLASK_APP=ujian_cari_pokemon.py FLASK_DEBUG=1 flask run