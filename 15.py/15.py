"""
This program attempts to solve the fifteen puzzle by means of an
A-star and IDA-star search algorithm.

@author: Amol P Dharmadhikari <amol.dharmadhikari@gmail.com>

This program solves the 15 sliding tile puzzle. Two options for the search
algorithm (A* or IDA*) and two options for heuristics (the Manhattan
Distance heuristic or the Misplaced tile heuristic) are available. 
 
The following is the command options that the user can enter at the command
prompt to specify which of the features to be needed. 

Search Algorithms:
  -astar	A* algorithm 
  -id		IDA* algorithm 

Heuristics:
  -mh		Manhattan Distance 
  -mt		Misplaced Tiles
 
Display Option:
  -v		Displays the sequence of the whole state 
 		from the problem state to the goal state 
"""

# Imports
import sys, string

def main(argv):
    print("Entry point")

if __name__ == '__main__':
    main(sys.argv)
