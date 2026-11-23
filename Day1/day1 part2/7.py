def main():
 x = (int(input("Enter a number: ")))
 if is_even(x):
    print("even.")
 else:
    print("odd.")


def is_even(num):
   return True if num % 2 == 0 else False
   
main()