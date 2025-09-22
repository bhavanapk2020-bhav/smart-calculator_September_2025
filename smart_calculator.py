import math

class Standard:

    def addition(self, *args : int | float):

        if sum(args).is_integer():

            print(int(sum(args)))
        
        else:

            print(sum(args))

    def subtraction(self, *args : int | float):

        diff = args[0]

        for i in args[1 :]:

            diff -= i

        if diff.is_integer():

            print(int(diff))
        
        else:

            print(diff)
            
    def multiplication(self, *args : int | float):

        product = 1

        for i in args:

            product *= i

        if product.is_integer():

            print(int(product))
        
        else:

            print(product)
            
    def division(self, *args : int | float):

        quotient = args[0]

        for i in args[1 :]:

            quotient /= i

        if quotient.is_integer():

            print(int(quotient))
        
        else:

            print(quotient)
            
st_ob = Standard()

class Conversion:

    def cm_m(self, from_val):

        to_val = from_val * 0.01

        print(f"{from_val} centimeters = {to_val} meters")

        repeat_3()

    def m_cm(self, from_val):

        to_val = from_val * 100

        print(f"{from_val} meters = {to_val} centimeters")

        repeat_3()


    def cm_inch(self, from_val):

        to_val = from_val * 0.393701

        print(f"{from_val} centimeters = {to_val} inches")

        repeat_3()

    def inch_cm(self, from_val):

        to_val = from_val * 2.54

        print(f"{from_val} inches = {to_val} centimeters")

        repeat_3()

    def km_m(self, from_val):

        to_val = from_val * 1000

        print(f"{from_val} kilometers = {to_val} meters")

        repeat_3()

    def m_km(self, from_val):

        to_val = from_val * 0.001

        print(f"{from_val} meters = {to_val} kilometers")

        repeat_3()

    
    def km_miles(self, from_val):

        to_val = from_val * 0.621371

        print(f"{from_val} kilometers = {to_val} miles")

        repeat_3()

    
    def miles_km(self, from_val):

        to_val = from_val * 1.60934

        print(f"{from_val} miles = {to_val} kilometers")

        repeat_3()

    
    def m_feet(self, from_val):

        to_val = from_val * 3.28084

        print(f"{from_val} meters = {to_val} feet")

        repeat_3()

    
    def feet_m(self, from_val):

        to_val = from_val * 0.3048

        print(f"{from_val} feet = {to_val} meters")

        repeat_3()

    def kg_g(self, from_val):

        to_val = from_val * 1000

        print(f"{from_val} kg = {to_val} g")

        repeat_3()

    def p_kg(self, from_val):

        to_val = from_val * 0.453592

        print(f"{from_val} lb = {to_val} kg")

        repeat_3()

    def g_ounce(self, from_val):

        to_val = from_val * 0.035274

        print(f"{from_val} g = {to_val} oz")

        repeat_3()

    def kg_ounce(self, from_val):

        to_val = from_val * 35.274

        print(f"{from_val} kg = {to_val} oz")

        repeat_3()

    def p_g(self, from_val):

        to_val = from_val * 453.592

        print(f"{from_val} lb = {to_val} kg")

        repeat_3()

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

        main_ob.scientific()

    elif rpt == "no" or rpt == "n" :

        main_ob.menu()

    else:

        exit()

def repeat_3():

    rpt = input("Do you want to continue ? (YES / NO)").lower()

    if rpt == "yes" or rpt == "y":

        main_ob.conversion()

    elif rpt == "no" or rpt == "n" :

        main_ob.scientific()

    else:

        exit()

