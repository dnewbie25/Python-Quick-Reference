import re

# findall( )

""" 
search( ) will match and return one object, the one that first matches the RegEx

findall( ) will return a list of strings of every match in the searched string
"""

phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

test = phone_number.search('Cell: 415-555-5874 Work: 212-555-2020')

print(test.group()) # Returns 415-555-5874

############# with findall( ) it will look like this   ###############

test2 = phone_number.findall('Cell: 415-555-5874 Work: 212-555-2020')

print(test2) # returns ['415-555-5874', '212-555-2020']

phone_number_groups = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

test3 = phone_number_groups.findall('Cell: 415-555-5874 Work: 212-555-2020')

print(test3) # will return a list of tuples with all the groups inside the tuples 
# [('415', '555', '5874'), ('212', '555', '2020')]