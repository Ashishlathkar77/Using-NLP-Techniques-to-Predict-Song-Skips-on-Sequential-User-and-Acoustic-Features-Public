<p align="center">
  <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_Green.png">
</p>

# Prediction of Song Skips on Spotify based on Sequential User and Acoustic Data

Music consumption habits have changed dramatically with the rise of streaming services like Spotify, Apple Music and Tidal. The skip button plays a large role in the user;s experience, as they are free to abondon songs as they choose. Music providers are also incentivized to recommend songs that their users like in order to increase user experience and time spent on the platform.

Machine learning in the context of music often users recommender system. There hasn't been much research on how a user's interaction with music over time can help recommend music to the user. So this system will predict the likehood of whether the customer will skip the song or not by providing song characteristics.

## 0. Introduction
Spotify is one of the most popular online music streaming services, with hundreds of million users and more than 40 million music tracks. Recommending the right music track to the right user at the right time is their key to success.

In 2018, Spotify released an open dataset of sequential listening data. According to them, "_a central challenge for Spotify is to recommend the right music to each user. While there is a large related body of work on recommender systems, there is very little work, or data, describing how users sequentially interact with the streamed content they are presented with. In particular within music, the question of if, and when, a user skips a track is an important implicit feedback signal._"

## 1. Dataset
Spotify Sequential Skip dataset, consisting of roughly 130 million listening sessions with associated user behaviors. Each session consists of multiple music tracks (songs, podcasts, etc.). User interaction features are provided for the first half of the session, but only track ids are provided for the second half.

<p align="center">
  <img src="https://github.com/Ashishlathkar77/Using-NLP-Techniques-to-Predict-Song-Skips-on-Sequential-User-and-Acoustic-Features-Public/blob/main/Product/data_spotify.png">
</p>


## 2. Pre-Processing
We merged user behavior and acoustic features for each track ids. We also preprocessed categorical features into one-hot representations or label encoding and normalized them (z-score and min/max). This pre-processing created an input track embedding for our model.

## 3. Features Details
We chose to create target variable "_skipped_" using formula:

```python
df["skipped"] = df["skip_1"]*df["skip_2"]*df["skip_3"]
df.drop(["skip_1", "skip_2", "skip_3", "not_skipped"], axis=1, inplace=True)
```
for whether the song was skipped / not skipped since it better reprents whether a user like the track they are on.

## 4. Exploratory Data Analysis (EDA)
[Jupyter notebook of EDA](https://github.com/Ashishlathkar77/Using-NLP-Techniques-to-Predict-Song-Skips-on-Sequential-User-and-Acoustic-Features-Public/blob/main/Internship_may_29.ipynb)

"_Some Insights from EDA_"

## 5. Skip Prediction system

"_Some Insights_"

![](https://github.com/Ashishlathkar77/Using-NLP-Techniques-to-Predict-Song-Skips-on-Sequential-User-and-Acoustic-Features-Public/blob/main/Product/spotify1.png)
![](https://github.com/Ashishlathkar77/Using-NLP-Techniques-to-Predict-Song-Skips-on-Sequential-User-and-Acoustic-Features-Public/blob/main/Product/spotify2.png)

## 6. Training and Testing Models

### a. Logistic Regression

### b. Naive Bayes Classifier

### c. Decision Tree Classifier

### d. KNN Classifier

## 7. What Features Contribute to the Prediction?

## 8. Conclusion








