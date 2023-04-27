import random  
import string  
from operator import xor  
def konvers_dec(key):  
    textcipher = open('ciphertext.txt','r').read( ) 
    print ("\nCipheteks yang digunakan adalah : " +textcipher)  
    key = input("Kunci yang digunakan adalah  : ")  
    print ("-----------------------------------")   
    convdecimal = []  
    for i in range(len(textcipher)):  
        convdecimal.append(str(ord(textcipher[i]) ))  
        decimal = ' '.join(convdecimal)  
        print ("Hasil konversi ke decimal karakter Ciphertext : ")  
        print (' '.join(convdecimal))  
    convbiner = []  
    for i in range(len(convdecimal)):  
        convbiner.append(str(bin(int(convdecimal[ i]))[2:].zfill(8)))  
        biner = ''.join(convbiner)  
        print ("hasil konversi ke biner karakter Ciphertext : ")  
        print (' '.join(convbiner))  
    convkeydecimal = []  
    for i in range(len(key)):  
        convkeydecimal.append(str(ord(key[i])))   
        print ("\nHasil konversi ke desimal karakter  kunci : ")  
        keydecimal = ' '.join(convkeydecimal)   
        print (" ".join(convkeydecimal))  
    convkeybiner = []   
    for i in range(len(convkeydecimal)):   
        convkeybiner.append(str(bin(int(convkeydecimal[i]))))  
        binerkey = ''.join(convkeybiner)  
        print ("Hasil Konversi ke biner karakter kunc i :")  
        print (' '.join(convkeybiner))  
        print ("==> Didapatkan :")  
        binercipher =biner.replace("b","")   
        print ("Biner Ciphertext : \n"+binercipher)   
        binerkey =binerkey.replace("b","")   
        print ("Biner kunci : \n"+binerkey)   
    plaintext = []  
    for i in range(len(binercipher)):  
        plaintext.append(xor(int(binercipher[i]), 
        int(binerkey[i])))  
        plain =''.join(map(str,plaintext))   
        print ("Hasil XOR : ")  
        print (plain)  
        splits=[plain[x:x+8] for x in range(0,len(plaintext),8)]  
        print ("\nHasil XOR variabel ciphertext dan kunci : \n"+str(splits))  
    hexa = []  
    for i in range(len(splits)):  
        hexa.append(hex(int(splits[i],2)))   
        print ("\nKonversi hasil dari XOR ke Hexa : \n"+str(hexa))  
    dec = []  
    for i in range(len(hexa)):  
        dec.append(int(hexa[i], 16))  
        print ("\nKonversi Hasil dari Hexa ke Desimal  : \n"+str(dec))  
    teks = []  
    for i in range(len(dec)):  
        teks.append(chr(dec[i]))  
        print ("\n---------------------------------")   
        print ("Didapatkan Hasil Plaintext Pesan Sementara : ")  
    return ''.join(teks)  
def main():  
    print ("Program Konversi HasiL Enkripsi ASCII  Ke Algoritma Caesar Cipher")  
    print ("-----------------------------------")   
    print ("konversi ASCII Ke Klasik")   
    key=("")  
    print (konvers_dec(key))  
if __name__ == '__main__':  
    main()

