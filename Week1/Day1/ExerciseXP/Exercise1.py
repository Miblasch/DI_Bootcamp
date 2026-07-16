print('Hello world\n' * 4)
print((99 ** 3) * 8)
print(5 < 3)         # my guess: False
print(3 == 3)         # my guess: True
print(3 == "3")        # my guess: ?
#print("3" > 3)         # my guess: ?
print("Hello" == "hello")  # my guess: ?
computer_brand = "old gaming computer"  

print(f"I have an {computer_brand} computer.")
name = "Mihal"
age = 41
shoe_size = 38  

info = f"My name is {name}, I'm {age} years old, and my shoe size is {shoe_size}. I'm also a microbiologist working on my own health-tech startup!"

print(info)
a = 10
b = 5
if a > b:
    print("Hello World")
    number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    my_name = "Mihal"
user_name = input("What's your name? ")

if user_name.lower() == my_name.lower():
    print(f"No way, {user_name}?! I'm having an identity crisis.")
else:
    print(f"Nice to meet you, {user_name}! I'm {my_name} — my identity is safe for now.")
    height = float(input("Enter your height in centimeters: "))

if height > 145:
    print("You're tall enough to ride! Enjoy the roller coaster.")
else:
    print("Sorry, you need to grow a bit more before you can ride.")
    
git add .
git commit -m "Complete Week1 Day1 ExerciseXP exercises"
git push