#!/usr/bin/python3

class Data():
    combo = ""
    serialNumber = "" 
    optionalCombo = ""
    server = ""
    status = ""
    flow = ""
    
    # constants
    
    # envoriment
    integration = "10.40.1.6:8110" 
    homologation = "10.40.1.58:7110" 
    production = "200.185.142.54:7110" 

    #optional combo - define tags here
    high = "<optional>high</optional>"
    low = "<optional>low</optional>"
    journey = "<optional>journey</optional>"
    fast_response = "<optional>fast</optional>"

    #combo
    advanced = "platinum"    
    premium = "full"    
    fleet = "intermediate"    

    # Getters and Setters

    ## Serial Number
    def getSerialNumber(self):
        global serialNumber
        return serialNumber
    
    def setSerialNumber(self, serial):
        global serialNumber
        serialNumber = serial
    
    # Combo - only one for each activation
    def getCombo(self):
        global combo
        return combo
    
    def setCombo(self, arg):
        global combo
        if arg == "f" or arg == "F":
            combo = self.fleet
        elif arg == "p" or arg == "P":
            combo = self.premium
        else :
            combo = self.advanced

    # Evoriment - INT - HMG - PROD
    def getServer(self):
        global server
        return server

    def setServer(self, arg):
        global server
        if arg == "i" or arg == "I":
            server = self.integration
        elif arg == "h" or arg == "H":
            server = self.homologation
        else:
            server = self.production
    
    # Optional - combo is an additional combo
    def getOptionalCombo(self):
        global optionalCombo
        return optionalCombo

    def setOptionalCombo(self, arg):
        global optionalCombo
        i = 0
        while i < len(arg):
            optionalCombo += "<optional>"+arg[i]+"</optional>\n"
            i += 1

    #Status
    def getStatus(self):
        global status
        return status

    def setStatus(self, arg):
        global status
        status = arg
        
    # Flow
    def getFlow(self):
        global flow
        return flow

    def setFlow(self, arg):
        global flow
        flow = arg
        
    def init_values(self):
        global combo
        global cnpj
        global serialNumber
        global optionalCombo
        global plate
        global server
        global status
        global flow
        
        combo = ""
        cnpj = ""
        serialNumber = "" 
        optionalCombo = ""
        plate = ""
        server = ""
        status = ""
        flow = ""
    