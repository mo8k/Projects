class Employee:

    def __init__(self, fullname, hoursworked, hourlyrate):
        
        self.__fullname = fullname
        self.__hoursworked = hoursworked
        self.__hourlyrate = hourlyrate
        self.__tax_rate = 0.07  
        self.__overtimethreshold = 40  
        self.__overtimemultiplier = 1.5 
    
    def get_fullname(self):

        return self.__fullname

    def get_hoursworked(self):

        return self.__hoursworked

    def get_hourlyrate(self):

        return self.__hourlyrate

    def calculate_gross_pay(self):
       
        if self.__hoursworked <= self.__overtimethreshold:
        
            gross_pay = self.__hoursworked * self.__hourlyrate
        else:

            regular_hours = self.__overtimethreshold
            overtime_hours = self.__hoursworked - self.__overtimethreshold
            regular_pay = regular_hours * self.__hourlyrate
            overtime_pay = overtime_hours * (self.__hourlyrate * self.__overtimemultiplier)
            gross_pay = regular_pay + overtime_pay
            
        return gross_pay

    def calculate_tax_amount(self, gross_pay):
       
        return gross_pay * self.__tax_rate

    def calculate_net_pay(self, gross_pay, tax_amount):
       
        return gross_pay - tax_amount
    
def get_validated_name():
   
    while True:
        name = input("Enter the employee's full name: ").strip()
        if name:  
            return name
        else:
            print("Error: Name cannot be empty. Please try again.")

def get_validated_hours():
    
    while True:
        try:
            hours = float(input("Enter hours worked: "))
  
            if hours < 0:
                print("Error: Hours worked cannot be negative. Please try again.")
            else:
                return hours
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def get_validated_rate():
    
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            
            
            if rate < 15.00:
                print(f"Error: Hourly rate cannot be less than $15.00. Please try again.")
            else:
                return rate
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def main():
    
    print("Welcome to the Employee Pay Calculator")
    
    while True:

        name = get_validated_name()
        hours = get_validated_hours()
        rate = get_validated_rate()

        employee = Employee(name, hours, rate)

        gross_pay = employee.calculate_gross_pay()
        tax_amount = employee.calculate_tax_amount(gross_pay)
        net_pay = employee.calculate_net_pay(gross_pay, tax_amount)
 
        print("\n Employee Pay Slip ")
        print(f"Employee: {employee.get_fullname()}")
        print("---------------------------")
        print(f"Gross Pay: ${gross_pay:,.2f}")
        print(f"Tax (7%):  ${tax_amount:,.2f}")
        print(f"Net Pay:   ${net_pay:,.2f}")
        print("---------------------------\n")
   
        while True:
            choice = input("Do you want to enter another employee? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                print("\n" + "="*30 + "\n")
                break  
            elif choice in ['no', 'n']:
                print("\nThank you for using the pay calculator. Goodbye!")
                return  
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()