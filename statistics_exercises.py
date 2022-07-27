import pandas as pd
import numpy as np

    # How likely is it that you roll doubles when rolling two dice?

# poss = [1, 2, 3, 4, 5, 6]
# dice = 2
# n_sims = 100_000
# rolls = np.random.choice(poss, (n_sims, dice))
# rolls = pd.DataFrame(rolls)
# doubles = rolls.nunique(axis = 1)
# doubles = doubles == 1
# prob = doubles.mean()
#print(prob)

    # If you flip 8 coins, what is the probability of getting exactly 3 heads? 
 

# poss = ["heads", "tails"]
# coins = 8
# n_sims = 100_000
# flips = np.random.choice(poss, (n_sims, coins))
# flips = pd.DataFrame(flips)
# n_heads = (flips == "heads").sum(axis = 1)
# prob = (n_heads == 3).mean()
#print(prob)

   # What is the probability of getting more than 3 heads?

#prob = (n_heads > 3).mean()
#print(prob)

    # There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
    # Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards 
    # I drive past both have data science students on them?


# poss = ["web1", "web2", "web3", "data"]
# billbs = 2
# n_sims = 100_000
# picks = np.random.choice(poss, (n_sims, billbs))
# picks = pd.DataFrame(picks)
# n_data_alum = (picks == "data").sum(axis = 1)
# prob = (n_data_alum == 2).mean()
#print(prob)

    # Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from the snack vending machine. 
    # If on Monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some 
    # poptarts on Friday afternoon? (Remember, if you have mean and standard deviation, use the np.random.normal) 
    # You'll need to make a judgement call on how to handle some of your values

# ptarts = 3
# days = 5
# n_sims = 100_000
# vend = np.random.normal(ptarts, 1.5, (n_sims, days))
# vend = pd.DataFrame(vend)
# buy = vend.sum(axis = 1)
# stock = (buy <= 16)
# prob = stock.mean()
# print(prob)


    # Compare Heights
    #     Men have an average height of 178 cm and standard deviation of 8cm.
    #     Women have a mean of 170, sd = 6cm.
    #     Since you have means and standard deviations, you can use np.random.normal to generate observations.
    #     If a man and woman are chosen at random, what is the likelihood the woman is taller than the man?

# hm = 178
# hw = 170
# n_sims = 100_000
# men = np.random.normal(hm, 8, (n_sims, 1))
# wmen = np.random.normal(hw, 6, (n_sims, 1))
# h_men = pd.DataFrame(men) 
# h_wmen = pd.DataFrame(wmen)
# comp = (h_wmen > h_men)
# prob = comp.mean()
# print(prob)

    # When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted 
    # and the installation fails. What are the odds that after having 50 students download anaconda, 
    # no one has an installation issue? 

# poss = (249 * ["pass"]) + ["fail"]
# students = 50
# n_sims = 100_000
# installs = np.random.choice(poss, (n_sims, students))
# installs = pd.DataFrame(installs)
# p_f = (installs == "fail").sum(axis = 1)
# prob = 1 - p_f.mean()
# print(prob)

    # 100 students?

fail_poss = (1/250)
poss = ["pass","fail"]
students = 100
n_sims = 100_000
installs = np.random.choice(poss, (n_sims, students))
installs = pd.DataFrame(installs)


    # What is the probability that we observe an installation issue within the first 150 students that download anaconda?

    # How likely is it that 450 students all download anaconda without an issue?

    # There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
    # However, you haven't seen a food truck there in 3 days. How unlikely is this?

    # How likely is it that a food truck will show up sometime this week?

    # If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?
