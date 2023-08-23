import sqlite3
conn = sqlite3.connect('db/database_alunos.db')
from db.db_utils import *
cria_tabela(conn)
estudantes = [
    ( 'Ana Silva', 'Computação',2019),
    (' Pedro Mendes', 'Física',  2021),
    ('Carla Souza','Computação', 2020),
    ('João Alves',' Matemática',2018),
    ('Maria Oliveira','Química',2022)

]

inserir(conn,estudantes)

atualizar(conn,' Ano_de_Ingresso','1','WHERE ID==1')

deletar_registros(conn, 'WHERE ID==1')

consultar(conn,' WHERE Ano_de_Ingresso >= 2019 and Ano_de_Ingresso <= 2020 ')
