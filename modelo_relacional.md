
# Modelo Relacional del Proyecto Batalla Naval

Este documento describe el modelo relacional del sistema **Batalla Naval**, el cual fue diseñado para gestionar usuarios, partidas, tableros, jugadas y puntajes dentro de una estructura coherente y normalizada.

## Entidades y Relaciones

### Usuario
- `id` (PK)
- `nombre_usuario`
- `contrasena`
- `puntaje`

### Partida
- `id` (PK)
- `fecha_inicio`
- `fecha_fin`
- `estado`

### Tablero
- `id` (PK)
- `id_partida` (FK a Partida)
- `id_usuario` (FK a Usuario)

### Casilla
- `id` (PK)
- `id_tablero` (FK a Tablero)
- `coordenada`
- `estado` (agua, barco, golpe, hundido)

### Jugada
- `id` (PK)
- `id_partida` (FK a Partida)
- `id_usuario` (FK a Usuario)
- `coordenada_disparo`
- `resultado`

### Relaciones:
- Un **usuario** puede jugar muchas **partidas**
- Una **partida** tiene múltiples **tableros**
- Un **tablero** contiene muchas **casillas**
- Una **jugada** está ligada a un usuario y una partida
