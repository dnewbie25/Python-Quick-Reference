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

for item in matches_tuples: # converts the tuple matches_tuples into a list called matches
  for item1 in  item:
    matches.append(item1)
print(matches)

# creates a list of corrected values, without the / characters

corrected_dates = []

# days

del matches[0] # the matches list will be something like this one ['04/07/2012', '04', '/', '07', '/', '2012'] we don't need the first item at all

if int(matches[0]) <= 31: 
  if int(matches[0]) < 10:
    corrected_dates.append(f"0{int(matches[0])}")
  else:
    corrected_dates.append(int(matches[0]))
else:
  print("Incorrect DAY value")
  sys.exit()


# months

if int(matches[2]) <= 12: 
  corrected_dates.append(int(matches[2])) 
else:
  print("Incorrect MONTH value")
  sys.exit()

# year


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

if corrected_dates[1] == 4 or corrected_dates[1] == 6 or corrected_dates[1] == 9 or corrected_dates[1] == 11: # april, june, september and november 30 days
  if int(corrected_dates[0]) > 30:
    print("Incorrect Days. April, June, September and November have 30 days")
    sys.exit()
elif corrected_dates[1] == 2: # february 28 or 29 
  if int(corrected_dates[0]) > 28 and int(int(corrected_dates[2])%4)%2 == 0:
    if int(int(corrected_dates[2])%400)%2 == 0  and int(int(corrected_dates[2])%100)%2 != 0:
      print("This is a lap year")
    else:
      print("February's day is incorrect")
      sys.exit()
elif corrected_dates[1] == 1 or corrected_dates[1] == 3 or corrected_dates[1] == 5 or corrected_dates[1] == 7 or corrected_dates[1] == 8 or corrected_dates[1] == 10 or corrected_dates[1] == 12:
  if int(corrected_dates[0]) > 31:
    print("Error in dates. Please check 31 days months")
    sys.exit()


print(f"The date is: {actual_month[corrected_dates[1]]} {corrected_dates[0]}, {corrected_dates[2]}")

