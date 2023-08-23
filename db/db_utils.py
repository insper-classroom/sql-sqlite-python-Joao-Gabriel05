import sqlite3
conn = sqlite3.connect('db/database_alunos.db')
def cria_tabela(conn):
    cursor = conn.cursor()
    cursor.execute(
    '''
   CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER);
    '''
)
    conn.commit()

def consultar(conn,adicional):
    cursor = conn.cursor()
    cursor.execute(
    f'''
    SELECT * FROM Estudantes {adicional} 
 
    '''
)
    conn.commit()
def inserir(conn,estudantes):
    cursor = conn.cursor()
    cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
VALUES (?, ?, ?);
""", estudantes)
    conn.commit()

def atualizar(conn,SET,set_value,adicional):
    cursor = conn.cursor()
    cursor.executemany(
    f"UPDATE Estudantes SET {SET} = ?  {adicional}", (set_value))
    conn.commit()


def deletar_registros(conn,adicional):
    cursor = conn.cursor()
    cursor.execute(
    f"DELETE FROM Estudantes {adicional}")
    conn.commit()
