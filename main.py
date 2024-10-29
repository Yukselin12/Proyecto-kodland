from flask import Flask, send_file
import random
import os

app = Flask(__name__)

# Lista de frases sobre la dependencia tecnológica
waza = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna.",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos.",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas."
]

@app.route("/")                    
def hello_world():
    return '<h1>WAAAAAAZAAAAAAAAAAA!!!</h1><a href="/8">Ver datos de Don pollo</a> <style>a:hover{color: blue; transition: 1s;}a{transition: 1s;}</style>'

@app.route("/8")                          
def dato_de_Don_pollo():
    return f'<h2>{random.choice(waza)}</h2> <a href="/">Regresar a ver los datos de don pollo</a>'

@app.route("/eldonpollo")
def Waza():
    meme_alet = random.choice(os.listdir("images_gatitos"))
    return send_file(f'images_gatitos/{meme_alet}', mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
