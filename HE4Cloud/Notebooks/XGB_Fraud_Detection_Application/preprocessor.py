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
        df['NAME_CONTRACT_TYPE'] = (df['NAME_CONTRACT_TYPE'] == 'Cash loans').astype('int')
        df['CODE_GENDER'] = (df['CODE_GENDER'] == 'F').astype('int')
        df['FLAG_OWN_CAR'] = (df['FLAG_OWN_CAR'] == 'Y').astype('int')
        df['FLAG_OWN_REALTY'] = (df['FLAG_OWN_REALTY'] == 'Y').astype('int')

        if is_train:
            final = self.feature_scaler.fit_transform(df)
        else:
            final = self.feature_scaler.transform(df)
        return final