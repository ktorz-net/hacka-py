#----------------------------------------------------------------------------------------------------------#
#                                   H A C K A P Y  :  P O D
#
# Pod : Piece Of Data
# An HackaGame element ([hackagames](https://bitbucket.org/imt-mobisyst/hackagames))
# 
#----------------------------------------------------------------------------------------------------------#

class Podable() : # Can be transform into Pod (Piece Of Data)

    # Pod accessor:
    def intAttributes(self):
        # Should return the list of integer attributes (max 256)
        return []
    
    def floatAttributes(self):
        # Should return the list of floating point attributes (max 256)
        return []
    
    def wordAttributes(self):
        # Should return the list of word attributes (max 256 words of 256 lenght)
        return []

    def children(self):
        # Should return the list of Podable children
        return []

    def initializeFrom( self, aPodable ):
        # Should initialize self with aPodable [wordAttributes(), intAttributes(), floatAttributes() and children()]
        return self

    def asPod(self):
        return Pod().initializeFrom(self)
    
    # Serializer :
    def dump(self):
        # Element to dumps:
        words= self.wordAttributes()
        integers= self.intAttributes()
        values= self.floatAttributes()
        children= self.children()

        wordSize= len(words)
        maxWordLen= 0
        for w in words :
            maxWordLen= max( maxWordLen, len(w) )
        intSize= len( integers )
        valuesSize= len( values )
        childrenSize= len( self.children() )

        buffer= f'{wordSize} {maxWordLen} {intSize} {valuesSize} {childrenSize} :'
        if wordSize > 0 :
            buffer+= ' '+ ' '.join( str(i) for i in words )
        if intSize > 0 :
            buffer+= ' '+ ' '.join( str(i) for i in integers )
        if valuesSize > 0 :
            buffer+= ' '+ ' '.join( str(i) for i in values )
        for c in children :
            buffer+= "\n" + c.dump()
        return buffer

    def load(self, buffer):
        pod= Pod().load(buffer)
        self.initializeFrom(pod)
        return self

class Pod(Podable): # Piece Of Data...

    def __init__( self, words=[], integers=[], values=[], podChildren=[]  ):
        # word attributes
        if type( words ) == str :
            self._words= [words]
        else: 
            self._words= list(words)
        self._integers= list(integers)
        self._values= list(values)
        self._children= list(podChildren)

    # Podable accessor:
    def wordAttributes(self):
        return self._words
    
    def intAttributes(self):
        return self._integers
    
    def floatAttributes(self):
        return self._values
    
    def children(self):
        return self._children
    
    # Other accessor:
    def word(self, i=1):
        return self._words[i-1]
    
    def intAttribute(self, i=1):
        return self._integers[i-1]
    
    def floatAttribute(self, i=1):
        return self._values[i-1]
    
    def child(self, i=1):
        return self._children[i-1]
    
    # Initialize:
    def initializeFrom( self, aPodable ):
        self._words= aPodable.wordAttributes()
        self._integers= aPodable.intAttributes()
        self._values= aPodable.floatAttributes()
        self._children= [
            Pod().initializeFrom( child )
            for child in aPodable.children()
        ]
        return self
    
    # Construction:
    def setWords(self, aListOfStr):
        self._words= aListOfStr
    
    def setIntAttributes(self, aListOfInt):
        self._integers= aListOfInt
    
    def setFloatAttributes(self, aListOfFloat):
        self._values= aListOfFloat
    
    def resetChildren(self):
        self._children= []

    def appendChild( self, child ):
        self._children.append( child )
    
    def popChild(self, i=1):
        self._children.pop(i-1)

    # Coping:
    def copy(self):
        cpy= type(self)()
        cpy._words= [ ''+w for w in self.wordAttributes() ]
        cpy._integers= [ i for i in self.intAttributes() ]
        cpy._values= [ f for f in self.floatAttributes() ]
        cpy._children= [ child.copy() for child in self.children() ]
        return cpy
    
    # Serializer :
    def load(self, buffer):
        if type(buffer) == str :
            buffer= buffer.splitlines()
        self.loadLines( buffer )
        return self
    
    def loadLines(self, buffer):
        # current line:
        line= buffer.pop(0)

        # Get meta data (type, name and structure sizes):
        metas, elements= tuple( line.split(' :') )
        metas= [ int(x) for x in metas.split(' ') ]
        wordSize, maxWordLen, intSize, valuesSize, childrenSize= tuple( metas )
        elements= elements.split(" ")[1:]

        assert( len(elements) == wordSize + intSize + valuesSize )

        # Get words:
        self._words= [ w for w in elements[:wordSize] ]
        wiSize= wordSize+intSize
        self._integers= [ int(i) for i in elements[wordSize:wiSize] ]
        self._values= [ float(f) for f in elements[wiSize:] ]
        
        # load children
        self.resetChildren()
        for iChild in range(childrenSize) :
            child= Pod()
            buffer= child.loadLines(buffer)
            self._children.append( child )

        return buffer

    # Comparison :
    def __eq__(self, another):
        return ( list(self.wordAttributes()) == list(another.wordAttributes())
                and list(self.intAttributes()) == list(another.intAttributes())
                and list(self.floatAttributes()) == list(another.floatAttributes())
        )

    # String :
    def __str__(self):
        return self.str(0)

    def str(self, ident=0):
        # Get pod info
        words= self.wordAttributes()
        flags= self.intAttributes()
        values= self.floatAttributes()

        # Print
        if len( words ) == 1 :
            msg= words[0] +":"
        elif len( words ) > 1 :
            msg= words[0] +": " + ", ".join( words[1:] )
        else :
            msg= ":"
        if len( flags ) > 0 :
            msg+= ' ['+ ', '.join( str(i) for i in flags ) + "]"
        if len( values ) > 0 :
            msg+= ' ['+ ', '.join( str(i) for i in values ) + "]"
        # Print children
        msg+= self.strChildren( ident )
        return msg
    
    def strChildren( self, ident ):
        msg= ""
        newLine= '\n'
        for i in range(ident) :
            newLine+= '  '
        newLine+= '- '
        
        for c in self.children() :
            msg+= newLine + c.str(ident+1)
        return msg
