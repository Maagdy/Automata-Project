import pandas as pd
import numpy as np
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

def load_employee_data(filepath='data/employees.csv'):
    df = pd.read_csv(filepath)
    print(f"✅ Data loaded: {len(df)} employees")
    return df


def preprocess_data(df):
    df = df.copy()
    df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'], format='%d-%b-%y')

    current_date = datetime.now()
    df['TENURE_YEARS'] = (current_date - df['HIRE_DATE']).dt.days / 365.25

    df['COMMISSION_PCT'] = pd.to_numeric(df['COMMISSION_PCT'].replace('-', np.nan), errors='coerce')
    df['MANAGER_ID'] = pd.to_numeric(df['MANAGER_ID'].replace('-', np.nan), errors='coerce')
    df['FULL_NAME'] = df['FIRST_NAME'] + ' ' + df['LAST_NAME']
    print("✅ Data preprocessing completed!")
    return df
