import numpy as np

class Mortgage:
    def __init__(self, 
                 apr, 
                 loan_total, 
                 loan_duration, 
                 down_payment = 0):
        # params
        self.apr = apr
        self.loan_total = loan_total
        self.loan_duration = loan_duration
        self.down_payment = down_payment

        # values based off params
        self.principal = self.loan_total - self.down_payment
        self.monthly_apr = self.apr / 12
        self.min_monthly_payment = self.calc_monthly_payment()
        self.monthly_payment = self.min_monthly_payment

        self.calculate()

    def calc_monthly_payment(self):
        months_in_a_year = 12
        return (self.monthly_apr * self.principal) / \
               (1 - (1 + self.monthly_apr)**(-(self.loan_duration * months_in_a_year)))

    def calculate(self):
        loan_remaining = self.loan_total - self.down_payment
        self.loan_remainings = [loan_remaining]
        self.interests = []
        self.principals = []
        while loan_remaining > 0.01:
            interest_paid = loan_remaining * self.monthly_apr
            self.interests.append(interest_paid)
            
            principal_paid = self.monthly_payment - interest_paid
            if principal_paid > loan_remaining: 
                principal_paid = loan_remaining
            self.principals.append(principal_paid)
            
            loan_remaining = loan_remaining - principal_paid
            self.loan_remainings.append(loan_remaining)

        self.convert_arrs_to_np()
        self.calculate_summary_stats()

    def convert_arrs_to_np(self):
        self.loan_remainings = np.array(self.loan_remainings)
        self.interests = np.array(self.interests)
        self.principals = np.array(self.principals)

    def calculate_summary_stats(self):
        self.months = np.arange(len(self.interests))
        self.cost_interest = self.interests.sum()
        self.cost_total = self.cost_interest + self.principals.sum()

        
