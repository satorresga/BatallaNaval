
from sqlalchemy import (
    create_engine, Column, Integer, String, Boolean,
    ForeignKey, DateTime
)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String, unique=True, nullable=False)
    clave_hash = Column(String, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now)

    partidas = relationship("Partida", back_populates="usuario")
    puntuaciones = relationship("Puntuacion", back_populates="usuario")

class Partida(Base):
    __tablename__ = 'partidas'
    id_partida = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    fecha_inicio = Column(DateTime, default=datetime.now)
    fecha_fin = Column(DateTime)
    resultado = Column(String)

    usuario = relationship("Usuario", back_populates="partidas")
    puntuaciones = relationship("Puntuacion", back_populates="partida")
    tableros = relationship("Tablero", back_populates="partida")
    disparos = relationship("Disparo", back_populates="partida")

class Puntuacion(Base):
    __tablename__ = 'puntuaciones'
    id_puntuacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_partida = Column(Integer, ForeignKey('partidas.id_partida'))
    puntos = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.now)

    usuario = relationship("Usuario", back_populates="puntuaciones")
    partida = relationship("Partida", back_populates="puntuaciones")

class Tablero(Base):
    __tablename__ = 'tableros'
    id_tablero = Column(Integer, primary_key=True)
    id_partida = Column(Integer, ForeignKey('partidas.id_partida'))
    ancho = Column(Integer, nullable=False)
    alto = Column(Integer, nullable=False)

    partida = relationship("Partida", back_populates="tableros")
    naves = relationship("Nave", back_populates="tablero")

class Nave(Base):
    __tablename__ = 'naves'
    id_nave = Column(Integer, primary_key=True)
    id_tablero = Column(Integer, ForeignKey('tableros.id_tablero'))
    tamaño = Column(Integer, nullable=False)
    hundida = Column(Boolean, default=False)

    tablero = relationship("Tablero", back_populates="naves")
    posiciones = relationship("PosicionNave", back_populates="nave")

class PosicionNave(Base):
    __tablename__ = 'posiciones_naves'
    id_posicion = Column(Integer, primary_key=True)
    id_nave = Column(Integer, ForeignKey('naves.id_nave'))
    fila = Column(Integer, nullable=False)
    columna = Column(Integer, nullable=False)
    impactada = Column(Boolean, default=False)

    nave = relationship("Nave", back_populates="posiciones")

class Disparo(Base):
    __tablename__ = 'disparos'
    id_disparo = Column(Integer, primary_key=True)
    id_partida = Column(Integer, ForeignKey('partidas.id_partida'))
    fila = Column(Integer, nullable=False)
    columna = Column(Integer, nullable=False)
    resultado = Column(String, nullable=False)
    fecha_hora = Column(DateTime, default=datetime.now)

    partida = relationship("Partida", back_populates="disparos")

# Configuración
def init_db():
    engine = create_engine('sqlite:///database/batalla_naval.db')
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
