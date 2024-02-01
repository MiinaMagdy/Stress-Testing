import subprocess
import random

def is_correct(myRes, correctRes, inputFile):
    return myRes == correctRes


## DO NOT FORGET: freopen("test.in", "r", stdin);
## Make Sure: TO BE IN THE SAME DIRECTORY or Change the path below
subprocess.run(["g++", "myCode.cpp", "-o", "myCode"])
subprocess.run(["g++", "anotherCode.cpp", "-o", "anotherCode"])

while True:
    ## write INPUTS in test.in
    with open('test.in', 'w') as file:
        ## INPUTS use random module
        ## use this function to random.randint
        ## use write method and cast inputs to str()
        ## uncomment next line if there are testcases
        # t = random.randint(1, 1); file.write(str(t) + '\n')
        pass

    ## DO NOT CHANGE ANY THING BELOW!!!
    myRes = subprocess.run(["./myCode"], capture_output=True).stdout.decode()
    anotherRes = subprocess.run(["./anotherCode"], capture_output=True).stdout.decode()

    ## Displaying
    print("\n\nTest:")
    with open('test.in', 'r') as file:
        for line in file:
            print(line, end='')

    print("\n\nMy Code's Output: ")
    print(myRes)
    print("Your Code's Output: ")
    print(anotherRes)
    # checker below
    if not is_correct(myRes, anotherRes, 'test.in'):
        break
