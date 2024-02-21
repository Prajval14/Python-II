# Print array with only even digits using function
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def printEvenNumbers(list1):
    return [num for num in list1 if num % 2 == 0]

print(printEvenNumbers(list1))

#----------------------------------------------------------------------------------------------------
# Define IceShoppeOrder class
class IceShoppeOrder:
    def __init__(self, customer_name, flavor, size):
        self.customer_name = customer_name
        self.flavor = flavor
        self.size = size

# Create an array to store IceShoppeOrder objects
order_list = []

# Add orders to the array
order1 = IceShoppeOrder("Alice", "Chocolate", "Large")
order_list.append(order1)

order2 = IceShoppeOrder("Bob", "Vanilla", "Medium")
order_list.append(order2)

order3 = IceShoppeOrder("Eve", "Strawberry", "Small")
order_list.append(order3)

# Print the orders
for order in order_list:
    print(f"Customer: {order.customer_name}, Flavor: {order.flavor}, Size: {order.size}")
#----------------------------------------------------------------------------------------------------
def filter_string_values(input_dict):
    return {key: value for key, value in input_dict.items() if isinstance(value, str)}

# Test the function
input_dict = {'a': 1, 'b': 'hello', 'c': 3.14, 'd': 'world'}
print(filter_string_values(input_dict))

#----------------------------------------------------------------------------------------------------
def set_intersection(set1, set2):
    return set1.intersection(set2)

# Test the function
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set_intersection(set1, set2))

#----------------------------------------------------------------------------------------------------
from array import array

# Create an array of colors
colors = array('u', ['r', 'e', 'd', 'g', 'r', 'e', 'e', 'n', 'b', 'l', 'u', 'e'])

# Create an array of pets
pets = array('u', ['c', 'a', 't', 'd', 'o', 'g', 'b', 'i', 'r', 'd'])

print(colors)
print(pets)

#----------------------------------------------------------------------------------------------------
# Implementing a stack using a list FIFO
stack = []

# Push pets onto the stack
stack.append('cat')
stack.append('dog')
stack.append('bird')

# Pop pets from the stack
print(stack.pop())  # Output: 'bird'
print(stack.pop())  # Output: 'dog'

#----------------------------------------------------------------------------------------------------
from queue import Queue

# Create a FIFO queue for colors
color_queue = Queue()

# Enqueue colors
color_queue.put('red')
color_queue.put('green')
color_queue.put('blue')

# Dequeue colors
print(color_queue.get())  # Output: 'red'
print(color_queue.get())  # Output: 'green'