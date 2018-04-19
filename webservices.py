#!/use/bin/python3

import requests
from bs4 import BeautifulSoup
from data import Data

data = Data()

# This class will be manage and create web services(xml) to send for server
class SendForm():
    # First scenario - send the first web service
    def sendStart(self):
        url = "http://"+data.getServer()+"/something?wsdl"
        headers = {'content-type' : 'text/xml'}
        body = """<soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:act='some host'>
                <soapenv:Header/>
                <soapenv:Body>       
                <act:start>
                <serialNumber>"""+data.getSerialNumber()+"""</serialNumber>
                </act:start>
                </soapenv:Body>
                </soapenv:Envelope>"""

        # Get response that web service response - Note we wanted the answer in text format
        response = requests.post(url,data=body,headers=headers)
        # Search for answer tag in xml
        soup = BeautifulSoup(response.text,"xml")
        ret = soup.find("msgError")
        
        if ret is not None:
            if "Success" in ret:
                return True
            else:
                return None
        else:
            return None

    def sendMidle(self):
        url = "http://"+data.getServer()+"/portal-orion-ws/something?wsdl"
        headers = {'content-type' : 'text/xml'}
        body =  """<soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:act='some host'>
                <soapenv:Header/>
                <soapenv:Body>
                <act:midle>
                <serialNumber>"""+data.getSerialNumber()+"""</serialNumber>
                </act:midle>
                </soapenv:Body></soapenv:Envelope>"""

        # Get response that web service response - Note we wanted the answer in text format
        response = requests.post(url,data=body,headers=headers)
        # Search for answer tag in xml
        soup = BeautifulSoup(response.text,"xml")
        ret = soup.find("msgError")

        if ret is not None:
            if "Sucesso" in ret:
                return True
            else:
                return None
        else:
            return None


    def sendFinish(self):
        url = "http://"+data.getServer()+"/portal-orion-ws/Something?wsdl"
        headers = {'content-type' : 'text/xml'}
        body =  """<soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:act='some host'>
                <soapenv:Header/> 
                <soapenv:Body>
                <act:finish>
                <serialNumber>"""+data.getSerialNumber()+"""</serialNumber>
                <combo>"""+data.getCombo()+"""</combo>
                """+data.getOptionalCombo()+"""
                <contractStatus>"""+data.getStatus()+"""</contractStatus>
                </act:finish>
                </soapenv:Body>
                </soapenv:Envelope>"""
        # Get response that web service response - Note we wanted the answer in text format
        response = requests.post(url,data=body,headers=headers)
        # Search for answer tag in xml
        soup = BeautifulSoup(response.text,"xml")
        ret = soup.find("msgError")

        if ret is not None:
            if "success" in ret:
                return True
            else:
                return None
        else:
            return None

    def __init__(self):
        pass
        
