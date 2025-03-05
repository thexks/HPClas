#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from catboost import CatBoostClassifier
from imblearn.pipeline import make_pipeline


# In[ ]:


def catBoost_model():
    pipeline = make_pipeline( #pipeline是将多个数据处理步骤和模型训练步骤串联起来的一个流程。使用pipeline，可以将数据预处理、特征工程和模型训练等步骤整合在一起
                              #make_pipeline()`是一个方便的函数，确保每个步骤的输出正确传递到下一个步骤的输入，用于创建pipeline对象
        MinMaxScaler(),
        SelectKBest(chi2, k=310),
        CatBoostClassifier(verbose=False, task_type='CPU', thread_count=-1,                                                         iterations=3000,
                                                learning_rate=0.1,                                                                   depth=5, border_count=20, 
                                                l2_leaf_reg=5)
    )
    return pipeline


# In[ ]:


#path_data = f"features/train.csv"
# datasets = pd.read_csv(path_data, header=None, low_memory=False)
# X_train, y_train = np.array(datasets.iloc[:, 1:]), np.array(datasets.iloc[:, 0])
# catBoost_model = catBoost_model().fit(X_train, y_train)
# joblib.dump(catBoost_model, "model/catBoost_model.pkl")

