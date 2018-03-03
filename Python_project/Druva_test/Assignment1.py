import subprocess

# This is a hashtable where the key
# is a number to be used as a test case, and
# the value is the expected output
test_cases = {
    -1: 'error',
     0: 'no',   
     1: 'no',   
     2: 'yes',  
    10: 'no',   
    13: 'yes',  
    49: 'no',   
    50: 'no',   
    51: 'error' 
}

# Go through all the test cases
for test_case in test_cases.items():
    n = test_case[0]         # the number to test
    expected = test_case[1]  # expected answer

    # now call `is_small_prime` with `n` as argument
    # 
    # subprocess.check_output takes the name of a 
    # program and it's arguments, runs the program, 
    # and returns the output of the program. 
    # The output is stored as a string in `prog_output`
    prog_output = subprocess.check_output(['is_small_prime', n])

    # remove whitespace from `prog_output`
    prog_output = prog_output.strip()

    if prog_output == expected:
        print('Test ' + str(n) + ' passed')
    else:
        print('Test ' + str(n) + ' failed')
        
def is_small_prime(n):
    return True