import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS maquina (id INTEGER PRIMARY KEY, tiempo text, volumen text, productividad text, rendimient text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM maquina")
        rows = self.cur.fetchall()
        return rows

    def insert(self, tiempo, volumen, productividad, rendimiento):
        self.cur.execute("INSERT INTO maquina VALUES (NULL, ?, ?, ?, ?)", (tiempo, volumen, productividad, rendimiento))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM maquina WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, tiempo, volumen, productividad, rendimiento):
        self.cur.execute("UPDATE maquina SET tiempo = ?, volumen = ?, productividad = ?, rendimiento = ? WHERE id = ?", (tiempo, volumen, productividad, rendimiento, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()