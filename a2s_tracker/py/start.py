import pycurl
import io
import os
import a2s
import api.dialog as dialog
import common.common as common
import time
import socket


def parseAddress(address):
    newAddress = ['']*2
    newAddress[0] = address.split(':')[0]
    newAddress[1] = address.split(':')[1]
    parsedAddress = (newAddress[0], int(newAddress[1]))
    return parsedAddress

def queryServer(address):
    rawQuery = a2s.info(address)
    serverInfo = ['']*5
    serverInfo[0] = rawQuery.map_name
    serverInfo[1] = rawQuery.player_count
    serverInfo[2] = rawQuery.server_name
    serverInfo[3] = rawQuery.game
    serverInfo[4] = rawQuery.max_players
    return serverInfo

def queryPlayers(address):
    rawQueryResult = a2s.players(address)
    overallPlayerInfo = []
    i = 0
    while i < len(rawQueryResult):
        playerInfo = [None]*2
        playerInfo[0] = rawQueryResult[i].name
        playerInfo[1] = rawQueryResult[i].score
        overallPlayerInfo.append(playerInfo)
        i += 1
    return overallPlayerInfo

def createReport(queryResult,queryPlayersResult):
    message = ''
    message = message + 'Заходи на сервер ' + queryResult[2] + ': ' + os.environ['SERVERADDR'] + '\n'
    message = message + 'Игроков: * ' + str(queryResult[1]) + '/' + str(queryResult[4]) + ' * - Карта: * ' + queryResult[0] + ' * \n' 
    message = message + os.environ['CUSTOMMSG'] + '\n'
    message = message + 'Сейчас на сервере: \n```'
    message = message + ' Фраги | Никнейм \n-------+--------------\n'
    i = 0
    while i < len(queryPlayersResult):
        fragsSpaceCount = 5 - len(str(queryPlayersResult[i][1]))
        fragsSpaces = ''
        j = 0
        while j < fragsSpaceCount:
            fragsSpaces = fragsSpaces + ' '
            j += 1
        message = message + ' ' + str(queryPlayersResult[i][1]) + fragsSpaces + ' | ' + queryPlayersResult[i][0]
        i += 1
    message = message.replace('\n','\\n')
    return message

def mainLoop(address):
    queryResult = queryServer(address)
    while True:
        try:
            if (queryServer(address)[1] > 0 and queryServer(address)[0] != queryResult[0]) or (queryServer(address)[1] != queryResult[1] and queryResult[1] == 0):
                queryResult = queryServer(address)
                queryPlayersResult = queryPlayers(address)
                dialog.sendMessage(createReport(queryResult,queryPlayersResult))
            else:
                queryResult = queryServer(address)
        except socket.timeout:
            online = False
            while online == False:
                try:
                    queryResult = queryServer(address)
                    online = True
                    #common.conMsg('bot','Server ' + os.environ['SERVERADDR'] + ' is Online: ' + str(queryResult))
                except socket.timeout:
                    common.conMsg('bot','Lost connection to server, trying to reconnect...')
                    time.sleep(15)
        time.sleep(25)

if __name__ == '__main__':
    address = parseAddress(os.environ['SERVERADDR'])
    try:
        queryResult = queryServer(address)
        common.conMsg('bot','Server ' + os.environ['SERVERADDR'] + ' is Online: ' + str(queryResult))
    except socket.timeout:
        while True:
            common.conMsg('bot','Invalid server. Make sure that you entered correct address and restart bot')
            time.sleep(60)
    mainLoop(address)