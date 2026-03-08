def greetings_function(name, age):
    print("Welcome", name, ". You are", age, "years old.")

name = input("Enter your name: ")
age = input("Enter your age: ")
greetings_function(name, age)


# def greetings_function(*names):
#     print("Welcome", names[1])

# greetings_function("John", "Glory", "Mercy")