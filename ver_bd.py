import sqlite3

conn = sqlite3.connect("database/batalla_naval.db")
cursor = conn.cursor()

# Mostrar nombres de tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("📋 Tablas encontradas:")
for table in tables:
    print("-", table[0])

# Mostrar columnas de una tabla
for table in tables:
    print(f"\n📑 Esquema de '{table[0]}':")
    cursor.execute(f"PRAGMA table_info({table[0]});")
    for col in cursor.fetchall():
        print(" ", col)
