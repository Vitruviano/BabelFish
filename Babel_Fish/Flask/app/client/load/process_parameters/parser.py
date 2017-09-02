from app import app
#---------------------Import----------------------------------------------------------------#
import os.path
import json
#-------------------------------------------------------------------------------------------#



#---------------------Import de Funções-----------------------------------------------------#
from glob import glob
from collections import OrderedDict
#-------------------------------------------------------------------------------------------#



#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#


def parse_json():
    data = []
    pattern = os.path.join((os.path.dirname(os.path.abspath(__file__)) + '/JSON'), '*.json')
    for file_name in glob(pattern):
        with open(file_name) as f:
            data.append(json.load(f))

    value = {}
    tag = {}
    indexjson = 0

    for jsonreads in data[indexjson]:
    #----------------------------------FirstBlock------------------------------------#
        root = "Process"
        node = "ProcessParams"
        value[node] = []
        tag[node] = []

        for key in data[0][root][node]:
            tag[node].append(key)
            value[node].append(data[0][root][node][key])

        #print(tag[node])
        #print(value[node])
    #-----------------------------------SecondBlock------------------------------------#

        root = "Process"
        node = "GlobalVars"
        first_sub_node = "GlobalVar"

        value[node] = []
        tag[node] = []

        sweeping = 0
        end_list = False
        tag[node].append(tag["ProcessParams"][0])
        value[node].append(value["ProcessParams"][0])

        while end_list == False:
            try:
                for key in data[0][root][node][first_sub_node][sweeping]:
                    tag[node].append(key)
                
                    value[node].append(data[0][root][node][first_sub_node][sweeping][key])
            except IndexError:
                end_list = True
            sweeping += 1
    
    
        #print(tag[node])
        #print(value[node])

    #-----------------------------------ThirdBlock------------------------------------#
        root = "Process"
        node = "Connections"
        first_sub_node = "Connection"

        value[node] = []
        tag[node] = []

        tag[node].append(tag["ProcessParams"][0])
        value[node].append(value["ProcessParams"][0])

        for key in data[0][root][node][first_sub_node]:
                    tag[node].append(key)
                    value[node].append(data[0][root][node][first_sub_node][key])

        #print(tag[node])
        #print(value[node])

    #-----------------------------------FourthBlock------------------------------------#
        root = "Process"
        node = "MemoryTables"
        first_sub_node = "MemoryTable"

        value[node] = []
        tag[node] = []

        tag[node].append(tag["ProcessParams"][0])
        value[node].append(value["ProcessParams"][0])

        for key in data[0][root][node][first_sub_node]:
                    tag[node].append(key)
                    value[node].append(data[0][root][node][first_sub_node][key])

        #print(tag[node])
        #print(value[node])

    #-----------------------------------FifhtBlock------------------------------------#
        root = "Process"
        node = "Components"
        first_sub_node = "Component"

        value[node] = []
        tag[node] = []
    
        sweeping = 0
        end_list = False
        tag[node].append(tag["ProcessParams"][0])
        value[node].append(value["ProcessParams"][0])

        while end_list == False:
            try:
                     for key in data[0][root][node][first_sub_node][sweeping]:
                              tag[node].append(key)
                              value[node].append(data[0][root][node][first_sub_node][sweeping][key])
            except IndexError:
                end_list = True
            sweeping += 1
        
        #print(tag[node])
        #print(value[node])

    #-----------------------------------SixthBlock------------------------------------#

        root = "Process"
        node = "ComponentConnections"
        first_sub_node = "ComponentConnection"

        value[node] = []
        tag[node] = []
    
        sweeping = 0
        end_list = False
        tag[node].append(tag["ProcessParams"][0])
        value[node].append(value["ProcessParams"][0])

        while end_list == False:
            try:
                     for key in data[0][root][node][first_sub_node][sweeping]:
                              tag[node].append(key)
                              value[node].append(data[0][root][node][first_sub_node][sweeping][key])
            except IndexError:
                end_list = True
            sweeping += 1
        
        #print(tag[node])
        #print(value[node])

    #-----------------------------------End-------------------------------------------------#
    #print(tag.values())
    #print(value.values())

    bigclass = {}
    classname = "Process" + str (indexjson)

    class MyClass:
        ID = value["ProcessParams"][0]
        Name = value["ProcessParams"][1]
        StartComponent = value["ProcessParams"][2]

    bigclass[classname] = MyClass()

    print(bigclass[classname].ID, bigclass[classname].Name, bigclass[classname].StartComponent)


    #print(tag["ProcessParams"][1])
    #print(value["ProcessParams"][1])

    indexjson += 1


    return tag, value



