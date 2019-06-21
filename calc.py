# Number1 = input("What is the first number?")
# Number2 = input("What is the second number?")
# operation = input("What operation do you want to do?")
# if operation == "multiplication":
#     product = int(Number1) * int(Number2)
#     print(product)
# if operation == "addition":
#     sum = int(Number1) + int(Number2)
#     print(sum)
# if operation == "division":
#     quotient = int(Number1)/int(Number2)
#     print(quotient)
# if operation == "subtraction":
#     answer = int(Number1)- int(Number2)
#     print(answer)

name = input("what is your name?")

print("Hello", name + ".")

age = input("what is your age?")

if name == "luke":
    print("I'm not gonna recommend a pet because you will probably kill it on the first day via not feeding it and neglecting its existence")
    
elif name == "sophie":
    print("You deserve a pet monkey!")
    
elif name == "jeff":
    print("I think a jaguar is the perfect pet for you!")

elif age <= "10":
    print("Bee boop bop, I think a turtle is good for you!")

elif age >= "11" and age <= "14":
    print("Bee boop bap ding, I recommend a snake or a lizard!")
    
elif age >= "15" and age <= "20":
        print("Our data suggest that you need a rabbit.")

elif age >= "21" and age <= "30":
    print("Woof, woof, get a dog!!!")

elif age >= "31" and age <= "40":
    print("boop beep, I think you should get a cat")

elif age >= "41" and age <= "80":
    print("get a bird, they sing beautifully!")
    
elif age >"80":
    print("oops! You're too old for a pet. Stick to humans.")

    