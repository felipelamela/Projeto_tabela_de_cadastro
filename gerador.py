from random import *
import sqlite3
from datetime import datetime

'''
GERADOR DE NOMES ALEATORIOS

Gera um numero X de valores de cadastro
"ID"
"Nome"
"Sobrenome"
"Email"
"Data de criação"
"Categoria"
"Telefone"

'''

#  Nome do seu arquivo.sqlite3
BANCO_DE_DADOS = 'YOURBANK' 

#Quantade de valores gerados
X_VALORES = 'YOURVALUES'

connection = sqlite3.connect(BANCO_DE_DADOS)
cursor = connection.cursor()
 
nomes = 'Miguel Arthur Heitor Bernardo Théo Davi Gabriel Pedro Samuel Lorenzo Benjamin Matheus Lucas Benício Gael Joaquim Nicolas Henrique Rafael Isaac Guilherme Murilo Lucca Gustavo João Miguel Noah Felipe Anthony Enzo João Pedro Pietro Bryan Daniel Pedro Henrique Enzo Gabriel Leonardo Vicente Valentim Eduardo Antônio  Emanuel Davi Lucca João João Lucas'

nomes = nomes.split()

sobrenomes = 'Abbott Abernathy Adair Adams Adkins Aguirre Alexander Allen Allison Almeida Alvarado Alvarez Andersen Anderson Anderson Andrews Archer Armstrong Arnold Arsenault Ashby Ashworth Atkinson Austin Ayers Fagan Fallon Fanning Farley Farrell Faulkner Ferguson Fernandez Figueroa Finch Finn Finnegan Fischer Fisher Fitch Fitzgerald Fitzpatrick Fitzsimmons Flanagan Fletcher Flood Flores Floyd Flynn Forbes Ford Forsyth Foster Fournier Fowler Fox Franklin Fraser Frazier Freeman Frost Fry Fuller'

sobrenomes = sobrenomes.split()
for i in range(1, (X_VALORES+1)):
    id = i
    nome = choice(nomes)
    sobrenome = choice(sobrenomes)
    email = nome+'@email.com'
    data_criacao = data_criacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    descricao = 'Gerado a partir de um script.'
    #Supondo que você tem 3 categorias, caso não, só alterar o segundo valor.
    categoria_id = randint(1, 3) 
    telefone = str(randint(888888888, 999999999))
 
 
    cursor.execute(f"INSERT INTO contatos_contato"
          f" (id, nome, sobrenome, email, data_criacao, descricao, categoria_id, telefone)"
          f" VALUES ('{id}', '{nome}', '{sobrenome}', '{email}', '{data_criacao}', '{descricao}', '{categoria_id}', '{telefone}');")
 
connection.commit()
 
cursor.close()
connection.close()
 
 
