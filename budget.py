# helper functions
def calculate_stars(n, len_cat):
    # if even number
    if (n % 2) == 0:
        x = (n - len_cat) / 2
        y = (n - len_cat) / 2
    else:
        x = round((n - len_cat) / 2)
        y = round((n - len_cat) / 2) + 1
    
    return int(x), int(y)

def create_spend_chart():
    pass

# define class category
class Category:

    def __init__(self, name, balance=0, ledger=None):
        self.name = name
        self.balance = balance
        self.ledger = []
    
    def __str__(self):
        n_starts = calculate_stars(30, len(self.name))

        header = """{x}{name}{y}""".\
            format(name=self.name, x="*" * n_starts[0], y="*" * n_starts[1])

        body = ""

        for i in self.ledger:

            f_num = "{:.2f}".format(i['amount'])
            x = len(i['description'][:23])
            y = len("{:.2f}".format(i['amount']))
  
            space_count = 30 - (x + y)
            spaces = " " * space_count
            
            s1 = ("{a1}{sp}{a2}".format(a1=i['description'][:23], sp=spaces, a2=str(f_num)))

            body = body + s1 + "\n"
        
        total_amt = "Total: " + str("{:.2f}".format(self.balance))
        
        cat_str = "\n" + header + "\n" + body + total_amt

        return cat_str
    
    def deposit(self, amount, description = "No description"):
        self.balance += amount
        self.ledger.append({"amount": amount, "description":description})

    def withdraw(self, amount, description="No description"):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -abs(amount), "description":description})

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other):
        # check if there are enough funds:
        if self.check_funds(amount):
            description_s1 = "Transfer to {cat}.".format(cat=other.name)
            description_s2 = "Transfer from {cat}.".format(cat=self.name)

            self.withdraw(amount, description_s1)
            other.deposit(amount, description_s2)

    def check_funds(self, amount):
        if amount < self.balance:
            return True
        else:
            return False

