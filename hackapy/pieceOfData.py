
class PodInterface() :

    # Pod interface:
    def asPod(self, name="Cell"):
        # Should return a Pod describing self.
        pass
    
    def fromPod(self, aPod):
        # Should regenerate self form the pod description
        pass
        #return self

class Pod(): # Piece Of Data...

    def __init__( self, family= False, attributes=[], values=[], status= "" ):
        if not family :
            family= type(self).__name__
        self._family= family
        self._status= ''+status
        self._attrs= attributes
        if not bool(attributes) :
            self._attrs= []
        self._values= values
        if not bool(values) :
            self._values= []
        self._children= []

    def copy(self):
        cpy= type(self)()
        cpy._family= self._family
        cpy._status= ''+self.status()
        cpy._attrs= [ a for a in self.attributes() ]
        cpy._values= [ x for x in self.values() ]
        cpy._children= [ child.copy() for child in self.children() ]
        return cpy

    # Pod interface:

    def asPod(self):
        return self.copy()
   
    def fromPod(self, aPod):
        self._family= aPod.family()
        self._status= aPod.status()
        self._attrs= aPod.attributes()
        self._values= aPod.values()
        self._children= aPod.children()
        return self

    # Accessors:
    
    def family(self):
        return self._family
    
    def status(self):
        return self._status

    def attributes(self):
        return self._attrs
        
    def attribute(self, i):
        assert( 0 < i and i <=  len(self.attributes()) )
        return self._attrs[i-1]
    
    def values(self):
        return self._values
        
    def value(self, i):
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
    
    def setAttributes(self, aListOfIntergers):
        self._attrs= aListOfIntergers
    
    def setAttribute(self, i, anInteger):
        self._attrs[i-1]= anInteger
    
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
        attrs= self.attributes()
        values= self.values()
        children= self.children()
        statusSize= len(status)
        attrsSize= len( attrs )
        valuesSize= len( values )
        childrenSize= len( children )
        msg= f'{self.family()} - {statusSize} {attrsSize} {valuesSize} {childrenSize} :'
        if statusSize > 0 :
            msg+= ' '+ status
        if attrsSize > 0 :
            msg+= ' '+ ' '.join( str(i) for i in attrs )
        if valuesSize > 0 :
            msg+= ' '+ ' '.join( str(i) for i in values )
        for c in children :
            msg+= "\n" + c.dump()
        return msg
    
    def load(self, buffer):
        self.loadLines( buffer.split('\n') )
        return self
    
    def loadLines(self, buffer):
        print( f"< LOAD {buffer}\n>" )
        if type(buffer) == str :
            buffer= buffer.split('\n')
        
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
            self.setAttributes( attrs )
            values= [ float(params.pop(0)) for i in range(valuesSize) ]
            self.setValues( values )
        
        # load children
        self.resetChildren()

        for iChild in range(childrenSize) :
            child= Pod()
            buffer= child.loadLines(buffer)
            self._children.append( child )

        return buffer
    
    # String :
    def __str__(self):
        return self.str(0)
    
    def str(self, ident):
        newLine= '\n'
        for i in range(ident) :
            newLine+= '  '
        newLine+= '- '
        status= self.status()
        attrs= self.attributes()
        values= self.values()
        children= self.children()
        msg= self.family() +":"
        if len( attrs ) > 0 :
            msg+= ' flags: ['+ ', '.join( str(i) for i in attrs ) + "]"
        if len( values ) > 0 :
            msg+= ' values: ['+ ', '.join( str(i) for i in values ) + "]"
        if len(status) > 0 :
            msg+= " status: ["+ status +"]"
        for c in children :
            msg+= newLine + c.str(ident+1)
        return msg
