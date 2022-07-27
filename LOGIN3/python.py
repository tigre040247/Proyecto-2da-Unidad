#importamos la libreria Flask
from flask import Flask, render_template



app = Flask(__name__, template_folder='templates')



#---------------------------------------
#Ruta de pagina alumnos
#---------------------------------------


@app.route('/')
def alumnos():
    return render_template('/alumnos.html')

#---------------------------------------
#Ruta de pagina inicio 
#---------------------------------------


@app.route('/inicio')
def inicio():
    return render_template('/inicio.html')

#---------------------------------------
#Ruta de pagina Docentes
#---------------------------------------
@app.route('/Docentes')
def Docentes():
    return render_template('/Docentes.html')

#---------------------------------------
#Ruta de pagina index
#---------------------------------------


@app.route('/index')
def index():
    return render_template('/index.html')




#---------------------------------------
#Ruta de pagina loginD
#---------------------------------------
@app.route('/loginD')
def loginD():
    return render_template('/loginD.html')

#---------------------------------------
#Ruta de pagina opciones
#---------------------------------------

@app.route('/opciones')
def opciones():
    return render_template('/opciones.html')


#---------------------------------------
#Ruta de pagina paralelos
#---------------------------------------

@app.route('/paralelos')
def paralelos():
    return render_template('/paralelos.html')


#---------------------------------------
#Ruta de pagina paralelos
#---------------------------------------

@app.route('/Juegos/memory-game-master/indexj')
def juegoUno():
    return render_template('/Juegos/memory-game-master/indexj.html')



#---------------------------------------
#iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
