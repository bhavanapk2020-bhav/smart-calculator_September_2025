class Arithmetic:

    def addition(self, *args : int | float):

        if sum(args).is_integer:

            print(int(sum(args)))
        
        else:

            print(sum(args))

        repeat_1()

    def subtraction(self, *args : int | float):

        diff = args[0]

        for i in args[1 :]:

            diff -= i

        if diff.is_integer():

            print(int(diff))
        
        else:

            print(diff)

        repeat_1()


    def multiplication(self, *args : int | float):

        product = 1

        for i in args:

            product *= i

        if product.is_integer():

            print(int(product))
        
        else:

            print(product)

        repeat_1()


    def division(self, *args : int | float):

        quotient = args[0]

        for i in args[1 :]:

            quotient /= i

        if quotient.is_integer():

            print(int(quotient))
        
        else:

            print(quotient)

        repeat_1()


ar_ob = Arithmetic()

class Conversion:

    def cm_m(self, from_val):

        to_val = from_val * 0.01

        print(f"{from_val} centimeters = {to_val} meters")

    def m_cm(self, from_val):

        to_val = from_val * 100

        print(f"{from_val} meters = {to_val} centimeters")

    def cm_inch(self, from_val):

        to_val = from_val * 0.393701

        print(f"{from_val} centimeters = {to_val} inches")

    def inch_cm(self, from_val):

        to_val = from_val * 2.54

        print(f"{from_val} inches = {to_val} centimeters")

    def km_m(self, from_val):

        to_val = from_val * 1000

        print(f"{from_val} kilometers = {to_val} meters")

    def m_km(self, from_val):

        to_val = from_val * 0.001

        print(f"{from_val} meters = {to_val} kilometers")

    
    def km_miles(self, from_val):

        to_val = from_val * 0.621371

        print(f"{from_val} kilometers = {to_val} miles")

    
    def miles_km(self, from_val):

        to_val = from_val * 1.60934

        print(f"{from_val} miles = {to_val} kilometers")

    
    def m_feet(self, from_val):

        to_val = from_val * 3.28084

        print(f"{from_val} meters = {to_val} feet")

    
    def feet_m(self, from_val):

        to_val = from_val * 0.3048

        print(f"{from_val} meters = {to_val} centimeters")




    






convert = Conversion()

def repeat_1():

    rpt = input("Do you want to continue ? (YES / NO)").lower()

    if rpt == "yes" or rpt == "y":

        main_ob.operations()

    elif rpt == "no" or rpt == "n" :

        main_ob.menu()

    else:

        exit()

def repeat_2():

    rpt = input("Do you want to continue ? (YES / NO)").lower()

    if rpt == "yes" or rpt == "y":

        main_ob.conversion()

    elif rpt == "no" or rpt == "n" :

        main_ob.menu()

    else:

        exit()

class Main:
    def menu(self):

        print("Welcome to smart calculator")  

        choice = int(input("Arithmetic Operation (Please enter 1 to select)\nUnit conversion (Please enter 2 to select)\n(To exit from the program type 0)\nPlease select :  "))

        if choice == 0:

            exit()

        elif choice == 1:

            main_ob.operations()

        elif choice == 2:

            main_ob.conversion()

    def operations(self):

        print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION")

        op = input("Enter the operation to be performed : ").lower()

        if op == "1" or op == "addition":

            try:

                num = input("Enter the numbers to be added seperated by space : ")

                numbers = list(map(float,num.split()))

                ar_ob.addition(*numbers)

            except ValueError:

                print("Enter a valid number")

        elif op == "2" or op == "subtraction":

            try:

                num = input("Enter the numbers to be subtracted seperated by space : ")

                numbers = list(map(float,num.split()))
                    
                ar_ob.subtraction(*numbers)

            except ValueError:

                print("Enter a valid number")

        elif op == "3" or op == "multiplication":

            try:

                num = input("Enter the numbers to be multiplied seperated by space : ")

                numbers = list(map(float,num.split()))
                    
                ar_ob.multiplication(*numbers)

            except ValueError:

                print("Enter a valid number")

        elif op == "4" or op == "division":

            try:

                num = input("Enter the numbers to be divided seperated by space : ")

                numbers = list(map(float,num.split()))
                    
                ar_ob.division(*numbers)

            except ValueError:

                print("Enter a valid number")

        else:

            print("Invalid option")

            main_ob.operations()

    def conversion(self):

        print("1.LENGTH\n2.MASS/WEIGHT\n3.TEMPERATURE\n4.TIME\n5.VOLUME\n6.ENERGY\n7.DIGITAL STORAGE\n8.SPEED")

        conv = input("Enter the category : ").lower()

        if conv == "length" or conv == "1":

            c_type = input(("1. Centimeter to meter\n\n2. Meter to Centimetern\n3. Centimeter to Inches\n\n4. Inches to Centimeter\n\n5. Kilometer to Meter\n\n6. Meters to Kilometer\n\n7. Kilometer to Miles\n\n8. Miles to Kilometer\n\n9. Meter to Feet\n\n10. Feet to Meter\n\n\nSelect the conversion type: "))

            if c_type == "1":

                try:

                    f_val = int(input("Enter the value in centimeters : "))

                    convert.cm_m(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "2":

                try:

                    f_val = int(input("Enter the value in meters : "))

                    convert.m_cm(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "3":

                try:

                    f_val = int(input("Enter the value in centimeters : "))

                    convert.cm_inch(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "4":

                try:

                    f_val = int(input("Enter the value in inches : "))

                    convert.inch_cm(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "5":

                try:

                    f_val = int(input("Enter the value in kilometers : "))

                    convert.km_m(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "6":

                try:

                    f_val = int(input("Enter the value in meters : "))

                    convert.m_km(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "7":

                try:

                    f_val = int(input("Enter the value in kilometers : "))

                    convert.km_miles(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "8":

                try:

                    f_val = int(input("Enter the value in kilometers : "))

                    convert.miles_km(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "9":

                try:

                    f_val = int(input("Enter the value in meters : "))

                    convert.m_feet(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")

            elif c_type == "10":

                f_val = int(input("Enter the value in meters : "))

                convert.feet_m(f_val)

                repeat_2()

            else:

                print("Invalid option")

                main_ob.conversion()

        if conv == "mass/weight" or conv == "2":

            c_type = input(("1. Kilograms to Grams\n\n2. Pounds to Kilograms\n3. Grams to Ounces\n\n4. Kilograms to Ounces\n\n5. Pounds to Grams\n\n\nSelect the conversion type: "))

            if c_type == "1":

                try:

                    f_val = int(input("Enter the value in centimeters : "))

                    convert.cm_m(f_val)

                    repeat_2()

                except ValueError:

                    print("Invalid input")





main_ob = Main()

main_ob.menu()




      



        
        





        
        
