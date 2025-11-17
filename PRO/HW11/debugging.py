# The CellPhone class holds data about a cell phone
# <Put your name here>
class CellPhone:
    def __init__(self, manufact, model, price):
        # private data fields
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    ''' The set_manufact method accepts an argument for the phone's manufacturer '''
    def set_manufact(self, manufact):
        self.__manufact = manufact

    ''' The set_model method accepts an argument for the phone's model number '''
    def set_model(self, model):
        self.__model = model

    ''' The set_retail_price method accepts an argument for the phone's retail price '''
    def set_retail_price(self, price):
        self.__retail_price = price

    ''' The get_manufact method returns the phone's manufacturer '''
    def get_manufact(self):
        return self.__manufact

    ''' The get_model method returns the phone's model number '''
    def get_model(self):
        return self.__model

    ''' The get_retail_price method returns the phone's retail price '''
    def get_retail_price(self):
        return self.__retail_price


def main():
    # Get the phone data.
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    # Create an instance of the CellPhone class.
    phone = CellPhone(man, mod, retail)

    # Display the data that was entered.
    print('Here is the data that you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: ${:,.2f}'.format(phone.get_retail_price()))


if __name__ == "__main__":
    main()