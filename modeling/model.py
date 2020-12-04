import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error

def model(laptopData: DataFrame):
    ###CURRENTLY UNDER REFINEMENT
    #to do: break into construct_model and validate_model
    #to do: illustrate in jupyter notebook

    #drop irrelevant columns
    laptopData = laptopData.drop('description', axis=1)
    laptopData = laptopData.drop('title', axis=1)
    laptopData = laptopData.drop('itemId', axis=1)
    laptopData = laptopData.drop('watchCount', axis=1)
    laptopData = laptopData.drop('condition', axis=1)
    #top4 is highly collinear with top8, hence drop
    laptopData = laptopData.drop('top4', axis=1)

    #features that assess whether a spec-value (e.g., "13 inches") is mentioned in title/description depends on
    #there existing the value in the spec feature (e.g., size: 13);
    #but if the latter data are missing, then there's no way to assess the former
    #hence, dropna
    laptopData = laptopData.dropna()

    print(laptopData.head())

    #split the data
    X = data.drop("price", axis=1)
    y = data[['price']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    #subset columns for baseline model
    print("LINEAR BASELINE MODEL")
    print("-----------")
    X_train2 = X_train[["year", "size", "memory"]]
    X_test2 = X_test[["year", "size", "memory"]]

    #instantiate model
    regression_model = LinearRegression()
    regression_model.fit(X_train2, y_train)

    #print model coefficients
    for idx, col_name in enumerate(X_train2.columns):
        print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))
    intercept = regression_model.intercept_[0]
    print("The intercept for our model is {}".format(intercept))

    #print model performance
    print("R-squared: ", regression_model.score(X_test2, y_test))

    y_predict = regression_model.predict(X_test2)
    regression_model_mse = mean_squared_error(y_predict, y_test)

    print("RMSE: ", np.sqrt(regression_model_mse))
    print("-----------")

    #subset columns for baseline model
    print("LINEAR FULL MODEL")
    print("-----------")

    #instantiate model
    regression_model = LinearRegression()
    regression_model.fit(X_train, y_train)

    #print model coefficients
    for idx, col_name in enumerate(X_train.columns):
        print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))
    intercept = regression_model.intercept_[0]
    print("The intercept for our model is {}".format(intercept))

    print("R-squared: ", regression_model.score(X_test, y_test))

    y_predict = regression_model.predict(X_test)
    regression_model_mse = mean_squared_error(y_predict, y_test)

    print("RMSE: ", np.sqrt(regression_model_mse))
    print("-----------")

    #subset columns for baseline model
    print("LASSO FULL MODEL")
    print("-----------")

    #instantiate model
    model_lasso = Lasso(alpha=1)
    model_lasso.fit(X_train, y_train)

    #print model coefficients
    for idx, col_name in enumerate(X_train.columns):
        print("The coefficient for {} is {}".format(col_name, model_lasso.coef_[idx]))
    intercept = model_lasso.intercept_[0]
    print("The intercept for our model is {}".format(intercept))

    print("R-squared: ", model_lasso.score(X_test, y_test))

    y_predict = model_lasso.predict(X_test)
    model_lasso_mse = mean_squared_error(y_predict, y_test)

    print("RMSE: ", np.sqrt(model_lasso_mse))
    print("-----------")