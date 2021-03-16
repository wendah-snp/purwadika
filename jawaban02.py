def nomor_ponsel(nomor):
    if len(nomor) > 13:
        print('Nomor HP maksimal hanya 13 angka')
    elif nomor[0] != '0' and nomor[1] != '8':
        print('Nomor HP harus dimulai dengan \'08\' ')
    else:
        print(nomor)

hp_user = input('Masukkan Nomor HP : ')
print(nomor_ponsel(hp_user))