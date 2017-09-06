from app import app                                                                         #import padrão da instancia Flask
#---------------------Import----------------------------------------------------------------#
from flask import render_template                                                           #Basicamente transforma HTML em uma string
from flask import redirect                                                                  #Usado para redirecionar para páginas desejadas
from flask import url_for                                                                   #Utilizado para pegar app.route da função desejada
from flask import jsonify                                                                   #Envio de resposta assíncrona para client-side
from flask import request                                                                   #
from flask import session
from functools import wraps
from flask import flash
#-------------------------------------------------------------------------------------------#
       


#---------------------Import de Funções-----------------------------------------------------#
from app.client.components.helper import get_parameters, db_connection                      #Função para buscar parâmetros do arquivo config.json
from app.client.interface.basic_interface.interface import login 
from app.client.run.standard_process.start import print_xml
from app.client.load.global_vars.variables import  read
from app.client.load.global_vars.variables import  write

from app.client.load.db_connections.connections import connections
from app.client.load.global_vars.variables import stored_data
#-------------------------------------------------------------------------------------------#



#---------------------Import de Classes-----------------------------------------------------#
from app.client.form import Login, Basic_interface, Manutencao_parada
#-------------------------------------------------------------------------------------------#


#---------------------Variáveis Globais-----------------------------------------------------#

 
#-------------------------------------------------------------------------------------------#



#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#


timer = 1



#---------------------Funções Críticas------------------------------------------------------#
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return (redirect(url_for('index')))
    return wrap 
#-------------------------------------------------------------------------------------------#



#---------------------Index - LOGIN---------------------------------------------------------#
@app.route('/', methods=['GET','POST'])
def index():
    form = Login()
 
    if form.validate_on_submit():
        login_response = login(form.username.data, form.password.data)
        if login_response:
            session['logged_in'] = True
            session['username'] = request.form['username']
            return redirect(url_for('basic_interface'))
            
        
    return render_template('login.html', form = form) 
#-------------------------------------------------------------------------------------------#




#---------------------BASIC INTERFACE-------------------------------------------------------#



@app.route('/basic_interface', methods=['GET','POST'])                                      #Roteamento 
@login_required
def basic_interface():
    #Temporário
    dv = [123245334234, 21353445656, 'TIRA FQ TUBO SMTH', 0, 2324354634, 0, 183218, 10, 'METALSA CA', '00/00/00', 'Descrição', 6565, 432546546, 1,443, 21, 'MTM 125 05'] #Variáveis teste
    dv2 = [20280, 20279, 'F05', 'T25', 1421, 'Pronto', 'METALSA CA', 'TUBO RET S460MC 60 X 100 X 4,00 FQ', 'Stringse', 6860, 0, '00/00/00-13:34', 736542, 0, 20, '21:09:43', 'P'] #Variáveis teste
    #Temporário

    response1 = '...'
    response2 = '...'
    response3 = '...'

    parameters = get_parameters()

    form = Basic_interface()                                                                #Criação de uma instância da classe
    form2 = Manutencao_parada()

    if (form.btn.data == True):                                                             #Verifica se o botão de POST foi pressionado
        teste(form.btn.data)                                                                #Chama função fora do request handler
   
    if form2.send.data == True:
        print('Foiiii')
        print(form2.select.data)

    return render_template('basic_interface.html', 
                           dv = dv, 
                           dv2 = dv2, 
                           form = form, 
                           form2 = form2,
                           response1 = response1,
                           response2 = response2,
                           response3 = response3,
                           parameters = parameters)                                         #Render de HTML localizado na pasta tramplates + Passagem de vars para HTML
#-------------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------------#
@app.route('/industrial_automation/', methods=['GET','POST'])
def automation_interface():
    form = Manutencao_parada()

    if form.send.data == True:
        print("Sendende")

    if form.validate_on_submit():
        show = form.select.data
        print(show)

    return render_template('industrial_automation.html', form=form)
#-------------------------------------------------------------------------------------------#



#---------------------BACKGROUND PROCESS----------------------------------------------------#
@app.route('/_background_process')
def background_process():
    global classe
    parameters = get_parameters()
    response1 = parameters['interface']['current_order']
    response2 = parameters['interface']['next_order_1']
    response3 = parameters['interface']['next_order_2']
    return jsonify(result = response1, result2 = response2, result3 = response3)

@app.route('/_timer')
def timer():
    global timer
    parameters = get_parameters()
    time = parameters['run']['timer']
    timer = timer + 1
    return jsonify(time = time, balance_status = parameters['run']['balance_status'])
#-------------------------------------------------------------------------------------------#



#---------------------ROTAS PARA TESTE------------------------------------------------------#
@app.route('/print/')
def print():
    response = print_xml()
    return response



@app.route('/algum_lugar/')
def algum_lugar():  
        return "----------------------"


@app.route('/header/')
def header():
    return render_template('header.html')



@app.route("/viewer/")
def viewer():
    dv2 = [20280, 20279, 'F05', 'T25', 1421, 'Pronto', 'METALSA CA', 'TUBO RET S460MC 60 X 100 X 4,00 FQ', 'Stringse', 6860, 0, '00/00/00-13:34', 736542, 0, 20, '21:09:43', 'P'] #Variáveis teste

    parameters = get_parameters()
    status = parameters['run']['balance_status']
    timer = parameters['run']['timer']
    print(status)
    return render_template('viewer_interface.html', status = status, dv2 = dv2, timer = timer)
#-------------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------------#
@app.route("/valar/")
def vars():
    #return_status = globalvar_dict = {}
    string = "SELECT TOP 3 * FROM %Peso1 kg %Altura"
    writes = {'Peso': 31231231, 'Altura': 1.84}
    #write(writes)
    stored_data()
    connections()

    return "1"
#-------------------------------------------------------------------------------------------#