class Main:
    def menu(self):

        print("Welcome to smart calculator")  

        mode = int(input("Standard Calculator (Please enter 1 to select)\nScientific Calculator (Please enter 2 to select)\n(To exit from the program type 0)\nPlease select :  "))

        if mode == 0:

            exit()

        elif mode == 1:

            main_ob.operations()

        elif mode == 2:

            main_ob.scientific()

        else:

            print("Invalid Input")

            main_ob.menu()

    def operations(self):

        print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.Go Back")

        op = input("Enter the operation to be performed : ").lower()

        if op == "1" or op == "addition":

            try:

                num = input("Enter the numbers to be added, seperated by space : ")

                numbers = list(map(float,num.split()))

                st_ob.addition(*numbers)

                repeat_1()

            except ValueError:

                print("Enter a valid number")

                self.operations()

        elif op == "2" or op == "subtraction":

            try:

                num = input("Enter the numbers to be subtracted, seperated by space : ")

                numbers = list(map(float,num.split()))
                    
                st_ob.subtraction(*numbers)

                repeat_1()

            except ValueError:

                print("Enter a valid number")

                self.operations()

        elif op == "3" or op == "multiplication":

            try:

                num = input("Enter the numbers to be multiplied, seperated by space : ")

                numbers = list(map(float,num.split()))
                    
                st_ob.multiplication(*numbers)

                repeat_1()

            except ValueError:

                print("Enter a valid number")

                self.operations()

        elif op == "4" or op == "division":

            try:

                num = input("Enter the numbers to be divided seperated, by space : ")

                numbers = list(map(float,num.split()))
                    
                st_ob.division(*numbers)

                repeat_1()

            except ValueError:

                print("Enter a valid number")

                self.operations()

            except ZeroDivisionError:

                print("Division by zero is not possible")

                repeat_1()

        elif op == "5" or op == "go back":

            main_ob.menu()

        else:

            print("Invalid option")

            main_ob.operations()

    def conversion(self):

        print("1.LENGTH\n2.MASS/WEIGHT\n3.TEMPERATURE\n4. GO BACK")

        conv = input("Enter the category : ").lower()

        if conv == "length" or conv == "1":

            c_type = input(("1. Centimeter to meter\n\n2. Meter to Centimetern\n3. Centimeter to Inches\n\n4. Inches to Centimeter\n\n5. Kilometer to Meter\n\n6. Meters to Kilometer\n\n7. Kilometer to Miles\n\n8. Miles to Kilometer\n\n9. Meter to Feet\n\n10. Feet to Meter\n11.Go Back\n\n\nSelect the conversion type: "))

            if c_type == "1":

                try:

                    f_val = int(input("Enter the value in centimeters : "))

                    convert.cm_m(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "2":

                try:

                    f_val = int(input("Enter the value in meters : "))

                    convert.m_cm(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "3":

                try:

                    f_val = int(input("Enter the value in centimeters : "))

                    convert.cm_inch(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "4":

                try:

                    f_val = int(input("Enter the value in inches : "))

                    convert.inch_cm(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "5":

                try:

                    f_val = int(input("Enter the value in kilometers : "))

                    convert.km_m(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "6":

                try:

                    f_val = int(input("Enter the value in meters : "))

                    convert.m_km(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "7":

                try:

                    f_val = int(input("Enter the value in kilometers : "))

                    convert.km_miles(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "8":

                try:

                    f_val = int(input("Enter the value in kilometers : "))

                    convert.miles_km(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "9":

                try:

                    f_val = int(input("Enter the value in meters : "))

                    convert.m_feet(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "10":

                f_val = int(input("Enter the value in meters : "))

                convert.feet_m(f_val)

            elif c_type == "11":

                main_ob.conversion()

            else:

                print("Invalid option")

                main_ob.conversion()

        elif conv == "mass/weight" or conv == "2":

            c_type = input(("1. Kilograms to Grams\n\n2. Pounds to Kilograms\n3. Grams to Ounces\n\n4. Kilograms to Ounces\n\n5. Pounds to Grams\n6.GO BACK\n\n\nSelect the conversion type: "))

            if c_type == "1":

                try:

                    f_val = float(input("Enter the value in Kilograms : "))

                    convert.kg_g(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "2":

                try:

                    f_val = float(input("Enter the value in Pounds : "))

                    convert.p_kg(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "3":

                try:

                    f_val = float(input("Enter the value in Grams : "))

                    convert.g_ounce(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "4":

                try:

                    f_val = float(input("Enter the value in Kilograms : "))

                    convert.kg_ounce(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "5":

                try:

                    f_val = float(input("Enter the value in Pounds : "))

                    convert.p_g(f_val)


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "6":

                main_ob.conversion()

            else:

                print("Invalid Input")

                main_ob.conversion()

        elif conv == "temperature" or conv == "3":

            c_type = input(("1. Celcius to Fahrenheit\n\n2. Fahrenheit to Celcius \n3. Celcius to Kelvin\n\n4. Kelvin to Celcius\n\n5. Fahrenheit to Kelvin\n6.Kelvin to Fahrenheit\n\n\nSelect the conversion type: "))

            if c_type == "1":

                try:

                    f_val = float(input("Enter the value in Celcius : "))

                    print(f"{(f_val * 9/5) + 32} F")

                    repeat_3()


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "2":

                try:

                    f_val = float(input("Enter the value in Farenheit : "))

                    print(f"{(f_val - 32) * 5/9} C")

                    repeat_3()


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "3":

                try:

                    f_val = float(input("Enter the value in Celcius : "))

                    print(f"{f_val + 273.15} K")

                    repeat_3()


                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "4":

                try:

                    f_val = float(input("Enter the value in Kelvin : "))

                    print(f"{f_val - 273.15} C")

                    repeat_3()

                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "5":

                try:

                    f_val = float(input("Enter the value in Fahrenheit : "))

                    print(f"{(f_val - 32) * 5/9 + 273.15} K")

                    repeat_3()

                except ValueError:

                    print("Invalid input")

                    self.conversion()

            elif c_type == "6":

                try:

                    f_val = float(input("Enter the value in Kelvin : "))

                    print(f"{(f_val - 273.15) * 9/5 + 32} F")

                    repeat_3()
                    
                except ValueError:

                    print("Invalid input")

                    self.conversion()
            else:

                print("Invalid Input")

                main_ob.conversion()


        if conv == "go back" or conv == "4":

            main_ob.scientific()

    def tri(self,ang_val):

        print(f" Sin {math.degrees(ang_val)} degrees or {ang_val} radians = {math.sin(ang_val)}\n")

        print(f" Cos {math.degrees(ang_val)} degrees or {ang_val} radians = {math.cos(ang_val)}\n")

        print(f" Tan {math.degrees(ang_val)} degrees or {ang_val} radians = {math.tan(ang_val)}\n")

    def factorial(self,num):

        if num == 1 or num == 0:

            return 1

        else:

            return num * self.factorial(num - 1)


    def scientific(self):

        print("1.Arithmetic Operations\n2.Trigonometric functions\n3.Square root\n4.Unit Conversion\n5.Power\n6.Logarithms\n7.Circle Operations\n8.Exponentials\n9.Factorial\n10.Angle conversion\n11.Go Back")
        try :
            
            option = int(input("Enter the serial number of the options : "))

            if option == 1:

                main_ob.operations()

            elif option == 2:

                ang = input("Degree or Radian ?").lower()

                value = float(input("Enter the value / angle : "))

                if ang == "degree":

                    value = math.radians(value)

                    main_ob.tri(value)

                elif ang == "radian":

                    main_ob.tri(value)

                elif ang != "degree" or ang != "radian":

                    print("Invalid Input")
                    
                repeat_2()
                
            elif option == 3:

                val = int(input("Enter the value :"))

                print(f"Square root of {val} = {math.sqrt(val)}")

                repeat_2()

            elif option == 4:

                main_ob.conversion()

            elif option == 5:

                val = int(input("Enter the value : "))

                power = int(input("Power value : "))

                print(f"{val} raised to {power} = {val ** power} ")

                repeat_2()

            elif option == 6:

                val = int(input("Enter the value : "))

                print(f"Log of {val} = {math.log(val)}")

                repeat_2()

            elif option == 7:

                rad = float(input("Enter the radius : "))

                print(f"Area = {math.pi * (rad ** rad)} ")

                print(f"Circumference / Perimeter = { 2 * math.pi * rad}")

                repeat_2()

            elif option == 8:

                val = float(input("Enter the value : "))

                print(f"e raised to {val} = {math.exp(val)}")

                repeat_2()

            elif option == 9:

                number = int(input("Enter the number : "))

                print(f"Factorial = {main_ob.factorial(number)  }")  
                
                repeat_2()           

            elif option == 10:

                val = int(input("Choose the serial number : \n1. Degree -> Radian\n2. Radian -> Degree"))

                if val == 1:

                    ang = float(input("Enter the value : "))

                    print(f"{math.radians(ang)} radians")

                elif val == 2:

                    ang = float(input("Enter the value : "))

                    print(f"{math.degrees(ang)} degrees")

                else:

                    print("Invalid Input")

                    main_ob.scientific()
                
                repeat_2()

            elif option == 11:

                self.menu()

            else:
                print("Invalid input")

                main_ob.scientific()
        except:

            print("Invalid input")

            main_ob.scientific()     

main_ob = Main()

main_ob.menu()




      



        
        





        
        
