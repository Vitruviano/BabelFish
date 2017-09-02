from app import app
#---------------------Import----------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#



#---------------------Import de Funções-----------------------------------------------------#
from app.client.load.process_parameters.parser import parse_json
#-------------------------------------------------------------------------------------------#

########################
#Lembrar de trocar os numeros do json para ints
#Validar modo Read Write Check
#Write em aberto


global flag
flag = False
global vars_dict
vars_dict = {}

#-------------------------------------------------------------------------------------------#
def globalvar_parse():
    global flag
    global vars_dict
    value = {}
    tag = {}
    variables = []
    globalvars_dict = {}
    tag, value = parse_json()
    root = "GlobalVars"
    
    for i in range(len(value[root])):
        variables.append(tag[root][i])
        variables.append(value[root][i])
   
    for i in range(len(variables)):
        if variables[i] == 'Name':
            dict_index = str(variables[i+1])
            globalvars_dict[dict_index] = variables[i+5]

    #print(globalvars_dict) #{'Peso': 0, 'Altura': 1.84}
    flag = True
    vars_dict = globalvars_dict
#-------------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------------#
def text_sweeping(string):
    global flag
    global vars_dict
    if flag == False:
        globalvar_parse()

    key_word = ''
    special_char = '%'
    
    if type(string) is str:
        for i in range(len(string)):
            if string[i] == special_char:
                for a in range(i, (len(string))):
                    print(a+1)
                    print(len(string))
                    if (string[a] == ' ') or (a+1) == len(string):
                        new_key_word = key_word
                        key_word = key_word.replace(special_char, "")
                        new_string = string
                        for key in vars_dict:
                            if str(key) == str(key_word):
                                new_string = new_string.replace(str(new_key_word),str(vars_dict[key]))
                        break
                    key_word += str(string[a])
    else:
        return ('Not a String Type')

    print(new_string)
    
    

#-------------------------------------------------------------------------------------------#

