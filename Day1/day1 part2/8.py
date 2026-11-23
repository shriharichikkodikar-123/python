name = input("Enter your name: ")
match name:
    case "Alice":
        print("Hello, Alice!")
    case "Bob":

        print("Hello, Bob!")
    case _:
        print("Hello, stranger!")
        
#match statement is used to compare the value of a variable against multiple patterns. In this case, it checks the value of the variable name and executes the corresponding block of code based on the match. If the name is "Alice", it prints "Hello, Alice!". If the name is "Bob", it prints "Hello, Bob!". If the name does not match either of these cases, it prints "Hello, stranger!".