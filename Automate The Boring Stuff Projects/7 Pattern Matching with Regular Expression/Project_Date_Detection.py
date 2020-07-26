"""Program that detects dates in DD/MM/YYYY format"""

import re, sys

input_date = str(input("Enter the date in DD/MM/YYYY. The program will output the date in format MONTH DAY, YEAR:"))

dateRegex = re.compile(r'''(
(\d{2}) # DD
(/|-|,) # separator
(\d{2}) # MM
(/|-|,) # separator
(\d{4}) # YYYY
)''', re.VERBOSE)


# append matches to a list

matches_tuples = []

for groups in dateRegex.findall(input_date):
  matches_tuples.append(groups)

matches = []

# converts the tuple matches_tuples into a list called matches
for item in matches_tuples: 
  for item1 in  item:
    matches.append(item1)
print(matches)

# creates a list of corrected values, without the / characters in the list

corrected_dates = []

# days range

del matches[0] # the matches list will be something like this one ['04/07/2012', '04', '/', '07', '/', '2012'] we don't need the first item at all
# the new list would be ['04', '/', '07', '/', '2012'], we'll work with indexes 0, 2 and 4

# days are index 0
if int(matches[0]) <= 31: 
  if int(matches[0]) < 10:
    corrected_dates.append(f"0{int(matches[0])}")
  else:
    corrected_dates.append(int(matches[0]))
else:
  print("Incorrect DAY value")
  sys.exit()


# months range, index 2

if int(matches[2]) <= 12: 
  corrected_dates.append(int(matches[2])) 
else:
  print("Incorrect MONTH value")
  sys.exit()

# year range, index 4


if int(matches[4]) <= 2999 and int(matches[4]) >= 1000: 
    corrected_dates.append(matches[4])
else:
  print("Incorrect YEAR value")
  sys.exit()


# Assign Month to Values in new Array with a dictionary

actual_month = {
1: "January",
2: "February",
3: "March",
4: "April",
5: "May",
6: "June",
7: "July",
8: "August",
9: "September",
10: "October",
11: "November",
12: "December"
}

# Correctted dates will save this type of list [DD, MM, YYYY]
                                              # 0    1   2

if corrected_dates[1] == 4 or corrected_dates[1] == 6 or corrected_dates[1] == 9 or corrected_dates[1] == 11: # april, june, september and november have 30 days
  if int(corrected_dates[0]) > 30:
    print("Incorrect Days. April, June, September and November have 30 days")
    sys.exit()
elif corrected_dates[1] == 2: # february 28 or 29 
  if int(corrected_dates[0]) == 29: # if day is 29 
    if  int(corrected_dates[2])%4 == 0 or int(corrected_dates[2])%400 == 0 and int(corrected_dates[2])%100 != 0: # it should be evenly divisible by 4 unless it's divisible by 400 but not by 100
      print("This is a lap year")
    else:
      print("This year is not a lap year")
      sys.exit()
  elif int(corrected_dates[0]) > 29: # if it has more than 29 days is incorrect, otherwise is correct
    print("February date out of range")
    sys.exit()
  
# here I specified 31 days months January, March, May, July, August, October and December  
elif corrected_dates[1] == 1 or corrected_dates[1] == 3 or corrected_dates[1] == 5 or corrected_dates[1] == 7 or corrected_dates[1] == 8 or corrected_dates[1] == 10 or corrected_dates[1] == 12:
  if int(corrected_dates[0]) > 31:
    print("Error in dates. Please check 31 days months")
    sys.exit()


# Prints the months formatted in MONTH DAY, YEAR
print(f"The date is: {actual_month[corrected_dates[1]]} {corrected_dates[0]}, {corrected_dates[2]}")

