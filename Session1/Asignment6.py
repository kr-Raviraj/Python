d=dict()
for x in range(1,6):
    d[x]=x**3
print(d)


'''nums = []
for i in range(1000, 3000):
    cs = str(i)
    if (int(cs[0])%2==0) and (int(cs[1])%2==0) and (int(cs[2])%2==0) and (int(cs[3])%2==0):
        nums.append(cs)
print( ",".join(nums))'''

items = input()
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

