import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
class Database():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                 database='<database name>',
                                 user='<username>',
                                 password='<password>')
        except Error as e :
            print ("Error", e)

    def insert(self, data):
        try:
            sql_insert_query = """ INSERT INTO `product`( `name`, `category`, `description`) VALUES ('"""+data["name"]+"""','"""+data["category"]+"""', '"""+data["description"]+"""')"""
            cursor = self.connection.cursor()
            result  = cursor.execute(sql_insert_query)
            self.connection.commit()
        except mysql.connector.Error as error :
            self.connection.rollback()
            print("Failed inserting record {}".format(error))
            return 0
        finally:
            if(self.connection.is_connected()):
                cursor.close()
                self.connection.close()
        return 1

    def selectID(self,id):
        try:
            sql_select_Query = "select * from product where id='"+id+"' ;"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            result={}

            for row in records:
                result[row[0]]=[row[1],row[2],row[3]]
        except Error as e :
            print ("Error while connecting to MySQL", e)
            return (result,0)
        finally:
            if(self.connection.is_connected()):
                cursor.close()
                self.connection.close()
        return(result,1)

    def select(self):
        try:
            sql_select_Query = "select * from product;"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            result={}
            for row in records:
                result[row[0]]=row[1]

        except Error as e :
            print ("Error while connecting to MySQL", e)
            return (result,0)
        finally:
            if(self.connection.is_connected()):
                cursor.close()
                self.connection.close()
        return(result,1)

    def update(self, id,data):
            try:
                cursor = self.connection.cursor()
                sql_update_query = """Update product set name='""" + data["name"] + """' ,category= '""" + data["category"] + """' ,description=' """ + data["description"] + """' where id = """+id+""";"""
                cursor.execute(sql_update_query)
                self.connection.commit()
            except mysql.connector.Error as error :
                print("Failed to update record to database: {}".format(error))
                self.connection.rollback()
                return 0
            finally:
                if(self.connection.is_connected()):
                    cursor.close()
                    self.connection.close()
            return 1




    def delete(self, id):
        try:
            cursor = self.connection.cursor()
            sql_Delete_query = """Delete from product where id = """+id+""";"""
            cursor.execute(sql_Delete_query)
            self.connection.commit()
        except mysql.connector.Error as error :
            print("Failed to delete record: {}".format(error))
            return 0
        finally:
            if(self.connection.is_connected()):
                cursor.close()
                self.connection.close()
        return 1




