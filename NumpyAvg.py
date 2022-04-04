# Import packages
import numpy as np
import pandas as pd

# Read author data
greatest_books = pd.read_csv("StatisticsPython/hundredbooks.csv")
print(greatest_books)

# Set author ages to a NumPy array
author_ages = greatest_books['ages']
print(author_ages)

# # Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

print("The average age of the authors, is: " + str(average_age))