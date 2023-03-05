def withdraw(self):
    if self.balance > 0:
        print("""
=========================
MENU PENARIKAN ATM-KOE
=========================
Silahkan input jumlah 
penarikan!
            """)
        print("*Batas penarikan: $", self.balance)
        amount = input("$") 
        try:
            amount = int(amount)
        except ValueError:
            print("""
+++++++++++++++++++++++++++++++++++++++++++++
+ ERROR: Masukan tidak valid. Mencoba lagi! +
+++++++++++++++++++++++++++++++++++++++++++++
                """)
            self.withdraw()
        while amount > self.balance or amount < 0:
            print("""
+++++++++++++++++++++++++++++++++++++++++++++
+ ERROR: Masukan tidak valid. Mencoba lagi! +
+++++++++++++++++++++++++++++++++++++++++++++
                """)
            self.withdraw()
        self.balance -= amount
        print("Penarikan sukses, sisa saldo anda: $", self.balance)
        self.question()
    else:
        print("""
=========================
    W A R N I N G !
=========================
Anda berada pada masa 
dormant! Saldo anda saat 
ini $0. Lakukan pengisian
saldo agar dapat bertansaksi
kembali! (y)
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
