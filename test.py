## This is test Python File

#To check commmon letters in 2 strings
s1=input("Enter the first string : ")
s2=input("Enter the second string : ")
#print(set(s1),set(s2),set(s1)&set(s2))
a=list(set(s1)&set(s2))
print("Comman letter are ")
for i in a:
    print(i)