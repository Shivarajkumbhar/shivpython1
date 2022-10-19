shiv=[1,3,5,12,9,78,12,89,200,100]
shiv.sort()
print(shiv)
shiv.sort(reverse=True)
print(shiv)
shiv.reverse()
print(shiv)
print(len(shiv))
print(shiv[9])
shiv[9]=1000
print(shiv)

languages=["cpp","java","html","css","python","c","javascript"]
apple=["swift","thar","audi"]
print(languages)
print(apple)
programming=languages.copy()
programming=list(languages)
programming=languages
print(programming)

all=languages+apple
print(all)
all=languages.extend(apple)
print(all)


my_list = [21, 44, 35, 11]
for index, val in enumerate(my_list): 
    print(index, val)
    
    
my_list = [21, 44, 35, 11]
for index, val in enumerate(my_list, start=1):
    print(index, val)


my_list = [21, 44, 35, 11]
for index in range(len(my_list)): 
    value = my_list[index] 
    print(index, value)
    
    
my_list = [[1], [2, 3], [4, 5, 6, 7]]
flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
