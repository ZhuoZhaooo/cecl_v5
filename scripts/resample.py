import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE


datapath = "~/cecl_dnn/data/LoanCleaned.csv"
df = pd.read_csv(datapath)

# Delete loans that are default and exceeds time_to_d
df = df[~((df["time_to_d"]<0) & (df["d_flag"]==1))]

# Set all good loans time_to_d as 99
def set_g(row):
    if row["d_flag"] == 0:
        return 99
    else:
        return row["time_to_d"]
    
df["time_to_d"] = df.apply(set_g, axis=1)

train_set, test_set = train_test_split(df, test_size = 0.2)
test_set.to_csv("test_set.csv")
#%%
# Vectorization for Categorical data
# Categorial Fields to be encoded using onehot method
loans_cat_1hot = ["flag_fthb", "ppmt_pnlty", "st"]

# Normalization for numerical data
loans_num_norm = ["orig_loan_term","loan_age","fico","mi_pct",
                  "cltv","dti","ltv","int_rt","current_int_rt",
                 "median_income","unemployment_rate","house_index"]

# Resample the data
pipeline = ColumnTransformer([
    ("num",Normalizer(),loans_num_norm),
    ("cat",OneHotEncoder(), loans_cat_1hot)
])

X_train = pipeline.fit_transform(train_set)

smte = SMOTE(random_state=42, k_neighbors=3)
res_train, res_target = smte.fit_sample(X_train, train_set["time_to_d"])

res_target = res_target.reshape(-1,1)
res_target = OneHotEncoder(categories="auto").fit_transform(res_target).toarray()

# %%
# save resampled data
np.save("res_train.npy", res_train.toarray())
np.save("res_target.npy", res_target)
