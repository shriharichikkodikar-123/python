def main():
 x = (int(input("Enter a number: ")))
 if is_even(x):
    print("even.")
 else:
    print("odd.")


def is_even(num):
   if num % 2 == 0:
         return True  #boolean value True
   else:
       return False   #boolean value False
   
main()