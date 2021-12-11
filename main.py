from random import randint
start = 1
end = 1000
value = randint(start,end)
print ("The computer will choose a random number between 1 and 1000")
choice = 0
while choice!=value:
    text = input("Please enter a number : ")
    choice = int(text)
    if choice < value:
        print("the number is a bit higher than that")
    elif choice > value:
        print("the number is a bit lower than that")
print("Congrats you guessed right!")
