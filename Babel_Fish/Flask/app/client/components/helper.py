from app import app
#----------------Import---------------------------------------------------------------------#
import json
import os
import pymysql
#-------------------------------------------------------------------------------------------#



def get_parameters():
    filename = os.path.join(app.static_folder, 'config.json')
    with open(filename) as config_file:
        json_object = config_file
        json_readable = json.load(json_object) 
    
    return json_readable



def db_connection(login):
    parameters = get_parameters()
    conn = pymysql.connect(host = parameters['run']['db_host'],
                       user = parameters['run']['db_user'],
                       passwd = "Teevo@2017!",
                       db = parameters['run']['db_db'])

    c = conn.cursor()

    if login[1]:
        print(str(login[1]))
        data = c.execute("SELECT * FROM logs WHERE username='"+login[1]+"'")
        data = c.fetchone()[2]
        for row in c:
            print(row)

        if str(data) == str(login[2]):
            print("Senhas.......")
            return True
        else:
            return False

    return False


