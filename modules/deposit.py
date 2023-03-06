def deposit(self):
    print("""
=========================
MENU SETORAN ATM-KOE
=========================
Silahkan input jumlah 
penyetoran!
        """)
    print("Saldo saat ini: $", self.balance)
    amount = input("$") 
    try:
        amount = int(amount)
    except ValueError:
        pass
    while amount < 1:
        print("Masukan tidak valid. Coba lagi!")
        amount = input("$")
        try:
            amount = int(amount)
        except ValueError:
            pass
    self.balance += amount
    print("Penyetoran sukses, saldo anda sekarang: $", self.balance)
    self.question()
