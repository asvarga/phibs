'''
Created on Aug 4, 2014

@author: avarga
'''

from numpy import array
import sys

sides = [array([0,-1]),array([0,1]),array([-1,0]),array([1,0])]
spacer = '-'*16
welcome = """
 ===========
  P H I B S
 ===========
 
Find a friend to play this game with and choose a board size. 

Players make moves by adding phibs to the board. A phib can:
1. Add a 1 to the player's team.
2. Increase one of the player's numbers by 1.
3. Cancel out an opponent's 1.
4. Die pathetically against an opponent's number greater than 1.

Players move simultaneously by choosing a square, and either promising
not to change their minds, or writing down their choice.

Top left is (0, 0).

Between moves, the board runs one step at a time until it comes to a halt.
Each step, every number is pushed a certain distance by up to 4 neighbors.

 0 0 0
 2 x 0    Here, the x will be pushed East by 2, because of the 2 to it's West.
 0 0 0
 
 0 1 0
 2 x 2    Here, the x will be pushed South by 1, because pushes summate.
 0 0 0
 
 0 0 0 0    0 0 0 0
 0 1 1 0 -> 1 0 0 1    All pushes occur simultaneously.
 0 0 0 0    0 0 0 0
 
If 2 numbers land on the same square:
Each team sums their total phibs that landed on that square.
If one team has the highest sum for that square, they survive, and the rest die.
Otherwise, all phibs die.

Phibs pushed off the board die.
First player to create a 10 wins. Or something.

Type 'quit' at any time to quit.
"""
    
def get(o, k, d=None):
    return o[k] if k in o else d
        
class Phib:
    def __init__(self, val=1, pos=None, team=0):
        self.val = val
        self.pos = array([0,0]) if pos==None else pos
        self.team = team
        
    def preJump(self, phibs):
        #if self.species == FROG:
        self.newPos = sum([-phib.val*d for (d,phib) in [(d, get(phibs, tuple(self.pos+d))) for d in sides] if phib], self.pos)
        
    def jump(self):
        if hasattr(self, 'newPos'):
            moved = any(self.pos != self.newPos)
            self.pos = self.newPos
            return moved
        return False
        
    def __str__(self):
        if self.team:
            return '|'+str(self.val)+'|'
        else:
            return '{'+str(self.val)+'}'

class Board:
    def __init__(self, phibs=None, w=0, h=0, board=None):
        if phibs != None and len(phibs) > 0:
            self.phibs = phibs
            self.h = h
            self.w = w
        elif board != None:
            self.phibs = {(x,y):Phib(val=v,pos=array([x,y])) for (y,row) in enumerate(board) for (x,v) in enumerate(row) if v>0}
            self.h = len(board)
            self.w = len(board[0])
        else:
            self.phibs = {}
            self.h = h
            self.w = w
        self.collisions = []
        
    def step(self):
        [phib.preJump(self.phibs) for phib in self.phibs.values()]
        moved = any([phib.jump() for phib in self.phibs.values()])
            
        oldPhibs = self.phibs.values()
        self.phibs = {}
        for phib in oldPhibs:
            self.addPhib(phib)
                    
        self.fixCollisions()
                
        return moved
    
    def addPhib(self, phib):
        tup = tuple(phib.pos)
        if 0 <= tup[0] < self.w and 0 <= tup[1] < self.h:
            if tup in self.phibs:
                phibs = self.phibs[tup]
                if isinstance(phibs, basestring):
                    phibs.append(phib)
                else:
                    self.phibs[tup] = [phibs, phib]
                    self.collisions.append(tup)
            else:
                self.phibs[tup] = phib
                
    def fixCollisions(self):
        for col in self.collisions:
            scores = {}
            for phib in self.phibs[col]:
                if not phib.team in scores:
                    scores[phib.team] = 0
                scores[phib.team] += phib.val
                
            highest = max(scores.values())
            winners = [k for k,v in scores.items() if v == highest]
            if len(winners) == 1:
                self.phibs[col] = Phib(val=highest, pos=array(col), team=winners[0])
            else:
                del self.phibs[col]
        self.collisions = []
    
    def run(self):
        while self.step():
            pass
            
    def __str__(self):
        return '\n\n'.join([' '.join([str(get(self.phibs, (x,y)) or ' - ') for x in range(self.w)]) for y in range(self.h)])

#b = [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[0,2,1,0,0],[0,0,0,0,0]]
#b = [[0,3,1,0,3,0,0,3,0,0,3,0,0,0,0]]
#b = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
##b = [[0,1,1,0,2,1,0]]
##b = [[1,1,0]]
#board = Board(board=b)
#print board
##for _ in range(10):
##    print "\n\n\n"
##    print board.step()
##    print board
#board.run()
#print "\n\n\n"
#print board
    
#board = Board(board=[[0,0,1,1,0,2,1,0,0]])
#board.phibs[(5,0)].team = 2
#print board
#print
#board.step()
#print board

def getInt(prompt="int: ", low=float("-inf"), high=float("inf")):
    while True:
        s = raw_input(prompt)
        if s == "quit":
            print "\nGOOD BYE!"
            sys.exit(0)
        try:
            i = int(s)
            if low <= i <= high:
                return i
            else:
                print "ERROR: out of bounds"
        except ValueError:
            print "ERROR: not an int"
            
print welcome
print spacer
print

size = getInt("Board size (8 maybe?): ", 4, 32)
board = Board(phibs=[], w=size, h=size)
numTeams = 2  #getInt("Number of players: ", 2)

print board
while True:
    print spacer
    for team in range(numTeams):
        x = getInt("Player "+str(team)+", X: ", 0, size-1)
        y = getInt("Player "+str(team)+", Y: ", 0, size-1)
        board.addPhib(Phib(val=1, pos=array([x,y]), team=team))
    board.fixCollisions()
    print spacer
    print board
    while board.step():
        print spacer
        print board
        








