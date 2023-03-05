def menu(self):
    print("""
=========================
SELAMAT DATANG DI ATM-KOE
=========================
1. Tarik uang
2. Deposit uang
3. Periksa saldo
4. Keluar
        """)
    select = input("Pilih menu: ") 
    try:
        select = int(select)
    except ValueError:
        pass
    while not(select == 1 or select == 2 or select == 3 or select == 4):
        print("Masukan tidak valid. Coba lagi!")
        select = input("Pilih menu: ")
        try:
            select = int(select)
        except ValueError:
            pass
    if select == 1:
        self.withdraw()
    elif select == 2:
        self.deposit()
    elif select == 3:
        self.get_balance()
    elif select == 4:
        print("Terima kasih telah bertransaksi di ATM KOE. Sampai jumpa!")
        pass