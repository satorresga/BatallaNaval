from database.models import Usuario, Partida, Tablero, Nave, Disparo

def get_user_games(session, username):
    """
    Retorna todas las partidas asociadas a un usuario por nombre.

    :param session: Sesión activa de SQLAlchemy
    :param username: Nombre de usuario
    :return: Lista de objetos Partida
    """
    user = session.query(Usuario).filter_by(nombre_usuario=username).first()
    if not user:
        return []
    return session.query(Partida)\
        .filter_by(id_usuario=user.id_usuario)\
        .order_by(Partida.fecha_inicio.desc())\
        .all()


def get_game_details(session, game_id):
    """
    Obtiene todos los datos relacionados a una partida: tablero, naves y disparos.

    :param session: Sesión activa de SQLAlchemy
    :param game_id: ID de la partida
    :return: Diccionario con detalles de la partida
    """
    game = session.query(Partida).get(game_id)
    if not game:
        return None

    board = session.query(Tablero).filter_by(id_partida=game_id).first()
    ships = session.query(Nave).filter_by(id_tablero=board.id_tablero).all() if board else []
    shots = session.query(Disparo).filter_by(id_partida=game_id)\
        .order_by(Disparo.fecha_hora.asc()).all()

    return {
        'partida': game,
        'tablero': board,
        'naves': ships,
        'disparos': shots
    }
