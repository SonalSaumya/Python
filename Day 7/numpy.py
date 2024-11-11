import math
import sklearn.metrics
actual = [0,1,2,0,3]
predicted = [0.2, 2.3, 4.5, 0.5,1.1]
mse = sklearn.metrices.mean_squared_error(actual, predicted)

rmse = math.sqrt(mse)

print("The difference between actual and predicted values", rmse)