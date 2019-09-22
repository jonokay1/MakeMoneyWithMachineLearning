# **Credit Card Fraud Detection**
This was completed as an assignment for a Make Money With Machine Learning Course offered by Siraj Raval
The dataset for this submission was taken from a Kaggle Competition by [IEEE-CIS Fraud Detection](https://www.kaggle.com/c/ieee-fraud-detection/overview)

## Flow of the Code

- Started by importing the data from kaggle to google drive. 
- RAM optimisation code was adapted code from [Ashish Gupta](https://github.com/RoyMachineLearning)
- The imported data was then read into dataframes
- The dataframes were visualised and quickly analysed to aid feature selection
- The selected features were then used to train a logistic model
- The logistic model was used to predict fraudlent and non-fraudlent transactions
- Recall matrix was plotted to show the performance of the model

## Visualisations
**How much of the data is Fraud and not Fraud?**
![Fraud barplot](https://github.com/jonokay1/MakeMoneyWithMachineLearning/blob/master/Week%203/Images/FraudinTraining.jpg)

**How many cells are empty in the training data?**
![Empty Cells barplot](https://github.com/jonokay1/MakeMoneyWithMachineLearning/blob/master/Week%203/Images/NaNTraining.jpg)

**How is the data correlated?**
![Correlation Image](https://github.com/jonokay1/MakeMoneyWithMachineLearning/blob/master/Week%203/Images/CorrTraining.jpg)


## Summary of Results
- Upon fiting and testing the model, it was found to be 98% accurate
- The model was then used on the validation data whose results were submitted on Kaggle. 
- The results were 49.98%

## Conclusion
- In order to improve the results, better data cleaning and optimisation would be required. Some of the droped rows, could have outliers that would help the model with better prediction

- Comparing with different training models and tuning of hyper parameters would also improve the score.

- For the training of this model, given the 98% fit of the training data, there was over fitting by the model. This causes it to fail when faced with totally new data
