# CECL_V5
The project is to build DNN model for credit losses estimation based on current expected credit losses methodology (CECL). The project focuses on the probability of default (PD) in future periods. 

## Data Source
Freddie Mac Single Family Loan-Level Dataset

## Workflow

### Data Preparation

#### clean.py
- Delete unuseful characteristics 
#### label.py
- Determine the delinquency threshold (Now we choose 6 periods)
- Compute the “years to default”. Set “years to default” as our labels. Use the information of the first loan in each year to represent the that year. 
#### resample.py
- For categorical data, use onehot encoder
- For numerical data, normalize the data
- The dataset is highly imbalanced. Non-delinquent loans account for most of the dataset (Nearly 96%). This will exaggerate the accuracy of the model. And the prediction for the training set will not make sense (Most will be predicted to be non-delinquent). Possible Solution SMOTE + ENN
- Split the data into training set and test set (80% training, 20%testing). Remember that data should be split first before resampling 

### Model
#### model.py
- One input layer; Two hidden Layer; One output Layer to predict probability of time_to_d

### Evaluation
#### summary.py
In progress...

### Authors
- **Zhuo Zhao** 
- **Prof. Georges Tsafack** 
