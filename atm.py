class ATM:

    def __init__(self):
        self.balance = 1000
        self.failed_attemps = 0
        self.locked_time = None 

    from modules.login import login
    from modules.menu import menu
    from modules.withdraw import withdraw
    from modules.deposit import deposit
    from modules.get_balance import get_balance
    from modules.question import question