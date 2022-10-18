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
