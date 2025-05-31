import sys
import os
from flask import Flask, render_template, request, redirect, url_for, session as flask_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Configuración de paths
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))

# Importaciones locales
from src.autenticacion.gestion_usuarios_orm import GestionUsuariosORM
from src.juego.juego import Juego
from database.models import init_db
from database.queries import get_user_games, get_game_details

# Flask App
app = Flask(__name__)
app.secret_key = 'secreto_seguro'

# Base de datos
engine = init_db()
Session = sessionmaker(bind=engine)
db_session = Session()
gestor_usuarios = GestionUsuariosORM(db_session)

# Diccionario de juegos en memoria por usuario
juegos_activos = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            try:
                gestor_usuarios.registrar_usuario(username, password)
                return redirect(url_for('home'))
            except Exception as e:
                return render_template('error.html', error=str(e))
    return render_template('registro.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if gestor_usuarios.autenticar_usuario(username, password):
        flask_session['usuario'] = username
        return redirect(url_for('jugar'))
    else:
        return render_template('error.html', error='Credenciales inválidas')

@app.route('/logout')
def logout():
    flask_session.pop('usuario', None)
    return redirect(url_for('home'))

@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    usuario = flask_session.get('usuario')
    if not usuario:
        return redirect(url_for('home'))

    if usuario not in juegos_activos:
        juegos_activos[usuario] = Juego(8, 8, gestor_usuarios, usuario)

    juego = juegos_activos[usuario]
    mensaje = ''
    tablero = juego.tablero.representacion()

    if request.method == 'POST':
        fila = int(request.form.get('fila')) -1
        columna = int(request.form.get('columna')) -1
        mensaje = juego.disparar(fila, columna)
        tablero = juego.tablero.representacion()
        estado = juego.verificar_estado()
        if estado != "El juego continúa":
            mensaje += f" - {estado}"

    return render_template('juego.html', usuario=usuario, tablero=tablero, mensaje=mensaje)

@app.route('/puntajes/<username>')
def puntajes(username):
    try:
        juegos = get_user_games(db_session, username)
        return render_template('puntajes.html', username=username, juegos=juegos)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/detalle/<int:game_id>')
def detalle(game_id):
    try:
        datos = get_game_details(db_session, game_id)
        return render_template('detalle.html', datos=datos)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="Página no encontrada"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error="Error interno del servidor"), 500

if __name__ == '__main__':
    app.run(debug=True)
