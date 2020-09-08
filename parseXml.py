#Takes in the data set loads into pandas then saves off as a csv
import os
import pandas as pd
import xml.etree.ElementTree as et 

os.chdir('data')

headers = ['filename', 'width', 'height', 'xmin', 'ymin', 'xmax', 'ymax']
df = pd.DataFrame(columns = headers)

for file in os.listdir():
        if ".xml" not in file:
                continue
        xml = et.parse(file)
        r = xml.getroot()
        filename = r[1].text
        width = r[4][0].text
        height = r[4][1].text
        xmin = r[6][4][0].text
        ymin = r[6][4][1].text
        xmax = r[6][4][2].text
        ymax = r[6][4][3].text
        df = df.append(pd.Series([filename, width, height, xmin, ymin, xmax, ymax], index = df.columns), ignore_index = True)

print(df)

percent = 80
train = df.head(int(len(df)*(percent/100)))
test = df.iloc[max(train.index):]


train.to_csv('/Users/josephamato/Drone-Classification/trainData.csv', index=False)
test.to_csv('/Users/josephamato/Drone-Classification/testData.csv', index=False)
