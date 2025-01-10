class SupportVoid():

    # Accessor:
    def width(self):
        return 1200
    
    def height(self):
        return 800
    
    # Control:
    def clear(self):
        pass
    
    def render( self ):
        return None
    
    def flip( self ):
        old= self.render()
        self.clear()
        return old
    
    # Drawing primitives:
    def traceLine( self, pixxA, pixyA, pixxB, pixyB, strokeColor, strokeWidth ):
        pass

    def traceCircle( self, pixx, pixy, radius, strokeColor, strokeWidth ):
        pass

    def fillCircle( self, pixx, pixy, radius, fillColor ):
        pass

    def drawCircle( self, pixx, pixy, radius, fillColor, strokeColor, strokeWidth):
        pass

    def tracePolygon( self, pixXs, pixYs, strokeColor, strokeWidth ):
        pass

    def fillPolygon( self, pixXs, pixYs, fillColor ):
        pass

    def drawPolygon( self, pixXs, pixYs, fillColor, strokeColor, strokeWidth ):
        pass

class Artist():
    def __init__(self, frame= SupportVoid() ):
        #  Initialize support:
        self._frame= frame
        # Initialize brush :
        self._backgroundColor= 0xffbb55
        self._fillColor= 0xbb7711
        self._strokeColor= 0xaa1100
        self._strokeWidth= 4
        # Initialize Frame :
        self._x= 0.0
        self._y= 0.0
        self._scale= 100.0
        self.flip()
    
    # Accessor:
    def support(self):
        return self._frame

    def render( self ):
        return self._frame.render()

    # Transformation World <-> Frame
    def toFrame(self, x, y ):
        dwidth= self._frame.width()*0.5
        dheight= self._frame.height()*0.5
        dx= (x-self._x)*self._scale
        dy= (y-self._y)*-self._scale
        return dx+dwidth, dy+dheight

    def xToFrame(self, x ):
        dwidth= self._frame.width()*0.5
        return (x-self._x)*self._scale + dwidth

    def yToFrame(self, y ):
        dheight= self._frame.height()*0.5
        return (y-self._y)*-self._scale + dheight

    def toWorld(self, pixx, pixy):
        return 0, 0

    # Drawing primitives:
    def tracePoint( self, x, y ):
        pixx, pixy= self.toFrame( x, y )
        self._frame.fillCircle( pixx, pixy, self._strokeWidth, self._strokeColor )
        return self

    def traceLine( self, ax, ay, bx, by ):
        pixxA, pixyA= self.toFrame( ax, ay )
        pixxB, pixyB= self.toFrame( bx, by )
        self._frame.traceLine( pixxA, pixyA, pixxB, pixyB, self._strokeColor, self._strokeWidth)
        return self

    def traceCircle( self, x, y, radius):
        pixx, pixy= self.toFrame(x, y)
        self._frame.traceCircle( pixx, pixy, radius*self._scale, self._strokeColor, self._strokeWidth)
        return self

    def fillCircle( self, x, y, radius):
        pixx, pixy= self.toFrame(x, y)
        self._frame.fillCircle( pixx, pixy, radius*self._scale, self._fillColor )
        return self

    def drawCircle( self, x, y, radius ):
        pixx, pixy= self.toFrame( x, y )
        self._frame.drawCircle( pixx, pixy, radius*self._scale, self._fillColor, self._strokeColor, self._strokeWidth )
        return self

    def tracePolygon( self, coordXs, coordYs ):
        self._frame.tracePolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            self._strokeColor, self._strokeWidth
        )
        return self

    def fillPolygon( self, coordXs, coordYs ):
        self._frame.fillPolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            self._fillColor
        )
        return self

    def drawPolygon( self, coordXs, coordYs ):
        self._frame.drawPolygon(
            [ self.xToFrame( x ) for x in coordXs ],
            [ self.yToFrame( y ) for y in coordYs ],
            self._fillColor, self._strokeColor, self._strokeWidth
        )
        return self

    # Drawing frame:
    def drawFrameGrid( self, step= 1.0, color=None ):
        
        pixX, pixY= self.toFrame( 0, 0 )
        pixStep= step*self._scale

        while pixX > pixStep :
            pixX-= pixStep
        
        while pixY > pixStep :
            pixY-= pixStep
        
        width= self._frame.width()
        height= self._frame.height()

        if not color :
            color= 0x080800
        
        # Vertical
        for i in range( (int)(width/pixStep)+1 ) :
            self._frame.traceLine( pixX+(pixStep*i), 10, pixX+(pixStep*i), height-10, color, 2 )
        # Horizontal
        for i in range( (int)(height/pixStep)+1 ) :
            self._frame.traceLine( 10, pixY+(pixStep*i), width-10, pixY+(pixStep*i), color, 2 )
        return self

    def drawFrameAxes( self ):
        strokeColor= self._strokeColor
        self._strokeColor= 0xE26060
        self.traceLine(  0, 0, 1, 0 )
        self._strokeColor= 0x60E260
        self.traceLine(  0, 0, 0, 1 )
        self._strokeColor= 0x0606E2
        self.tracePoint( 0, 0 )
        self._strokeColor= strokeColor
        return self
    
    # Control:
    def flip(self):
        h= self._frame.height()
        w= self._frame.width()
        old= self._frame.flip()
        self._frame.fillPolygon(
            [0, 0, w, w],
            [0, h, h, 0],
            self._backgroundColor
        )
        return old

