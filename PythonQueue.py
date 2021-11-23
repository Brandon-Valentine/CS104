#Python Queue
names = []

for x in range (10):
    name = input('Enter Name:')
    names.append(name)
    #print(names)

for i in range(len(names)):
    print(names.pop(0))
    
    
