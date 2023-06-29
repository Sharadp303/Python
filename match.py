a=int(input("Enter a number: "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 4:
        print("Case is 4")
    case 111:
        print("Case is 111")
    case _:
        print("No match found")