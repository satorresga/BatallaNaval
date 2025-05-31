
# Ejemplos de consultas ORM usando SQLAlchemy

# Obtener todos los usuarios
usuarios = session.query(Usuario).all()

# Buscar un usuario por nombre
usuario = session.query(Usuario).filter_by(nombre_usuario='player1').first()

# Crear una nueva partida
nueva_partida = Partida(fecha_inicio=datetime.now(), estado='en curso')
session.add(nueva_partida)
session.commit()

# Agregar tablero a una partida
tablero = Tablero(id_partida=nueva_partida.id, id_usuario=usuario.id)
session.add(tablero)
session.commit()

# Registrar una jugada
jugada = Jugada(id_partida=nueva_partida.id, id_usuario=usuario.id, coordenada_disparo='B4', resultado='agua')
session.add(jugada)
session.commit()

# Consultar jugadas de una partida
jugadas = session.query(Jugada).filter_by(id_partida=nueva_partida.id).all()
