
CREATE TABLE Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    puntaje INTEGER DEFAULT 0
);

CREATE TABLE Partida (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_inicio DATETIME NOT NULL,
    fecha_fin DATETIME,
    estado TEXT CHECK(estado IN ('en curso', 'finalizada')) NOT NULL
);

CREATE TABLE Tablero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_partida INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_partida) REFERENCES Partida(id),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
);

CREATE TABLE Casilla (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tablero INTEGER NOT NULL,
    coordenada TEXT NOT NULL,
    estado TEXT CHECK(estado IN ('agua', 'barco', 'golpe', 'hundido')) NOT NULL,
    FOREIGN KEY (id_tablero) REFERENCES Tablero(id)
);

CREATE TABLE Jugada (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_partida INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    coordenada_disparo TEXT NOT NULL,
    resultado TEXT CHECK(resultado IN ('agua', 'tocado', 'hundido')) NOT NULL,
    FOREIGN KEY (id_partida) REFERENCES Partida(id),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
);
