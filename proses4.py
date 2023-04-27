from string import ascii_lowercase,ascii_uppercase ,digits  
def caesar_dec(ciphertext, key_dec):  
    hasil = []  
    for d in ciphertext:  
        if d in ascii_lowercase:  
            dekripsi = ascii_lowercase.index(d)   
            dekripsi = (dekripsi - key_dec) % 26  
            hasil.append(ascii_lowercase[dekripsi])   
        elif d in ascii_uppercase:  
            dekripsi = ascii_uppercase.index(d)   
            dekripsi = (dekripsi - key_dec) % 26  
            hasil.append(ascii_uppercase[dekripsi])   
        elif d in digits:  
            dekripsi = digits.index(d)  
            dekripsi = (dekripsi - key_dec) % 10  
            hasil.append(digits[dekripsi])  
        else:  
            hasil.append(d)
            return "".join(hasil)  
def main():  
    print ("Program Modifikasi Algoritma Caesar Ciph er Dengan Mengalikan kata kunci yang diinputkan de ngan 4")  
    print ("---------------------------------------- ")  
    print ("Program Konversi HasiL Enkripsi ASCII Ke  Algoritma Caesar Cipher")  
    textcipher = open('ciphertext.txt','r').read()   
    ciphertext = input("Masukkan Plainteks Sementara  : ")  
    kunci_awal = input("Masukan Kunci  : ")  
    key_dec = int(kunci_awal) *4  
    print ('\nDeskripsi Cipherteks : \"' + textcipher + '" dengan Kunci ' + str(kunci_awal) + " ")   
    print ("Didapatkan pesan : ")  
    print (caesar_dec(ciphertext, key_dec))   
    print ("---------------------------------------- ")  
if __name__ == '__main__':  
    main()

