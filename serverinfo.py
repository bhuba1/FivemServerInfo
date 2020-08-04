from bs4 import BeautifulSoup

import urllib.request
import winsound


serverList = ["http://116.202.234.15:30145/webadmin/"]

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

def main():
    print("\n|" + "-" * 30 + "| FiveM Server Info |" + "-" * 30 + "|\n")
    
    html = getData(serverList[0])
    soup = BeautifulSoup(html, 'html.parser')
    
    serverName = getServerName(soup)
    playerCount = getPlayerCount(soup)
    
    print(serverName)
    print("\nPlayers online:",playerCount)
    print("\n|" + "-" * 81 + "|\n")

if __name__ == "__main__":
    main()
