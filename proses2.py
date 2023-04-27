import random  
import string  
from operator import xor  
def konvers_enc(pesan):  
    key1 = input("Masukkan Kunci Konversi Cipher") 
    print ("---------------------------------\n")   
    convdecimal = []  
    for i in range(len(pesan)):  
        convdecimal.append(str(ord(pesan[i])))   
        decimal = ' '.join(convdecimal)  
        print ("Hasil Konversi ke Desimal Karakter Pe san : ")  
        decimal = ' '.join(convdecimal)  
    print (' '.join(convdecimal))  
    convbiner = []  
    for i in range(len(convdecimal)):  
        convbiner.append(str(bin(int(convdecimal[ i]))[2:].zfill(8)))  
        biner = ''.join(convbiner)  
        print ("hasil konversi ke biner karakter pesa n : ")  
        print (' '.join(convbiner))  
    convkeydecimal = []  
    for i in range(len(key1)):  
        convkeydecimal.append(str(ord(key1[i])))   
        keydecimal = ' '.join(convkeydecimal)   
        print ("\nHasil Konversi ke Desimal Karakter  Kunci : ")  
        print (' '.join(convkeydecimal))  
    convkeybiner = []  
    for i in range(len(convkeydecimal)): 
        convkeybiner.append(str(bin(int(convkeydecimal[i]))))  
    binerkey = ''.join(convkeybiner)  
    print ("Hasil Konversi ke biner karakter kunc i :")  
    print (' '.join(convkeybiner))  
    binerpesan =biner.replace("b","")  
    print ("\n Sehingga ")  
    print ("Biner pesan : \n"+binerpesan)   
    binerkey =binerkey.replace("b","")   
    print ("Biner Key : \n"+binerkey)  
    ciphertext = []  
    for i in range(len(binerpesan)):  
        ciphertext.append(xor(int(binerpesan[i]), int(binerkey[i])))  
        cipher =''.join(map(str,ciphertext))   
        print ("Hasil XOR Biner Pesan dan Biner Key :  ")  
        print (cipher)  
    splits=[cipher[x:x+8] for x in range(0,len(ciphertext),8)]  
    print ("\nHasil XOR Akhir : \n"+str(splits))   
    hexa = []
    for i in range(len(splits)):  
        hexa.append(hex(int(splits[i],2)))   
        print ("\n==>> Konversi Hasil dari XOR ke Hex a : \n"+str(hexa))  
    dec = []  
    for i in range(len(hexa)):  
        dec.append(int(hexa[i], 16))  
        print ("\n==>> Konversi Hasil dari Hexa ke De simal : \n"+str(dec))  
    teks = []  
    for i in range(len(dec)):  
        teks.append(chr(dec[i]))  
        save2file = ''.join(teks)  
    print ("\n---------------------------------")   
    print ("\t Cipherteks Pesan : "+''.join(teks) )  
    print ("-----------------------------------")   
    outfile = open('ciphertext.txt','w')   
    print ("\n\nBukti ::")  
    outfile.write(save2file)  
    return save2file  
def main():  
    print ("Program Konversi Hasil Enkripsi Algor itma Caesar Cipher Yang Telah di Modifikasi Denga n Menambah Nominal Perkalian")  
    print ("-----------------------------------")  
    print ("konversi Klasik Ke ASCII ")   
    pesan = input("Masukkan Cipherteks sementara  :")  
    print (konvers_enc(pesan))  
    if __name__ == '__main__':  
        main()
    