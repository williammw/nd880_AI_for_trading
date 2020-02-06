word counter
```python
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
    
print(word_counter)
```

split, handy
```python
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)
```

loop with key, value
```python
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
```



loop 
```python
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
        result += count
    
#if the key is in the list of fruits, add the value (number of fruits) to result

#print(basket_items.items())
print("result {}".format(result))
```

while loop :: factorials
```python
# number to find the factorial of
number = 10

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current < number:
    
    # multiply the product so far by the current number
    product *= current 
    current += 1
    # increment current with each iteration until it reaches number

print (product)

```
while for :: factorials
```python
# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# write your for loop here
for num in range(2,number + 1) :
    product *= num
# print the factorial of number
print(product)
```
