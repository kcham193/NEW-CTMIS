
# Import the libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv('Salary_Data.csv')

# Dependent and independent data
A = data.iloc[:, 0].values
B = data.iloc[:, 1].values

# Split the data into training and test sets
A_train, A_test, B_train, B_test = train_test_split(A, B, test_size=0.2, random_state=0)

# Random state = 0 means we want to obtain consistent results across multiple runs.

# Scaling
sc_A = StandardScaler()
A_train = sc_A.fit_transform(A_train.reshape(-1, 1))
A_test = sc_A.transform(A_test.reshape(-1, 1))
# Reshape transforms single feature or a 1D array to 2D array of shape required during fitting

# Fitting the Random Forest model to the training set
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(A_train, B_train.reshape(-1, 1))

# Predicting the test set results
B_pred = regressor.predict(A_test)  # Random Forest model

# Fitting the linear regression model to the training set
# Train the model on A_train and B_train
from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(A_train, B_train.reshape(-1, 1))

# Predicting the test set results
B_pred1 = regressor1.predict(A_test)  # Regression model

# Evaluating the Random Forest model using mean squared error
mse = mean_squared_error(B_test, B_pred)
print("Random Forest Mean Squared Error:", mse)

# Evaluating the Linear Regression model using mean squared error
mse1 = mean_squared_error(B_test, B_pred1)
print("Linear Regression Mean Squared Error:", mse1)

# Visualizing the test set results for Linear Regression
plt.scatter(A_test, B_test, color='red')
plt.plot(A_train, regressor1.predict(A_train), color='blue')
plt.title('Linear Regression')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the test set results for Random Forest
plt.scatter(A_test, B_test, color='red')
plt.plot(A_test, B_pred, color='blue')
plt.title('Random Forest Regression')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# fitting the SVM model to the training set
regressor_svm = SVR(kernel='linear')
regressor_svm.fit(A_train, B_train.ravel())  # use ravel to flatten to 1D array

# predicting the test set results
B_pred_svm = regressor_svm.predict(A_test)

# Evaluating the SVM model using mean squared error
mse = mean_squared_error(B_test, B_pred_svm)
print("SVM Mean Squared Error:", mse)


# Visualizing the test set results for SVM
plt.scatter(A_test, B_test, color='red')
plt.plot(A_test, B_test, color='blue')
plt.title('Support Vector Machine (SVM)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


#fitting the Neural Network Model
from sklearn.neural_network import MLPRegressor
clf2 = MLPRegressor(solver= "adam" , alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1, max_iter=10000)
clf2.fit(A_train,B_train.reshape(-1,1).ravel())

#making predictions from our fitted model neural networks
B_pred==clf2.predict(A_test)
print(B_pred)
print(B_test)

#evaluating the modelusing mean squared error
from sklearn.metrics import mean_squared_error
mse2 = mean_squared_error(B_test, B_pred)
print(mse2)

# Visualizing the test set results for neural network.
plt.scatter(A_test, B_test, color='green')
plt.scatter(A_test, B_pred, color='blue')
plt.title('Neural Network Regression')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#checking for the best model
#make a list for the MSE data(values)

MSE_values = [('Linear Regression',25498988.42),('Random Forest',12823412.3),('Support vector machine',8218983694),('Neural network',25498988.42)]

# make the dataframe for the mean squared errors
df = pd.DataFrame(MSE_values, columns=[('model'),('mean_squared_error')])
print(df)



descriptive_analysis = df.describe()


Best_model = df.min()['mean_squared_error']
print(Best_model)

index_ = df.index.get_loc(df[df['mean_squared_error']==Best_model].index[0])
print(index_)

print("The best model is",df['model'][index_])

best_model = min([(mse2, 'Neural Network'),(mse, 'Random Forest')])
print(best_model)
