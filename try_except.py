try:        
    x = int(input("Enter an integer: "))
    print(x)
except:
    print("An error occurred. Please enter a valid integer.")
finally:
    print("This block will always be executed, regardless of whether an exception occurred or not.")


# else:
#     print("The input was successfully processed.")
    
# try:        
#     x = int(input("Enter an integer: "))
#     print(x)
# except ValueError:
#     print("ValueError: Please enter a valid integer.", name)