# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
a= filter(lambda x:x<0 ,lst1)
b= list(map(lambda x:abs(x),a))
print(b)