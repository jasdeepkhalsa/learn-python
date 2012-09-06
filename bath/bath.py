#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jasdeep HBS Khalsa - bath.py
"""
Bath is an object with color, depth and taps

A user can decide what its colour is, how many taps it has and its depth
Bath.py then works out how many minutes it will take for the bath to fill up
by running a simulation in seconds, and assuming each second is a minute
It also assumes that each tap helps fill the bath by 1 cm per second
"""
import time

class Bath():
  def __init__(self, taps, colour, depth):
    self.colour = colour
    self.depth_cm = depth # bath depth in cm
    self.water_level_cm = 0 # initial water level in cm
    self.taps = taps
  def water(self):
    while self.water_level_cm < self.depth_cm:
      time.sleep(0.098765) # less than a second to simulate more realism
      self.water_level_cm += self.taps # each tap contributes 1 cm of water per second
    
def main():
  try:
    print """
    Hi, typically baths have 2 taps, are white
    and have a depth of 125cm, but you choose...
    """
    taps_number = raw_input("How many taps are on this bath? ")
    bath_colour = raw_input("What colour is the bath? ")
    bath_depth = raw_input("What is the depth of the bath in cm? ")
    bath = Bath(int(taps_number), bath_colour, int(bath_depth))
    print "\nInput..."
    print "This bath is %d cm in depth, is %s and has %d tap(s)" % (bath.depth_cm, bath.colour, bath.taps)
  except:
    print "Please enter a number for taps and depth"
    return
  print "\nOutput..."
  if bath.taps == 1:
    print "%d tap has been switched on" % (bath.taps)
  else:
    print "%d taps have been switched on" % (bath.taps)
  print "The %s bath is starting to fill up..." % (bath.colour)
  start = time.time()
  bath.water()
  elapsed = (time.time() - start)
  print "\nResult!"
  print "It took", int(elapsed*9), "minute(s) to fill up the %d cm bath\n" % (bath.depth_cm)

if __name__ == '__main__':
	main()
