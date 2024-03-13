##ONE WAY ANOVA

import numpy as np
from scipy.stats import f

# Define the data sets for each group
group1 = [63.87,68.89,59.02,67.03,47.96,65.36,60.61,70.93,55.60,55.60]
group2 = [56.47,51.94,54.94,50.21,46.25,61.96,49.83,54.72,43.26,49.64]
group3 = [56.19,38.34,54.19,52.20,51.15,51.69,54.31,54.18,39.65,51.16]
group4 = [55.51,38.06,57.71,52.82,49.24,51.27,54.01,52.69,39.55,48.13]

# Calculate the means and overall mean
mean1 = sum(group1) / len(group1)
mean2 = sum(group2) / len(group2)
mean3 = sum(group3) / len(group3)
mean4 = sum(group4) / len(group4)          
overall_mean = (sum(group1) + sum(group2) + sum(group3) + sum(group4)) / (len(group1) + len(group2) + len(group3) + len(group4))

# Calculate the sum of squares between groups
ss_between = len(group1) * ((mean1 - overall_mean) ** 2) + len(group2) * ((mean2 - overall_mean) ** 2) + len(group3) * ((mean3 - overall_mean) ** 2) + len(group4) * ((mean4 - overall_mean)**2)

# Calculate the sum of squares within groups
ss_within = sum([(x - mean1) ** 2 for x in group1]) + sum([(x - mean2) ** 2 for x in group2]) + sum([(x - mean3) ** 2 for x in group3]) + sum([(x - mean4) ** 2 for x in group4])

# calculate the sum of squares of total
ss_total = ss_between + ss_within

# Calculate the degrees of freedom
df_between = 4 - 1
df_within = len(group1) + len(group2) + len(group3) + len(group3) - 4
df_total = df_between + df_within

# Calculate the mean squares
ms_between = ss_between / df_between
ms_within = ss_within / df_within

# Calculate the F-statistic
f_statistic = ms_between / ms_within
p_value = 1 - f.cdf(f_statistic, df_between, df_within)


# Print the results
print("ss_between:", ss_between)
print("ss_within:", ss_within)
print("ss_total:", ss_total)
print("degree of freedom_between:",df_between)
print("degree of freedom_within:",df_within)
print("degree of freedom_total:",df_total)
print("ms_between:", ms_between)
print("ms_within:", ms_within)
print("F-statistic:", f_statistic)
print("p_value:",p_value)
