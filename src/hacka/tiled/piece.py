from .shape import Shape

class Piece(Shape):

    # Initialization Destruction:
    def __init__( self, num= 0, type= 0, center= (0.0, 0.0), size= 1.0 ):
        super().__init__(num, type, center, size)
