import json
import requests
import stomp

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

def stop():
    conn.disconnect()
    

if __name__ == '__main__':
    try:
        response = requests.get('http://193.191.176.129:8080/createplayer')
        player = response.json()
        
        conn = stomp.Connection()
        conn.set_listener('', MyListener())
        conn.start()

        conn.subscribe(destination='http://193.191.176.129:8080/topic/scores/' + player['id'])

        while True:
            player['score'] = player['score'] + 1
            conn.send(body = player, destination = 'http://193.191.176.129:8080/app/scores/' + player['id'])
            time.sleep(1);

        response = requests.post('http://193.191.176.129:8080/setplayer', json = player)
        print(response.json())
        
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
           stop()
