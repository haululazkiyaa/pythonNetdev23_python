def question(self):
    print("""
=========================
TERIMA KASIH TELAH
BERTRANSAKSI DI ATM-KOE
=========================
Apakah anda ingin melakukan
transaksi kembali? (y/n)
        """)
    confirmation = str(input("Pilih menu: ")) 
    while not(confirmation == "y" or confirmation == "n"):
        print("Masukan tidak valid. Coba lagi!")
        confirmation = str(input("Pilih menu: ")) 
    if confirmation == "y":
        self.menu()
    elif confirmation == "n":
        print("Terima kasih telah bertransaksi di ATM KOE. Sampai jumpa!")
        pass