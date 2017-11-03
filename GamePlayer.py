"""
GamePlayer class

Implements a gameplayer token with attributes for  position and direction,
and methods for movment and direction-change.

Instance Variables accessed and modified by the methods...
  direction: 0..3 for NESW
  xpos: 0..4
  ypos: 0..4
"""

class gameplayer:

    def __init__(self,debugflag) :
        self.direction = 0
        self.xpos = 0
        self.ypos = 0
        self.debug = debugflag

    def move(self):
        '''
        Move one step in current direction. Prevent movement outside range 0..4
        '''
        (xpos,ypos,direction) = (self.xpos,self.ypos,self.direction)      #for verbosity reduction

        if self.debug:
            print "pre-move x,y,d: {0},{1},{2}".format(xpos,ypos,direction)

        # Effect of moving 1 step in each direction on xpos and ypos :
        xmap = { 0: xpos, 1: xpos+1, 2: xpos, 3: xpos-1 }
        ymap = { 0: ypos+1, 1: ypos, 2: ypos-1, 3: ypos }

        #The following could all be done in one or two lines; broken up for legibility.
        xpos = xmap.get(direction, xpos)
        ypos = ymap.get(direction, ypos)

        (xpos,ypos) = (min(xpos, 4), min(ypos,4))
        (xpos,ypos) = (max(xpos, 0), max(ypos,0))

        (self.xpos,self.ypos,self.direction) = (xpos,ypos,direction)
        if self.debug:
            print "post-move x,y,d: {0},{1},{2}".format(self.xpos,self.ypos,self.direction)

    def turnleft(self):
        '''
        Turn anticlockwise by decrementing the direction integer. wrap back to +3 when we go from N to W.
        '''
        dmap = {0:3, 1:0, 2:1, 3:2}
        self.direction = dmap.get(self.direction, self.direction)

    def turnright(self):
        '''
        Turn clockwise by incrementing the direction integer. wrap back to 0 when we go from W to N.
        '''
        dmap = {0:1, 1:2, 2:3, 3:0}
        self.direction = dmap.get(self.direction, self.direction)

    def getstate(self):
        (xpos,ypos,direction) = (self.xpos,self.ypos,self.direction)      
        return "{0} {1} {2}".format(xpos, ypos, { 0:'N', 1:'E', 2:'S', 3:'W' }[direction])

    '''
    Main control function for the player. Input a string of [M,R,L] characters causing the token
    to move, turn left and turn right respectively.
    '''

    def obey(self,commandstring):
        # Loop over each character in commandstring and execute. PO says no validation required. 
        for char in commandstring:
            if char == "M":
                self.move();
            elif char == "R":
                self.turnright();
            elif char == "L":
                self.turnleft()

    def _RESET(self):
        (self.xpos, self.ypos, self.direction) = (0,0,0)
