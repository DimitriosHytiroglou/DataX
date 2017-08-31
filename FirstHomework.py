#Task 1
a=[]

#Task 2
i=1
while i <= 100:
    a.append(i)
    i+=3

print(i)
print(a)

#Task 3
a2=[]

j=2
while j <= 46:
    a2.append(j)
    j+=0.5

print(a2)

#Task 4
for k in range(len(a)):
    if a[k] % 2 == 0:
        a[k]=a[k]*2

print(a)

#Task 5
sum_of_a = a[0]+ sum(a[2:19]) + sum(a[21:])
print(sum_of_a)

#Task 6

sum_a=sum(a)
len_a=len(a)
mean_a=sum_a/len_a
print(mean_a)

#Task 7
b=[]

#Task 8

sentence='I am so excited about Data-X. It is important to be able to work with data.'

b = sentence.split()
print(b)

#Task 9

count=0
for c in range(len(b)):
    count+=b[c].count('e')
print(count)

#Task 10

for r in range(len(b)):
    if 'i' or 'I' in b[r]:
        b[r]=b[r].replace('i','1')
        b[r]=b[r].replace('I','1')

print(b)

#Task 11

eofhw='This is the end of the first HW'
bb=eofhw.split()

for bc in range(len(bb)):
    b.append(bb[bc])


for c13 in range(len(b)):
    b[c13]=b[c13][::-1]

print(b)

#Task 12

sentence=''
for c14 in reversed(range(len(b))):
    sentence+=(b[c14]+' ')

print(sentence)

#Task 13

dictionary={1001:'Alpha',1002:'Beta',1003:'Gamma',1004:'Delta',1005:'Tau'}

for key, value in dictionary.items():
    dictionary[key] = dictionary[key].lower()

print(dictionary)

#Task 14

SetA=[1,3,5,7,8,9]
SetB=[2,5,30,10]

SetC=[]

for st in range(len(SetA)):
    if SetA[st] in SetB:
        SetC.append(SetA[st])

print(SetC)
