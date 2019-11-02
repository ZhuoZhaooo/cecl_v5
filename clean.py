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

#%%

df = df[df["delq_sts"] != "XX"]

df = df[df["delq_sts"] != "R"]

df["delq_sts"] = pd.to_numeric(df["delq_sts"])

# Group by the data to years 
df["age_year"] = (df["loan_age"] // 12) + 1
df["delq_year"] = (df["delq_sts"] // 12) + 1

# drop unuseful columns
drop_list = ['preharp_id_loan', 'dt_matr', 
            "prod_type", "mths_remng", "dt_zero_bal", 
            "current_int_rt", "actual_loss"]

    ## create a list to store the fields to needed to be determined
    drop_to_d = ["mi_pct"]


    drop_list.append(df0.columns[0])
    drop_list.append(drop_to_d[0])
    df0 = df0.drop(drop_list, axis = 1)


    ## Note that cd_zero_bal and harp_flag should be categorical data rather than float 


    # fill characters columns NaN with 'U'
    to_char_list = ["flag_fthb", "ppmt_pnlty", "st", "repch_flag", "cd_zero_bal"]
    df0[to_char_list] = df0[to_char_list].fillna('U')

    df0["cd_zero_bal"] = df0["cd_zero_bal"].astype('str')

    df0["time_to_d"] = pd.to_numeric(df0["time_to_d"])

    # drop Na
    df0.dropna(inplace = True)
print(df.info())
#%%

delq_target = 6

df = df[df["delq_sts"] <= delq_target]

df["default_age"] = 0

df_new = df.copy()

default_loans = df[df["delq_sts"] == delq_target]

for index in default_loans.index:
    df_new.loc[index]["default_age"] = default_loans.loc[index]["loan_age"]
    