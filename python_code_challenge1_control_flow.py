"""
1. Large Power 

Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will 
use a conditional statement to return True if the result is greater than 5000 or return False if it is not.  In order to accomplish this, we will need the 
following steps:

- Define the function to accept two input parameters called base and exponent
- Calculate the result of base to the power of exponent
- Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False
"""

def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
print(large_power(2, 12))
print("")


"""
2. Over Budget
    
Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent. 

The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.
"""
    
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill + electricity_bill + internet_bill + rent:
        return True
    else:
        return False
    
print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 30))
print("")
    

"""
3. Twice As Large

Create a function named twice_as_large() that has two parameters named num1 and num2.

- Return True if num1 is more than double num2. Return False otherwise.
"""

def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False
        
print(twice_as_large(10, 5))
print(twice_as_large(11,5))
print("")




"""
4. Divisible By Ten 

Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.
"""

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
    
print(divisible_by_ten(20))
print(divisible_by_ten(25))
print("")


"""
5. Not Sum To Ten 

Create a function named not_sum_to_ten() that has two parameters named num1 and num2.

Return True if num1 and num2 do not sum to 10. Return False otherwise.
"""

def not_sum_to_ten(num1, num2):
    if (num1 + num2 != 10):
        return True
    else:
        return False 
    
print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5, 5))