dictionary1  = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
total =0
for key,value in dictionary1.items():
    total+=value
print(dictionary1)
print("Total amount is :",total)
