#print the count of characters that needs to be added at any position in the given string to make that string palindrome
def palindrome(s):
  if(s==s[::-1]):
    return 0
  j=len(s)-1
  cnt = 0
  i=0
  while(i < j):
    if(s[i] != s[j]):
      cnt += 1
    else:
      j -= 1
    i += 1
  print(cnt)
  
if __name__ == "__main__":
  palindrome(input("Enter the string : "))