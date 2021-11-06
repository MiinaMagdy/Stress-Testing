import subprocess
import random

# DO NOT FORGET:
# freopen("test.in", "r", stdin);
# TO BE IN THE SAME DIRECTORY

while True:
    n = random.randint(1, 25)
    m = random.randint(1, 25)
    comm = "RLDU"
    ln = random.randint(1, 50)
    inpu = ""

    for i in range(ln):
        inpu = inpu + comm[random.randint(0, 3)]

    with open('test.in', 'w') as file:
        file.write(str(n) + ' ')
        file.write(str(m) + '\n')
        for i in inpu:
            file.write(str(i))
            
    # DO NOT CHANGE ANY THING HERE!!!
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


