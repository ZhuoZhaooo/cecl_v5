#%%
import pandas as pd

# Load the data
datapath = "~/cecl_dnn/data/LoansSample01.csv"

df = pd.read_csv(datapath, low_memory=False)

# Drop harp loans
df = df[df.harp_flag  == 0]

# drop all extra cols
df = df.drop(["preharp_id_loan","dt_matr","prod_type",
              "repch_flag", "mths_remng","dt_zero_bal",
              "actual_loss", "harp_flag", "cd_zero_bal"], axis=1)

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

df.to_csv("test.csv")

