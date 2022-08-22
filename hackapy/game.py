from matplotlib.pyplot import table
import zmq

def at( table, i, default ):
    if( len(table) > i ):
        return table[i]
    return default

class Piece():
    def __init__(self, name='Piece', attributes=[] ):
        self.name= name
        self.position= 0
        self.attributes= attributes

    def dump(self):
        msg= f'{self.name} on {self.position}'
        msg+= f' attributes {len(self.attributes)} : ' + ' '.join( [str(x) for x in self.attributes] )
        return msg

    def load(self, buffer):
        buffer= buffer.split(' ')
        self.name= buffer[0]
        self.position= buffer[2]
        self.attributes= []
        if int(buffer[4]) > 0 :
            self.attributes= [ int(x) for x in buffer[6:] ]
        return self

class Cell():
    def __init__( self, id ):
        self.id= id
        self.position= [0.0, 0.0]
        self.attributes= []
        self.pieces= []

    def dump(self):
        buffer= f'cell {self.id} position {self.position[0]} {self.position[1]}'
        buffer+= f' attributes {len(self.attributes)} : ' + ' '.join( [str(x) for x in self.attributes] )
        return buffer
    
    def load(self, buffer):
        pass

class Tabletop():
    def __init__(self, size= 0):
        self.cells= [ Cell(i) for i in range(size) ]
        self.connection= [ [] for i in range(size) ]
    
    def initializeFromMsg(self, msg):
        pass
    
    def dump(self):
        size= len(self.cells)
        msg= f'{size} cells:'
        for i in range(size) :
            msg+= '\n' + self.cells[i].dump()
            msg+= f' connects {len(self.connection[i])} : ' + ' '.join( [str(x) for x in self.connection[i]] )
        return msg

    def load(self, buffer):
        pass  

class Game():
    # Constructor
    def __init__(self, numerOfPlayers= 1, port=1400):
        self.numberOfPlayers= numerOfPlayers
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.ROUTER)
        print( f'HackaGame: Start a server on {port}' )
        self.socket.bind( 'tcp://*:'+str(port) )

    # Game interface :
    def play(self):
        pass

    # Engine process :
    def start(self, numberOfGames= 1):
        print( f'HackaGame: wait for {self.numberOfPlayers} players' )
        self.waitForPlayers()
        print( f'HackaGame: process {numberOfGames} games' )
        self.play()
        for i in range(numberOfGames-1) :
            first= self.players.pop(1) # 0 is the game itself.
            first= self.players.append(first)
            self.play()
        print( f'HackaGame: stop player-clients' )
        for i in range(self.numberOfPlayers) :
            self.send( i+1, 'stop' )
    
    def waitForPlayers(self):
        self.players= [0]
        playerId= 1
        nbReady= 0
        while nbReady < self.numberOfPlayers :
            sockid, none, msg = self.socket.recv_multipart()
            if msg == b'player' and sockid not in self.players :
                self.players.append( sockid )
                self.send( playerId, 'yes' )
                playerId+= 1
            elif msg == b'ready' and sockid in self.players :
                print( f'HackaGame: player-{ self.players.index(sockid) } ready' )
                nbReady+= 1
            else :
                self.socket.send_multipart( [sockid, b'', b'nop'] )
    
    # Communication to players :
    def send( self, playerId, msg ):
        assert( 0 < playerId and playerId <= self.numberOfPlayers )
        self.socket.send_multipart( [self.players[playerId], b'', bytes(msg, "utf-8")] )
    
    def wakeUpPlayers( self, gameConfigurationMsg='' ):
        if gameConfigurationMsg != '' :
            gameConfigurationMsg= f'on {self.numberOfPlayers}\n' + gameConfigurationMsg
        else :
            gameConfigurationMsg= f'on {self.numberOfPlayers}'
        for i in range(1, self.numberOfPlayers+1) :
            self.send( i, f'wake-up\nplayer {i} ' + gameConfigurationMsg )
        nbReady= 0
        ready= []
        while nbReady < self.numberOfPlayers :
            sockid, none, msg = self.socket.recv_multipart()
            if msg == b'ready' and sockid in self.players and sockid not in ready :
                print( f'HackaGame: player-{ self.players.index(sockid) } ready' )
                ready.append(sockid)
                nbReady+= 1
            else :
                self.socket.send_multipart( [sockid, b'', b'stop\nerror protocol'] )
    
    def activatePlayer( self, playerId, gameStateMsg ):
        assert( 0 < playerId and playerId <= self.numberOfPlayers )
        playerSockId= self.players[playerId]
        msg= f'perception\n'+ gameStateMsg
        self.socket.send_multipart( [playerSockId, b'', bytes(msg, 'utf8')] )
        while True :
            sockid, none, msg = self.socket.recv_multipart()
            if sockid == playerSockId :
                action= msg.decode('utf8')
                print( f'HackaGame: player-{ self.players.index(sockid) } action : {action}' )
                return action
            else :
                self.socket.send_multipart( [sockid, b'', b'stop\nerror protocol'] )
    
    def sleepPlayer( self, playerId, gameStateMsg, result ):
        assert( 0 < playerId and playerId <= self.numberOfPlayers )
        playerSock= self.players[playerId]
        msg= f'sleep\nresult {result}\n{gameStateMsg}'
        self.socket.send_multipart( [playerSock, b'', bytes(msg, "utf-8")] )
        while True :
            sockid, none, msg = self.socket.recv_multipart()
            if sockid == playerSock and msg == b'ready' :
                print( f'HackaGame: player-{ self.players.index(sockid) } sleep' )
                return True
            else :
                self.socket.send_multipart( [sockid, b'', b'stop\nerror protocol'] )