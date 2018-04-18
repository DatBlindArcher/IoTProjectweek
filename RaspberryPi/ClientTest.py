import json
import requests

if __name__ == '__main__':
    try:
        response = requests.get('http://193.191.176.129:8080/createplayer')
        player = response.json()
        player['score'] = 20
        response = requests.post('http://193.191.176.129:8080/setplayer', json = player)
        print(response.json())
        
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
           stop()
