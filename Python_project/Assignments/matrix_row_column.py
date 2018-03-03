import itertools

def print_matrix(n, list1):
    for i in range(n):
        for j in range(n):
            print(list1[i][j], end=" ")
        print()
    print()

def input_matrix(n, list1):
    for i,j in itertools.product(range(n), range(n)):
        list1[i][j] = int(input("Enter element [{}][{}]: ".format(i,j)))
        
    print_matrix(n, list1)
    return list1

def swap_diagonals(n, list1):
    for i,j in zip(range(len(list1)), range(len(list1[0])-1, -1, -1)):
        list1[i][i], list1[i][j] = list1[i][j], list1[i][i]
    return list1

def swap_rows_columns(n, list1):
    for i in range(len(list1)):
        for j in range(i+1, len(list1[0])):
            list1[i][j], list1[j][i] = list1[j][i], list1[i][j]
    return list1

def main():
    n = int(input("Enter the matrix size (Ex. for 4X4 matrix enter 4): "))
    list1 = [[0 for _ in range(n)] for _ in range(n)]
    list1 = input_matrix(n, list1)
    list1 = swap_rows_columns(n, list1)
    print_matrix(n, list1)
    
if __name__ == "__main__":
    main()