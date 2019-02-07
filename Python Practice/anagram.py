#find whether given two strings are anagrams or not
#find how many characters from the string needs to be removed to make the two strings anagrams
#Also print which characters needs to be removed from which string

#first step take the difference of two sets s1-s2 and s2-s1
#This will give how many characters needs to be removed from s1 and s2 respectively
#But one scenario needs to handle for the duplicate characters in string

str1="Harman"
str2="Rank"
cnt = 0

s1=set(str1.lower())
s2=set(str2.lower())

rem_s1 = s1.difference(s2)
rem_s2 = s2.difference(s1)

cnt = len(rem_s1) + len(rem_s2)

for ch in s1.intersection(s2):
	c1 = str1.lower().count(ch)
	c2 = str2.lower().count(ch)
	
	if c1 != c2:
		rem_s1.add(ch) if c1 > c2 else rem_s2.add(ch)
		cnt += 1
		
print("Number chars to be removed from string1 and string2 : {}".format(cnt))
print("Characters to be removed from String1: {}".format(rem_s1))
print("Characters to be removed from String2: {}".format(rem_s2))

#Solution2
# If we want to know how many characters needs to remove to make two strings anagrams of each other
total = 0
str1="Harman"
str2="Rank"

for i in "abcdefghijklmnopqrstuvwxyz":
	total += abs(str1.count(i) - str2.count(i))
	
print(total)