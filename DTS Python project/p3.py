# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='oeiairy.utomo@gmail.com'
#nama=Oei,Airy Utomo


# Graded
def caesar_encript(txt,shift):
    encripted_text = ""
    shift =shift%26
    
    for ch in txt:
        if ch.isalpha() & ch.islower():
            shifted_alphabet = ord(ch) + shift
            if shifted_alphabet > ord('z'):
                shifted_alphabet -= 26
            if shifted_alphabet < ord('a'):
                shifted_alphabet += 26
            finalLetter = chr(shifted_alphabet)

        elif ch.isalpha() & ch.isupper():
            shifted_alphabet = ord(ch) + shift
            if shifted_alphabet > ord('Z'):
                shifted_alphabet -= 26
            if shifted_alphabet < ord('A'):
                shifted_alphabet += 26
            finalLetter = chr(shifted_alphabet)
            
        else :
            finalLetter = ch

        encripted_text += finalLetter

    return encripted_text

def caesar_decript(chiper,shift):
    return caesar_encript(chiper,-shift)


# Graded
 
# Fungsi mengacak urutan
def shuffle_order(text,order):
  return ''.join([text[i] for i in order])
 
# Fungsi untuk mengurutkan kembali sesuai order
def deshuffle_order(sftxt,order):
    sftxt_des=""
    for i in order :
        j = order.index(i)
        sftxt_des += sftxt[order.index(j)]

    return sftxt_des


#Graded
import math

# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
def send_batch(txts,batch_order,shift=3):
    batch_list = []
    batch_cpr=[]
    n=len(batch_order)

    txts = caesar_encript(txts,shift)  
    
    while len(txts)%n != 0 :
        txts=txts+"_"
    
    batch_list= [txts[i:i+n] for i in range(0, len(txts), n)]
    
    for k in batch_list :
        k_shuffle = shuffle_order(k,batch_order)
        batch_cpr.append(k_shuffle) 
    
    return batch_cpr
                 
# batch_cpr: list keluaran send_batch
# fungsi ini akan mengembalikan lagi ke txt semula
def receive_batch(batch_cpr,batch_order,shift=3):
    batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
    return ''.join(batch_txt).strip('_')
