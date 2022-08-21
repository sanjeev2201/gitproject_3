"""TO SORT ALPHANUMERIC
 OUTPUT-ABD134"""
s1 = "B9Adabvxg5D13"
alpha = []
num = []
for i in s1:
    if i.isalpha():
        alpha.append(i)
    if i.isdigit():
        num.append(i)

print(alpha)
print(num)
sort = ' '.join(sorted(alpha) + sorted(num))
print("sorted alphanumeric in string", sort)
