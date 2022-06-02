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
        df['telephone'] = df['telephone'].replace(['A191', 'A192'], [0, 1])
        df['foreign-worker'] = df['foreign-worker'].replace(['A201', 'A202'], [1, 0])

        cat_features_list = ['checking', 'credit-hist', 'purpose', 'savings-account', 'employment-duration',
                            'marital-gender-status', 'debtors-guarantors', 'property', 'installment-plans', 'housing',
                            'num-existing-credits','job' ]

        for f in cat_features_list:
            dummy = pd.get_dummies(df[f], prefix=f.strip())
            df = pd.concat([df, dummy], axis='columns')

        final = df.drop(cat_features_list,axis=1)
        # print(f'data shape: {final.shape}')

        if is_train:
            self.columns = final.columns
            final = self.feature_scaler.fit_transform(final)
        else:
            final = final.reindex(columns= self.columns, fill_value=0)
            final = self.feature_scaler.transform(final)
        return final