#Error Handling
try:
    a=int(input("Enter your num: "))
    print(a+3)
except Exception as e:
    print("Some error occurred",e)