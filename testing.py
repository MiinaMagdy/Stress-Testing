import subprocess
import random

# DO NOT FORGET: freopen("test.in", "r", stdin);
# Make Sure: TO BE IN THE SAME DIRECTORY or Change the path below

while True:
    # INPUTS use random module


    # write INPUTS in test.in
    with open('test.in', 'w') as file:
        # use write method and cast inputs to str()
        

    # DO NOT CHANGE ANY THING BELOW!!!
    with open('test.in', 'r') as file:
        for line in file:
            print(line, end='')
    
    print("\n\nTesting...")

    subprocess.run(["g++", "myCode.cpp", "-o", "myCode"])
    subprocess.run(["g++", "anotherCode.cpp", "-o", "anotherCode"])
    myRes = subprocess.run(["./myCode", "<", "test.in"], capture_output=True).stdout.decode()
    anotherRes = subprocess.run(["./anotherCode", "<", "test.txt"], capture_output=True).stdout.decode()
    print("myCode: ")
    print(myRes)
    print("anotherCode: ")
    print(anotherRes)
    if myRes != anotherRes:
        break


