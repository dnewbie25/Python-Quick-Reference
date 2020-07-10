import re

# A greedy matching will find the longest string

greedy = re.compile(r'(Ha){3,5}')
test1 = greedy.search('HaHaHaHaHaHaHaHaHaHa') # will return just five Ha, the longest

print(test1.group())

# Non greedy will return the shortest. It has the ? at the end of the RegEx

non_greedy = re.compile(r'(Ha){3,5}?')
test2 = non_greedy.search('HaHaHaHaHaHaHaHaHaHa') # will return 3 Ha's

print(test2.group())

"""The ? for non-greedy doesn't work the same as the ? from match zero or only one set of characters"""




