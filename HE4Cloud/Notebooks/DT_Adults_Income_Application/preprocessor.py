import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle

class Preprocessor():

    @staticmethod
    def load(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def __init__(self, feature_scaler=None, columns=None) -> None:
        if feature_scaler is None:
            self.feature_scaler = MinMaxScaler()
        else:
            self.feature_scaler = feature_scaler
        if columns is None:        
            self.columns = []
        else:
            self.columns = columns    
    
    def fit_transform(self, df):
        return self._prep(df,is_train=True)
    
    def transform(self, df):
        return self._prep(df,is_train=False)

    def encode(self, dict):
        return self.transform(pd.DataFrame([dict]))

    def save(self, path):
        with open(os.path.join(path), "wb") as f:
            pickle.dump(self, f)

    def _prep(self, df, is_train):
        df = df.copy()
        
        df['marital-status'] = df['marital-status'].str.strip()
        df['marital-status'] = df['marital-status'].replace(['Married-civ-spouse','Married-spouse-absent','Married-AF-spouse'], 'Married')
        df['marital-status'] = df['marital-status'].replace(['Never-married','Divorced','Separated','Widowed'], 'Single')
        df['marital-status'] = df['marital-status'].map({'Married':0, 'Single':1})
        df['marital-status'] = df['marital-status'].astype('int')
        df = df[['age', 'education-num', 'marital-status', 'hours-per-week', 'capital-loss', 'capital-gain']]
       
        if is_train:
            self.columns = df.columns
            final = self.feature_scaler.fit_transform(df)
        else:
            final = df.reindex(columns= self.columns, fill_value=0)
            final = self.feature_scaler.transform(final)
        return final