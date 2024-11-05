from sklearn.linear_model import LinearRegression
import numpy as np 

X= np.array([[1,2],[1,3],[2,2],[2,3]])
y = np.dot(X,np.array([1,3])) + 3

reg = LinearRegression().fit(X,y)
print("Coefficient",reg.coef_)
print("Intercept: ",reg.intercept_)