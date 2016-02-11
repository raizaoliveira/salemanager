# -*- coding: utf-8 -*-
#DB

import MySQLdb
import main as GUI

#import class here
class conBD():

    host = 'localhost'
    user = 'root'
    password = 'raiza9608'
    db = 'deskschema'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("insert ok")
        except:
            print("insert not ok")
            self.connection.rollback()

    def delete(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("delete ok")
        except:
            print("delete not ok")
            self.connection.rollback()

    def consul(self, query):
        try:
            self.cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )#dicionario de dados
            self.cursor.execute(query)
            print("consulta ok")
            return self.cursor.fetchall()

        except:
            print("consulta not ok")
            self.connection.rollback()


class input_data():

    obdb = conBD()
    def data_estq(self):
        pk = input("primary key:  ")
        qtd = input("quantidade:  ")
        valor = input("valor:  ")
        desc = raw_input("descricao:  ")
        query ="insert into produto_estoque values(" + str(pk) + "," + str(qtd) + ","+ str(valor) +",'"+ desc +"' ) "
        self.obdb.insert(query)

    def data_card(self):
        pk = input("primary key:  ")
        produto = raw_input("produto:  ")
        valor = input("valor:  ")
        desc = raw_input("descricao:  ")
        query ="insert into cardapio values(" + str(pk) + ",'" + produto + "',"+ str(valor) +",'"+ desc +"' ) "
        self.obdb.insert_est(query)

class del_data():
    obdb = conBD()
    def del_est(self):
        pk = input("primary key: ")
        query = "delete from produto_estoque where id = " + str(pk) +" "
        self.obdb.delete(query)

class cons_data():

    obdb = conBD()

    def cons_estq(self):
        pk = input("primary key: ")
        query = "select * from produto_estoque where id =" + str(pk) + " "
        people = self.obdb.consul(query)
        for person in people:
            print ("Found %s " % person['id'])

    def cons_card(self):
        pk = input("primary key: ")
        query = "select * from cardapio where id =" + str(pk) + " "
        people = self.obdb.consul(query)
        for person in people:
            print ("Found %s " % person['produto'])

