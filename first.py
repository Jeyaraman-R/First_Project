#list_basics
print('*****************list_basics_output*********************')

menu=['apple','orange','pine','grapes','lime']

fav=menu

print(menu)


print(menu[2])
print(menu[1:])


#for_in
print('\n\n******************for_in_output********************')

cost=[20,50,40,65,25]
tot=0

for price in cost:
    tot+=price

print(tot)

#if condition
print('\n\n***********if_condition_output*************')

if fav:
    print('all fruites are fav')
else:print('none of this is fav')

if 'kiwi' in menu:
    print('kiwi available here')
else:
    print('kiwi is not available here')


#range
print('\n\n*************range_output***************')

for x in range(5):
    print(x)

for x in range(1,9,2):
    print(x)


#while loop
print('*****************while_loop_output*********************')

count=20

while count>19:
    count+=5

    if count == 35:
        continue
    
    if count == 60:
        break
    

    print(count)


#list_methods
print('\n\n******************list_methods_output*******************')

list1=['apple','pine','grapes','banana']

list2=['papaya','kiwi',]

list1.append('mango')
print(list1) 

list2.extend(list1)
print(list2)

print(len(list2))
list2.insert(10,'lime')
print(list2)

list2.remove('apple')
print(list2)

print(list1)
list1.sort() # it will arrange the values according to alphabatic 
print(list1)
list1.reverse() # it will reverse the value according to index
print(list1)

list2.pop() #last element will be popped.
print(list2)

list2.pop(2)
print(list2)

#list_buildup
print('\n\n********************list_buildup_ouput*******************')

menulist=[]

menulist.append('chicken')
menulist.append('mutton')
menulist.append('sweet')
menulist.insert(1,'onion')
print(menulist)


#list_slices

print('\n\n***********************list_slices_output******************')
print(list1)
print(list2)

print(list1[1:])

list1[1:3]=list2
print(list1)

#list_comphrehension 
print('\n\n******************list_comprehension_output*********************')
#normal method

numbers=[1,2,3,4,5]
cubes=[]

for num in numbers:
    cubes.append(num*num*num)

print(cubes)

#comprehension method
cubes=[num*num*num for num in numbers]
print(cubes)
#############################################
#normal_method
print(menulist)

dish=[]

for name in menulist:
    dish.append(name.upper()+' ''Dish')

print(dish)
#comprehension_method

dish=[name.upper()+' ''Dish' for name in menulist]
print(dish)

########################################################
#normal method
print(numbers)
above=[]
for x in numbers:
    if x>3:
        above.append(x)

print(above)

#comprehension method

above=[x for x in numbers if x>3]
print(above)
print('\n\n********************The_End*******************')
