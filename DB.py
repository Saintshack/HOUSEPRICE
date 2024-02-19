import pandas as pd


data = {'SQFT': [1200, 3384, 1515, 1159, 2350], 'Bedrooms': [4, 4, 3, 2, 2], 'Bathrooms': [5, 3, 2, 1, 2], 'Location Rating': [5, 3, 5, 4, 5], 'Price': [4300000, 495000, 1495000, 325000, 4650000]}

df = pd.DataFrame(data)

#Converts the dataframe to a csv file
df.to_csv('House.csv', sep=',', index=False, encoding='utf-8')
