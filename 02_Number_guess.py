import random

print("You have 3 chancess")
for i in range (3):
    comp=random.randint(1,10)

    user=int(input("Enter the number  in  range 1-10 :"))
    if comp==user:
        print("you won")
        print(f"computer output is {comp} and user out put is {user}")

        break
    elif comp>=user:
        print("computer output is greater")
    elif comp<=user:
        print("user output is greater")    

    print(f"computer output is {comp} and user out put is {user}")
