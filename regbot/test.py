import numpy as np
import json
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.pipeline import make_pipeline


# Define a more complex non-linear function F(x)
def F(x):
    return (x + x**3)/(x**2 + 1)

def linear_regression(x_train, y_train, x_test, y_test):
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Linear Regression MSE:", mse)
    print("Linear Regression R^2 score:", r2)
    plt.plot(x_test,y_pred)
    return model,r2

def polynomial_regression(x_train, y_train, x_test, y_test, degree=2):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Polynomial Regression MSE for degree", degree, ":", mse)
    print("Polynomial Regression R^2 score for degree", degree, ":", r2)
    plt.plot(x_test,y_pred)
    return model

def nonlinear_regression(x_train, y_train, x_test, y_test, kernel='rbf'):
    model = KernelRidge(kernel=kernel)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Non-linear Regression MSE with", kernel, "kernel:", mse)
    print("Non-linear Regression R^2 score with", kernel, "kernel:", r2)
    plt.plot(x_test,y_pred)
    return model

# Generate a larger sample data set
np.random.seed(42)  # For reproducibility
x = np.linspace(0, 1000, 1000).reshape(-1, 1)
y = F(x).flatten()

data = json.load(open("../src/output/parcour.json"))

x = np.array([alt["x"] for alt in data[0]["parcour"]]).reshape(-1, 1)
y = np.array([alt["y"] for alt in data[0]["parcour"]]).flatten()
# Determine the split index
split_index = int(0.8 * len(x))

# Split the data into training (80%) and testing (20%) sets without shuffling
x_train, x_test = x[:split_index], x[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

linear_model = linear_regression(x_train, y_train, x_test, y_test)
poly_model = polynomial_regression(x_train, y_train, x_test, y_test, degree=3)
nonlinear_model = nonlinear_regression(x_train, y_train, x_test, y_test, kernel='rbf')

plt.scatter(x_test, y_test, color='black', label='Actual data')
plt.show()