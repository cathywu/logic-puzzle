logic-puzzle
============

Based off of David Strauß's implementation of Conway's Game of Life, found [here](http://www.ibm.com/developerworks/web/library/wa-coffeescriptcanvas/).

Compiling
---------

    coffee --output javascripts/ --watch --compile coffeescripts/

Notes
-----
Alice enters carrying the white rabbit with the magic watch. Mirrors
make her turn 180 degrees. Feathers make her sneeze and drop the
rabbit if she's holding it, who immediately runs away. Chess pieces
make her nap for a bit [ allowing the rabbit to get farther away if
she's not holding it ]. Alice, the rabbit, and Alice while holding
the rabbit all follow specific movement rules [ which the team may or
may not have to deduce, depending on how interesting the puzzle is
otherwise ]. The goal is to force Alice into the wormhole without the
rabbit, who can then seal it with the magic watch. 

we need to determine the grid and the 3 movement rules 

a simple movement rule for Alice with rabbit could be "Go straight if possible, else turn right, else turn left, else u-turn."
and then she follows the outside edge of the grid or something
but that makes putting a mirror in her path relevant
because now the right and left paths are different

maybe Alice moves twice as fast as the rabbit after dropping it
in some sort of "shortest path to rabbit" motion
and when she hits it, she picks it back up, and resumes the "Alice with rabbit" motion

reset condition?
stopping condition?

given movement rules, given object rules and ranges (rules)
for each location-object [x * y * 3]
    place objects
    play: compute steps
    display state w/ slider

desired
    rules that imply unique solution for given grid
    unique solution with a relatively large number of steps

Pseudocode
----------
**Objects**
Grid:
    Size: x,y
    IsValid: bool=function(x,y) (i.e. not an obstacle)

Tools: feathers, chess pieces, mirror
    Position: x,y (i.e. grid cell)
    InRange: bool=function(x,y) (e.g. in range)

Characters: White rabbit, Alice
    Position: x,y
    Step: function(state)
    HasRabit: bool (for Alice)

**Functions**
init() - initialize grid, tools, characters
reset() - initial puzzle condition

**
