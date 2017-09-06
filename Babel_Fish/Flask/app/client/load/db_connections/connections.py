from app import app
#---------------------Import----------------------------------------------------------------#
import pymysql
#-------------------------------------------------------------------------------------------#



#---------------------Import de Funções-----------------------------------------------------#
from app.client.load.process_parameters.parser import parse_json
#-------------------------------------------------------------------------------------------#



#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#



#-------------------------------------------------------------------------------------------#
def connections():
    value = {}
    tag = {}
    variables = []
    root = 'Connections'
    current_db = ''

    tag, value = parse_json()

    #['ID', 'P1', 'ID', '1', 'Name', 'DBTESTE', 'DBType', 'MySQL', 'ConnectionString', '52.77; ; ; ;', 'HaveToWork', 1]
    for i in range(len(value[root])):
        variables.append(tag[root][i])
        variables.append(value[root][i])

    for i in range(len(variables)):
        if str(variables[i]) == 'DBType':
            current_db = variables[i+1]
            #print(current_db)

    if current_db.lower() == 'mysql':
        mysql_response = mysql(variables)



    #print(variables) 
    #print(tag)
    #print(value)
#-------------------------------------------------------------------------------------------#



#---------------------MySQL-----------------------------------------------------------------#
def mysql(variables):
    flag = False
    connection_string_name = 'connectionstring'

    for i in range(len(variables)):
        if str(variables[i]).lower() == connection_string_name:
            print(variables[i+1])
            connection_string = variables[i+1]
            
    connection_string = connection_string.split(';')

    if len(connection_string) > 3:
        return False

    host = connection_string[0]
    user = connection_string[1]
    passwd = connection_string[2]
    
    for i in range(len(variables)):
        if variables[i] == 'Name':
            db = variables[i+1]
            flag = True

    #Verifica se foi encontrado o 'name' do db
    if not flag == True:
        return False


    #print(host, user, passwd, db)

    #------------------------------------------------------------#
    try:
        conn = pymysql.connect(host=host,
                           user = user,
                           passwd = passwd,
                           db = db)
        c = conn.cursor()
        c.execute()
        print(c.description)

        for row in c:
            print(row)
    except pymysql.err.OperationalError as e:
        #arquivo erro
        print('erro')
        return False
    
    #------------------------------------------------------------#

    
#-------------------------------------------------------------------------------------------#
