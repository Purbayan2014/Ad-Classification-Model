## Ad Classification Model

This Ad-Classification Model predicts whether an user is likely to view an
Advertisement using Auto-AI feature of IBM . It is a supervised machine learning
algorithm whose back-end is entirely dependent on the IBM Cloud as IBM Watson back-end
it's services has been used.

## Overview

![image](https://user-images.githubusercontent.com/90950629/165959575-89a43afd-dc67-45ae-a4f0-4a49247958b9.png)


## Architecture Components

## Flow-Description

1. A IBM Watson Studio Instance has been created .
2. After that the dataset has been loaded in the Watson Studio and I have created a
   machine learning Instance .
3. Then I have used the best promoted algorithm pipeline and used it to deploy the model.
4. After the deployment has been completed I had integrated the API key with the UI.
5. After integrating the code with the UI, the model has been deployed on heroku cloud
   service.

## Included components

  1.	[IBM Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio) - IBM Watson® Studio helps data scientists 
      and analysts prepare data and build models at scale across any cloud.

  2.	[IBM Watson Machine Learning](https://cloud.ibm.com/catalog/services/machine-learning) - IBM Watson® Machine Learning helps data scientists 
      and developers accelerate AI and machine-learning deployment.

  3.	[IBM Cloud Object Storage](https://cloud.ibm.com/catalog/services/cloud-object-storage) - IBM Cloud™ Object Storage makes it possible to store 
      practically limitless amounts of data, simply and cost effectively.

## Featured technologies

  + [artificial-intelligence](https://developer.ibm.com/technologies/artificial-intelligence/) - Build and train models, and create apps, with a trusted AI-infused platform.

  + [Python](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.


  # About the dataset
  
  ![image](https://user-images.githubusercontent.com/90950629/165960160-b9da6bf2-5fe3-412c-abe8-b460d8851c6b.png)


  Dataset can be downloaded from [here](https://www.kaggle.com/fayomi/advertising)

  ## Attributes in the dataset

  This data set contains the following features:

  **'Daily Time Spent on Site'**: consumer time on site in minutes

  **'Age'**: cutomer age in years

  **'Area Income'**: Avg. Income of geographical area of consumer

  **'Daily Internet Usage'**: Avg. minutes a day consumer is on the internet

  **'Ad Topic Line'**: Headline of the advertisement

  **'City'**: City of consumer

  **'Male'**: Whether or not consumer was male

  **'Country'**: Country of consumer

  **'Timestamp'**: Time at which consumer clicked on Ad or closed window

  **'Clicked on Ad'**: 0 or 1 indicated clicking on Ad

Alogrithm used :


![image](https://user-images.githubusercontent.com/90950629/165959799-9c91e28f-325b-4489-947f-40ce7def38ec.png)




1. LightGBM is a gradient boosting classifier in machine learning that uses tree-based learning algorithms. It is designed to be distributed and efficient with faster drive speed and higher efficiency, lower memory usage and better accuracy.
   In machine learning, the LightGBM classifier is part of the Boosting family, and today it is the most common classification model in the machine learning community. LightGBM is a powerful machine learning model that can be shaped depending on the task you are working on.


2.The random forest classifier is a supervised learning algorithm which you can use for regression and classification problems. It is among the most popular machine learning algorithms due to its high flexibility and ease of implementation.
  It consists of multiple decision trees just as a forest has many trees. On top of that, it uses randomness to enhance its accuracy and combat overfitting, which can be a huge issue for such a sophisticated algorithm. These algorithms make decision trees based on a random selection of data samples and get predictions from every tree. After that, they select the best viable solution through votes.

  It has numerous applications in our daily lives such as feature selectors, recommender systems, and image classifiers.
  Assuming your dataset has “m” features, the random forest will randomly choose “k” features where k < m.  Now, the algorithm will calculate the root node among the k features by picking a node that has the highest information gain.

  After that, the algorithm splits the node into child nodes and repeats this process “n” times. Now you have a forest with n trees. Finally, you’ll perform bootstrapping, ie, combine the results of all the decision trees present in your forest.

  It’s certainly one of the most sophisticated algorithms as it builds on the functionality of decision trees.

  Technically, it is an ensemble algorithm. The algorithm generates the individual decision trees through an attribute selection indication. Every tree relies on an independent random sample. In a classification problem, every tree votes and the most popular class is the end result. On the other hand, in a regression problem, you’ll compute the average of all the tree outputs and that would be your end result.

  A random forest Python implementation is much simpler and robust than other non-linear algorithms used for classification problems.

## Pipelines

![image](https://user-images.githubusercontent.com/90950629/165961526-391d8057-c0ea-4351-a366-0009e9862474.png)




![image](https://user-images.githubusercontent.com/90950629/165959371-6fb1a5d6-067f-4808-acc5-9e07690a1a19.png)


## About the Model

![image](https://user-images.githubusercontent.com/90950629/165961451-e37c1c71-9528-47a7-8758-12afbf1b3c55.png)

The **Precision vs. Recall Curve** chart plots the proportion of outcomes predicted to be positive that are positive, also known as precision, on the vertical axis, against the proportion of positive outcomes that are correctly predicted, also known as recall, sensitivity, probability of detection or true positive rate (TPR), on the horizontal axis, as the threshold for positive classification is varied across the predicted probability range from 1 down to 0. When the threshold is set high, few false positives will occur and precision will be high, while recall will be low. As the threshold is decreased, recall will increase and precision will generally decrease. Although there is generally a trade off between precision and recall, the curve may not be strictly monotonically decreasing. The area under the Prevision vs. Recall curve is generally preferred to the area under the ROC curve as an evaluation statistic for binary classification when the proportions of positive and negative observed instances are highly imbalanced.

![image](https://user-images.githubusercontent.com/90950629/165961112-b75037c7-a86e-4506-a965-891cde28099f.png)

The **Confusion Matrix** shows numbers and proportions of correct and incorrect classifications for appropriate models.

![image](https://user-images.githubusercontent.com/90950629/165961207-cea534fe-4390-4448-8e93-dd59aa2eda30.png)

The **ROC (Receiver Operating Characteristic) Curve** chart plots the true positive rate (TPR) on the vertical axis against the false positive rate (FPR) on the horizontal axis, as the threshold for positive classification is varied across the probability range. The true positive rate is the proportion of positive outcomes that are correctly predicted, also known as sensitivity, recall, or probability of detection. The false positive rate is the proportion of negative outcomes that are falsely predicted to be positive, also known as one minus specificity (1-specificity), fall-out, probability of false alarm, or false discovery rate (FDR).

![image](https://user-images.githubusercontent.com/90950629/165961257-9bc15522-91aa-4d91-94ce-b611782cdf86.png)




