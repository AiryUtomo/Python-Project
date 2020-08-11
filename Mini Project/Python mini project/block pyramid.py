#buatlah bentuk piramid dari "*"
#input user = jumlah "*" yang tersedia
#contoh input = 5, output :
# *
# **
#sisa "*" tidak terpakai = 2

stars = int(input("Enter the number of stars : "))
	
i=1 #jumlah "*" di layer terakhir
j=0 #tinggi piramid
k=1 #jumlah "*" terpakai

while k<stars :
    sisa = stars-k
    if sisa < i :
        break
    k = k+i
    print("*"*i)
    i=i+1
    j=j+1
    
height = j
    
print("The height of the pyramid:", height)
