'''
33. WaP to sort a given list
'''

def built_in(li):
    print("************** Built IN *************")
    print("Original List : {} ".format(li))
    print(sorted(li))
    li.sort()
    print(li)

def bubble_sort(li):
    print("************** Bubble Sort *************")
    print("Original List : {} ".format(li))
    for _ in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j+1] < li[j]:
                li[j],li[j+1] = li[j+1],li[j]
    print("Sorted List   : {} ".format(li))
    
def merge_sort(li):
    print("************** Merge Sort *************")
    print("Original List : {} ".format(li))
    print("Sorted List   : {} ".format(li))
    
def quick_sort(li):
    print("************** Quick Sort *************")
    print("Original List : {} ".format(li))
    li1 = quick_sort1(li,  0, len(li)-1)
    print("Sorted List   : {} ".format(li1))
    
    
def quick_sort1(li, lb, ub):
    try:
        if(lb < ub):
            pivot = lb
            i = lb
            j = ub
            
            while(i < j):
                while(li[i] <= li[pivot] and i < ub):
                    i += 1
                while(li[j] > li[pivot] and j >= lb):
                    j -= 1
                if(i < j):
                    li[i],li[j] = li[j],li[i]
            li[pivot],li[j] = li[j],li[pivot]
            quick_sort1(li,  lb, j-1)
            quick_sort1(li,  j+1, ub)
            return li
    except Exception as e:
        print(e,i,j)
    
def heap_sort(li):
    print("************** Quick Sort *************")
    print("Original List : {} ".format(li))
    print("Sorted List   : {} ".format(li))
    
def selection_sort(li):
    print("************** Selection Sort *************")
    print("Original List : {} ".format(li))
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[j] < li[i]:
                li[i],li[j] = li[j],li[i]
    print("Sorted List   : {} ".format(li))
    
def main():
    li = [6,5,7,4,9,2,5,6,1,8]
    #built_in(li)
    #bubble_sort(li)
    #selection_sort(li)
    quick_sort(li)
    #merge_sort(li)

if __name__ == "__main__":
    main()