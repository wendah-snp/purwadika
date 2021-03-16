def kata(word):
    upper_word = word.upper()
    words = upper_word.replace(' ','')

    if words == '':
        print('Masukkan sebuah inputan')
    elif len(words) > 200:
        print('Batas Karakter Maksimal Hanya 200')
    else:
        print('*'+ words + '*')

word = input('Masukkan Sebuah Kalimat: ')
print(kata(word))

