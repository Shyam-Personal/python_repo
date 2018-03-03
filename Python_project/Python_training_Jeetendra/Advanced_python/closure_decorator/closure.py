#!/usr/bin/python
def add_number(num):
    def adder(number):
        return num+number
    return adder

def main():
    adder_of_20 = add_number(20)
    print(adder_of_20(10))
    adder_of_100 = add_number(100)
    print(adder_of_100(10))

if __name__ == "__main__":
    main()
