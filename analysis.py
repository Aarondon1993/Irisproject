#Aaron Donnelly
# This program is written as a requirement for the Programming and Scripting module in the Data Analytics course.
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
# The above libraries will be used to read the data in the .csv file, summarise the variables
# and then produce both the histograms and scatter plots.

df = pd.read_csv("IrisDataset.csv")
# Using the .read_csv function of pandas the dataset can be read.
desc= df.groupby('species').describe()

# in order to generate a summary of the dataset contents the df.describe function is used.
# This is used by the groupby function in order to describe the data relative to the particular species.
f = open ('datasetsummary.txt','w')
# The variable 'f' is used to open the destination txt file in write mode.
# Using write mode 'w' this will ensure that the code will overwrite the contents
# of the .txt file each time to keep it tidy. 
f.write (desc.to_string())
# The desc must be converted into a string in order for the write funtion to work.

a = df ["sepal_length"]

plt.hist(a, bins=30, color= "blue")
plt.xlabel("Size in centimeters")
plt.ylabel("Number of occurences")
plt.title("Size of Iris flowers")


b = df ["sepal_width"]
plt.hist(b, bins=30, color= "green")



c = df ["petal_length"]
plt.hist(c, bins=30, color= "red")



d = df ["petal_width"]
plt.hist(d, bins=30, color= "yellow")

plt.legend(['sepal_length','sepal_width','petal_length','petal_width'])
plt.show()







