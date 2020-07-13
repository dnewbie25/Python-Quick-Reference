import re

"""
Normally a regex is case sensitive
You can specify not to do so by using re.I
"""

# without re.I you would have to match these one by one:
"""
regex1 = re.compile(r'RoBoCop')
regex2 = re.compile(r'ROBOcop')
regex3 = re.compile(r'Robocop')
"""

# With re.I you only need to do it once

robocop = re.compile(r'robocop', re.I)

test1 = robocop.search('RoBoCop is part man, part machine, all cop')

test2 = robocop.search('ROBOcop is part man, part machine, all cop')

test3 = robocop.search('Robocop is part man, part machine, all cop')

print(f"{test1.group()}\n{test2.group()}\n{test3.group()}") 

# Matches these three: 
#RoBoCop
#ROBOcop
#Robocop



