list = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p = "udinus"
c = ""
for i in range(len(p)):
    a = (list.index(p[i])+13)%26
    c = c + list[a]
print(c)
nm = ""
for line in range(25):
    for l in range(len(c)):
        de = (list.index(c[l])-line)%26
        nm = nm + list[de]
        print(nm)
print(nm)



