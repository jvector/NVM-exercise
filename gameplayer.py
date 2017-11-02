"""
Variables accessed and modified by the functions...
  direction: 0..3 for NESW
  xpos: 0..4
  ypos: 0..4
"""

direction = 0
xpos = 0
ypos = 0

debug = 0

def move():
    '''
    Move one step in current direction. Prevent movement outside range 0..4
    '''
    global xpos, ypos

    # Effect of moving 1 step in each direction on xpos and ypos :
    xmap = { 0: xpos, 1: xpos+1, 2: xpos, 3: xpos-1 }
    ymap = { 0: ypos+1, 1: ypos, 2: ypos-1, 3: ypos }

    #The following could all be done in one or two lines; broken up for legibility.
    xpos = xmap.get(direction, xpos)
    ypos = ymap.get(direction, ypos)

    (xpos,ypos) = (min(xpos, 4), min(ypos,4))
    (xpos,ypos) = (max(xpos, 0), max(ypos,0))

    if debug:
        print 'Move : ' + getstate()

def turnleft():
    '''
    Turn anticlockwise by decrementing the direction integer. wrap back to +3 when we go from N to W.
    '''
    global direction
    dmap = {0:3, 1:0, 2:1, 3:2}
    direction = dmap.get(direction, direction)

    if debug:
        print 'Left : ' + getstate()

def turnright():
    '''
    Turn clockwise by incrementing the direction integer. wrap back to 0 when we go from W to N.
    '''
    global direction
    dmap = {0:1, 1:2, 2:3, 3:0}
    direction = dmap.get(direction, direction)

    if debug:
        print 'Right : ' + getstate()

def getstate():
    return "{0} {1} {2}".format(xpos, ypos, { 0:'N', 1:'E', 2:'S', 3:'W' }[direction])

'''
Main control function for the player. Input a string of [M,R,L] characters causing the token
to move, turn left and turn right respectively.
'''

def obey(commandstring):
    # Loop over each character in commandstring and execute. PO says no validation required. 
    for char in commandstring:
        if char == "M":
            move();
        elif char == "R":
            turnright();
        elif char == "L":
            turnleft()

def _RESET():
    global xpos, ypos, direction
    (xpos, ypos, direction) = (0,0,0)
    if debug:
        print 'RESET : ' + getstate()

