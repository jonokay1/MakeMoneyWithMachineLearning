# **Pneumonia Detection Using Transfer Learning**
Keras library was used to train a machine learning model on detecting Pneumonia from an X-Ray image dataset on Kaggle. [Chest X-Ray Images - Pneumonia](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

## Flow of the Code

- Started by importing the data from kaggle to the server 
- Imported data was visualised. Some of the chest X-Ray images are shown below
- A pretrained model was imported from InceptionV3 imagenet
- It failed to predict what the image was. Its highest percentage of 7.6% referred to the chest scan as a Conch
- The model was then trained 

## Visualisations
**Normal X-Ray Image**

![Normal](https://github.com/jonokay1/MakeMoneyWithMachineLearning/blob/master/Week%204/Images/normalx_ray.jpg)

**Pneumonia infected X-Ray Image**

![Pneumonia](https://github.com/jonokay1/MakeMoneyWithMachineLearning/blob/master/Week%204/Images/pneumoniax_ray.jpg)

<p align="center">
  <img width="615" height="188" src="https://github.com/jonokay1/MakeMoneyWithMachineLearning/blob/master/Week%204/Images/pneumoniax_ray.jpg">
</p>

## Summary of Results
- Upon fiting and testing the model, it was found to be 68.75% accurate
- From the DataFrame below the model correctly predicts all the cases of Pneumonia and has 2 False Positives
- This gives a prediction accuracy score of 86.67%

![validation](https://github.com/jonokay1/MakeMoneyWithMachineLearning/blob/master/Week%204/Images/PneumoniaDataFrame.JPG) 

