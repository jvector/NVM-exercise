#!/usr/bin/python -tt

import sys
import gameplayer as gp

# Define a main() function that runs the gameplayer
def main():

  gp.move()
  gp.turnleft()
  gp.move()
  gp.turnright()
  gp.move()
  gp.turnright()
  gp.move()
  gp.turnright()
  gp.move()
  gp.move()
  gp.move()
  gp.move()
  gp.move()
  gp.move()
  print gp.getstate()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
