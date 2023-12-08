"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=False, hours=False, rate=False, contract=False, contract_rate=False, bonus=False):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.rate = rate
        self.contract = contract
        self.contract_rate = contract_rate
        self.bonus = bonus

    def get_pay(self):
        pay = 0

        if self.salary:
            pay += self.salary
        if self.hours and self.rate:
            pay += (self.hours * self.rate)
        if self.contract and self.contract_rate:
            pay += (self.contract * self.contract_rate)
        if self.bonus:
            pay += self.bonus

        return pay

    def __str__(self):
        string = self.name + " works on a "
        if self.salary:
            string += "monthly salary of " + str(self.salary)
        if self.hours:
            string += f"contract of {str(self.hours)} hours at {str(self.rate)}/hour"

        if self.contract:
            string += f" and receives a commission for {str(self.contract)} contract(s) at {str(self.contract_rate)}/contract"
        if self.bonus:
            string += f" and receives a bonus commission of {str(self.bonus)}"

        string += f". Their total pay is {str(self.get_pay())}."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, contract=4, contract_rate=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, rate=25, contract=3, contract_rate=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, rate=30, bonus=600)
