# Bankamatik Uygulaması



hesapA = {
    'ad': 'Aykan SARIDOĞAN',
    'hesapNo' : '13245876',
    'bakiye': 3000,
    'ekHesap':2000
}

hesapB = {
    'ad': 'Ahmet DENİZ',
    'hesapNo' : '13248876',
    'bakiye': 4000,
    'ekHesap':1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        print('Paranızı alabilirsiniz...')
    else:
        toplam = hesap['bakiye']+ hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                print('Paranızı alabilirsiniz....')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")


        else:
            print('Üzgünüz... Bakiyeniz yetersiz...')



paraCek(hesapA, 3000)








