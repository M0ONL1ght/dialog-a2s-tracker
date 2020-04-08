import time
import io
import shutil
import os

def now():
    return time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime())

def conMsg(product,text):
    print (now() + ' : ' + product + ' : ' + text)

def parseCreds(creds):
    credsArray = creds.split('@')
    hostname = credsArray[1]
    credsArray = credsArray[0].split(':')
    credsArray.append(hostname)
    return credsArray

def cleanPyCache():
    if os.path.exists("__pycache__"): shutil.rmtree('__pycache__')
    if os.path.exists("api/__pycache__"): shutil.rmtree('api/__pycache__')
    if os.path.exists("common/__pycache__"): shutil.rmtree('common/__pycache__')
    if os.path.exists("tests/__pycache__"): shutil.rmtree('tests/__pycache__')
    if os.path.exists("interpreter/__pycache__"): shutil.rmtree('interpreter/__pycache__')

def appendToTestList(testList,testResult):
    newTestResult = [['1']*2]*1
    newTestResult[0][0] = testResult[0]
    newTestResult[0][1] = testResult[1]
    testList = testList + newTestResult
    return testList