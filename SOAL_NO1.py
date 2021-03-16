def kata(words):
    x = '*'
    for k in words.split():
        x = x + k.upper()
    x = x + '*'
    if 0 < len(x) < 200:
        print(x)
    elif len(x) == ' ' or len(x) == 0:
        print('Masukkan Sebuah Inputan')
    else:
        print('Batas Karakter Maksimal Hanya 200')
    return x

words = input('Masukkan Sebuah Kalimat: ')
print(kata(words))


