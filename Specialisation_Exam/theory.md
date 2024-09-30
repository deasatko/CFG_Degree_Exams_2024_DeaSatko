# Specialisation Exam 2024: Theory Questions

## 1.1 In your own words, what does the role of a `data scientist` involve?
```
- A data scientist is a professional who analyses and interprets data to help businesses make informed decisions. They handle large datasets, applying machine learning and predictive modelling techniques to uncover patterns and insights. Additionally, they contribute to the development of AI technologies.
```

## 1.2 What is an `outlier`? Here we expect to see the following:
```
a. Definition
- An outlier is a data point that significantly differs from other observations in a dataset.

b. Examples
- For example, in a dataset of movie reviews ranging from 5 to 9, a review of 2 would be considered an outlier.
  
c. Should outliers always be removed? Why?
- Not always. If outliers are due to errors, they should be removed. However, they could also represent special events or variations that are critical to understanding the dataset and should therefore be retained.
  
d. What are other possible issues that you can find in a dataset?
- Possible issues include missing data, duplicates, incorrect data types, and inconsistency (e.g., various date formats or measurement units). Identifying and addressing these issues is crucial during the data cleaning process.
```

## 1.3 Describe the concepts of `data cleaning` and `data quality`. Here we expect to see the following:
```
a. What is data cleaning?
- Data cleaning is the process of detecting, correcting, or removing errors and inconsistencies in a dataset. This may be necessary due to corrupted datasets or inaccurate entries submitted by individuals.
  
b. Why is data cleaning important?
- Proper data cleaning is essential because any conclusions drawn from unclean data could be inaccurate and lead to incorrect decisions, which could harm the business. Therefore, ensuring data quality through cleaning is crucial for making reliable analyses and decisions.

c. What type of mistakes do we expect to commonly see in datasets?
- Common mistakes include missing values (which may need to be populated rather than deleted), duplicates, formatting issues (e.g., inconsistent text or date formats), and unaddressed outliers.
```

## 1.4 Discuss what is `Unsupervised Learning` - Clustering in Machine Learning using an example. Here we expect to see the following:
```
a. Definition.
Unsupervised learning is a type of machine learning where the algorithm is trained using unlabelled data, meaning the input data does not have corresponding output labels. Clustering, a specific type of unsupervised learning, groups similar data points together based on shared features.

b. When is it used?
Clustering is used when there is a need to understand the structure of data before having predefined categories. This approach is especially useful for large datasets where manual categorisation is impractical.

c. What is a possible real-world application of unsupervised learning?
An example is text clustering. For instance, search engines or digital libraries use clustering to group similar documents together. When a user searches with keywords like "Star Wars", the engine presents groups of results related to the same topic.

d. What are its main limitations?
Limitations include difficulty in determining the optimal number of clusters and challenges in interpreting and validating results. Clustering algorithms can be sensitive to unclean data, particularly outliers, which can lead to inaccurate groupings. Additionally, different clustering algorithms may produce varying results even on the same dataset.
```


## 1.5 Discuss what is `Supervised Learning - Classification in Machine Learning using an example. Here we expect to see the following:
```
a. Definition.
Supervised learning is a machine learning approach where an algorithm is trained on labelled datasets, meaning each input comes with an associated correct label. Classification is a type of supervised learning that involves predicting categorical labels based on preset inputs. The goal is to assign new instances to predefined categories.

b. When is it used?
Classification is used when a specific task requires to predict a categorical outcome, such as sorting emails into different categories in an inbox.

c. What is a possible real-world application of supervised learning? 
A common application is in banks, where classification models detect fraudulent transactions. These models analyse past data labelled as "fraudulent" or "legitimate" and learn to identify patterns associated with fraud. For each new transaction, the model predicts whether it is likely to be fraudulent.

d. What data do we need for it? Is there any processing that needs to be done?
Labelled data is essential, with each data point tagged with the correct label. The data must be clear and accurately labelled. This requires thorough data cleaning, including noise removal, fixing missing values, and normalising features. Feature selection or extraction can further enhance model performance by focusing on the most relevant variables, reducing noise, and simplifying the data.

```