#1
def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

#optional: we are now just checking by passing arguments in our function and printing return value
name="sirjan_Ghimire"
age=19
print(format_string(name,age)) # function call and print

#2
def conditional_check(number):
    if number > 10: return "Greater"
    if number < 10: return "Lesser"
    if number == 10: return "Equal"
   
# optional: we are now checking our function by passing number as argument
number=15
print (f"{number} is {conditional_check(number)}") # function call and print here

#3
def loop_sum(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
    return sum

 # optional: we check the validitiy of our function by passing a number as our parameter
n=5
print (f"sum of number from 1 to {n} is {loop_sum(n)}")

def list_operations(numbers):
  
# Handling empty list case
    if not numbers:
        return (0, None, None)
    
    total_sum = sum(numbers)
    maximum_number = max(numbers)
    minimum_number = min(numbers)
    
    return (total_sum, maximum_number, minimum_number)

# passing parametrs and printing the result
numbers = [4, 7, 2, 9, 12]
result = list_operations(numbers)
print("Sum is", result[0], "Maximun number is", result[1], "Minimum number is", result[2])


def dict_operations(students_dict):

    # we filter the name of students above 80
    high_scorers = [name for name, score in students_dict.items() if score > 80]
    return high_scorers

# Example Usage and printing
students = {
    "Ram": 75,
    "Hari": 82,
    "Sirjan": 95,
    "kedar": 60,
    "samir": 88
}

result = dict_operations(students)
print("Students scoring above 80:", result)


def set_operations(list1, list2):
    return set(list1) & set(list2)

# initializing a list and printing common value
list1 = [1, 2, 3, 4, 5,6]
list2 = [4, 6,9,10,23]
print(set_operations(list1, list2))



def arithmetic_ops(a, b):
    result = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': a / b if b != 0 else 'not defined'  # Handle division by zero
    }
    return result
 
 # passing parameters and printing
a = 10.3
b = 2.5
print(arithmetic_ops(a, b))

def logical_ops(x, y):
    result = {
        'and': x and y,
        'or': x or y,
        'not_x': not x
    }
    return result
    
    # assigning , passing arguments and printing
x = True
y = False
print(logical_ops(x, y))

def bitwise_ops(a, b):
    result = {
        'and': a & b,
        'or': a | b,
        'xor': a ^ b
    }
    return result

# assigning , passing arguments and printing
a = 5  
b = 3  
print(bitwise_ops(a, b))