
-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT UNIQUE NOT NULL,
    clave_hash TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de partidas
CREATE TABLE IF NOT EXISTS partidas (
    id_partida INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_fin TIMESTAMP,
    resultado TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Tabla de puntuaciones
CREATE TABLE IF NOT EXISTS puntuaciones (
    id_puntuacion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_partida INTEGER NOT NULL,
    puntos INTEGER NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_partida) REFERENCES partidas(id_partida)
);

-- Tabla de tableros
CREATE TABLE IF NOT EXISTS tableros (
    id_tablero INTEGER PRIMARY KEY AUTOINCREMENT,
    id_partida INTEGER NOT NULL,
    ancho INTEGER NOT NULL,
    alto INTEGER NOT NULL,
    FOREIGN KEY (id_partida) REFERENCES partidas(id_partida)
);

-- Tabla de naves
CREATE TABLE IF NOT EXISTS naves (
    id_nave INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tablero INTEGER NOT NULL,
    tamaño INTEGER NOT NULL,
    hundida BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_tablero) REFERENCES tableros(id_tablero)
);

-- Tabla de posiciones de naves
CREATE TABLE IF NOT EXISTS posiciones_naves (
    id_posicion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_nave INTEGER NOT NULL,
    fila INTEGER NOT NULL,
    columna INTEGER NOT NULL,
    impactada BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_nave) REFERENCES naves(id_nave)
);

-- Tabla de disparos
CREATE TABLE IF NOT EXISTS disparos (
    id_disparo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_partida INTEGER NOT NULL,
    fila INTEGER NOT NULL,
    columna INTEGER NOT NULL,
    resultado TEXT NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_partida) REFERENCES partidas(id_partida)
);
