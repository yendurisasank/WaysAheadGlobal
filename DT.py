import pandas as pd
import warnings
warnings.filterwarnings('ignore')

dataf=pd.read_csv("Bank_Marketing Analaysis.csv")
dataf.drop(['Target Revenue'],axis=1,inplace=True)
data = dataf.copy()

from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
cate_col=['job','marital','education','marital-education','targeted','default','housing','loan','contact','month','poutcome']
for i in cate_col:
  data[i]=label_encoder.fit_transform(data[i])

from sklearn import preprocessing 
  
min_max_scaler = preprocessing.MinMaxScaler(feature_range =(0, 1)) 
data[['age', 'Age_Group','job','salary','marital','education','marital-education','targeted','default','balance','housing','contact','day','month','duration','campaign','pdays','previous','poutcome','Response']]= min_max_scaler.fit_transform(data[['age', 'Age_Group','job','salary','marital','education','marital-education','targeted','default','balance','housing','contact','day','month','duration','campaign','pdays','previous','poutcome','Response']])  

corr_mat = data.corr()
cols_to_drop = []
CORR_THRESH = 0.02
for col in data:
    corr = data[col].corr(data['loan'])
    print(corr,col)
    if (abs(corr) < CORR_THRESH):
        cols_to_drop.append(col)

df=data
for col in df:
    if col in cols_to_drop:
        df.drop(labels=[col], axis=1, inplace=True)
cf=data.drop(['loan'],axis=1)
cat_feat = ['job','marital',"education","marital-education","targeted","default","housing","month","loan"]

from sklearn.model_selection import train_test_split
dataf =dataf.loc[:, cat_feat]

dataf['loan'] = dataf['loan'].replace(['yes', 'no'], [1.0,0.0]) 
dataf = dataf.rename(columns={"marital-education": "marital_education"})       
train, test = train_test_split(dataf, test_size=0.2)
cat_feat = ['job','marital',"education","marital_education","targeted","default","housing","month","loan"]
cat_feat.pop()

import catboost as cat
model = cat.CatBoostRegressor(cat_features=cat_feat,verbose=0)
features = list(set(dataf.columns)-set(['loan']))
model.fit(train[features],train['loan'])

import pickle
import os

save_path = 'prediction/'
completeName = os.path.join(save_path, "DTmodel.pkl")         
pickle.dump(model, open(completeName, 'wb'))