#%%
import pandas as pd 
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("./withlabel.csv")
timetod = df["time_to_d"]
timetod = timetod[timetod>0]

sns.distplot(timetod, kde = False, rug = True)
# %%
