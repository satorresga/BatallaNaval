
from sqlalchemy import func
from .models import init_db, get_session, Usuario, Puntuacion, Partida, Tablero, Nave, Disparo

engine = init_db()
session = get_session(engine)

def get_top_players(limit=10):
    """Obtiene los mejores jugadores por puntuación total."""
    result = session.query(
        Usuario.nombre_usuario,
        func.sum(Puntuacion.puntos).label('total')
    ).join(Puntuacion).group_by(Usuario.id_usuario).order_by(func.sum(Puntuacion.puntos).desc()).limit(limit).all()
    return result

def get_user_games(username):
    """Devuelve las partidas de un usuario."""
    user = session.query(Usuario).filter_by(nombre_usuario=username).first()
    if not user:
        return []
    return session.query(Partida).filter_by(id_usuario=user.id_usuario).order_by(Partida.fecha_inicio.desc()).all()

def get_game_details(game_id):
    """Obtiene todos los datos relacionados a una partida."""
    game = session.query(Partida).get(game_id)
    if not game:
        return None

    board = session.query(Tablero).filter_by(id_partida=game_id).first()
    ships = session.query(Nave).filter_by(id_tablero=board.id_tablero).all() if board else []
    shots = session.query(Disparo).filter_by(id_partida=game_id).order_by(Disparo.fecha_hora).all()

    return {
        'partida': game,
        'tablero': board,
        'naves': ships,
        'disparos': shots
    }
