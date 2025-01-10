from . import artist
from .color import percentColor

import math, cairo
#from .geometry import Coord2, Segment

class SupportPNG( artist.SupportVoid ):
    def __init__(self, width= 800, height= 600, filePath= "shot-hacka.png" ):
        self._canvas= cairo.ImageSurface( cairo.Format.RGB24, width, height )
        self._width= width
        self._height= height
        self._filePath= filePath
        self.save( self._filePath )
    
    # Accessor: 
    def width(self):
        return self._width
    
    def height(self):
        return self._height
    
    def canvas(self):
        return self._canvas
    
    def filePath(self):
        return self._filePath

    # Control:
    def clear(self):
        self._canvas= cairo.ImageSurface( cairo.Format.RGB24, self._width, self._height )
    
    def render(self):
        return self._canvas
    
    def flip(self):
        if self._filePath :
            arts= self.save( self._filePath )
        else :
            arts= self.render()
        self.clear()
        return arts

    def save( self, filePath ):
        self._canvas.write_to_png( filePath )
        return

    # Drawing primitives:
    def traceLine( self, pixxA, pixyA, pixxB, pixyB, strokeColor, strokeWidth ):
        ctx = cairo.Context( self._canvas )
        r, g, b= percentColor(strokeColor)
        ctx.set_line_width(strokeWidth)
        ctx.move_to(pixxA, pixyA)
        ctx.line_to(pixxB, pixyB)
        ctx.set_source_rgb( r, g, b )
        ctx.stroke()
        return self
    
    def traceCircle( self, pixx, pixy, radius, strokeColor, strokeWidth ):
        ctx = cairo.Context( self._canvas )
        r, g, b= percentColor( strokeColor )
        ctx.set_line_width( strokeWidth )
        ctx.arc(pixx, pixy, radius, 0, 2.0*math.pi)
        ctx.set_source_rgb( r, g, b )
        ctx.stroke()
        return self

    def fillCircle( self, pixx, pixy, radius, fillColor ):
        ctx = cairo.Context( self._canvas )
        r, g, b= percentColor( fillColor )
        ctx.arc(pixx, pixy, radius, 0, 2.0*math.pi)
        ctx.set_source_rgb( r, g, b )
        ctx.fill()
        return self

    def drawCircle( self, pixx, pixy, radius, fillColor, strokeColor, strokeWidth):
        ctx = cairo.Context( self._canvas )
        sr, sg, sb= percentColor(strokeColor)
        fr, fg, fb= percentColor( fillColor )
        ctx.set_line_width(strokeWidth)
        ctx.arc(pixx, pixy, radius, 0, 2.0*math.pi)
        ctx.set_source_rgb( fr, fg, fb )
        ctx.fill_preserve()
        ctx.set_source_rgb( sr, sg, sb )
        ctx.stroke()
        return self
    
    def tracePolygon( self, pixXs, pixYs, strokeColor, strokeWidth ):
        ctx = cairo.Context( self._canvas )
        r, g, b= percentColor(strokeColor)
        ctx.set_line_width(strokeWidth)
        ctx.move_to( pixXs[0], pixYs[0] )
        for pixx, pixy in zip( pixXs[1:], pixYs[1:] ) :
            ctx.line_to(pixx, pixy)
        ctx.close_path()
        ctx.set_source_rgb( r, g, b )
        ctx.stroke()
        return self

    def fillPolygon( self, pixXs, pixYs, fillColor ):
        ctx = cairo.Context( self._canvas )
        r, g, b= percentColor( fillColor )
        ctx.move_to( pixXs[0], pixYs[0] )
        for pixx, pixy in zip( pixXs[1:], pixYs[1:] ) :
            ctx.line_to(pixx, pixy)
        ctx.close_path()
        ctx.set_source_rgb( r, g, b )
        ctx.fill()
        return self

    def drawPolygon( self, pixXs, pixYs, fillColor, strokeColor, strokeWidth ):
        ctx = cairo.Context( self._canvas )
        sr, sg, sb= percentColor(strokeColor)
        fr, fg, fb= percentColor( fillColor )
        ctx.set_line_width(2)
        ctx.move_to( pixXs[0], pixYs[0] )
        for pixx, pixy in zip( pixXs[1:], pixYs[1:] ) :
            ctx.line_to(pixx, pixy)
        ctx.close_path()
        ctx.set_source_rgb( fr, fg, fb )
        ctx.fill_preserve()
        ctx.set_source_rgb( sr, sg, sb )
        ctx.stroke()
        return self


























