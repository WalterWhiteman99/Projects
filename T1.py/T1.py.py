n1 = int(input("Select an integer: "))
n2 = int(input("Select an integer: "))
operation = input("Select an operation")

if operation == "+":
  print(n1 + n2)

elif operation == "-":
   print(n1 - n2)

elif operation == "*":
  print(n1 * n2)

elif operation == "/":
 print(n1 / n2)    

elif n1 != int:
    print("Invalid")

elif n2 != int:
    print("Invalid")

elif operation != "+,-,*,/":
    print("invalid")
   

