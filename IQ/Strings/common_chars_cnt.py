"""
Take two strings as input from user.
S1="Hellosds"
s2="Worldsds"
In this case the char l is in both the strings.
Then print only the common count in both the strings.
Output:
    l - 01
    o - 01
    d - 01
    s - 02
"""


def main():
    try:
        #Solution 1
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        d = {}

        for c in s1:
            if c in s2:
                cnt = min(s1.count(c), s2.count(c))
                d[c] = cnt

        for k,v in d.items():
            print(f"{k} - {v:02d}")

        # Solution 2
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")

        common = set(s1).intersection(set(s2))
        for c in common:
            cnt = min(s1.count(c), s2.count(c))
            print("{0} - {1:02d}".format(c, cnt))

    except Exception as e:
        print("Exception while executing program. Error details: {}".format(str(e)))


if __name__ == "__main__":
    main()
