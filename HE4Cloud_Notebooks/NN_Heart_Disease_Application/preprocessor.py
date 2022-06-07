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
        df.rename(columns={'age': 'Age', 'sex': 'Sex', 'cp': 'Chest_pain', 'trestbps': 'Resting_blood_pressure',
                       'chol': 'Cholesterol', 'fbs': 'Fasting_blood_sugar',
                       'restecg': 'ECG_results', 'thalach': 'Maximum_heart_rate',
                       'exang': 'Exercise_induced_angina', 'oldpeak': 'ST_depression', 'ca': 'Major_vessels',
                       'thal': 'Thalassemia_types', 'target': 'Heart_attack', 'slope': 'ST_slope'}, inplace=True)

        print(f'data shape: {df.shape}')
        print(df.dtypes)

        dummy1 = pd.get_dummies(df.Chest_pain)
        dummy2 = pd.get_dummies(df.Thalassemia_types)
        dummy3 = pd.get_dummies(df.ECG_results)
        dummy4 = pd.get_dummies(df.ST_slope)
        dummy5 = pd.get_dummies(df.Major_vessels)
        merge = pd.concat([df, dummy1, dummy2, dummy3, dummy4, dummy5], axis='columns')

        final = merge.drop(['Chest_pain', 'Thalassemia_types', 'ECG_results', 'ST_slope', 'Major_vessels'], axis=1)

        final = final.drop(['Heart_attack'], axis=1)
        # print(f'data shape: {final.shape}')

        if is_train:
            self.columns = final.columns
            final = self.feature_scaler.fit_transform(final)
        else:
            final = final.reindex(columns= self.columns, fill_value=0)
            final = self.feature_scaler.transform(final)
        return final