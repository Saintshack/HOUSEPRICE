from numpy import array
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense


# Gets Database file, reads it, creates predictors and target, and shapes the dataset to be trained
house_data = pd.read_csv('House.csv')
house_data.head()
house_data.shape
house_data.describe()
house_data.isnull().sum()
house_data_columns = house_data.columns
predictors = house_data[house_data_columns[house_data_columns != 'Price']]
target = house_data[house_data_columns[house_data_columns == 'Price']]
predictors.head()
target.head()
predictors_norm = (predictors - predictors.mean()) / predictors.std()
predictors_norm.head()
n_cols = predictors_norm.shape[1]


#Neural Network model is used to create the trained AI with 80 neurons, activation funtion of relu, input being the columns, optimizer adam, and error calculated by mean squared error
def regression_model():
    model = Sequential()
    model.add(Dense(80, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

#Creates a variable to store the model
model = regression_model()


#Inputs are asked here
model.fit(predictors_norm, target, validation_split=0.2, epochs=1100, verbose=2)
area = float(input("How big is the house"))
bed = float(input("How many bedrooms"))
bath = float(input("How many bathrooms"))
location = float(input("What is the location rating (1 = rural and 5 = downtown of a major city)"))

#Inputs are turned into an area to create the prediction
xnew = array([[area, bed, bath, location]])

#Prediction made here
ynew = model.predict(xnew)

#Prediction is adjusted to scale and printed
if ynew >= 100000000 and bed <= 8 or bath <= 8:
    ynew = ynew/100
    ynew = ynew * 1.65
elif ynew <=50000 and area >=500:
    ynew = ynew * 50
print("X=%s, Predicted=%s" % (xnew[0], ynew[0]))

#Answers are narrow as a result of the short dataset.