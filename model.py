import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

#import data and get first 5 entries
train = pd.read_csv("trainData.csv")
train.head(5)
print(train.head())

#image = plt.imread("data/foto00088.png")
#plt.imshow(image)
#plt.show()

train['filename'].nunique()
