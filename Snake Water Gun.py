import random
List= ["Snake","Water", "Gun"]
chances= 10
no_of_chances= 0
computer_point= 0
human_point= 0

while no_of_chances< chances:
    print(List)
    a: str= input("Choose one from the list: ")

    b= random.choice(List)
    print("Computer selected: ", b)

    if a==b:
        print("Match Tie both get 0 mark")

    elif a== "Snake" and b== "Gun":
        computer_point= computer_point+1
        print("Computer Won 1 point")
        print(f"Computer's Point is {computer_point} and Human's Point is {human_point}")

    elif a == "Snake" and b == "Water":
        human_point = human_point + 1
        print("Human Won 1 point")
        print(f"Computer's Point is {computer_point} and User's Point is {human_point}")

    elif a== "Water" and b== "Gun":
        human_point= human_point+1
        print("Computer Won 1 point")
        print(f"Computer's Point is {computer_point} and User's Point is {human_point}")

    elif a== "Water" and b== "Snake":
        computer_point= computer_point+1
        print("Computer Won 1 point")
        print(f"Computer's Point is {computer_point} and User's Point is {human_point}")

    elif a== "Gun" and b== "Snake":
        human_point= human_point+1
        print("Computer Won 1 point")
        print(f"Computer's Point is {computer_point} and User's Point is {human_point}")

    elif a== "Gun" and b== "Water":
        computer_point= computer_point+1
        print("Computer Won 1 point")
        print(f"Computer's Point is {computer_point} and User's Point is {human_point}")

    else:
        print("You have input wrong")

    no_of_chances= no_of_chances + 1
    print(f"{chances- no_of_chances} is left out of {chances}")

print("Game Over")

if a == b:
    print("Tie Match")
elif a > b:
    print("You Won and Computer Lose")
else:
    print("Computer Won and you Lose")

print(f"Your point is {human_point} and computer point is {computer_point}")
