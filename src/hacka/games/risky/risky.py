import random, pathlib

"""
HackaGame - Game - Risky 
"""
from ... import core as hk
from ... import board as hkboard

gamePath= str( pathlib.Path( __file__ ).parent )

# Army .Flags
ACTION= 1
FORCE=  2

def log(aString):
    pass

class GameRisky( hk.AbsSequentialGame ) :

    # Constructor :
    #--------------
    def __init__(self, numerOfPlayers= 2, map="board-4"):
        super().__init__(numerOfPlayers)
        # .Flags
        self.map= map
        self.counter= 0
        self.duration= 0
        self.maximalArmyForce= 24
        self.board= hkboard.Board()
        self.wrongAction= [ 0 for i in range(0, numerOfPlayers+1) ]
        self._ended= False
        # Trace
        self.actionList= []
        # Configuration
        self.degatMethod= self.degatStochastic
        self.verbose= log

    def copy(self):
        cpy= GameRisky( self.numberOfPlayers, self.map )
        # .Flags
        cpy.counter= self.counter
        cpy.duration= self.duration
        cpy.maximalArmyForce= self.maximalArmyForce
        cpy.board= self.board.copy()
        cpy.wrongAction= [ x for x in self.wrongAction ]
        cpy._ended= self._ended
        # Trace
        self.actionList= [ x for x in self.actionList ]
        # Configuration
        #self.degatMethod= self.degatStochastic
        #self.verbose= log
        return cpy

    # Pod interface :
    #-----------------
    def asPod( self ):
        # Return the game elements in the player vision (an Pod)
        gamePod= hk.Pod( "Risky", self.map, [ self.counter, self.duration ] )
        gamePod.append( self.board.asPod() )
        return gamePod

    def fromPod( self, gamePod ):
        self.map= gamePod.status()
        self.counter= gamePod.flag(1)
        self.duration= gamePod.flag(2)
        self.board.fromPod( gamePod.child() )
        self._ended= False
        return self

    # Game interface :
    #-----------------
    def initialize(self):
        # Initialize a new game (returning the game setting as a Gamel, a game ellement shared with player wake-up)
        self.actionList= []
        f= open(f"{gamePath}/resources/map-{self.map}.pod")
        self.board.load( f.read() )
        f.close()
        for i in range(1, self.numberOfPlayers+1) :
            self.popArmy( i, i, 1, 12 )
        self.counter= 1
        if self.duration == 0 :
            self.duration= self.board.size()
        self._ended= False
        return  self.asPod()

    def setRandomSeed(self, newSeed= 42):
        random.seed(newSeed)

    def playerHand( self, iPlayer=1 ):
        return self.asPod()

    def applyPlayerAction( self, iPlayer, action ):
        r= self._applyPlayerAction(iPlayer, action)
        #for i in range( self.size()) :
        #    if self.tileIsArmy(i) and self.tileArmyForce(i) == 0 :
        #        print( f"> What ?\n{self.playerHand(iPlayer)}\n{self.searchMetaActions(iPlayer)}\n{self.actionList}\n{self.playerHand(iPlayer)}>" )
        return r

    def _applyPlayerAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer. return a boolean at True if the player terminate its actions for the current turn.
        self.actionList.insert(0, self.playerLetter(iPlayer)+' '+action )
        action= action.split(' ')
        if action[0] == "move" and len( action ) == 4 :
            tileFrom= int(action[1])
            tileTo= int(action[2])
            force= int(action[3])
            army= self.armyOn(tileFrom)
            if ( self.isTile(tileFrom) and tileTo in self.tile(tileFrom).adjacencies() and army and army.status() == self.playerLetter(iPlayer) and 0 < force and force <= army.flag(FORCE) ):
                return self.actionMove( iPlayer, tileFrom, tileTo, force )
        if action[0] == "grow" and len( action ) == 2 :
            tileId= int(action[1])
            army= self.armyOn(tileId)
            if self.isTile(tileId) and army and army.status() == self.playerLetter(iPlayer) :
                return self.actionGrow( iPlayer, tileId)
        if action[0] == "sleep" :
            return self.actionSleep( iPlayer )
        if action[0] == "expend" and len( action ) == 2 :
            return self.actionExpend( iPlayer, int(action[1]) )
        if action[0] == "fight" and len( action ) == 2 :
            return self.actionFight( iPlayer, int(action[1]) )
        if action[0] == "defend" :
            return self.actionDefend( iPlayer )

        return self.actionWrongAction(iPlayer, "applying: "+str(action) )
    
    def actionWrongAction(self, iPlayer, actionMsg):
        self.wrongAction[iPlayer]+= 1
        print( f"!!! Wrong action-{self.wrongAction[iPlayer]} ({self.actionList[0]}): {actionMsg} !!!" )
        #print(self.playerHand(iPlayer))
        if self.wrongAction[iPlayer] >= 8 :
            return self.actionSleep( iPlayer )
        return False

    def tic( self ):
        # called function at turn end, after all player played its actions. 
        self.counter= min( self.counter+1, self.duration )

    def isEnded( self ):
        # must return True when the game end, and False the rest of the time.
        # The game already ended...
        if self._ended :
            return True
        # is ending ?
        self._ended= (len( self.activePlayers() ) == 1 or self.counter >= self.duration)
        # if yes
        if self._ended :
            # remove any possible actions...
            for tile in self.board.tiles() :
                for army in tile.pieces() :
                    army.setFlag( ACTION, 0 )
        return self._ended
    
    # Player access :
    #----------------
    def size(self):
        return self.board.size()
    
    def tile(self, i):
        return self.board.tile(i)
    
    def tileArmy(self, i):
        if self.tileIsArmy(i) :
            return self.board.tile(i).piece()
        return False
    
    def tileArmyOwner(self, i):
        return self.tileArmy(i).status()
    
    def tileArmyAction(self, i):
        return self.tileArmy(i).flag(ACTION)
    
    def tileArmyForce(self, i):
        return self.tileArmy(i).flag(FORCE)
    
    def tileIsArmy(self, i):
        return bool(self.board.tile(i).pieces())
    
    def tileIsFree(self, i):
        return not bool(self.board.tile(i).pieces())

    def playerActions(self, iPlayer):
        playerId= self.playerLetter(iPlayer)
        actsGrow= {}
        actsMove= {}
        for i in range( 1, self.board.size()+1) :
            tile= self.board.tile(i)
            if tile.pieces() and tile.piece(1).status() == playerId and tile.piece(1).flag(ACTION) > 0 :
                actsGrow[i]= {}
                actsMove[i]= self.moveActions(i)

        acts= { "sleep": {} }
        if actsGrow :
            acts["grow"]= actsGrow
        if actsMove :
            acts["move"]= actsMove
        return acts

    def moveActions( self, iTile ):
        force= self.armyOn(iTile).flag(FORCE)
        moves= {}
        for target in self.tile(iTile).adjacencies() :
            moves[target]= { i:{} for i in range(1, force+1) }
        return moves

    def buildActionDescritors(self, playerId):
        acts= [ ["sleep"] ]
        for i in range( 1, self.board.size()+1) :
            tile= self.board.tile(i)
            if tile.pieces() and tile.piece().status() == playerId and tile.piece().flag(ACTION) > 0 :
                acts.append( ["grow", i] )
                acts+= self.searchMoveAction(i)
        return acts
        
    def searchMoveAction( self, iTile ):
        force= self.armyOn(iTile).flag(FORCE)
        return [ [ "move", iTile, target, force ] for target in self.tile(iTile).adjacencies() ]
    
    def searchReadyActions(self, playerId):
        acts= [ "sleep" ]
        actMoves= []
        for i in range( 1, self.board.size()+1) :
            tile= self.board.tile(i)
            if tile.pieces() and tile.piece().status() == playerId and tile.piece().flag(ACTION) > 0 :
                acts.append( "grow " + str(i) )
                actMoves+= self.searchMoveAction(i)
        # Explose move actions:
        for move in actMoves :
            if move[3] <= 4 :
                for force in range(1, move[3]+1) :
                    acts.append( f"move {move[1]} {move[2]} {force}" )
            else :
                acts.append( f"move {move[1]} {move[2]} 1" ) # just one
                half= int(move[3]/2)
                acts.append( f"move {move[1]} {move[2]} {half}" )# half
                acts.append( f"move {move[1]} {move[2]} {move[3]-1}" ) # but one
                acts.append( f"move {move[1]} {move[2]} {move[3]}" ) # all
        return acts
    
    def tileIsReadyForFight(self, iTile, playerId):
        army= self.tileArmy(iTile)
        return army and army.status() == playerId \
            and army.flag(ACTION) > 0 \
            and army.flag(FORCE) > 1
        
    def searchMetaActions(self, playerId):
        # Search expendable and contestable:
        expendable= []
        contestable= []
        for i in range( 1, self.board.size()+1) :
            if self.tileIsReadyForFight(i, playerId) :
                if self.isExpendable(i) :
                    expendable.append(i)
                contestable+= self.contestableFrom(i)
        # Clean:
        contestable= list(set(contestable))
        # Build Meta action consequentlly:
        acts= [ "defend" ]
        for i in expendable:
            acts.append( f"expend {i}" )
        for i in contestable:
            acts.append( f"fight {i}" )
        return acts
    
    def isExpendable(self, iTile):
        if self.tileIsFree(iTile) \
            or self.tileArmyAction(iTile) == 0 \
            or self.tileArmyForce(iTile) == 1 :
            return False
        for jTile in self.tile(iTile).adjacencies() :
            if self.tileIsFree(jTile) :
                return True
        return False

    def contestableFrom(self, iTile):
        targets= []
        if self.tileIsFree(iTile): 
            return targets
        playerId= self.tileArmyOwner(iTile)
        for jTile in self.tile(iTile).adjacencies() : 
            if self.tileIsArmy(jTile) and self.tileArmyOwner(jTile) != playerId:
                targets.append(jTile)
        return targets
    
    def tileIds(self):
        return range(1, self.board.size()+1)

    def isTile(self, iTile) :
        return self.board.isTile(iTile)

    def armyOn(self, iTile) :
        if self.isTile(iTile) and self.board.tile(iTile).pieces() :
            return self.board.tile(iTile).piece()
        return False

    # Actions :
    #----------
    def actionMove( self, iPlayer, iFrom, iTo, force ):
        targetTile= self.board.tile(iTo)
        army= self.armyOn(iFrom)
        if army :
            actCounter= army.flag(ACTION)
            playerLetter= self.playerLetter(iPlayer)
            if playerLetter == army.status() and actCounter > 0 :
                # All the army ?
                if force >= army.flag(FORCE) :
                    force= army.flag(FORCE)
                    self.board.tile(iFrom).pieces().pop()
                else :
                    army.setFlag(FORCE, army.flag(FORCE)-force)
                # free target:
                if len( targetTile.pieces() ) == 0 :
                    self.popArmy( iPlayer, iTo, actCounter-1, force )
                # friend target:
                elif targetTile.piece().status() == playerLetter :
                    targetArmy= targetTile.piece()
                    targetArmy.setFlag(FORCE, targetArmy.flag(FORCE)+force)
                    targetArmy.setFlag( ACTION, min( targetArmy.flag(ACTION), actCounter-1) )
                else: 
                    self.fight( iPlayer, actCounter, force, iTo )
            else :
                print( f"!!! Wrong move: unvalid army on {iFrom}!!!" )
        else :
            print( f"!!! Wrong move: no army on {iFrom} !!!" )
        return False
        
    def fight( self, iPlayer, actCounter, attack, iTo ):
        # Initialize:
        defence= self.armyOn(iTo).flag(FORCE)
        # while fighters:
        while attack > 0 and defence > 0 :
            degatAtt, degatDef= self.degatMethod(attack, defence)
            self.verbose( f"Fight-{iTo}: {attack}({degatAtt}) vs {defence}({degatDef})" )
            attack= max( 0, attack - degatDef )
            defence= max( 0, defence - degatAtt )
        # Update tile: defence
        self.verbose( f"Fight-{iTo}: {attack} vs {defence}" )
        if defence == 0 :
            self.board.tile(iTo).pieces().pop()
        else :
            self.armyOn(iTo).setFlag(FORCE, defence)
        # Update tile: attack
        if attack > 0 :
            self.popArmy( iPlayer, iTo, actCounter-1, attack )

    def degatDeterministic( self, attack, defence ):
        attackForce= attack + max(0, attack - defence)
        return (1+attackForce)//2, (2+defence*2)//3

    def degatStochastic( self, attack, defence ):
        attackForce= attack + max(0, attack-defence)
        degatAtt= 0
        for i in range( attackForce ):
            if random.randrange(12) < 6 :
                degatAtt+= 1
        degatDeff= 0
        for i in range( defence ):
            if random.randrange(12) < 8 :
                degatDeff+= 1
        return degatAtt, degatDeff

    def actionSleep( self, iPlayer ):
        playerLetter= self.playerLetter(iPlayer) 
        for tile in self.board.tiles() :
            for army in tile.pieces() :
                if army.status() == playerLetter :
                    army.setFlag( ACTION, min( 2, army.flag(ACTION)+1) )
        return True

    def actionGrow( self, iPlayer, iTile ):
        playerLetter= self.playerLetter(iPlayer)
        army= self.armyOn(iTile)
        recrut= (2+army.flag(FORCE))//3
        if army and army.status() == playerLetter and army.flag(ACTION) > 0 :
            for iNeighbour in self.tile(iTile).adjacencies() :
                neighbourArmy= self.armyOn(iNeighbour)
                if neighbourArmy and neighbourArmy.status() == playerLetter :
                    recrut+= 1
            army.setFlag( FORCE, min(army.flag(FORCE)+recrut, self.maximalArmyForce) )
            army.setFlag( ACTION, army.flag(ACTION)-1 )
        return False

    def actionDefend( self, iPlayer ):
        playerId= self.playerLetter(iPlayer)
        actions= self.buildActionDescritors(playerId)
        for a in actions :
            if a[0] == "grow" :
                self.actionGrow( iPlayer, a[1])
        return self.actionSleep(iPlayer)

    def actionExpend( self, iPlayer, iTile ):
        playerId= self.playerLetter(iPlayer)
        if self.tileIsFree(iTile) or self.tileArmyOwner(iTile) != playerId :
            return self.actionWrongAction(iPlayer, f"expend {iTile} (not a player army)")
        if self.tileArmyForce(iTile) == 1 :
            return self.actionWrongAction(iPlayer, f"expend {iTile} (single army)")
        # Get target tiles
        targets= []
        for jTile in self.tile(iTile).adjacencies() :
            if self.tileIsFree(jTile) :
                targets.append(jTile)
        targetLen= len(targets)
        if targetLen < 1 :
            return self.actionWrongAction(iPlayer, f"expend {iTile} (no free tile)")
        # Compute expedend parameters
        force= self.tileArmyForce(iTile)-1
        reinforcement= force//targetLen
        residual= force-(reinforcement*targetLen)
        # Expend
        for i in targets :
            if residual > 0 :
                self.actionMove(iPlayer, iTile, i, reinforcement+1)
                residual-= 1
            elif reinforcement > 0 :
                self.actionMove(iPlayer, iTile, i, reinforcement)
        # Not the last action
        return False
    
    def actionFight( self, iPlayer, iTile ):
        playerId= self.playerLetter(iPlayer)
        if self.tileIsFree(iTile) or self.tileArmyOwner(iTile) == playerId :
            return self.actionWrongAction(iPlayer, f"fight {iTile} (not an oponent army)")
        # army candidate 
        baseTile= 0
        force= 0
        for jTile in self.tile(iTile).adjacencies() :
            if self.tileIsArmy(jTile) and self.tileArmyOwner(jTile) == playerId and self.tileArmyAction(jTile) > 0 :
                testForce= self.tileArmyForce(jTile)
                if testForce > force :
                    baseTile= jTile
                    force= testForce
        if force == 0 :
            return self.actionWrongAction(iPlayer, f"fight {iTile} (no force)")    
        if force == 1 :
            return self.actionMove( iPlayer, baseTile, iTile, 1 )
        return self.actionMove( iPlayer, baseTile, iTile, force-1 )

    def activePlayers(self):
        active= []
        for tile in self.board.tiles() :
            for army in tile.pieces() :
                iPlayer= self.playerNum( army.status() )
                if iPlayer not in active :
                    active.append( iPlayer )
                    active.sort()
        return active
    
    def playerArmies(self):
        armies= [ 0 for i in range( self.numberOfPlayers+1 ) ]
        for tile in self.board.tiles() :
            for army in tile.pieces() :
                iPlayer= self.playerNum( army.status() )
                armies[ iPlayer ]+= army.flag(FORCE)
        return armies
    
    def playerScore( self, iPlayer ):
        # return the player score for the current game (usefull at game ending)
        armies= self.playerArmies()
        bestArmy= armies[0]
        winners= 0
        for i in range(1, self.numberOfPlayers+1) :
            if armies[i] > bestArmy :
                bestArmy= armies[i]
                winners= 1
            elif armies[i] == bestArmy :
                winners+= 1
        if winners == 1 and armies[iPlayer] == bestArmy :
            return 1
        if armies[iPlayer] == bestArmy :
            return 0
        return -1
    
    # Risky tools :
    def popArmy( self, iPLayer, position, action, force ):
        army= hk.Pod( "Army", self.playerLetter(iPLayer), [action, force] )
        self.board.tile(position).append( army )

    def playerLetter(self, iPlayer):
        return chr( ord("A")+iPlayer-1 )

    def playerNum(self, playerLetter):
        return 1 + ord(playerLetter) - ord("A")
