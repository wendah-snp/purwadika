number = int(input('Masukkan angka : '))

if number > 0:
    if number % 2 == 0:
        print('Bilangan',number,'tergolong bilangan GENAP')
    elif number % 2 != 0:
        print('Bilangan',number,'tergolong bilangan GANJIL')
elif number < 0:
    print('Masukkan Bilangan Bulat Positif')
else:
    print(number, 'Bukanlah Bilangan Ganjil Maupun Genap')