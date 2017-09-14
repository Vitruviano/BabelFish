from app import app
#---------------------Import----------------------------------------------------------------#
import sqlite3
import pymysql
#-------------------------------------------------------------------------------------------#



#---------------------Import de Funções-----------------------------------------------------#
from app.client.load.process_parameters.parser import parse_json
#-------------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------------#
def table_info():
    value = {}
    tag = {}
    variables = []
    root = 'MemoryTables'
    current_db = ''

    tag, value = parse_json()

    for i in range(len(value[root])):
        variables.append(tag[root][i])
        variables.append(value[root][i])

    #print(variables) #['ID', 'P1', 'ID', '4', 'Name', 'potluck']

    for i in range(len(variables)):
        if variables[i] == 'Name':
            table_name = variables[i+1]
#-------------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------------#
def copy_from():
             

        c = sqlite3.connect('hello.db')
        c = c.cursor()

        
        conn = pymysql.connect(host="52.67.237.121",
                           user = "gabriel",
                           passwd = "bti",
                           db = "DBTESTE")
        mysql_c = conn.cursor(pymysql.cursors.DictCursor)
        mysql_c.execute("SELECT * FROM potluck")


        for row in mysql_c:
            print(row)
            
            c.executemany("INSERT INTO potluck VALUES (?,?,?,?,?);", row)

            

     

#-------------------------------------------------------------------------------------------#