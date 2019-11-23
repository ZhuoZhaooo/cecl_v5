# CECL_V5
The project is to build DNN model for credit losses estimation based on current expected credit losses methodology (CECL). The project focuses on the probability of default (PD) in future periods. 
## Roadmap
- [**Introduction to CECL Backgrounds**](#introduction)
- **ML CECL Architecture**
- **Data Source**
- **Workflow (Scripts Descriptions)**
- **Model Evaluation**

## Introduction to CECL Backgrounds <a name='introduction'></a>
- Current Expected Credit Losses (CECL) is a new credit loss accounting standard (mode)l issued by FASB.
- The CECL standard focuses on estimation of expected losses over the life of the loans, while the current standard relies on incurred losses (ALLL).
![][CECL_VS_ALLL]

## ML CECL Architecture
**Our model focuses on the probability of default in each period.**
- For a default loan, find its age when it defaults(default_age).
- Calculate how long it takes that loan to default(time_to_d = default_age - current_age)
- Set time_to_d as training label. Build a DNN to predict the probability distribution of time_to_d
![][time_to_d]
## Data Source
Freddie Mac Single Family Loan-Level Dataset  
[Data Manual](https://github.com/ZhuoZhaooo/cecl_v5/blob/master/project_description/user_guide.pdf)
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

[CECL_VS_ALLL]:https://github.com/ZhuoZhaooo/cecl_v5/blob/master/project_description/Screenshot_2019-11-23_12-55-49.png
[time_to_d]:https://github.com/ZhuoZhaooo/cecl_v5/blob/master/project_description/Screenshot_2019-11-23_12-56-56.png
