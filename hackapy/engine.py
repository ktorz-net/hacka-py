# Classical Engine for simple games.

import random

class Controler() :
    # Engine interface :
    def process(self, observation):
        pass

class Engine() :
    STATE_STOPPED= 0
    STATE_STOP= 1
    STATE_RUNNING= 2

    # Constructor
    def __init__( self, controlers= [] ):
        self.controlers= controlers
        self.stepper= self.regularStepper
        self.state= Engine.STATE_STOPPED

    # Engine interface :
    def initialize(self):
        pass

    def observation(self, idControler):
        '''
        Return the curent perception state of one of the controlers.
        '''
        pass
    
    def control(self, idControler, action):
        '''
        Excecute the action of one of the controlers.
        '''
        pass
    
    def step(self):
        '''
        Step, i.e. process the engine cycle. The `step` function is called after all controlers has been activated and before to start a new stepper cycle.
        '''
        pass

    def terminate(self):
        '''
        The las action to performe before to stop the engine
        '''
        pass

    # Engine process :
    def start(self):
        self.initialize()
        self.state= Engine.STATE_RUNNING
        while self.state >= Engine.STATE_RUNNING :
            self.stepper()
        self.terminate()
        self.state= Engine.STATE_STOPPED

    def stop(self):
        self.state= Engine.STATE_STOP

    # Engine steppers
    def regularStepper(self):
        numberOfControlers= len(self.controlers)
        for id in range( numberOfControlers ) :
            action= self.controlers[id].process( self.observation(id) )
            self.control( id, action )
        self.step()

    def randomStepper(self):
        ids= range( len(self.controlers) )
        random.shuffle( ids )
        for id in ids :
            action= self.controlers[id].process( self.observation(id) )
            self.control( id, action )
        self.step()

# Simple exemple

def main():
    print('# 3 steps\' test:')
    print('## No Controler:')
    engine= EngineTest()
    engine.start()
    print('\n## 2 Controlers:')
    engine= EngineTest( [ControlerTest('astrid'), ControlerTest('bob')] )
    engine.start()

class EngineTest(Engine) :
    # Engine interface :
    def initialize(self):
        print('intialize')
        self.counter= 0

    def observation(self, idControler):
        print(f'con-{idControler} observation')
        return [0]

    def control(self, idControler, action):
        print(f'con-{idControler} control: {action}')
        
    def step(self):
        print(f'step')
        self.counter+= 1
        if self.counter > 2 :
            self.stop()

    def terminate(self):
        print(f'terminate')

class ControlerTest() :
    def __init__(self, name):
        self.name= name
    
    # Engine interface :
    def process(self, observation):
        print( f'{self.name} process observation: {observation} and return ok' )
        return 'ok'

# run
if __name__ == '__main__' :
    main()
