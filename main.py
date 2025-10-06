while True:
    
    cal = input("Enter exit for Exit. \nenter two number and one operator seperated by space(2 * 5): ")
    if cal == "exit": break
    try:
        print(eval(cal))
    except:
        print("enter numbers correctly")
    
        
