# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'



class Rat:
    """ A rat caught in a maze. """
    def __init__(self, symbol, row, col):

        """ (Rat, str, int, int) -> NoneType
​        Initialize the rat with name of rat(one charcter), row (integer), column(integer)
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):

        """ (Rat, int, int) -> NoneType
        Set the rat's row and col instance variables to the given row and column.
        """

        self.row = row
        self.col = col

    def eat_sprout(self):
        """
        (Rat) -> NoneType
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str
        """

       
        return self.symbol + ' at ('  + str(self.row) + ', ' + str(self.col) + ') ate ' + str(self.num_sprouts_eaten) + ' sprouts.'
    
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ __init__(Maze, list of list of str, Rat, Rat))"""

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2= rat_2
        accumulater = 0

        for x in maze:
            accumulater = accumulater + x.count(SPROUT)
                
        self.num_sprouts_left = accumulater

    def is_wall(self, row, col):

      
        if self.maze[row][col] == WALL:
            return True
        else:
            return False

    def get_character(self,row,col):
        """    self.row = row
        self.col = col"""

        
        
        if row == self.rat_1.row and col == self.rat_1.col:
            return self.rat_1.symbol
        else:
            if row == self.rat_2.row and col == self.rat_2.col:
                return self.rat_2.symbol
            else:
                return self.maze[row][col]


    def move(self, rat, vert, hor):

               
        """(Maze, Rat, int, int) -> NoneType
        >>>maze2.move(rat1,1,1)
        >>>maze2.rat1.__str__
        """


        
        
        orig_col = rat.col
        orig_row = rat.row 

        new_row = orig_row + vert
        new_col = orig_col + hor

        if self.is_wall(new_row,new_col) == False:
            rat.col = new_col
            rat.row = new_row
            # check if new position is a sprout.   If so eat the sprout, replace maze with HALL. decrease the number of sprouts in maze.
            if self.maze[new_row][new_col] == SPROUT:
                rat.eat_sprout()
                self.maze[new_row][new_col]= HALL
                self.num_sprouts_left = self.num_sprouts_left-1
            
    
        
        

        




       
rat1 = Rat('a',3,2)
rat2 = Rat('b',2,2)


maze1=[['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']] 
     
maze2 = Maze(maze1,rat1,rat2)


