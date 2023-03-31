import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS maquina (id INTEGER PRIMARY KEY, excavadora text, cuchara text, material text, eactual text, econvertido text, capacidad text, rendimiento text)")
        
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM maquina")
        rows = self.cur.fetchall()
        return rows

    # def smallfetch(self):
    #     self.cur.execute("SELECT id, excavadora, cuchara, productividad, rendimiento FROM maquina")
    #     rows = self.cur.fetchall()
    #     return rows

    # def fetchtiempocarga(self, id):
    #     self.cur.execute("SELECT tiempocarga FROM maquina WHERE id = ?", (id,))
    #     rows = self.cur.fetchone()[0]
    #     return rows

    # def fetchcapacidadneta(self, id):
    #     self.cur.execute("SELECT capacidadneta FROM maquina WHERE id = ?", (id,))
    #     rows = self.cur.fetchone()[0]
    #     return rows

    def insert(self, excavadora, cuchara, material, eactual, econvertido, capacidad, rendimiento):
        self.cur.execute("INSERT INTO maquina VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (excavadora, cuchara, material, eactual, econvertido, capacidad, rendimiento))
        self.conn.commit()

    # def insertartiempocarga(self, id, excavadora, excavacion, balanceo, carga, tiempocarga, cuchara, capacidadcuchara, eficiencia, capacidadneta):
    #     self.cur.execute("UPDATE maquina SET excavadora = ?, excavacion = ?, balanceo = ?, carga = ?, tiempocarga = ?, cuchara = ?, capacidadcuchara = ?, eficiencia = ?, capacidadneta = ? WHERE id = ?", (excavadora, excavacion, balanceo, carga, tiempocarga, cuchara, capacidadcuchara, eficiencia, capacidadneta, id))
    #     self.conn.commit()

    # def insertarexcava(self, id, alto, ancho, largo, volumen, sobreexcavacion, tiempoalquiler, numerocicloshora, productividad, rendimiento):
    #     self.cur.execute("UPDATE maquina SET alto = ?, ancho = ?, largo = ?, volumen = ?, sobreexcavacion = ?, tiempoalquiler = ?, numerocicloshora = ?, productividad = ?, rendimiento = ? WHERE id = ?", (alto, ancho, largo, volumen, sobreexcavacion, tiempoalquiler, numerocicloshora, productividad, rendimiento, id))
    #     self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM maquina WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, excavadora, cuchara, material, eactual, econvertido, capacidad, rendimiento):
        self.cur.execute("UPDATE maquina SET excavadora = ?, cuchara = ?, material = ?, eactual = ?, econvertido = ?, capacidad = ?, rendimiento = ? WHERE id = ?", (excavadora, cuchara, material, eactual, econvertido, capacidad, rendimiento, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# db = Database('maq.db')
# db.insert("Doosan DX225LCA", "Cucharon de uso general", "Arcilla", "ES (3)", "Natural", "1.34", "24.4")



# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")
# db.insert("1", "1", "1", "1", "1", "1", "4")
# db.insert("2", "2", "2", "2", "2", "2", "4")
# db.insert("3", "3", "3", "3", "3", "3", "4")