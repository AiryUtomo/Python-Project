#this program display input from user in a LED-like-display
#input number only

a=["###","  #","###","###","# #","###","###","###","###","###"]
b=["# #","  #","  #","  #","# #","#  ","#  ","  #","# #","# #"]
c=["# #","  #","###","###","###","###","###","  #","###","###"]
d=["# #","  #","#  ","  #","  #","  #","# #","  #","# #","  #"]
e=["###","  #","###","###","  #","###","###","  #","###","###"]

listawal=[a,b,c,d,e]

number=input("enter number = ")
number=list(number)
newlist=[int(i) for i in number]

for i in range (5):
    for y in newlist :
        print(listawal[i][y], end=" ")
    print()
       
    
    
        
    
        
