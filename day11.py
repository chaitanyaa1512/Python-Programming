# name='Chay'
# i=0
# while i<5:
#     print(name)
#     i+=1

# for i in range(11):
#     print(i)
#     if i==5:
#         continue 
#     print("äfter continue",i)
# i=0
# while i<5:
#     print(i)

# import random
# while True:
#   number= random.randint(1,100)
#   print("Guess a number between 1 to 100")
#   for i in range(1,6):
#     ip=int(input("Guess your number:"))
#     if ip==number:
#         print("YOU WON!")
#         break
#     else:
#         if ip>number:
#           print("Guess a lower number")
#           print(5-i,"Try/ies left")
#         else:
#             print("Guess a higher number")
#             print(5-i,"Try/ies left")
#   else:
#     print("Better luck next time!")

def print_range(start, stop):
    for i in range(start, stop):
     print(i)

    print_range(0,5)
    print_range(6,12)


