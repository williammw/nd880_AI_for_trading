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


count by 
```python
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)
```

countby check
```python
start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)
```

countby conditional
```python 

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
```

Quiz break, Continue
```python
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
while len(news_ticker) < 140:
    for headline in headlines:
        news_ticker += headline + ' '
        if len(news_ticker) > 140:
            news_ticker = news_ticker[:140]
    


#print('{} and len {}'.format(news_ticker, len(news_ticker)))
print(news_ticker)
```

3\*4 to 4\*3 matrix
```python
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)
```

enumerate
```python
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)
```

Quiz: extract first names
```python
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split(' ')[0] for name in names]# write your list comprehension here
print(first_names)
```

Quiz Multiple of tree
```python
multiples_3 = [x * 3 for x in range(1, 21)]# write your list comprehension here
print(multiples_3)
```


filter names
```python
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
```