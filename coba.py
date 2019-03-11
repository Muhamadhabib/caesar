list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p = "habib"
c = ""
for i in range(len(p)):
    a = (list.index(p[i])+3)%26
    c = c + list[a]
print(c)