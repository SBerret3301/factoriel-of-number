x = int(input("Write a number : "))
while x < 0 :
    x = int(input("this number is negative, please enter a positive one : "))
if x > 0 :
    f = 1
    for i in range(1,x+1) :
        f = f * i 
    print("the factoriel is : ", f)
elif x == 0 :
    print("the factoriel is : 1")