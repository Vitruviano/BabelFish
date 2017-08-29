from app import app 
 #------------------------------------------------------------------------------------------#
from flask import render_template                                                           #Basicamente transforma HTML em uma string
from flask import redirect                                                                  #Usado para redirecionar para páginas desejadas
from flask import url_for                                                                   #Utilizado para pegar app.route da função desejada
from flask import jsonify                                                                   #Envio de resposta assíncrona para client-side
from flask import request           
from functools import wraps#
#-------------------------------------------------------------------------------------------#

           

#---------------------Import de Funções-----------------------------------------------------#
from app.client.components.helper import get_parameters, db_connection
#-------------------------------------------------------------------------------------------#



#----------------------Classes--------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#



#----------------------Funções--------------------------------------------------------------#
def login(username, password):
    '''
    try:
        login = [True, username, password]
        login_response = db_connection(login)
        if login_response == True:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
    '''

    return True




#-------------------------------------------------------------------------------------------#









    



    































































































dv = [123245334234, 21353445656, 'TIRA FQ TUBO SMTH', 0, 2324354634, 0, 183218, 10, 'METALSA CA', '00/00/00', 'Descrição', 6565, 432546546, 1,443, 21, 'MTM 125 05'] #Variáveis teste
dv2 = [20280, 20279, 'F05', 'T25', 1421, 'Pronto', 'METALSA CA', 'TUBO RET S460MC 60 X 100 X 4,00 FQ', 'Stringse', 6860, 0, '00/00/00-13:34', 736542, 0, 20, '21:09:43', 'P'] #Variáveis teste
