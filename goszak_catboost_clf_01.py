# -*- coding: utf-8 -*-
"""Goszak_catboost_clf_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UE3KV8YIcBopQIiF5YStjeabBt8MS3bj
"""

!pip install catboost

"""Baseline for detecting if firm will winn tender.

CatBoost version catboost-0.24.1
"""

#baseline 
import numpy as np
import pandas as pd
from catboost import Pool, CatBoostClassifier
from sklearn.model_selection import train_test_split  #to divide dataset into train and validation
from sklearn.metrics import accuracy_score  #metric to eval classification
RS=42  #we will state random state

# подключаем гугл диск на котором данные
from google.colab import drive
drive.mount ('/content/gdrive', force_remount = True)

!ls /content/gdrive/'My Drive'/dataset_goszak

#let s load data
PATH_TO_DATA='../content/gdrive/My Drive/dataset_goszak/'
df_train1=pd.read_csv(PATH_TO_DATA+'train01.csv',sep=';',encoding='windows-1251')
df_train1.head(2)

df_train1.columns

df_train1['Заказчик: ИНН'].value_counts()

df_train1['Target']=1

df_train2=pd.read_csv(PATH_TO_DATA+'train02.csv',sep=';',encoding='windows-1251')
df_train2.head(2)

df_train2['Target']=0

df_train=df_train1.append(df_train2)

#let s see how many NaNs
df_train.isnull().sum()

df_train.shape

df_train.fillna(value='',inplace=True)

X_features=['Заказчик: ИНН','Цена контракта','Объект закупки: наименование товаров, работ, услуг',
            'Информация о поставщиках (исполнителях, подрядчиках) по контракту: ИНН']

#divide dataset to train and test

X_train, X_test, y_train, y_test=train_test_split(df_train[X_features],
                                                  df_train[['Target']], shuffle = True,
                                                test_size=0.2,random_state=RS)

target_col = 'Target'
text_cols = ['Объект закупки: наименование товаров, работ, услуг']
categorical_cols = ['Заказчик: ИНН','Цена контракта',
                    'Информация о поставщиках (исполнителях, подрядчиках) по контракту: ИНН']

train_pool = Pool(
        X_train, 
        y_train, 
        cat_features=categorical_cols,
        text_features=text_cols,
        feature_names=X_features,
    )
    valid_pool = Pool(
        X_test, 
        y_test, 
        cat_features=categorical_cols,
        text_features=text_cols,
        feature_names=X_features,
    )

clf=CatBoostClassifier(iterations= 500,
    learning_rate= 0.2,
    depth=12,
    eval_metric= 'Logloss',  # logLoss
    task_type= 'CPU',
    early_stopping_rounds= 100,
    #class_weights=[0.95,0.05],
    use_best_model= True,
    random_seed=RS,
    verbose= 10
)

clf.fit(train_pool, eval_set=valid_pool,plot=True)

clf.save_model('cb_clf01.cbm',format='cbm',pool=train_pool)

clf.score(valid_pool)

X_test[1:2]

clf.predict(X_test[2:3])

!ls

from google.colab import files

files.download('cb_clf01.cbm')





