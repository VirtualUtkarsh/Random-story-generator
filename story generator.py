# Importing random module
import random

# Storing random data into lists to create story.
when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before The Doom']
who = ['Swordsman', 'The knight', 'Robinhood', 'Shepard', 'The king',]
went = ['Castle', 'Dragon Pit', 'River', 'Bat Cave', 'Village']
what = ['to eat a lot of pies', 'to fight for justice', 'to steal money', 'to dance','to save the princess']

# Using string concatenition & randome.choice() to print a random element from all the lists 
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')