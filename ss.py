sales=[120,23,45,48,46,45]
#x=eval(input("Enter Sales value"))
#sales.append(x)
#print(dir(sales))
print(sales)
#sales.clear()
#sales2=[x for x in sales if x!=45]
#sales.remove(45)
#del sales[sales.index(45):sales.index(48)+1]
print(sales)
for i in [2,-1]:
    del sales[i]

print(sales)
'''while(True):
    x=eval(input("Enter Sales value"))
    if x<0:
        break
    else:
        sales.append(x)
print(sales)
print(set(sales))'''
