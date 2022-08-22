#!env python3
"""
HackaGame player interface 
"""
import sys, zmq

# Local HackaGame:
from . import game

context = zmq.Context()

def serverFromCmd():
    if len(sys.argv) > 1 :
        url= sys.argv[1]
        if ':' in url :
            url= url.split(":")
            host= url[0]
            port= int(url[1])
        else :
            host= url
            port= 1400
    else :
        host= 'localhost'
        port= 1400
    return host, port

class Player() :

    # PLayer interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConfigurationMsg):
        pass

    def perceive(self, gameStateMsg):
        pass
    
    def decide(self):
        pass
    
    def sleep(self, result):
        pass

    # HackaGame Client:
    def takeASeat(self, host='localhost', port=1400 ):
        #  Socket to talk to server
        print( f'HackaGames: connect to game on {host}:{port}' )
        self.connectToGame(host, port)
        msg= 'go'
        results= []
        while msg[0] != 'stop' :
            msg= self.receive().split('\n')
            if msg[0] == 'perception' :
                self.perceive( msg[1:] )
                self.send( self.decide() )
            else :
                if msg[0] == 'wake-up' :
                    playerMsg= msg[1].split(' ')
                    gameConfigurationMsg= ''
                    if len(msg) > 2 : 
                        gameConfigurationMsg= msg[2:]
                    self.wakeUp( 
                        int( playerMsg[1] ), int( playerMsg[3] ), gameConfigurationMsg
                    )
                elif msg[0] == 'sleep' :
                    self.perceive( msg[2:] )
                    results.append( int( msg[1].split(' ')[1] ) )
                    self.sleep( results[-1] )
                self.send( "ready" )
        return results
        
    def connectToGame(self, host, port):
        self.socket = context.socket(zmq.REQ)
        self.socket.connect( f'tcp://{host}:{port}' )
        self.send("player")
        #  Get the reply.
        message = self.receive()
        if message != 'yes' :
            print('HackaGames: didn\'t reach the game')
            exit()
        self.send( "ready" )

    def send(self, msg):
        self.socket.send( bytes(msg, 'utf8') )

    def receive(self):
        bytesMsg= self.socket.recv()
        return bytesMsg.decode('utf8')


class PlayerIHM(Player) :
    # PLayer interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConfigurationMsg):
        print( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)\n' + '\n'. join([ str(line) for line in gameConfigurationMsg ]) )

    def perceive(self, gameStateMsg):
        print( f'---\ngame state\n' + '\n'. join([ str(line) for line in gameStateMsg ]) )
    
    def decide(self):
        action = input('Enter your action: ')
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')
