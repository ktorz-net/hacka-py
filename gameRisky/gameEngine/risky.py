#!env python3
"""
HackaGame - Game - Risky 
"""
import os, sys, random

sys.path.insert(1, __file__.split('gameRisky')[0])
import hackapy as hg

gamePath= __file__.split('gameRisky')[0] + "/gameRisky"

# Army .Flags
ACTION= 1
FORCE=  2

def log(aString):
    pass

class GameRisky( hg.AbsSequentialGame ) :

    # Constructor :
    #--------------
    def __init__(self, numerOfPlayers= 2, map="board-4"):
        super().__init__(numerOfPlayers)
        # .Flags
        self.map= map
        self.counter= 0
        self.duration= 0
        self.maximalArmyForce= 24
        self.board= hg.Board()
        self.wrongAction= [ 0 for i in range(0, numerOfPlayers+1) ]
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
        gamePod= hg.Pod( "Risky", self.map, [ self.counter, self.duration ] )
        gamePod.append( self.board.asPod() )
        return gamePod

    def fromPod( self, gamePod ):
        self.counter= gamePod.flag(1)
        self.duration= gamePod.flag(2)
        self.board.fromPod( gamePod.child() )
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
        return  self.asPod()

    def setRandomSeed(self, newSeed= 42):
        random.seed(newSeed)

    def playerHand( self, iPlayer=1 ):
        return self.asPod()

    def applyPlayerAction( self, iPlayer, action ):
        r= self._applyPlayerAction(iPlayer, action)
        #for i in range( self.size()) :
        #    if self.cellIsArmy(i) and self.cellArmyForce(i) == 0 :
        #        print( f"> What ?\n{self.playerHand(iPlayer)}\n{self.searchMetaActions(iPlayer)}\n{self.actionList}\n{self.playerHand(iPlayer)}>" )
        return r

    def _applyPlayerAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer. return a boolean at True if the player terminate its actions for the current turn.
        self.actionList.insert(0, self.playerLetter(iPlayer)+' '+action )
        action= action.split(' ')
        if action[0] == "move" and len( action ) == 4 :
            cellFrom= int(action[1])
            cellTo= int(action[2])
            force= int(action[3])
            army= self.armyOn(cellFrom)
            if ( self.isCell(cellFrom) and cellTo in self.cell(cellFrom).adjacencies() and army and army.status() == self.playerLetter(iPlayer) and 0 < force and force <= army.flag(FORCE) ):
                return self.actionMove( iPlayer, cellFrom, cellTo, force )
        if action[0] == "grow" and len( action ) == 2 :
            cellId= int(action[1])
            army= self.armyOn(cellId)
            if self.isCell(cellId) and army and army.status() == self.playerLetter(iPlayer) :
                return self.actionGrow( iPlayer, cellId)
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
        return len( self.activePlayers() ) == 1 or self.counter >= self.duration 

    # Player access :
    #----------------
    def size(self):
        return self.board.size()
    
    def cell(self, i):
        return self.board.cell(i)
    
    def cellArmy(self, i):
        if self.cellIsArmy(i) :
            return self.board.cell(i).piece()
        return False
    
    def cellArmyOwner(self, i):
        return self.cellArmy(i).status()
    
    def cellArmyAction(self, i):
        return self.cellArmy(i).flag(ACTION)
    
    def cellArmyForce(self, i):
        return self.cellArmy(i).flag(FORCE)
    
    def cellIsArmy(self, i):
        return bool(self.board.cell(i).pieces())
    
    def cellIsFree(self, i):
        return not bool(self.board.cell(i).pieces())

    def playerActions(self, iPlayer):
        playerId= self.playerLetter(iPlayer)
        actsGrow= {}
        actsMove= {}
        for i in range( 1, self.board.size()+1) :
            cell= self.board.cell(i)
            if cell.pieces() and cell.piece(1).status() == playerId and cell.piece(1).flag(ACTION) > 0 :
                actsGrow[i]= {}
                actsMove[i]= self.moveActions(i)

        acts= { "sleep": {} }
        if actsGrow :
            acts["grow"]= actsGrow
        if actsMove :
            acts["move"]= actsMove
        return acts

    def moveActions( self, iCell ):
        force= self.armyOn(iCell).flag(FORCE)
        moves= {}
        for target in self.cell(iCell).adjacencies() :
            moves[target]= { i:{} for i in range(1, force+1) }
        return moves

    def searchActions(self, playerId):
        acts= [ ["sleep"] ]
        for i in range( 1, self.board.size()+1) :
            cell= self.board.cell(i)
            if cell.pieces() and cell.piece().status() == playerId and cell.piece().flag(ACTION) > 0 :
                acts.append( ["grow", i] )
                acts+= self.searchMoveAction(i)
        return acts
    
    def searchMoveAction( self, iCell ):
        force= self.armyOn(iCell).flag(FORCE)
        return [ [ "move", iCell, target, force ] for target in self.cell(iCell).adjacencies() ]

    def cellIsReadyForFight(self, iCell, playerId):
        army= self.cellArmy(iCell)
        return army and army.status() == playerId \
            and army.flag(ACTION) > 0 \
            and army.flag(FORCE) > 1
        
    def searchMetaActions(self, playerId):
        # Search expendable and contestable:
        expendable= []
        contestable= []
        for i in range( 1, self.board.size()+1) :
            if self.cellIsReadyForFight(i, playerId) :
                if self.isExpendable(i) :
                    expendable.append(i)
                contestable+= self.contestableFrom(i)
        # Clean:
        contestable= list(set(contestable))
        # Build Meta action consequentlly:
        acts= [ ["defend"] ]
        for i in expendable:
            acts.append( ["expend", i] )
        for i in contestable:
            acts.append( ["fight", i] )
        return acts
    
    def isExpendable(self, iCell):
        if self.cellIsFree(iCell) \
            or self.cellArmyAction(iCell) == 0 \
            or self.cellArmyForce(iCell) == 1 :
            return False
        for jCell in self.cell(iCell).adjacencies() :
            if self.cellIsFree(jCell) :
                return True
        return False

    def contestableFrom(self, iCell):
        targets= []
        if self.cellIsFree(iCell): 
            return targets
        playerId= self.cellArmyOwner(iCell)
        for jCell in self.cell(iCell).adjacencies() : 
            if self.cellIsArmy(jCell) and self.cellArmyOwner(jCell) != playerId:
                targets.append(jCell)
        return targets
    
    def cellIds(self):
        return range(1, self.board.size()+1)

    def isCell(self, iCell) :
        return self.board.isCell(iCell)

    def armyOn(self, iCell) :
        if self.isCell(iCell) and self.board.cell(iCell).pieces() :
            return self.board.cell(iCell).piece()
        return False

    # Actions :
    #----------
    def actionMove( self, iPlayer, iFrom, iTo, force ):
        targetCell= self.board.cell(iTo)
        army= self.armyOn(iFrom)
        if army :
            actCounter= army.flag(ACTION)
            playerLetter= self.playerLetter(iPlayer)
            if playerLetter == army.status() and actCounter > 0 :
                # All the army ?
                if force >= army.flag(FORCE) :
                    force= army.flag(FORCE)
                    self.board.cell(iFrom).pieces().pop()
                else :
                    army.setFlag(FORCE, army.flag(FORCE)-force)
                # free target:
                if len( targetCell.pieces() ) == 0 :
                    self.popArmy( iPlayer, iTo, actCounter-1, force )
                # friend target:
                elif targetCell.piece().status() == playerLetter :
                    targetArmy= targetCell.piece()
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
        # Update cell: defence
        self.verbose( f"Fight-{iTo}: {attack} vs {defence}" )
        if defence == 0 :
            self.board.cell(iTo).pieces().pop()
        else :
            self.armyOn(iTo).setFlag(FORCE, defence)
        # Update cell: attack
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
        for cell in self.board.cells() :
            for army in cell.pieces() :
                if army.status() == playerLetter :
                    army.setFlag( ACTION, min( 2, army.flag(ACTION)+1) )
        return True

    def actionGrow( self, iPlayer, iCell ):
        playerLetter= self.playerLetter(iPlayer)
        army= self.armyOn(iCell)
        recrut= (2+army.flag(FORCE))//3
        if army and army.status() == playerLetter and army.flag(ACTION) > 0 :
            for iNeighbour in self.cell(iCell).adjacencies() :
                neighbourArmy= self.armyOn(iNeighbour)
                if neighbourArmy and neighbourArmy.status() == playerLetter :
                    recrut+= 1
            army.setFlag( FORCE, min(army.flag(FORCE)+recrut, self.maximalArmyForce) )
            army.setFlag( ACTION, army.flag(ACTION)-1 )
        return False

    def actionDefend( self, iPlayer ):
        playerId= self.playerLetter(iPlayer)
        actions= self.searchActions(playerId)
        for a in actions :
            if a[0] == "grow" :
                self.actionGrow( iPlayer, a[1])
        return self.actionSleep(iPlayer)

    def actionExpend( self, iPlayer, iCell ):
        playerId= self.playerLetter(iPlayer)
        if self.cellIsFree(iCell) or self.cellArmyOwner(iCell) != playerId :
            return self.actionWrongAction(iPlayer, f"expend {iCell} (not a player army)")
        if self.cellArmyForce(iCell) == 1 :
            return self.actionWrongAction(iPlayer, f"expend {iCell} (single army)")
        # Get target cells
        targets= []
        for jCell in self.cell(iCell).adjacencies() :
            if self.cellIsFree(jCell) :
                targets.append(jCell)
        targetLen= len(targets)
        if targetLen < 1 :
            return self.actionWrongAction(iPlayer, f"expend {iCell} (no free cell)")
        # Compute expedend parameters
        force= self.cellArmyForce(iCell)-1
        reinforcement= force//targetLen
        residual= force-(reinforcement*targetLen)
        # Expend
        for i in targets :
            if residual > 0 :
                self.actionMove(iPlayer, iCell, i, reinforcement+1)
                residual-= 1
            elif reinforcement > 0 :
                self.actionMove(iPlayer, iCell, i, reinforcement)
        # Not the last action
        return False
    
    def actionFight( self, iPlayer, iCell ):
        playerId= self.playerLetter(iPlayer)
        if self.cellIsFree(iCell) or self.cellArmyOwner(iCell) == playerId :
            return self.actionWrongAction(iPlayer, f"fight {iCell} (not an oponent army)")
        # army candidate 
        baseCell= 0
        force= 0
        for jCell in self.cell(iCell).adjacencies() :
            if self.cellIsArmy(jCell) and self.cellArmyOwner(jCell) == playerId and self.cellArmyAction(jCell) > 0 :
                testForce= self.cellArmyForce(jCell)
                if testForce > force :
                    baseCell= jCell
                    force= testForce
        if force == 0 :
            return self.actionWrongAction(iPlayer, f"fight {iCell} (no force)")    
        if force == 1 :
            return self.actionMove( iPlayer, baseCell, iCell, 1 )
        return self.actionMove( iPlayer, baseCell, iCell, force-1 )

    def activePlayers(self):
        active= []
        for cell in self.board.cells() :
            for army in cell.pieces() :
                iPlayer= self.playerNum( army.status() )
                if iPlayer not in active :
                    active.append( iPlayer )
                    active.sort()
        return active
    
    def playerArmies(self):
        armies= [ 0 for i in range( self.numberOfPlayers+1 ) ]
        for cell in self.board.cells() :
            for army in cell.pieces() :
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
        army= hg.Pod( "Army", self.playerLetter(iPLayer), [action, force] )
        self.board.cell(position).append( army )

    def playerLetter(self, iPlayer):
        return chr( ord("A")+iPlayer-1 )

    def playerNum(self, playerLetter):
        return 1 + ord(playerLetter) - ord("A")
