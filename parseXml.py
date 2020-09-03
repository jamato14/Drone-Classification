from lxml import objectify
import os
import pandas as pd
import xml.etree.ElementTree as et 

os.chdir('data')

headers = ['filename', 'width', 'height', 'xmin', 'ymin', 'xmax', 'ymax']
df = pd.DataFrame(columns = headers)

for file in os.listdir():
        if ".xml" not in file:
                continue
#        xml = objectify.parse(file)
#        root = xml.getroot()
#        print(root['ymin'])
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
df.to_csv('/Users/josephamato/Drone-Classification/xmlData.csv', index=False)
