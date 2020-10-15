def forever():
    print("input password")
    
    password = input("> ")

    if password == "1234":
        print("you win")
    else:
        print("you lose")    

forever()