# cecl_v5
The project is to build DNN model for credit losses estimation based on current expected credit losses methodology (CECL). The project focuses on the probability of default (PD) in future periods. 

## Data Source
Freddie Mac Single Family Loan-Level Dataset
## Procedures
### Data Preparation
#### clean.py
- Determine the delinquency threshold (Now we choose 6 periods) 
#### label.py
- Compute the “years to default” for each loan. Set “years to default” as our labels.
#### resample.py
- The dataset is highly imbalanced. Non-delinquent loans account for most of the dataset (Nearly 96%). This will exaggerate the accuracy of the model. And the prediction for the training set will not make sense (Most will be predicted to be non-delinquent). Possible Solution SMOTE + ENN
- Split the data into training set and test set (80% training, 20%testing). Remember that data should be split first before resampling 
