# list
my_list = [] #create empty list
print(my_list)
my_list = [1, 2, 3, 'example', 3.14] #create list with different data types
print(my_list)

# dictionary
my_dict = {'First': 'python', 'Second': 'java'} #create empty dictionary
print(my_dict)
my_dict['Second'] = 'C++' #changing element
print(my_dict)
my_dict['Third'] = 'Ruby' #adding keyvalue pair
print(my_dict)

# tuple
my_tuple = (1, 2, 3, 'myskill') #create tuple
print(my_tuple)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[:])
print(my_tuple[3][4])

#sets
my_set = {1, 2, 3, 4, 5, 5, 5} #create set
print(my_set)
my_set.add(5)
my_set.add(6) #add element
print(my_set)
my_set.remove(5) #remove element
print(my_set)

my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}

print(my_set.union(my_set_2)) #union
print(my_set.union(my_set_2),'------',my_set | my_set_2) #union
print(my_set.intersection(my_set_2)) #intersection
print(my_set.intersection(my_set_2),'------', my_set & my_set_2) #intersection
print(my_set.difference(my_set_2)) #difference
print(my_set.difference(my_set_2),'------', my_set ^ my_set_2) #difference
print(my_set.symmetric_difference(my_set_2),'------', my_set - my_set_2) #symmetric difference
my_set.clear()
print(my_set)

#conditional statment
#if statment
num = 5
if num > 0:
    print(num, "is a positive number")
print("This statment is  true")

#if else statements
num = 5
if num >= 0:
    print(num, "is a positive or zero")
else:
    print(num, "is a negative number")
print("This statment is  true")

#if elif else statements
num = 7
if num > 0:
    print(num, "is a positive")
elif num == 0:  
    print(num, "is a zero")
else:
    print(num, "is a negative number")
print("This statment is  true")

#nested if statements
num = 8
if num >= 0:
    if num == 0:
        print(num, "is zero")
    else:
        print(num, "is a positive number")
else:
    print(num, "is a negative number")
    
#while loop
num = 1
odd_nums = []
while num:
    if num % 2 != 0: # persen dua adalah modulus dengan 2
        odd_nums.append(num) # append adalah perintah menambahkan elemen ke list
    if num >=20:
        break # break adalah perintah untuk keluar dari loop
    num += 1 # num += 1 artinya num = num + 1
print("The odd numbers are: ", odd_nums)

#for loop
list =  [1, 2, 3, 4, 5]
for num in list: #num merupana pointer atau penunjuk items atau sequence dimana sequence ini adalah list atau list sebagai iteratornya
    print(num)

#for loop with range
for num in range(1, 6):
    print(num)

#for loop with step
for num in range(1, 6, 2): #range merupakan fungsi untuk membuat range dari 1 sampai 6 dengan step 2
    print(num)

#for loop with list comprehension
list = [1, 2, 3, 4, 5]
new_list = []
for num in list:
    new_list.append(num**2) # num**2 is the number of square
print(new_list)

#function with return
# def nama_fungsi(parameter1, parameter2):
#     # Kode di sini akan dijalankan saat fungsi dipanggil
#     hasil = parameter1 + parameter2
#     return hasil

def pow(a): #pow merupakan fungsi menghitung perpangkatan 
    return a**2
print(pow(2))

#function without return
def pow(a): #pow merupakan fungsi menghitung perpangkatan 
    print(a**2)
pow(2)