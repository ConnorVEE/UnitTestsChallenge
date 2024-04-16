import unittest
from user_input import UserInputs
from datetime import datetime

##TEST SYMBOL FUNCTION###
class TestSymbolInput(unittest.TestCase):

    def test_valid_symbol(self):
        # Test valid symbols
        valid_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NFLX', 'FB']
        for symbol in valid_symbols:
            self.assertTrue(UserInputs.check_stock(symbol, 'JLFXYX4J4I20CF8E'), f"Symbol '{symbol}' is not valid")

    def test_invalid_symbol(self):
        # Test invalid symbols
        invalid_symbols = ['', '123', 'Abcdefg', 'GOOGL1', 'MS/FT', 'ABCDEFG']
        for symbol in invalid_symbols:
            self.assertFalse(UserInputs.check_stock(symbol, 'JLFXYX4J4I20CF8E'), f"Symbol '{symbol}' is erroneously valid")


##TEST CHART TYPE FUNCTION###

#This is basically the logic that we have present in our actual chart selection function
def chartTypeFuncCOPY(input): 

    if (input == '1' or input == '2'):
        return True
    else: 
        return False

class TestChartTypeInput(unittest.TestCase):

    def test_valid_input(self):
        # Test valid inputs
        valid_inputs = ['2', '1']
        for input in valid_inputs: 
            self.assertTrue(chartTypeFuncCOPY(input), f"Input '{input}' is not valid")

    def test_invalid_input(self):
        # Test invalid inputs
        invalid_inputs = ['3', '5', '01', '02', '   2', '  1', '  01']
        for input in invalid_inputs:
            self.assertFalse(chartTypeFuncCOPY(input), f"Input '{input} is erroneously valid")


##TEST TIME SERIES INPUT###

# This is basically the logic that we have present in our actual timeSeries selection function
def selectTimeSeriesCOPY(input): 

    if input in ['1', '2', '3', '4']:
        return True
    else: 
        return False

class TestTimeSeries(unittest.TestCase):
    
    def test_valid_input(self):
        # Test valid inputs
        valid_inputs = ['2', '1', '3', '4']
        for input in valid_inputs: 
            self.assertTrue(selectTimeSeriesCOPY(input), f"Input '{input}' is not valid")

    def test_invalid_input(self):
        # Test invalid inputs
        invalid_inputs = ['5', '01', '02', '   2', '  1', '  01', '4.5']
        for input in invalid_inputs:
            self.assertFalse(selectTimeSeriesCOPY(input), f"Input '{input} is erroneously valid")

## DATE TESTING ###

def selectDateCOPY(startDate, endDate):
    try:
        parsedStartDate = datetime.strptime(startDate, "%Y-%m-%d")
        parsedEndDate = datetime.strptime(endDate, "%Y-%m-%d")
        if (parsedEndDate > parsedStartDate):
            return True
        else:
            return False
    except ValueError:
        return False
    

## TEST START DATE ##

class TestSelectDate(unittest.TestCase):

    def test_valid_dates(self):
        # Test valid date inputs
        valid_start_date = '2024-01-01'
        valid_end_date = '2024-01-15'
        result = selectDateCOPY(valid_start_date, valid_end_date)
        self.assertTrue(result)

    def test_invalid_dates(self):
        # Test invalid date inputs
        invalid_start_date = '2024-01-20'  # End date before start date
        invalid_end_date = '2024-01-10'
        result = selectDateCOPY(invalid_start_date, invalid_end_date)
        self.assertFalse(result)  

        invalid_format_start_date = '20-01-2024'  # Incorrect date format
        invalid_format_end_date = '2024/01/20'
        result = selectDateCOPY(invalid_format_start_date, invalid_format_end_date)
        self.assertFalse(result)  


if __name__ == '__main__':
    unittest.main()


