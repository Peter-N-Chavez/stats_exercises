import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import env

def get_db_url(hostname, username, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url

url = get_db_url(env.hostname, env.username, env.password, "employees")



# A bank found that the average number of cars waiting during the noon hour at a drive-up window 
# follows a Poisson distribution with a mean of 2 cars. 
# Make a chart of this distribution and answer these questions concerning the probability of
# cars waiting at the drive-up window.

#     What is the probability that no cars drive up in the noon hour?

λ = 2
drv_thru = stats.poisson(λ)
print(drv_thru.pmf(0))

#     What is the probability that 3 or more cars come through the drive through?

print(drv_thru.sf(2))

#     How likely is it that the drive through gets at least 1 car?

print(drv_thru.sf(0))

# Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3.
# Calculate the following:

mean = (3.0)
dev = (0.3)
grades = stats.norm(mean, dev)

#     What grade point average is required to be in the top 5% of the graduating class?

print(grades.ppf(.95))

#     What GPA constitutes the bottom 15% of the class?

print(grades.ppf(.15))

#     An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. 
#     Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

decile3 = grades.ppf(0.3)
decile2 = grades.ppf(0.2)
# or grades.ppf([0.2, 0.3])
r_dec3 = decile3 - decile2
print(decile2)
print(r_dec3)
# Yes, a student with a 2.8 GPA would qualify.

#     If I have a GPA of 3.5, what percentile am I in?

print(grades.cdf(3.5))

# A marketing website has an average click-through rate of 2%. 
# One day they observe 4326 visitors and 97 click-throughs. 
# How likely is it that this many people or more click through?

clicks = stats.binom(4326, .02)
print(clicks.sf(96))

# You are working on some statistics homework consisting of 100 questions where all of the answers 
# are a probability rounded to the hundreths place. 
# Looking to save time, you put down random probabilities as the answer to each question.

#     What is the probability that at least one of your first 60 answers is correct?

ans = stats.binom(60, .01)
print(ans.sf(0))

# The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when they visit it, 
# and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. 
# How likely is it that the break area gets cleaned up each day? 

# n_stud_on_break = 90% x 3 classes x 22 students per class = about 59 students 
clean = stats.binom(59, .03)
print(clean.pmf(0))

# How likely is it that it goes two days without getting cleaned up? 

# n_stud_on_break = 90% x 3 classes x 22 students per class x 2 days = about 118 trials

clean = stats.binom(118, .03)
print(clean.pmf(0))

# All week?

# n_stud_on_break = 90% x 3 classes x 22 students per class x 5 days = about 295 trials

clean = stats.binom(295, .03)
print(clean.pmf(0))

# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. 
# After several weeks of careful observation, you notice that the average number of people in line when
# your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. 
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, 
# what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? 
# Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

# 15 people x 2 minutes = mean of 30 minutes, 3 people x 2 minutes = std dev of 6 minutes
# time left for lunch = 60 minutes for lunch - 10 minutes to receive order - 15 minutes to eat - 2 minutes to order = 
# 33 minutes
 
line = stats.norm(30, 6)
lunch = line.cdf(33)
print(lunch)

# Connect to the employees database and find the average salary of current employees, along with the standard deviation. 
# For the following questions, calculate the answer based on modeling the employees salaries with a normal distribution 
# defined by the calculated mean and standard deviation then compare this answer to the actual values present in 
# the salaries dataset.

salaries = pd.read_sql('SELECT salary FROM employees \
                            JOIN salaries \
                            USING(emp_no) \
                            WHERE to_date > CURDATE()', url)

#     What percent of employees earn less than 60,000?

num_salaries_LT60K = len(salaries[salaries.salary < 60_000])
perc_LT60K = (num_salaries_LT60K / (len(salaries))) * 100
print(perc_LT60K)
emp_salaries = stats.norm(salaries.mean(), salaries.std())
print(salaries.mean(), salaries.std())
print(emp_salaries.cdf(60_000))

#     What percent of employees earn more than 95,000?

num_salaries_MT95K = len(salaries[salaries.salary > 95_000])
perc_MT95K = (num_salaries_MT95K / (len(salaries))) * 100
print(perc_MT95K)
emp_salaries = stats.norm(salaries.mean(), salaries.std())
print(emp_salaries.sf(95_000))

#     What percent of employees earn between 65,000 and 80,000?

num_salaries_65T80K = len(salaries[(salaries.salary > 65_000) & (salaries.salary < 80_000)])
perc_65T80K = (num_salaries_65T80K / (len(salaries))) * 100
print(perc_65T80K)
emp_salaries = stats.norm(salaries.mean(), salaries.std())
print(emp_salaries.cdf([65_000, 80_000]))

#     What do the top 5% of employees make?

emp_salaries = stats.norm(salaries.mean(), salaries.std())
print(emp_salaries.isf(.05))

# The top 5% make at least $100,484.64 salary.