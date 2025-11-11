class Employee:
    """
    A class to represent an Employee. 
    
    Attributes:
        __full_name (str): The employee's full name (private) [cite: 7]
        __hours_worked (float): The employee's hours worked (private) [cite: 7]
        __hourly_rate (float): The employee's hourly rate (private) [cite: 7]
    """
    
    # 1. Constructor to initialize the private attributes
    def __init__(self, full_name, hours_worked, hourly_rate):
        """
        Constructs all the necessary attributes for the employee object.
        """
        self.__full_name = full_name
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate
        self.__tax_rate = 0.07  # 7% tax rate 
        self.__overtime_threshold = 40  # Standard 40-hour week 
        self.__overtime_multiplier = 1.5  # Time-and-a-half 

    # --- Getters (Accessors) ---
    # These methods safely get the private attribute values
    
    def get_full_name(self):
        """Returns the employee's full name."""
        return self.__full_name

    def get_hours_worked(self):
        """Returns the employee's hours worked."""
        return self.__hours_worked

    def get_hourly_rate(self):
        """Returns the employee's hourly rate."""
        return self.__hourly_rate

    # --- Calculation Methods ---
    
    def calculate_gross_pay(self):
        """
        Calculates the employee's gross pay, including overtime. 
        """
        if self.__hours_worked <= self.__overtime_threshold:
            # Regular pay only [cite: 19]
            gross_pay = self.__hours_worked * self.__hourly_rate
        else:
            # Calculate regular pay and overtime pay separately
            regular_hours = self.__overtime_threshold
            overtime_hours = self.__hours_worked - self.__overtime_threshold
            
            # Regular pay part
            regular_pay = regular_hours * self.__hourly_rate
            
            # Overtime pay part [cite: 20]
            overtime_pay = overtime_hours * (self.__hourly_rate * self.__overtime_multiplier)
            
            # Total gross pay
            gross_pay = regular_pay + overtime_pay
            
        return gross_pay

    def calculate_tax_amount(self, gross_pay):
        """
        Calculates the 7% tax on the gross pay. [cite: 12, 21]
        """
        return gross_pay * self.__tax_rate

    def calculate_net_pay(self, gross_pay, tax_amount):
        """
        Calculates the net pay by subtracting tax from gross pay.
        """
        return gross_pay - tax_amount

# --- Helper Functions for Input Validation ---

def get_validated_name():
    """
    Gets the employee's name from the user. 
    """
    while True:
        name = input("Enter the employee's full name: ").strip()
        if name:  # Checks if the string is not empty
            return name
        else:
            print("Error: Name cannot be empty. Please try again.")

def get_validated_hours():
    """
    Gets and validates the hours worked from the user.
    Rejects negative numbers. [cite: 10, 11]
    """
    while True:
        try:
            hours = float(input("Enter hours worked: "))
            
            # validateHours logic [cite: 16]
            if hours < 0:
                print("Error: Hours worked cannot be negative. Please try again.")
            else:
                return hours
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def get_validated_rate():
    """
    Gets and validates the hourly rate from the user.
    Rejects rates less than $15.00. [cite: 10, 11]
    """
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            
            # validateRate logic [cite: 18]
            if rate < 15.00:
                print(f"Error: Hourly rate cannot be less than $15.00. Please try again.")
            else:
                return rate
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

# --- Driver Program ---

def main():
    """
    The main driver program.
    """
    print("Welcome to the Employee Pay Calculator")
    
    while True:
        # 1. Get validated input from the user
        name = get_validated_name()
        hours = get_validated_hours()
        rate = get_validated_rate()
        
        # 2. Create an instance of the Employee class
        #    This is where the object is "born"
        employee = Employee(name, hours, rate)
        
        # 3. Use the object's methods to perform calculations
        gross_pay = employee.calculate_gross_pay()
        tax_amount = employee.calculate_tax_amount(gross_pay)
        net_pay = employee.calculate_net_pay(gross_pay, tax_amount)
        
        # 4. Display the results for this employee 
        print("\n--- Employee Pay Slip ---")
        print(f"Employee: {employee.get_full_name()}")
        print("---------------------------")
        print(f"Gross Pay: ${gross_pay:,.2f}")
        print(f"Tax (7%):  ${tax_amount:,.2f}")
        print(f"Net Pay:   ${net_pay:,.2f}")
        print("---------------------------\n")

        # 5. Check if the user wants to enter another employee 
        while True:
            choice = input("Do you want to enter another employee? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                print("\n" + "="*30 + "\n")
                break  # Breaks inner loop and continues outer loop
            elif choice in ['no', 'n']:
                print("\nThank you for using the pay calculator. Goodbye!")
                return  # Exits the main function, ending the program
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

# This standard Python line checks if the script is being run directly
# If so, it calls the main() function to start the program.
if __name__ == "__main__":
    main()