#----------------------------------------------------------------------------------------------------------#
#                                   H A C K A P Y  :  P O D
#
# Pod : Piece Of Data
# An HackaGame element ([hackagames](https://bitbucket.org/imt-mobisyst/hackagames))
# 
#----------------------------------------------------------------------------------------------------------#

class PodInterface() :

    # Pod interface:
    def asPod(self, family="Pod"):
        # Should return a Pod describing self.
        pass
    
    def fromPod(self, aPod):
        # Should regenerate self form the pod description
        pass
        #return self

    # Pod shortcut:
    def dump(self): 
        return self.asPod().dump()
    
    def load(self, buffer):
        self.fromPod( Pod().load(buffer) )
        return self

    def copy(self) :
        cpy= type(self)().fromPod( self.asPod() )
        return cpy
    
    # String :
    def __str__(self):
        return self.str(0)

    def str(self, ident=0):
        # Get pod info 
        pod= self.asPod()
        status= pod.status()
        flags= pod.flags()
        values= pod.values()
        # Print 
        msg= self.family() +":"
        if len(status) > 0 :
            msg+= " "+ status
        if len( flags ) > 0 :
            msg+= ' ['+ ', '.join( str(i) for i in flags ) + "]"
        if len( values ) > 0 :
            msg+= ' ['+ ', '.join( str(i) for i in values ) + "]"
        # Print children
        msg+= strChildren( pod.children(), ident )
        return msg

def strChildren( children, ident ):
    msg= ""
    newLine= '\n'
    for i in range(ident) :
        newLine+= '  '
    newLine+= '- '
    
    for c in children :
        msg+= newLine + c.str(ident+1)
    return msg

class Pod(PodInterface): # Piece Of Data...

    def __init__( self, family= False, status= "", flags=[], values=[],  ):
        if not family :
            family= type(self).__name__
        self._family= family
        self._status= ''+status
        self._flags= flags
        if not bool(flags) :
            self._flags= []
        self._values= values
        if not bool(values) :
            self._values= []
        self._children= []

    def copy(self):
        cpy= type(self)()
        cpy._family= self._family
        cpy._status= ''+self.status()
        cpy._flags= [ a for a in self.flags() ]
        cpy._values= [ x for x in self.values() ]
        cpy._children= [ child.copy() for child in self.children() ]
        return cpy

    # Pod interface:

    def asPod(self):
        return self.copy()
   
    def fromPod(self, aPod):
        self._family= aPod.family()
        self._status= aPod.status()
        self._flags= aPod.flags()
        self._values= aPod.values()
        self._children= aPod.children()
        return self

    # Accessors:
    
    def family(self):
        return self._family
    
    def status(self):
        return self._status

    def flags(self):
        return self._flags

    def flag(self, i=1):
        assert( 0 < i and i <=  len(self.flags()) )
        return self._flags[i-1]
    
    def values(self):
        return self._values
        
    def value(self, i=1):
        assert( 0 < i and i <=  len(self.values()) )
        return self._values[i-1]

    def children(self):
        return self._children
        
    def child(self, i=1):
        assert( 0 < i and i <=  len(self.children()) )
        return self._children[i-1]
    
    # Construction:
    def setFamily(self, aStr):
        self._family= aStr
    
    def setStatus(self, aStr):
        self._status= aStr
    
    def setFlags(self, aListOfIntergers):
        self._flags= aListOfIntergers
    
    def setFlag(self, i, anInteger):
        self._flags[i-1]= anInteger
    
    def setValues(self, aListOfFloats):
        self._values= aListOfFloats
    
    # Children managment:
    def resetChildren(self):
        self._children= []

    def append(self, child):
        self._children.append(child)
        return self
    
    def pop(self, i=1):
        self._children.pop(i-1)

    # Serializer :

    def dump(self): 
        status= self.status()
        flags= self.flags()
        values= self.values()
        children= self.children()
        statusSize= len(status)
        flagsSize= len( flags )
        valuesSize= len( values )
        childrenSize= len( children )
        msg= f'{self.family()} - {statusSize} {flagsSize} {valuesSize} {childrenSize} :'
        if statusSize > 0 :
            msg+= ' '+ status
        if flagsSize > 0 :
            msg+= ' '+ ' '.join( str(i) for i in flags )
        if valuesSize > 0 :
            msg+= ' '+ ' '.join( str(i) for i in values )
        for c in children :
            msg+= "\n" + c.dump()
        return msg
    
    def load(self, buffer):
        if type(buffer) == str :
            buffer= buffer.splitlines()
        self.loadLines( buffer )
        return self
    
    def loadLines(self, buffer):
        
        # current line:
        line= buffer.pop(0)

        # Get meta data (type, name and structure sizes):
        metas, params= tuple( line.split(' :') )
        metas= tuple( metas.split(' - ') )
        self.setFamily( metas[0] )
        metas= [ int(x) for x in metas[1].split(' ') ]
        statusSize, attrsSize, valuesSize, childrenSize= tuple( metas )

        # Get status:
        status= ""
        if statusSize > 0 :
            status= params[1:1+statusSize]
            params= params[statusSize+1:]
        self.setStatus( status )
        
        # Get attributs and values:
        if attrsSize + valuesSize > 0 :
            params= params[1:].split(' ')
            attrs= [ int(params.pop(0)) for i in range(attrsSize) ]
            self.setFlags( attrs )
            values= [ float(params.pop(0)) for i in range(valuesSize) ]
            self.setValues( values )
        
        # load children
        self.resetChildren()

        for iChild in range(childrenSize) :
            child= Pod()
            buffer= child.loadLines(buffer)
            self._children.append( child )

        return buffer
