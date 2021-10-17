import random, time

odds = [ x for x in range(1,60) if (x % 2) != 0 ]

for i in range(1, 20):
    print("[+] Randomly selecting a number between 1 and 60 ...\n")
    num = random.randint(1, 60)
    print(f"This turns number is: {num}.")

    if num in odds:
        print(f"The number {num} seems a little odd.\n")
    else:
        print(f"Number {num} seems like a perfectly normal number.\n")

    time.sleep(5)