class Rgb:
    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r= r
        self.g= g
        self.b= b

class Pencil:

    def initializeSurface(self):
        self._surface= cairo.SVGSurface("shot-pencil", 800, 600)
        return 800, 600
    
    # Drawing primitives (level screen):
    def initBackground(self, color ):
        width, height= self.initializeSurface()
        ctx = cairo.Context(self._surface)
        ctx.move_to(0, 0)
        ctx.line_to(0, height)
        ctx.line_to(width, height)
        ctx.line_to(width, 0)
        ctx.close_path()
        #ctx.line_to(0, 0)
        ctx.set_source_rgba(color.r, color.g, color.b, 1.0)
        ctx.fill_preserve()
        ctx.set_line_width(8)
        ctx.set_source_rgba(0.0, 0.0, 0.0, 0.4)
        ctx.stroke()
        return width, height
    
    # Drawing primitives (level screen):
    def tracePoint( self, pixx, pixy, color ):
        ctx = cairo.Context(self._surface)
        #ctx.set_line_width(10)
        pixRadius= 2 #self._epsilon * self._scale
        ctx.arc(pixx, pixy, pixRadius, 0, 2.0*math.pi)
        ctx.set_source_rgb( color.r, color.g, color.b )
        ctx.fill()

    def traceLine( self, pixxA, pixyA, pixxB, pixyB, color ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(2)
        ctx.move_to(pixxA, pixyA)
        ctx.line_to(pixxB, pixyB)
        ctx.set_source_rgb( color.r, color.g, color.b )
        ctx.stroke()

    def traceCircle( self, pixx, pixy, radius, color ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(2)
        ctx.arc(pixx, pixy, radius, 0, 2.0*math.pi)
        ctx.set_source_rgb( color.r, color.g, color.b )
        ctx.stroke()

    def fillCircle( self, pixx, pixy, radius, color ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(2)
        ctx.arc(pixx, pixy, radius, 0, 2.0*math.pi)
        ctx.set_source_rgb( color.r, color.g, color.b )
        ctx.fill()
    
    def drawCircle( self, pixx, pixy, radius, colorFill, colorTrace ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(2)
        ctx.arc(pixx, pixy, radius, 0, 2.0*math.pi)
        ctx.set_source_rgb( colorFill.r, colorFill.g, colorFill.b )
        ctx.fill_preserve()
        ctx.set_source_rgb( colorTrace.r, colorTrace.g, colorTrace.b )
        ctx.stroke()
    
    def tracePolygon( self, pixxs, pixys, color ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(2)
        ctx.move_to( pixxs[0], pixys[0] )
        for pixx, pixy in zip( pixxs[1:], pixys[1:] ) :
            ctx.line_to(pixx, pixy)
        ctx.close_path()
        ctx.set_source_rgb( color.r, color.g, color.b )
        ctx.stroke()
    
    def fillPolygon( self, pixxs, pixys, color ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(2)
        ctx.move_to( pixxs[0], pixys[0] )
        for pixx, pixy in zip( pixxs[1:], pixys[1:] ) :
            ctx.line_to(pixx, pixy)
        ctx.close_path()
        ctx.set_source_rgb( color.r, color.g, color.b )
        ctx.fill()
    
    def drawPolygon( self, pixxs, pixys, colorFill, colorTrace ):
        ctx = cairo.Context(self._surface)
        ctx.set_line_width(2)
        ctx.move_to( pixxs[0], pixys[0] )
        for pixx, pixy in zip( pixxs[1:], pixys[1:] ) :
            ctx.line_to(pixx, pixy)
        ctx.close_path()
        ctx.set_source_rgb( colorFill.r, colorFill.g, colorFill.b )
        ctx.fill_preserve()
        ctx.set_source_rgb( colorTrace.r, colorTrace.g, colorTrace.b )
        ctx.stroke()
