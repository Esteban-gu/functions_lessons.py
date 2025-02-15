# def check_3_digits(number):
#     return number in range(100,100)

# result = check_3_digits(68)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             pass

# result = check_3_digits([55, 99, 6000])
# print(type(result))

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             return False

# result = check_3_digits([555, 999, 600])
# print(result)

# def check_3_digits(list1):

#     three_digits_list = []

#     for n in list1:
#         if n in range(100,1000):
#             three_digits_list.append(n)
#         else:
#             pass
    
#     return False

# result = check_3_digits([555, 99, 600])

# coffee_prices = [('cappuccino', 1.5),
#                  ('espresso', 1.2),
#                  ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):

#     highest_price = 0 
#     my_most_expensive_coffee = ''

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass
#     return (my_most_expensive_coffee, highest_price)

# print(most_expensive_coffee(coffee_prices))

# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

values = [(10, -50, 90, -150, 450)]

def all_positives(values):

    for n in values:
        if n in values > 0:
            return True
        else:
            pass
        
    return False
    

# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

values = [300, 50, 500]

def sum_of_numbers(values):
    total = 0
    for n in values:
        if n > 0 and n < 1000:
            total += n
        
    return total

print(sum_of_numbers(values))


# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

values = [7, 8, 12, 16, 17, 23, 36]

def count_even(values):
    count = 0
    for n in values:
        if n %2 == 0:
            count += 1

    return count

print(count_even(values))