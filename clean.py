'''
Project Name: cecl_dnn
Date: 11/1/2019
Author: Zhuo Zhao
Libraries Used: Pandas

'''
#%%
import pandas as pd

# Load the data
datapath = "~/cecl_dnn/data/LoansSample01.csv"

df = pd.read_csv(datapath, low_memory=False)


def clean_fico(df):
    df = df[df["fico"] != 9999]
    df = df[(df["fico"] <= 850) | (df["fico"] >= 301)]
        
    return df

def clean_fthb(df):
    df = df[df["flag_fthb"] != 9]

#%%

df[df["fico"].isna()]

# %%
