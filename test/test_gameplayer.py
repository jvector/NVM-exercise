#!/usr/bin/python -t

import gameplayer as gp

def test_startstate():
  
# Check no state at start
  state = gp.getstate()
  assert state == "0 0 N"

def test_moves():
  # Note: For anything more than a few tests it would make sense to loop using a dictionary of string:expectedState

  # Check a normal typical sequence
  string = "MRMLMRM"
  gp.obey(string) 
  state = gp.getstate()
  assert state == "2 2 E"

  # Check that state gets reset
  gp._RESET()
  state = gp.getstate()
  assert state == "0 0 N"

  # Another typical sequence check
  string = "RMMMLMM"
  gp.obey(string)
  state = gp.getstate()
  assert state == "3 2 N"

def test_limiting():
  # Confirm edge limiting
  gp._RESET()
  string = "MMMMM"
  gp.obey(string)
  state = gp.getstate()
  assert state == "0 4 N"

  gp._RESET()
  string = "MMRRMMMM"
  gp.obey(string)
  state = gp.getstate()
  assert state == "0 0 S"

  gp._RESET()
  string = "MMRMLLMMM"
  gp.obey(string)
  state = gp.getstate()
  assert state == "0 2 W"
