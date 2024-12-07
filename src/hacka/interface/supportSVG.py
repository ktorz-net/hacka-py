from . import artist
from .color import webColor

class SupportSVG( artist.SupportVoid ):
    def __init__(self, width= 800, height= 600 ):
        self._width= width
        self._height= height
        self._canvas= []
    
    # Accessor: 
    def width(self):
        return self._width
    
    def height(self):
        return self._height
    
    def canvas(self):
        return self._canvas
    
    def render(self):
        return f'<svg width="{self.width()}" height="{self.height()}">\n' + '\n'.join( self._canvas + ['</svg>'] ) 
    
    # Control:
    def flip(self):
        oldConvas= self._canvas
        self._canvas= []
        return oldConvas

    # Drawing primitives:
    def traceLine( self, pixxA, pixyA, pixxB, pixyB, strokeColor, strokeWidth ):
        self._canvas.append( f'<line x1="{pixxA}" y1="{pixyA}" x2="{pixxB}" y2="{pixyB}" style="stroke:{webColor(strokeColor)};stroke-width:{strokeWidth}"/>' )
        return self

    def traceCircle( self, pixx, pixy, radius, strokeColor, strokeWidth ):
        self._canvas.append( f'<circle r="{radius}" cx="{pixx}" cy="{pixy}" fill="none" stroke="{webColor(strokeColor)}" stroke-width="{strokeWidth}" />' )
        return self

    def fillCircle( self, pixx, pixy, radius, fillColor ):
        self._canvas.append( f'<circle r="{radius}" cx="{pixx}" cy="{pixy}" fill="{webColor(fillColor)}" />' )
        return self

    def drawCircle( self, pixx, pixy, radius, fillColor, strokeColor, strokeWidth):
        self._canvas.append( f'<circle r="{radius}" cx="{pixx}" cy="{pixy}" fill="{webColor(fillColor)}" stroke="{webColor(strokeColor)}" stroke-width="{strokeWidth}" />' )
        return self
    
    def tracePolygon( self, pixXs, pixYs, strokeColor, strokeWidth ):
        points= " ".join( [ f'{x},{y}' for x, y in zip(pixXs, pixYs) ] )
        self._canvas.append( f'<polygon points="{points}" style="fill:none;stroke:{webColor(strokeColor)};stroke-width:{strokeWidth}" />' )
        return self

    def fillPolygon( self, pixXs, pixYs, fillColor ):
        points= " ".join( [ f'{x},{y}' for x, y in zip(pixXs, pixYs) ] )
        self._canvas.append( f'<polygon points="{points}" fill="{webColor(fillColor)}" />' )
        return self

    def drawPolygon( self, pixXs, pixYs, fillColor, strokeColor, strokeWidth ):
        points= " ".join( [ f'{x},{y}' for x, y in zip(pixXs, pixYs) ] )
        self._canvas.append( f'<polygon points="{points}" style="fill:{webColor(fillColor)};stroke:{webColor(strokeColor)};stroke-width:{strokeWidth}" />' )
        return self