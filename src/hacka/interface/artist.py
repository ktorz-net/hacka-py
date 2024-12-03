class SupportVoid():
    # Control:
    def flip(self):
        pass

    # Drawing primitives:
    def tracePoint( self, pixx, pixy, color ):
        pass

    def traceLine( self, pixxA, pixyA, pixxB, pixyB, color ):
        pass

    def traceCircle( self, pixx, pixy, radius, color ):
        pass

    def fillCircle( self, pixx, pixy, radius, color ):
        pass

    def drawCircle( self, pixx, pixy, radius, colorFill, colorTrace):
        pass

    def tracePolygon( self, pixXs, pixYs, color ):
        pass

    def fillPolygon( self, pixXs, pixYs, color ):
        pass

    def drawPolygon( self, pixXs, pixYs, colorFill, colorTrace ):
        pass

class Artist():
    def __init__(self, frame= SupportVoid(), width=1200, height=800 ):
        #  Initialize support:
        self._frame= frame
        # Initialize Frame :
        self._dwidth= width/2
        self._dheight= height/2
        self._x= 0.0
        self._y= 0.0
        self._scale= 100.0
    
    # Accessor:
    def support(self):
        return self._frame

    # Transformation World <-> Frame
    def toFrame(self, x, y ):
        dx= (x-self._x)*self._scale
        dy= (y-self._y)*-self._scale
        return dx+self._dwidth, dy+self._dheight

    def xToFrame(self, x ):
        return (x-self._x)*self._scale + self._dwidth

    def yToFrame(self, y ):
        return (y-self._y)*-self._scale + self._dheight

    def toWorld(self, pixx, pixy):
        return 0, 0

    # Drawing primitives:
    def tracePoint( self, x, y, color= 0x020202 ):
        pixx, pixy= self.toFrame( x, y )
        self._frame.tracePoint( pixx, pixy, color )
        return self

    def traceLine( self, ax, ay, bx, by, color= 0x020202 ):
        pixxA, pixyA= self.toFrame( ax, ay )
        pixxB, pixyB= self.toFrame( bx, by )
        self._frame.traceLine( pixxA, pixyA, pixxB, pixyB, color)
        return self

    def traceCircle( self, x, y, radius, color= 0x020202 ):
        pixx, pixy= self.toFrame(x, y)
        self._frame.traceCircle( pixx, pixy, radius*self._scale, color)
        return self

    def fillCircle( self, x, y, radius, color= 0x020202 ):
        pixx, pixy= self.toFrame(x, y)
        self._frame.fillCircle( pixx, pixy, radius*self._scale, color)
        return self

    def drawCircle( self, x, y, radius, colorFill= 0xE2E2E2, colorTrace= 0x020202 ):
        pixx, pixy= self.toFrame(x, y)
        self._frame.drawCircle( pixx, pixy, radius*self._scale, colorFill, colorTrace)
        return self

    def tracePolygon( self, coordXs, coordYs, color= 0x020202 ):
        self._frame.tracePolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            color
        )
        return self

    def fillPolygon( self, coordXs, coordYs, color= 0x020202 ):
        self._frame.fillPolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            color
        )
        return self

    def drawPolygon( self, coordXs, coordYs, colorFill= 0xE2E2E2, colorTrace= 0x020202 ):
        self._frame.drawPolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            colorFill, colorTrace
        )
        return self

    # Drawing frame:
    def drawFrameGrid( self, step= 10.0, color=0x080808 ):
        pixX, pixY= self.toFrame( 0, 0 )
        pixStep= step*self._scale

        while pixX > pixStep :
            pixX-= pixStep
        
        while pixY > pixStep :
            pixY-= pixStep
        
        width= self._dwidth*2.0
        height= self._dheight*2.0

        # Vertical
        for i in range( (int)(width/pixStep)+1 ) :
            self._frame.traceLine( pixX+(pixStep*i), 10, pixX+(pixStep*i), height-10, color )
        # Horizontal
        for i in range( (int)(height/pixStep)+1 ) :
            self._frame.traceLine( 10, pixY+(pixStep*i), width-10, pixY+(pixStep*i), color )
        return self

    def drawFrameAxes( self ):
        self.traceLine(  0, 0, 1, 0, 0xE26060 )
        self.traceLine(  0, 0, 0, 1, 0x60E260 )
        self.tracePoint( 0, 0, 0x0606E2 )
        return self
