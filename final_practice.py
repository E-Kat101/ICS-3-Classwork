"""
INPUT AND OUTPUT
-----------------
"""
# 1. Ask the user for their name and output a message saying hello with the name included.
name = input("What is your name? ")
message = f"Hello, {name}!"
print(message)

# 2. Create a program that will ask the user for two numbers and add them together. Output the answer in a string with an appropriate message.
a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

total = a + b
print(f"The sum is {total}.")


"""
IF STATEMENTS
-----------------
"""
# 1. Give the user a choice of three songs to choose from. They will enter numbers 1-3 to select them from a menu. Depending on what song they choose, output the name of the song and a short lyric from the song.
print("Please choose a song")
print("[1] A")
print("[2] B")
print("[3] C")

choice = int(input("> "))

if choice == 1:
    print("You chose A")
    print("Lyric: One")
elif choice == 2:
    print("You chose B")
    print("Lyric: Two")
elif choice == 3:
    print("You chose C")
    print("Lyric: Three")
else:
    print("Invalid option")



# 2.  Create a program that will show the ticket  price of an event depending on a particular person's age.
"""
0-4: FREE
5-17: $5
18-54: $15
55+: $5
"""

age = int(input("Enter age: "))

if age >= 55:
    price = 5
elif age >= 18:
    price = 15
elif age >= 5:
    price = 5
else:
    price = 0

print(f"The ticket price is ${price}.")

"""
LOOPS
"""
# 1. Create a loop that will say hello 5 times.
for n in range(5):
    print("Hello")

# 2. Create a loop that will draw a row of 10 squares (pygame code below), starting at x=50 , and spaced out by 100. 
#     # pygame.draw.rect(screen, BLACK, (x, 200, 30, 30))

for x in range(50, 1000, 100):
    pygame.draw.rect(screen, BLACK, (x, 200, 30, 30))

for n in range(10):
    start = 50
    spacing = 100
    x = start + spacing * n
    pygame.draw.rect(screen, BLACK, (x, 200, 30, 30))

# 3. Use a loop to ask the user for 5 numbers. Add them together and output the sum.
total = 0

for _ in range(5):
    num = int(input("Enter a number: "))
    total += num

print(total)

# 4. Do the same as #3 except the program should add an undetermined amount of numbers. If they enter the word "stop" the program will stop asking for numbers.
total = 0

while True:
    response = input("Enter a number: ")
    if response == "stop":
        break

    num = int(response)
    total += num

print(total)

"""
LISTS
"""
# 1. Create a list of friends names and print them out using a loop.
friends = [
    "John",
    "Sally",
    "Frank",
]

for friend in friends:
    print(friend)

# 2. Create a list of marks and use a loop to change all marks below 50 to a 50. Print out the modified list.
marks = [67, 45, 87, 33, 66]
for i in range(len(marks)):
    if marks[i] < 50:
        marks[i] = 50

print(marks)

# 3. Create a new list to filter out all the marks below 75. The new list should only have 75+ in it. Do not destroy the original list.
marks = [65, 78, 98, 76, 45, 76, 75]
filtered = []
for m in marks:
    if m >= 75:
        filtered.append(m)

print(filtered)

# 4. Take in several angle measurements from the user. When they enter a negative number, stop asking. The user can enter any number from 0 to infinity, however before you store each angle in the list you need to convert the number to an angle that falls with in 0-359 (0 is 360). Use modulus ( % ) for this. Print out the list.
angles = []
while True:
    a = int(input("Enter an angle (-1 to quit): "))
    if a < 0:
        break

    a = a % 360
    angles.append(a)

"""
FUNCTIONS
"""
# 1. Create a function that prints out any message.
def some_message():
    print("This is some message.")

some_message()

# 2. Create a function that takes a name and prints out a message with the name inside.
def greet(name) -> None:
    print(f"Hello, {name}.")

greet("Mr. McGrin")

# 3. Repeat #2, except instead of printing, the function will return the new string message.
def greet(name: str) -> str:
    return f"Hello, {name}."

greeting = greet("Mike")
    
# 4. Create a function that will take any positive angle 0 to infinity and return the angle only within a 0-359 range.
def heading(rotation: int) -> int:
    # rotation = 360 ->
    # rotation = 361 -> 1
    # rotation = 720 -> 0

    return rotation % 360

angle = heading(5346)
    
# 5. Create a main function that will call all these functions to test them out. Use if __name__ == "__main__" .
def main():
    some_message()
    greet("Dave")
    greeting = greet("John")
    print(greeting)
    angle = heading(5345)
    print(angle)

if __name__ == "__main__":
    main()

"""
PROBLEM SOLVING
"""
# 1. Determine the number of points a basketball team scored in a game by entering the number of successful three pointers (3 pts.), field goals (2 pts.), and free throws (1 pt).
def calc_points(three_pointers, field_goals, free_throws):
    return three_pointers * 3 + field_goals * 2 + free_throws

def main():
    three_pointers = int(input("Three pointers: "))
    field_goals = int(input("Field goals: "))
    free_throws = int(input("Free throws: "))

    total_points = calc_points(three_pointers, field_goals, free_throws)
    print(f"Total points: {total_points}.")

if __name__ == "__main__":
    main()
    
# 2. A hockey team accumulates points over the season depending on their games outcomes. 2 points for a win, 1 point for a tie, 0 points for a loss. The user will enter each game outcome one at a time ("W","T" or "L"). Output the total number of points. This should work for any number of entered games.
wins = 0
ties = 0
while True:
    result = input("W/L/T (leave blank to quit): ").lower()
    if result == "":
        break
        
    if result == "w":
        wins += 1
    elif result == "t":
        ties += 1

points = wins * 2 + ties
print(f"The team has {points} points.")
