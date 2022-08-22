

class AbsPlayer() :
    # AI interface :
    def wakeUp(self, numberOfPlayers, playerId, tabletop):
        pass

    def perceive(self, turn, scores, pieces, deltaTabletop):
        pass

    def decide(self):
        pass # must return the action to perfom as a string.

    def sleep(self, result):
        pass

class AbsEngine() :
    STATE_STOPPED= 0
    STATE_STOP= 1
    STATE_RUNNING= 2

    # Constructor
    def __init__( self, controlers= [] ):
        self.controlers= controlers
        self.stepper= self.regularStepper
        self.state= Engine.STATE_STOPED

    # Engine interface :
    def initialize():
        pass

    def observation( self, idControler ):
        '''
        Return the curent perception state of one of the controlers.
        '''
        pass
    
    def control( self, idControler, action ):
        '''
        Excecute the action of one of the controlers.
        '''
        pass
    
    def step( self ):
        '''
        Step, i.e. process the engine cycle. The `step` function is called after all controlers has been activated and before to start a new stepper cycle.
        '''
        pass

    def terminate():
        '''
        The las action to performe before to stop the engine
        '''
        pass

    # Engine process :
    def start( self):
        '''
        start the engine with a list of controlers.
        '''
        pass


    def stop():
        '''
        process the engine before to start a new cycle.
        '''
        pass
