from typing import Any, Dict, List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
import mlflow
from prefect import task, flow
import warnings 
warnings.simplefilter('ignore')


@task
def load_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data

@task
#separating numerical columns
def separating_numerical(data:pd.DataFrame) -> pd.DataFrame:
    sep_numerical = data.select_dtypes(include=['int64', 'float64'])
    return sep_numerical

@task
def get_scaler(data: pd.DataFrame) -> Any:
    # scaling the numerical features
    scaler = StandardScaler()
    scaler.fit(data)
    
    return scaler

@task
def rescale_data(data: pd.DataFrame, scaler: Any) -> pd.DataFrame:    
    # scaling the numerical features
    # column names are (annoyingly) lost after Scaling
    # (i.e. the dataframe is converted to a numpy ndarray)
    data_rescaled = pd.DataFrame(scaler.transform(data),  columns = data.columns, index = data.index)
    return data_rescaled

@task
#seperating categorical data
def seperating_categorical(data:pd.DataFrame) -> pd.DataFrame:
    sep_categorical = data.select_dtypes(include=['object'])
    return sep_categorical

@task
def encoding(data:pd.DataFrame) -> pd.DataFrame:
    cut_encoder = {'Fair' : 1, 'Good' : 2, 'Very Good' : 3, 'Ideal' : 4, 'Premium' : 5}
    data['cut'] = data['cut'].apply(lambda x : cut_encoder[x])
    
    color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}
    data['color'] = data['color'].apply(lambda x : color_encoder[x])
    
    clarity_encoder = {'I1':1, 'SI2':2, 'SI1':3, 'VS2':4, 'VS1':5, 'VVS2':6, 'VVS1':7, 'IF':8}
    data['clarity'] = data['clarity'].apply(lambda x : clarity_encoder[x])

    return data

@task    
def concat_df(data:pd.DataFrame,data1:pd.DataFrame) -> pd.DataFrame:
    concated_df= pd.concat([data,data1], axis=1)
    return  concated_df

@task
def split_data(input_: pd.DataFrame, output_: pd.Series, test_data_ratio: float) -> Dict[str, Any]:
    X_tr, X_te, y_tr, y_te = train_test_split(input_, output_, test_size=test_data_ratio, random_state=0)
    return {'X_TRAIN': X_tr, 'Y_TRAIN': y_tr, 'X_TEST': X_te, 'Y_TEST': y_te}

@task
def find_best_model(X_train:pd.DataFrame,y_train:pd.Series,estimator:Any,parameters:List)->Any:
    #Enabling automatic MLFLOW logging for Scikit-learn runs
    mlflow.sklearn.autolog(max_tuning_runs=None)
    
    with mlflow.start_run():
        reg=GridSearchCV(
            estimator=estimator,
            param_grid=parameters,
            scoring='neg_mean_absolute_error',
            cv=5,
            return_train_score=True,
            verbose=1
        )
        reg.fit(X_train,y_train)
        
        #Disabling autologging
        mlflow.sklearn.autolog(disable=True)
        
        return reg


# Workflow
@flow
def main(path: str=r'C:\Users\hp\Desktop\internship_data_science_2022\Machine_Learning\Orchestrate_ML_Pipeline\version1\data\diamonds.csv',target:str='price',test_size:float=0.2):
    
    # Define Parameters
    TARGET_COL = target
    TEST_DATA_RATIO = test_size
    DATA_PATH = path

# def main(path: str):
#     # Define Parameters
#     TARGET_COL = 'price'
#     TEST_DATA_RATIO = 0.2
#     DATA_PATH = path
#     mlflow.set_tracking_uri("sqlite:///mlflow.db")
#     mlflow.set_experiment("diamond price tracker ")
    # Load the Data
    dataframe = load_data(path=DATA_PATH)

    # Identify Target Variable
    target_data = dataframe[TARGET_COL]
    input_data = dataframe.drop([TARGET_COL], axis=1)

    
    # Split the Data into Train and Test
    train_test_dict = split_data(input_=input_data, output_=target_data, test_data_ratio=TEST_DATA_RATIO)
    
    #Preprocessing X_train
    Numerical_train_df= separating_numerical(train_test_dict['X_TRAIN'])
    Categorical_train_df=seperating_categorical(train_test_dict['X_TRAIN'])
    X_train_cat_le=encoding(Categorical_train_df)
    concated_df1=concat_df(Numerical_train_df,X_train_cat_le)
    scaler = get_scaler(concated_df1)
    X_train_transformed = rescale_data(data=concated_df1, scaler=scaler)


    #Preprocessing X_test
    Numerical_test_df=separating_numerical(train_test_dict['X_TEST'])
    Categorical_test_df=seperating_categorical(train_test_dict['X_TEST'])
    X_test_cat_le=encoding(Categorical_test_df)
    concated_df2=concat_df(Numerical_test_df,X_test_cat_le)
    scaler = get_scaler(concated_df2)
    X_test_transformed = rescale_data(data=concated_df2, scaler=scaler)

    
     # Model Training
    ESTIMATOR=KNeighborsRegressor()
    HYPERPARAMETERS = [{'n_neighbors':[i for i in range(1, 31)], 'p':[1, 2]}]
    
    regressor=find_best_model(X_train_transformed,train_test_dict['Y_TRAIN'],ESTIMATOR,HYPERPARAMETERS)
    print(regressor.best_params_)
    print(regressor.score(X_test_transformed,train_test_dict['Y_TEST']))
    
# main(path=r'C:\Users\hp\Desktop\internship_data_science_2022\Machine_Learning\Orchestrate_ML_Pipeline\version1\data\diamonds.csv')    

# Deploy the main function
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta
deployment = Deployment.build_from_flow(
    flow=main,
    name="model_training",
    schedule=IntervalSchedule(interval=timedelta(days=7)),
    work_queue_name="ml"
)

deployment.apply()