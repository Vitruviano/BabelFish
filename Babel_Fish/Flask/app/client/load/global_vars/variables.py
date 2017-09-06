from app import app
#---------------------Import----------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#



#---------------------Import de Funções-----------------------------------------------------#
from app.client.load.process_parameters.parser import parse_json
#-------------------------------------------------------------------------------------------#



#Função para chamada


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
def read(string):
    global flag
    global vars_dict

    if flag == False:
        globalvar_parse()

    key_word = ''
    new_string = ''
    special_char = '%'
    final_string = string

    if type(string) is str:
        for i in range(len(string)):
            if string[i] == special_char:
                for a in range(i, (len(string))):
                    if ((string[a] == ' ') or (a+1) == len(string)):
                        if ((a+1) == len(string)):
                            key_word += str(string[a])
                        key_word = key_word.replace(" ", "")
                        new_key_word = key_word
                        key_word = key_word.replace(special_char, "")
                        new_string = final_string
                        for key in vars_dict:
                            if str(key) == str(key_word):
                                new_string = new_string.replace(str(new_key_word),str(vars_dict[key]))
                                final_string = new_string
                        key_word = ''   
                    key_word += str(string[a])
    else:
        return False

    
    for i in range(len(new_string)):
        if new_string[i] == special_char:
            print('Erro')
            return False


    print(new_string)

#-------------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------------#
def write(command):
    global flag
    global vars_dict
    success_count = 0
    if flag == False:
        globalvar_parse()

    for key1 in command:
        for key2 in vars_dict:
            if str(key1) == str(key2):
                vars_dict[key2] = command[key1]
                success_count += 1

    if not (success_count == len(command)):
        return False

    print(vars_dict)
#-------------------------------------------------------------------------------------------#
                



'''
import pickle
obj = [1, 2, 3, 4]
f = open("/path/to/the/file/where/the/data/should/be/stored.pickle", 'wb') 
pickle.dump(obj, f)
f.close()
'''



'''
f = open("/path/to/the/file/where/the/data/should/be/stored.pickle", 'rb')
obj = pickle.load(f)
f.close()
'''



