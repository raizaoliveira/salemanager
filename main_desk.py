import MySQLdb



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



if __name__ == '__main__':
    ins = input_data()
    dele = del_data()
    query = cons_data()
    opt = input("opcao:  1 insere 2 deleta 3 conulta : ")

    if opt == 1:
        ins.data_estq()
    if opt == 2:
        dele.del_est()
    if opt == 3:
        con = input("1 estoque  2 cardapio")
        if con == 1:
            query.cons_estq()
        if con == 2:
            query.cons_card()


    #query ="insert into produto_estoque values( '" + nome + "'," + str(age) + " ) "
    # db.query(query)
    #db.insert(query)

    # Data retrieved from the table
    #select_query = """
      ##WHERE idade = 21
        #"""

    #people = db.query(select_query)

    #or person in people:
      #  print "Found %s " % person['name']


