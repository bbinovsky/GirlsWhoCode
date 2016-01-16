# Learn how to use Virtual Environments and PIP below.
# It will be needed for the Hackathon
# http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

# Here are Jason Graves examples.
# http://code-junkies.org/hackathon/sdks/fc-buddy-sdk-0.5.1.tar.gz
# http://code-junkies.org/hackathon/sdks/fc-buddy-sdk-0.6.1.tar.gz
# http://code-junkies.org/hackathon/sdks/fc-buddy-sdk-testdriver-1.0.0.tar.gz
# http://code-junkies.org/hackathon/sdks/oneapp-buddy-js-sdk-1.0.0.tar.gz
# http://code-junkies.org/hackathon/sdks/oneapp-buddy-sdk-1.0.0.tar.gz
# http://code-junkies.org/hackathon/sdks/oneapp.js

# Converse the local Q&A program example.
# Author: Brian Binovsky
# Date:   1-16-2016
import sys

def converse():
  print ""
  print "> Program start!"
  name = raw_input("> Hi there, I'm ConvoBot 1.0. What is your name? \n")
  print "> Nice to meet you", name

  years = input("> How old are you this year? \n")
  seconds = years * 365 * 24 * 60 * 60
  print "> Oh my! You will be", seconds, "seconds old on your birthday!!"

  feeling = raw_input("> How are you feeling today? A: Good, B: Alright, C: Bad \n")
  if feeling.upper() == "A":
    print "> Response A"
  elif feeling.upper() == "B":
    print "> Response B"
  elif feeling.upper() == "C":
    print "> Response C"
  else:
    print "> That wasn't A, B or C"

if __name__ == "__main__":
  while True:
    converse()
