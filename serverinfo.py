from bs4 import BeautifulSoup
from pynput.keyboard import Key, Listener
from os import system 
from datetime import datetime
from player import Player
from os import path

import os.path
import time
import threading
import sys
import urllib.request
import winsound
import json

serverList = ["http://116.202.234.15:30145/webadmin/"]

globalPlayerList = []
playerList = [] 

def getData(url):
    htmlSource = ""
    
    with urllib.request.urlopen(url) as f:
        try:
            htmlSource = f.read()
        except ConnectionResetError:
            print("Error with the connection...")
            winsound.Beep(760, 100)

    return htmlSource

def getServerName(soup):
    serverName = soup.findAll("h1", {"class": "px-3"})[0].getText()
    
    return serverName

def getPlayerCount(soup):
    playerCount = soup.findAll("dd", {"class": "col-sm-10"})[0].getText()
    
    return playerCount

def getPlayerList(soup):
    players = []
    table = soup.findChildren('table')[0]
    rows = table.findChildren(['th', 'tr'])
    rows = rows[7:]

    for row in rows:
        cells = row.findChildren('td')
        links = []
        for cell in cells:
            if len(cell.findChildren('a')) > 0:
                for a in cell.findChildren('a'):
                    links.append(a.getText())

        players.append(Player(cells[1].getText(), links))
    
    return players

def mergeLists():
    global globalPlayerList, playerList
    for p in playerList:
        if not any(x.name == p.steam for x in globalPlayerList):
            globalPlayerList.append(p)

def saveToFile(file="players.txt"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump([ob.__dict__ for ob in globalPlayerList], f)
    print("Saved player datas")

def readFromFile(file="players.txt"):
    if not path.isfile(file):
        return []
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        print("Read player datas")
        return data
        
def on_release(key, ):
    if (key == Key.esc):
        mergeLists()
        saveToFile()
        sys.exit("ESC pressed") 

def loop(datas):
    while(True):
        global playerList
        _ = system("cls")
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print(current_time)

        print("\n|" + "-" * 30 + "| FiveM Server Info |" + "-" * 30 + "|\n")
        
        html = getData(serverList[0])
        soup = BeautifulSoup(html, 'html.parser')
        
        serverName = getServerName(soup)
        playerCount = getPlayerCount(soup)
        playerList = getPlayerList(soup)
        
        
        print("\n" + serverName + "\n\n")
        print('\n\n'.join(str(player) for player in playerList))
        print("\nPlayers online:", playerCount)
        print("\n|" + "-" * 81 + "|\n")
        print(globalPlayerList)
        print(len(globalPlayerList))
        mergeLists()
        saveToFile()
        time.sleep(10)

def setGlobalPlayerList(datas):
    global globalPlayerList
    if len(datas) > 0:
        for data in datas:
            globalPlayerList.append(Player(readDict=data))


def main():
    
    datas = readFromFile()
    x = threading.Thread(target=loop, args=(datas,))
    x.setDaemon(True)
    setGlobalPlayerList(datas)
    
    try:
        
        x.start()
        with Listener( on_release=on_release) as listener:
            listener.join()
    
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
        

if __name__ == "__main__":
    main()
