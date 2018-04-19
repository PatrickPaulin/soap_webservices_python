#!/usr/bin/python3

import json
from data import Data

data = Data()

class Parser():

    def jsonParser(self, noof_vehicle,  json_obj):
        if json_obj is not None:
            data.setFlow(json_obj[noof_vehicle]['flow'])
            data.setServer(json_obj[noof_vehicle]['environment'])
            data.setCombo(json_obj[noof_vehicle]['combo'])
            data.setOptionalCombo(json_obj[noof_vehicle]['optional'])
            data.setSerialNumber(json_obj[noof_vehicle]['serialNumber'])
            data.setStatus(json_obj[noof_vehicle]['status'])
        else :
            return None
        
        return True

    def __init__(self):
        pass 

