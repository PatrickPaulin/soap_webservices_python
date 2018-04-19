#!/usr/bin/python3
import json
import argparse
from data import Data
from activation import Ativacao
from jsonparser import Parser

#Instances
data = Data()
ativa = Ativacao()
decoder = Parser()
jsonObj = ""

class __main__():
    
    def runActivation():
        ativa.start_activation()

    def getArgs():
        parser = argparse.ArgumentParser()                                               
        parser.add_argument("--file", "-f", type=str, required=False)
        return parser.parse_args()
        
    def getFile(arg):
        global jsonObj

        if arg is None:
            return None
        
        json_file = arg.file 
        
        # If theres no file Json in arguments so get User input
        if json_file is None:
            return None
        
        # Read json file
        with open(json_file) as file:
            jsonObj = json.loads(file.read())
        
        return True

    if __name__== "__main__":
        global jsonObj
        i = 0

        #Get file from args
        if getFile(getArgs()) is None:
            exit("No JSON arquive")
        while i < len(jsonObj):
            # Clean values
            data.init_values()
            # Parser Json file input
            if decoder.jsonParser(i, jsonObj) is None:
                exit("Json Decoder Error 092")
 
            # Spin that sh*t
            if runActivation() is None:
                exit("Erro when running Activation flow")
            i += 1