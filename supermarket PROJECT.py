print("Olatokunbo Ogunlade, CodeLagos python class project\n")

print("Email address:olatokunboalege@gmail.com\n")

print("Facilitator:Mr Onasanya Dotun\n")

print("Muster point Ogba\n")

print("This program is an online fruit mart\n")


#Create a dictionary to store stock prices
price = {
    
 "pineapple": 250,
 "water melon": 200,
"apple": 100,
 "kiwi": 200,
"orange": 150,
"grapes": 300 
}





print("Welcome to Fruitee store.The following fruits are available\n1)pineapple\n2)water melon\n3)apple\n4)kiwi\n5)orange\n6)grapes")

#make a list to store items
shopping_list = []

#instructions
print("Enter your shoping list")
print("Enter 'DONE' to stop adding items")

while True:
    try:
        new_item = input("> ") #request for list
        if new_item == 'DONE'.lower(): #stop the program from running
            break
        shopping_list.append(new_item) #adding new fruits
    except KeyError:
        print('Sorry, we do not have that item')

print("Here's your list:") #display the list of users choice of fruits

#prints out the fruits
for item in shopping_list:
    try:
        print(item)
        print("price:%s" % price[item])
    except KeyError:
        print('Sorry, we do not have that item')
    
#Calculating total bill
def compute_bill(fruit):
    total = 0
    for item in fruit:
        total += price[item]
        return total
print ("Your total bill is: ",compute_bill(shopping_list))
print ("Thanks for shopping at Fruitee store")


