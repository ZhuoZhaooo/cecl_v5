import pandas as pd
import numpy as np
# Load the data
datapath = "~/cecl_dnn/data/LoansSample01.csv"

df = pd.read_csv(datapath, low_memory=False)

# Drop harp loans
df = df[df.harp_flag  == 0]

# drop all extra cols
df = df.drop(["preharp_id_loan","dt_matr","prod_type",
              "repch_flag", "mths_remng","dt_zero_bal",
              "actual_loss", "harp_flag", "cd_zero_bal",
             "current_upb"], axis=1)

# change the types from objetcs to characters
to_char_list = ["flag_fthb", "ppmt_pnlty", "st"]
df[to_char_list] = df[to_char_list].fillna('U')

# clean delq_sts 
df = df[df["delq_sts"] != "XX"]
df = df[df["delq_sts"] != "R"]
df["delq_sts"] = pd.to_numeric(df["delq_sts"])

# drop rows containing NAs
df.dropna(inplace = True)

# calculate time_to_d

# Find default loans
d_loans = df[df["delq_sts"] == 6].copy()
d_loans["d_flag"] = 1
d_loans = d_loans.sort_values(by = "loan_age", ascending=True)
d_loans = d_loans.groupby("id_loan").first()
default_age = d_loans[["loan_age","d_flag"]]
default_age["default_age"] = default_age["loan_age"]
default_age.drop(["loan_age"],axis =1,inplace = True)
df.set_index("id_loan", inplace=True)
df = df.join(default_age, how = "left")
df = df.fillna({"d_flag":0,"default_age":0})
df.reset_index(inplace = True)
# Merge loan level data and economics data
median_income = pd.read_csv("/home/zhuo/cecl_dnn/data/median_income.csv", index_col=0)
unemploy_rate = pd.read_csv("/home/zhuo/cecl_dnn/data/unemployement_rate.csv", index_col=0)
house_index = pd.read_csv("/home/zhuo/cecl_dnn/data/house_index.csv", index_col=0)
df["svcg_cycle"] = np.array(df["svcg_cycle"] / 100, "int32")
df = df.rename(columns = {"svcg_cycle":"year"})
df = pd.merge(df, median_income, on = ["year","st"])
df = pd.merge(df, unemploy_rate, on = ["year", "st"])
df = pd.merge(df, house_index, on = ["year", "st"])
df.set_index("id_loan", inplace = True)


# label the data
# extract character columns
char_cols = ["flag_fthb","ppmt_pnlty","st","d_flag"]
df_char = df[char_cols].copy()
df_char = df_char.groupby(df_char.index).first()

# extract date and numeric columns 
num_cols = ["fico", "mi_pct", "cltv", "dti",
            "ltv","int_rt","orig_loan_term",
            "loan_age","current_int_rt",
            "default_age","delq_sts",
           "median_income","unemployment_rate","house_index"]

df_num = df[num_cols].copy().reset_index()

toyear = df_num[["orig_loan_term","loan_age","default_age"]] / 12
toyear = toyear.apply(np.floor)
df_num[["orig_loan_term","loan_age","default_age"]] = toyear
df_num["time_to_d"] = df_num["default_age"] - df_num["loan_age"]
df_num = df_num.groupby(["orig_loan_term","loan_age","id_loan",
                         "time_to_d"], as_index = False).mean()

df_num.set_index(["id_loan"],inplace = True)
                        
df_year = df_num.join(df_char, how = "left")
df_year.to_csv("~/cecl_dnn/data/LoanCleaned.csv")

