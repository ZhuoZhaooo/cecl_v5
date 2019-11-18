#%%
import pandas as pd
import numpy as np

datapath = "./test.csv"
df = pd.read_csv(datapath, low_memory=False, index_col="id_loan")

# label the data

# extract character columns
char_cols = ["flag_fthb","ppmt_pnlty","st","d_flag"]
df_char = df[char_cols].copy()
df_char = df_char.groupby(df_char.index).first()

# extract date and numeric columns 
num_cols = ["fico", "mi_pct", "cltv", "dti",
            "ltv","int_rt","orig_loan_term",
            "current_upb","loan_age","current_int_rt","default_age"]

df_num = df[num_cols].reset_index().copy()

toyear = df_num[["orig_loan_term","loan_age","default_age"]] / 12
toyear = toyear.apply(np.floor)

df_num[["orig_loan_term","loan_age","default_age"]] = toyear
df_num["time_to_d"] = df_num["default_age"] - df_num["loan_age"]



df_num = df_num.groupby(["orig_loan_term","loan_age",
                         "id_loan","time_to_d"], as_index = False).mean()

df_num.set_index(["id_loan"],inplace = True)
                        
df_year = df_num.join(df_char, how = "left")

df_year.to_csv("withlabel.csv")



# %%
