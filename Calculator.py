from time import sleep
import pyautogui
while True:
     def add():
          a = int(input("Enter The First Number: "))
          b = int(input("Enter The Second Number: "))
          print(f"The answer after adding {a} and {b} is: ",a + b)
          sleep(4.0)
          return

     def sub():
          a = int(input("Enter The First Number: "))
          b = int(input("Enter The Second Number: "))
          print(f"The answer after subtrating {a} and {b} is: ",a - b)
          sleep(4.0)
          return

     def multiply():
          a = int(input("Enter The First Number: "))
          b = int(input("Enter The Second Number: "))
          print(f"The answer after multiplying {a} and {b} is: ",a * b)
          sleep(4.0)
          return

     def divide():
          a = int(input("Enter The First Number: "))
          b = int(input("Enter The Second Number: "))
          print(f"The answer after dividing {a} and {b} is: ",a / b)
          sleep(4.0)
          return

     def average():
          a = int(input("Enter The Sum Of Number: "))
          b = int(input("Enter The Total Counting Of Number: "))
          print(f"The answer after calculating average of {a} and {b} is: ",a / b)
          sleep(4.0)
          return

     def percent():
          a = int(input("Enter The First Number: "))
          b = int(input("Enter The Second Number: "))
          print(f"The answer after calculating percentage of {a} and {b} is: ",(a / b)*100)
          sleep(4.0)
          return

     def square():
          a = int(input("Enter The Number: "))
          print(f"The answer after squaring {a} is: ",a * a)
          sleep(4.0)
          return

     def cube():
          a = int(input("Enter The Number: "))
          print(f"The answer after cubing {a} is: ",a * a * a)
          sleep(4.0)
          return

     def square_root():
          a = int(input("Enter The Number: "))
          print(f"The answer of square root of {a} is: ",a ** (1/2))
          sleep(4.0)
          return


     c = int(input('''\n\nEnter The Number On The Right Side Of The Operation You Want To Perform\n------------------\nOptions Are:      \n1   Addition      \n2   Subtraction   \n3   Multiplication\n4   Division      \n5   Average       \n6   Percentage    \n7   Square        \n8   Cube          \n9   Square Root   \n------------------\nEnter Your Choice: '''))


     if(c == 1):
          add()
     elif(c == 2):
          sub()
     elif(c == 3):
          multiply()
     elif(c == 4):
          divide()
     elif(c == 5):
          average()
     elif(c == 6):
          percent()
     elif(c == 7):
          square()
     elif(c == 8):
          cube()
     elif(c == 9):
          square_root()
     else :
          print("Something Went Wrong ; Pls Try Again")