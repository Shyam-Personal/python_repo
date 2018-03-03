'''17. WaP to accept string from user and count number of consonants in a given string'''

#a = "abcarhshyashuydhsdhudhsyu"
a = "shyamuioeuislqmxv"
count = 0
for i in a:
    if i not in ['a','e','i','o','u']:
        count += 1
print(count)