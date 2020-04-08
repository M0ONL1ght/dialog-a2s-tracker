import json
import io
import os
import pycurl
import common.common as common

def sendMessage(message):
    message = message.encode('utf-8','surrogateescape').replace(b'\n',b'\\n').decode('utf-8','surrogateescape').replace('"','\\"')
    webhookurl = os.environ['WEBHOOKURL']
    message = '{"text":"'+message+' "}'
    response = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, webhookurl)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.setopt(c.HTTPHEADER, ["Content-Type: application/json"])
    c.setopt(c.POSTFIELDS, message.encode('utf-8','surrogateescape'))

    try:
        c.perform()
    except pycurl.error:
        common.conMsg('dialog','Pycurl error')
        return "Pycurl error. 404?"
        
    c.close()

    try:
        json.loads(response.getvalue())
    except json.decoder.JSONDecodeError:
        return "JSON not found in response from resource. Unauthorized?"
    
    response.close()

    return common.now() + " : Message sent successfully"