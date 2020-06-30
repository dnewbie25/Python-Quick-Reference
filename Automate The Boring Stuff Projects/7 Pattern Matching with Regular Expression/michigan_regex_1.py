import re
filename = open('Files Samples/regex_sum_723743.txt')
num_list = list()
for line in filename:
    matches = re.findall('[0-9]+', line)
    num_list.append(matches)
    '''for item in matches:
      integers = int(item)
      num_list.append(integers)'''

unwrapped_list = []

for item1 in num_list:
  for item2 in item1:
    unwrapped_list.append(item2)

total = 0

for num in unwrapped_list:
  num = int(num)
  total += num

print("The total is: ",total)

#print(num_list)
print(len(unwrapped_list))
'''total = 0
for num in num_list:
    total += num
'''
#rint(total)
#print(len(num_list))