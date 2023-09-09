"""
1. Every Three Numbers

Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed 
to the function as an input parameter. Here is what we need to do:

- Define the function to accept one parameter for our starting number
- Calculate the numbers between the starting number and 100 while incrementing by 3
- Store the numbers in a list
- Return the list
"""

def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))


"""
2. Remove Middle

Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an 
ending index. All elements with an index between the starting and ending index should be removed from the list. Here are the steps:

- Define the function to accept three parameters: the list, the starting index, and the ending index
- Get all elements before the starting index
- Get all elements after the ending index
- Combine the two partial lists into the result
- Return the result
"""

def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


"""
3. More Frequent Item

Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of 
two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another 
for the first item we are comparing, and another for the second item. Here are the steps:

- Define the function to accept three parameters: the list, the first item, and the second item
- Count the number of times item1 shows up in our list
- Count the number of times item2 shows up in our list
- Return the item that appears more frequently in my_list — if both items show up the same number of times, return item1
"""

def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


"""
4. Double Index

Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the 
value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

- Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
- Test if the index is invalid. If it’s invalid then return the original list
- If the index is valid then get all values up to the index and store it as a new list
- Append the value at the index times 2 to the new list
- Add the rest of the list from the index onto the new list
- Return the new list
"""

def double_index(my_list, index):
  if index >= len(my_list):
    return my_list
  else:
    my_new_list = my_list[0:index]
  my_new_list.append(my_list[index]*2)
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list

print(double_index([3, 8, -10, 12], 2))


"""
5. Middle Item

For the final code challenge, we are going to create a function that finds the middle item from a list of values. This will be different depending on 
whether there are an odd or even number of values. In the case of an odd number of elements, we want this function to return the exact middle value. If 
there is an even number of elements, it returns the average of the middle two elements. Here is what we need to do:

- Define the function to accept one parameter for our list of numbers
- Determine if the length of the list is even or odd
- If the length is even, then return the average of the middle two numbers
- If the length is odd, then return the middle number
"""

def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))