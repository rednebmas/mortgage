from mortgage import Mortgage
import numpy as np
import pandas as pd
import math
import locale
locale.setlocale(locale.LC_ALL, '')
import matplotlib.pyplot as plt

def money_fmt(num):
    return locale.currency(num, grouping = True)

m = Mortgage(
    apr = .04,
    loan_total = 500_000,
    loan_duration = 30
)

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(6, 6)
ax = fig.gca()

ax.text(0, 0, 
        'Principal: {}\nAPR: {}%\nMontly payment: {}\nCost in interest: {}\nTotal cost: {}'.format(
        	money_fmt(m.principal),
        	m.apr * 100, 
        	money_fmt(m.monthly_payment),
        	money_fmt(m.cost_interest),
        	money_fmt(m.cost_total)
        ), 
        bbox = {
                'facecolor':'white', 
                'alpha': 0.5, 
                'pad': 5 
            }
       )

ax.set_xticks(np.arange(0, len(m.months), 24*2))
ax.set_yticks(np.arange(0, max(m.principals), 500))
plt.grid(alpha=.25)

plt.plot(m.months, m.interests, label = 'interest')
plt.plot(m.months, m.principals, label = 'principal')
plt.xlabel('Month')
plt.ylabel('Money ($)')
plt.legend()

plt.show()