import datetime
from time import sleep

def login(self):
    time = datetime.datetime.now()
    pin = str(input("Masukan PIN: "))
    if pin == "123123":
        self.menu() 
    else:
        loggedIn = False
        while not loggedIn:
            if self.locked_time == None:
                if self.failed_attemps < 2:
                    self.failed_attemps += 1
                    print("PIN yang anda masukan salah!")
                    print("Sisa percobaan", 3 - self.failed_attemps)
                    pin = str(input("Masukan PIN: "))
                    if pin == "123123":
                        loggedIn = True
                else:
                    print("PIN yang anda masukan salah!")
                    print("Terlalu banyak percobaan!")
                    self.locked_time = datetime.datetime.now()
            else:
                difference = datetime.datetime.now() - self.locked_time
                if difference.seconds > 30:
                    self.failed_attemps = 0
                    self.locked_time = None
                else:
                    print("Harap tunggu", 30 - difference.seconds, "detik sebelum mencoba kembali!")
                    pin = str(input("Masukan PIN: ")) 
                    if pin == "123123":
                        loggedIn = True
        self.menu()