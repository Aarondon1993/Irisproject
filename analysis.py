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



a= df.loc[df.species=="setosa", "sepal_width"]
b= df.loc[df.species=="versicolor", "sepal_width"]
c= df.loc[df.species=="virginica", "sepal_width"]

plt.hist(a, color= "g", label= "setosa", alpha= 0.5, bins=60)
plt.hist(b, color= "r", label= "versicolor", alpha= 0.5, bins=60)
plt.hist(c, color= "b", label= "virginica", alpha= 0.5, bins=60)
plt.title("Measurement of sepal width among species")
plt.ylabel("Frequency of Occurence")
plt.xlabel("Width in Centimeters")
plt.xticks(np.arange(1.5,5, step= 0.2))
plt.legend()
plt.savefig('Measurement of sepal width among species.png')
plt.show()

a= df.loc[df.species=="setosa", "sepal_length"]
b= df.loc[df.species=="versicolor", "sepal_length"]
c= df.loc[df.species=="virginica", "sepal_length"]

plt.hist(a, color= "g", label= "setosa", alpha= 0.5, bins=60)
plt.hist(b, color= "r", label= "versicolor", alpha= 0.5, bins=60)
plt.hist(c, color= "b", label= "virginica", alpha= 0.5, bins=60)
plt.title("Measurement of sepal length among species")
plt.ylabel("Frequency of Occurence")
plt.xlabel("Length in Centimeters")
plt.xticks(np.arange(4,8, step= 0.5))
plt.legend()
plt.savefig('Measurement of sepal length among species.png')
plt.show()

a= df.loc[df.species=="setosa", "petal_length"]
b= df.loc[df.species=="versicolor", "petal_length"]
c= df.loc[df.species=="virginica", "petal_length"]

plt.hist(a, color= "g", label= "setosa", alpha= 0.5, bins=60)
plt.hist(b, color= "r", label= "versicolor", alpha= 0.5, bins=60)
plt.hist(c, color= "b", label= "virginica", alpha= 0.5, bins=60)
plt.title("Measurement of petal length among species")
plt.ylabel("Frequency of Occurence")
plt.xlabel("Length in Centimeters")
plt.xticks(np.arange(1,8, step= 0.5))
plt.legend()
plt.savefig('Measurement of petal length among species.png')
plt.show()

a= df.loc[df.species=="setosa", "petal_width"]
b= df.loc[df.species=="versicolor", "petal_width"]
c= df.loc[df.species=="virginica", "petal_width"]

plt.hist(a, color= "g", label= "setosa", alpha= 0.5, bins=60)
plt.hist(b, color= "r", label= "versicolor", alpha= 0.5, bins=60)
plt.hist(c, color= "b", label= "virginica", alpha= 0.5, bins=60)
plt.title("Measurement of petal width among species")
plt.ylabel("Frequency Of Occurence")
plt.xlabel("Width in Centimeters")
plt.xticks(np.arange(0,3, step= 0.5))
plt.legend()
plt.savefig('Measurement of petal width among species.png')
plt.show()


import seaborn as sns




sns.pairplot(df, hue="species")
plt.show()










