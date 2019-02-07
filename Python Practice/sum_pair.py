#print the pair of numbers whose sum is equal to given number k. def func(array, k):

def sum_t(a,k):
   a = list(set(a))
   for i in range(len(a)):
     for j in range(i+1, len(a)):
       if(a[i]+a[j] == k):
         print(tuple([a[i],a[j]]))

if __name__ == "__main__":
	sum_t([1,3,46,2,1,5,4,6,7],47)