from app import app
#---------------------Import----------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#



#---------------------Import de Funções-----------------------------------------------------#
from app.client.load.process_parameters.parser import parse_json
#-------------------------------------------------------------------------------------------#

#Variavéis Globais:
#
#Vão ser variáveis para poder ser escrito/consultado ao longo do processo, Ex: Valor retornado da balança será gravado
#na GlobalVar Peso (:Peso).
#Dica do Gustavo: Criar vetor com a primeira posição sendo o nome da variável (Ex: Peso) e a segunda posição o valor (Ex: 0).
#No momento da preparação de cada componente eu vou poder substituir o nome da variável global pelo seu valor.
#(Ex: SELECT * FROM BLABLABLA WHERE TF_PESO = :Peso (Substituir pelo valor da variável global) 
#

#2 - Transformar string em vars
#3 - Função para varredura


def teste():
    value = {}
    tag = {}
    tag, value = parse_json()

    #print(tag)
    #print(value)
    
    root = "ProcessParams"
    node = "GlobalVars"
    matrix = []
    print((tag[root][node]))
    for i in range(len(tag[node])):
        matrix.append([tag[node][i], value[node][i]])

    #print(matrix[1][1])
    

    #print(tag[node])
    #rint(value[node])
    '''
    print(matrix[0][0])
    print(matrix[0][1])
    print(matrix[1][0])
    print(matrix[1][1])
    print(matrix[2][0])
    print(matrix[2][1])
    print(matrix[3][0])
    '''
    return tag, value












