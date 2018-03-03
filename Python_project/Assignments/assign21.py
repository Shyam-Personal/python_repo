'''
21. Given strings A and B. Replace first 2 characters of strings and return a single string which is separated by space
Ex: S1 ="Dog" S2="Dinner"
Output: Dig Donner
'''

s1 = "Dog"
s2 = "Dinner"

print(s2[:2] + s1[2:] + " " + s1[:2] + s2[2:])