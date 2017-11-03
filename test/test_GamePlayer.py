#!/usr/bin/python -t

import GamePlayer

debugflag=0

gp = GamePlayer.gameplayer(debugflag);
if debugflag:
  print "x {0} y {1} d {2}".format(gp.xpos, gp.ypos, gp.direction)
  
def test_startstate():
  
  # Confirm no state at start
  
  state = gp.getstate()
  assert state == "0 0 N"

'''
Attempting to create the simple test_one_cmd function leads to pytest 'fixture 'cmd' not found' error 
which looks like it needs some @pytest.parametrize / @pytest.fixture voodoo to fix. Skip for now.

def test_one_cmd(cmd,expected):
  gp._RESET()
  gp.obey(cmd)
  assert gp.getstate() == expected 
'''

def test_moves():
  # Note: For anything more than a few tests it would make sense to loop using a dictionary of string:expectedState

  # Check a normal typical sequence
  string = "MRMLMRM"
  gp.obey(string) 
  state = gp.getstate()
  assert state == "2 2 E"

  #test_one_cmd("MRMLMRM", "2 2 E")

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
