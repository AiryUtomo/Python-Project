# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0

#nama: Oei Airy Utomo
#netacad email cth: 'abcd@gmail.com'
email='oeiairy.utomo@gmail.com'


# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
    katalog_letter=[]

    for i in items :
        if i.startswith(letter) :
            katalog_letter.append(i)

    return katalog_letter


#Graded

def counter_item(items):
    dict_jumlahitem={}

    for i in items :
        jumlah =items.count(i)
        dict_jumlahitem[i]=jumlah

    return dict_jumlahitem   


#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {} # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!
for i in range(len(fruits)):
    fruit_price[fruits[i]]= prices[i]
    
def total_price(dcounter,fprice):
    total_harga = 0

    for i in dcounter :
        price = dcounter[i]*fprice[i]
        total_harga = total_harga + price

    return total_harga
 

#Graded

def discounted_price(total,discount,minprice=100):
    if total >= minprice :
        harga_setelahdiskon = ((minprice-discount)/100)*total
    else :
        harga_setelahdiskon = total

    return harga_setelahdiskon
  

#Graded

def print_summary(items,fprice):
    chart_sorted = sorted(items)

    jumlahbuah = [i for i in (counter_item(chart_sorted).values())]
    namabuah = [i for i in (counter_item(chart_sorted).keys())]
    totalhargabuah = [(counter_item(chart_sorted)[i]*fprice[i]) for i in counter_item(chart_sorted)]

    for j in range(len(jumlahbuah)) :
        print (jumlahbuah[j],namabuah[j],":",totalhargabuah[j])
    
    print ("total :",total_price(counter_item(chart_sorted),fruit_price))
    print ("discount price :", discounted_price(total_price(counter_item(chart_sorted),fruit_price),10,minprice=100))

