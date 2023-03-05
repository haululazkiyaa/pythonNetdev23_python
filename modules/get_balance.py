def get_balance(self):
    print("""
=========================
SELAMAT DATANG DI ATM-KOE
=========================
        """)
    print("Saldo saat ini: $", self.balance)
    print("""
        (y) untuk kembali
        """)
    back = str(input("Kembali ke menu? ")) 
    while not(back == "y" or back == "n"):
        print("Masukan tidak valid. Coba lagi!")
        back = str(input("Kembali ke menu? ")) 
    if back == "y":
        self.menu()
    elif back == "n":
        print("Terima kasih telah bertransaksi di ATM KOE. Sampai jumpa!")
        pass
