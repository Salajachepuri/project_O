# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:58:50 2023

@author: sailaja chepuri
##variables and strings##"""
a=2
b=8
c=a+b
print(c)


###concatenation / combining###
first_name="sailaja"
last_name="chepuri"
full_name=first_name+' ' +last_name
print(full_name)  


###lists###
bikes =['treck', 'redline', 'giant']

first_bike= bikes[0]
print(first_bike)
last_bike= bikes[-2]
print(last_bike)
for bike in bikes:
    print(bike)
bikes=[]
bikes.append('treck')
bikes.append('redline')
bikes.append('giant')   
print(bikes)
squares= []
for x in range(1,11):
    squares.append(x**2)
    print(squares)
 ###slicing a list###
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
    print(finishers)

###loops###
for number in range(1, 1001):
  print(number)
  ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
  print(ages)

ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
oldest = max(ages)
  print(ages)
  dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')
for dog in dogs:
 print("Hello " + dog + "!")


users = []
users.append('val')
users.append('bob')
users.append('mia')
print(users)
users.insert(0, 'joe')
users.insert(3, 'bea')
print(users)

users.sort()
print(sorted(users))
print(sorted(users, reverse=True))

for user in users:
print(user)
for user in users:
print("Welcome, " + user + "!")

print("Welcome, we're glad to see you all!")




for number in range(1001):
 print(number)

for number in range(1, 1001):
 print(number)

numbers = list(range(1, 1000001))
  




alien_0 = {'color': 'green', 'points': 5}


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])



alien_0 = {'color': 'green'}
alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)
print(alien_color)
print(alien_points)

alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)



#%%
"Week of 8th July 2023"
#%%


"Variables and Strings"

a=2
print(a)

s="Python"
print(s)
"revers string"
s_rev=s[::-1]
print(s_rev)

"accessing elements in a string"

first_element = s[0]
last_element = s[-1]
last_element = s[5]

"loop through a string"

for char in s:
    
    print(char)

"conditional statements "    
if s[1]=='P':
    print("item is P")
else:
    print("Item is other than P")
    
    
    
    
    
    
































   