from string import ascii_lowercase,ascii_uppercase,digits
def caesar_en(text, key):
    result = []
    for c in text:
        if c in ascii_lowercase:
            enkripsi = ascii_lowercase.index(c)
            enkripsi = (enkripsi + key) % 26
            result.append(ascii_lowercase[enkripsi])
        elif c in ascii_uppercase:
            enkripsi = ascii_uppercase.index(c)
            enkripsi = (enkripsi + key) % 26
            result.append(ascii_uppercase[enkripsi])
        elif c in digits:
            enkripsi = digits.index(c)
            enkripsi = (enkripsi + key) % 10
            result.append(digits[enkripsi])
        else:
            result.append(c)
    return "".join(result)
def main():
    text = input("Masukkan Plaintext :")
    kunci = input("Masukkan Kunci : ")
    key = int(kunci) * 4
    print ("\nProgram Modifikasi Algoritma Caesar Cipher Dengan Mengalikan kata kunci yang diinputkan dengan 4") 
    print ("------------------------------------")
    print ("Kasus Caesar Cipher Modifikasi")
    print ("\nPesan : "+text)
    print ("Kunci : "+str(kunci))
    print ('\n Enkripsi \"' + text + '\" dengan Kunci ' + str(kunci) + " ")
    print ("-------------------------------------")
    print ("\t Chiperteks Sementara : "+caesar_en(text, key))
    print ("-------------------------------------")
if __name__ == '__main__':
    main()

