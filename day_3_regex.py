import re

# check your regex at https://regex101.com
# use parenthsis to capture a match to the group object
string = "today is monday"

# compile your pattern  first

pattern = 'monday$'
regexObj = re.compile(pattern)

result = regexObj.search(string)

print(result)

