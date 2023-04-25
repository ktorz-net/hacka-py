
class Pod(): # Piece Of Data...

    def __init__( self, status= "pod", attributes=[], values=[] ):
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
        cpy._status= ''+self.status()
        cpy._attrs= [ a for a in self.attributes() ]
        cpy._values= [ x for x in self.values() ]
        cpy._children= [ child.copy() for child in self.children() ]
        return cpy

    # Accessors:
    def pod(self):
        return self
    
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
    
    # Modification:
    def setFrom(self, aPod):
        self._status= aPod.status()
        self._attrs= aPod.attributes()
        self._values= aPod.values()
        self._children= aPod.children()
        return self

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

    def loadChild( self, childBuffer ):
        child= Pod()
        self._children.append( child.load(childBuffer) )
        return child

    # Serializer :
    def dump(self, ident= 0):
        newLine= '\n'
        for i in range(ident) :
            newLine+= '  '
        newLine+= '- '
        status= self.status()
        attrs= self.attributes()
        values= self.values()
        children= self.children()
        statusSize= len(status)
        attrsSize= len( attrs )
        valuesSize= len( values )
        childrenSize= len( children )
        msg= f'{statusSize} {attrsSize} {valuesSize} {childrenSize} :'
        if statusSize > 0 :
            msg+= ' '+ status
        if attrsSize > 0 :
            msg+= ' '+ ' '.join( str(i) for i in attrs )
        if valuesSize > 0 :
            msg+= ' '+ ' '.join( str(i) for i in values )
        for c in children :
            msg+= newLine + c.dump(ident+1)
        return msg
    
    def load(self, buffer):
        print( f">> L O A D |\n{buffer}\n|")
        if type(buffer) == str :
            buffer= buffer.split('\n')
        line= buffer.pop(0)

        print( f">> {line}")

        # Get meta data (type, name and structure sizes):
        metas, params= tuple( line.split(' :') )
        metas= [ int(x) for x in metas.split(' ') ]
        print( f">> metas: {metas}")
        statusSize, attrsSize, valuesSize, childrenSize= tuple( metas )

        # Get status:
        status= ""
        if statusSize > 0 :
            status= params[1:1+statusSize]
            params= params[statusSize+1:]
        self.setStatus( status )
    
        print( f">> status: {self.status()}")
        print( f">> params: {params}")
        
        # Get attributs and values:
        if attrsSize + valuesSize > 0 :
            params= params[1:].split(' ')
            attrs= [ int(params.pop(0)) for i in range(attrsSize) ]
            self.setAttributes( attrs )
            values= [ float(params.pop(0)) for i in range(valuesSize) ]
            self.setValues( values )
        
        # load children
        self.resetChildren()
        if childrenSize > 0 :
            iChild= 0
            while buffer and buffer[0][0:2] == '- ' :
                childBuffer= [ buffer.pop(0)[2:] ]
                while buffer and buffer[0][0:2] == '  ' :
                   childBuffer.append( buffer.pop(0)[2:] )
                self.loadChild( childBuffer )
        return self
    
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
        statusSize= 0
        if status != '' :
            statusSize= status.count(' ')+1
        attrsSize= len( attrs )
        valuesSize= len( values )
        msg= status
        if attrsSize > 0 :
            msg+= ' ['+ ', '.join( str(i) for i in attrs ) + "]"
        if valuesSize > 0 :
            msg+= ' ('+ ', '.join( str(i) for i in values ) + "]"
        for c in children :
            msg+= newLine + c.str(ident+1)
        return msg
