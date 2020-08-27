import re

##URL https://www.hackerrank.com/challenges/matching-specific-string/problem
#Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

####ULR https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem
#Regex_Pattern = r"^\S\S\s\S\S\s\S\S$"	# Do not delete 'r'.


#URL https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem
#regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.

#URL https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem
#Regex_Pattern = r'^[0-9]+[A-Z]+[a-z]+$'	# Do not delete 'r'.

#https://www.hackerrank.com/challenges/matching-ending-items/problem?h_r=next-challenge&h_v=zen
#Regex_Pattern = r'^[a-zA-Z]*s$'

#https://www.hackerrank.com/challenges/matching-x-y-repetitions/problem
#Regex_Pattern = r'^[0-9]{1,2}[a-zA-Z]{3,1000}\.{0,3}$'	# Do not delete 'r'.


##groupp and capturing
#1)
##https://www.hackerrank.com/challenges/matching-word-boundaries/problem
##Regex_Pattern = r'\b[aeiouAEIOU]{1}[a-zA-Z]*\b'	# Do not delete 'r'.
#this is because \b meaning \w\W, \W\w, ^\w o \w$ any of this cases

#2)
##https://www.hackerrank.com/challenges/capturing-non-capturing-groups/problem?h_r=next-challenge&h_v=zen
##Regex_Pattern = r'(ok){3,}'

#3)
#https://www.hackerrank.com/challenges/alternative-matching/problem
##Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'

Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
