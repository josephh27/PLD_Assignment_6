while True:
    try:
        number1 = float(input("Input the first number: "))
        number2 = float(input("Input the second number: "))
        number3 = float(input("Input the third number: "))
        number4 = float(input("Input the fourth number: "))
        break
    except:
        print("Please input number values")



def numberSorter(): 
    #If number1 is the highest of them all
    if number1 >= number2 and number1 >= number3 and number1 >= number4:
        #If number2 is the second highest number
        if number2 >= number3 and number2 >= number4:
            #number3 and number4 getting compared
            if number3 >= number4:
                print(number1)
                print(number2)
                print(number3)
                print(number4)
            else:
                print(number1)
                print(number2)
                print(number4)
                print(number3)
        #number3 is the second highest number 
        elif number2 <= number3 >= number4:
            #number4 and number2 getting compared
            if number4 >= number2:
                print(number1)
                print(number3)
                print(number4)
                print(number2)
            else:
                print(number1)
                print(number3)
                print(number2)
                print(number4)
        #number4 is the second highest number
        elif number2 <= number4 >= number3:
            #number3 and number2 getting compared
            if number3 > number2:
                print(number1)
                print(number4)
                print(number3)
                print(number2)
            else:
                print(number1)
                print(number4)
                print(number2)
                print(number3)
    #If number2 is the highest of them all
    elif number2 >= number3 and number2 >= number4 and number2 >= number1:
        #If number1 is the second highest number
        if number3 <= number1 >= number4:
            #Comparing the number3 and number4
            if number3 >= number4:
                print(number2)
                print(number1)
                print(number3)
                print(number4)
            else:
                print(number2)
                print(number1)
                print(number4)
                print(number3)
        #If number 3 is the second highest number
        elif number1 <= number3 >= number4:
            #Comparing number4 and number1
            if number1 >= number4:
                print(number2)
                print(number3)
                print(number1)
                print(number4)
            else:
                print(number2)
                print(number3)
                print(number4)
                print(number1)
        #If number 4 is the second highest number
        elif number1 <= number4 >= number3:
            #Comparing number1 and number3
            if number3 >= number1:
                print(number2)
                print(number4)
                print(number3)
                print(number1)
            else:
                print(number2)
                print(number4)
                print(number1)
                print(number3)
    #If number3 is the highest number of them all
    elif number3 >= number1 and number3 >= number2 and number3 >= number4:
        #If number2 is the second highest number
        if number1 <= number2 >= number4:
            #Comparing number1 and number4
            if number1 >= number4:
                print(number3)
                print(number2)
                print(number1)
                print(number4)
            else:
                print(number3)
                print(number2)
                print(number4)
                print(number1)
        #If number1 is the second highest number
        elif number2 <= number1 >= number4:
            #Comparing the number2 and number4
            if number2 >= number4:
                print(number3)
                print(number1)
                print(number2)
                print(number4)
            else:
                print(number3)
                print(number1)
                print(number4)
                print(number2)
        #If number4 is the second highest number
        elif number1 <= number4 >= number2:
            #Comparing number1 and number2
            if number1 >= number2:
                print(number3)
                print(number4)
                print(number1)
                print(number2)
            else:
                print(number3)
                print(number4)
                print(number2)
                print(number1)
    #If number4 is the highest of them all
    elif number4 >= number1 and number4 >= number2 and number4 >= number3:
        #If number1 is the second highest number
        if number2 <= number1 >= number3:
            #Comparing number2 and number3
            if number2 >= number3:
                print(number4)
                print(number1)
                print(number2)
                print(number3)
            else:
                print(number4)
                print(number1)
                print(number3)
                print(number2)
        #if number2 is the second highest number
        elif number1 <= number2 >= number3:
            #Comparing number1 and number3
            if number1 >= number3:
                print(number4)
                print(number2)
                print(number1)
                print(number3)
            else:
                print(number4)
                print(number2)
                print(number3)
                print(number1)
        #if number 3 is the second highest number
        elif number2 <= number3 >= number1:
            #Comparing number1 and number2
            if number1 >= number2:
                print(number4)
                print(number3)
                print(number1)
                print(number2)
            else:
                print(number4)
                print(number3)
                print(number2)
                print(number1)
numberSorter()

                   
        
                