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

plt.hist(a, bins=[1,2,3,4,5,6,7,8], color= "blue",)
plt.xlabel("Length in centimeters")
plt.ylabel("Number of occurences")
plt.title("Length of sepals")
plt.xticks([1,2,3,4,5,6,7,8])
plt.savefig("Sepal_Length.png")
plt.show()


b = df ["sepal_width"]
plt.hist(b, bins=[1,2,3,4,5,6,7,8], color= "#5b5682")
plt.xlabel("Width in centimeters")
plt.ylabel("Number of occurences")
plt.title("Width of sepals")
plt.xticks([1,2,3,4,5,6,7,8])
plt.savefig("Sepal_Width.png")
plt.show()


c = df ["petal_length"]
plt.hist(c, bins=[1,2,3,4,5,6,7,8], color= "#b8ba52",)
plt.xlabel("Length in centimeters")
plt.ylabel("Number of occurences")
plt.title("Length of petals")
plt.xticks([1,2,3,4,5,6,7,8])
plt.savefig("Petal_Length.png")
plt.show()


d = df ["petal_width"]
plt.hist(d, bins=[1,2,3,4,5,6,7,8], color= "#7ca15c",)
plt.xlabel("Width in centimeters")
plt.ylabel("Number of occurences")
plt.title("Width of petals")
plt.xticks([1,2,3,4,5,6,7,8])
plt.savefig("Petal_Width.png")
plt.show()












