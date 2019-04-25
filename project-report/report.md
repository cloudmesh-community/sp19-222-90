:warning: in review 

# Rookie Fantasy Football Point Prediction

| Andrew Gotts, Ethan Japundza, Brian Schwantes  
| adgotts@iu.edu, ejapundz@iu.edu, bschwant@iu.edu  
| Indiana University
| hid: sp19-222-94, sp19-222-90, sp19-222-92  
| github: [:cloud:](https://github.com/cloudmesh-community/proceedings-fa18/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/proceedings-fa18/blob/master/project-code)


---

Keywords: KNN, Fantasy Football, REST, Docker

---

## Abstract

We created a REST service that predicts which 2019 NFL Rookies will score the most fantasy football points based on their position and list them in order. 

:wave: add a few sentences to this, the abstract should encapsulate the entire project. 

## Introduction

Who should be my top draft picks in this years fantasy football draft?  This is a question that has plagued fantasy football enthusiast since its creation in XXXX. According to one Joris Drayer, "more than 29 million Americans and Canadians participate in some kind of fantasy sports league." \cite{@article:drayer2010effects}  especially when it comes to drafting rookies due to their inexperience. For those trying to make an educated pick on an untested rookie 'the Rookie Fantasy Football Point Predictor' will finally provide some data points to assist end users make more informed decisions.	 

Our project utilizes information from three data sets consisting of the 2000-18 NFL Combine stats for all participants, 2019 NFL Combine stats for this years rookies, and 2001-18 Fantasy Football Data for current players. From this data, it was our goal to be able to predict any rookie combine participants fantasy football points per season and per game and rank which rookies will score the most points based on their position. 

We employed the K-Nearest Neighbor machine learning algorithm to compare the combine stats of each incoming rookies to current players combine stats and determine who they are most similar to. After finding the current player that is most like each rookie, we average the current players fantasy football points. This gives us a prediction of how many points a rookie while score in the season and per game.  These rookies are then sorted by their football position and ranked by most predicted points to allow one to quickly, and easily decide who the best pick is for a given position.

:wave: histroy of fantasy football maybe?

:wave: how big of an industry is FF million? billion?

:wave: could this revolutionize FF?

## How To Use
```
test
```
## Requirements


### Images

Image locations that start with http are not allowed. All images must be in an images folder within your directory.

All images must be referred to in the text. The words bellow and above
must not be used in your paper for images, tables, and code. For code you could use 

> In the previous

> In the following 

> As explained next

> We install the softwere with

BUT DO NOT USE THEM FOR IMAGES, ANY IMAGE MUST HAVE A MEANINGFUL CAPTION AS SHOWN IN OUR EXAMPLE

Comment: Above and bellow in a paper means you ask the reader to look at their shoes or the ceiling :smiley:.

+@fig:fromonetotheorther shows a nice figure exported from Powerpoint
to png. If you like you can use this as a basis for your drawings.

![A simple flow chart](images/from-one-to-the-other.png){#fig:fromonetotheorther}

Figures must not be cited with an explicit number, but automated
numbering must be used. Here is how we did it for this paper:

```
+@fig:fromonetotheorther shows a nice
figure exported from Powerpoint to png.
If you like you can use this as a basis
for your drawings.

![A simple flow chart](images/from-one-to-the-other.png){#fig:fromonetotheorther}
```

If the paper is copied form another source you MUST use a citation in the caption. 

![A simple flow chart [@vonLaszwski-fa18-sample-report]](images/from-one-to-the-other.png){#fig:fromonetotheorthertwo}

This is done as follows

```
![A simple flow chart [@vonLaszwski-fa18-sample-report]](images/from-one-to-the-other.png){#fig:fromonetotheorthertwo}
```

### Sylistic Issues

Your report must not include the phrases


* In this term project we show
* In this project we describe
* In this chapter we have
* In this report we do

or similar

Instead you use

* We show
* We describe
* We have
* We do

You will not use the word `I` but instead you will use `we` or third person.



### Copy from this document

In case you want to copy part of this document you need to do this from raw mode

* <https://raw.githubusercontent.com/cloudmesh-community/proceedings-fa18/master/project-report/report.md>

**HOWEVER, YOU MUST NOT COPY THIS EXAMPLE IN YOUR REPORTS. IF YOU DO YOU MUST
CHANGE THE IMAGE REFERNCES. THIS IS LOGICAL AS ALL IMAGE REFERNCES
MUST BE UNIQUE.**


## Design 

## Architecture

## Dataset

## Implementation / Design

The machine learning technique KNN (k nearest neighbors) is a technique often used for classification or linear regression predictive problems. The algorithm relies on feature similarity, or the process of checking how an input sample will resemble the training set. Using the Euclidean distance, KNN calculates which features of the input sample are nearest to the training set. Choosing the value of k is dependent on the training datasets used, and the desired outcome. To get the optimal value of k, you can segregate the training and validation from the initial dataset, and plot the validation error curve to visualize the optimal value of K. Compared to other machine learning algorithms KNN has an advantage as it does not make assumptions about the data it uses, it is simple and highly effective, and it is versatile, as it can be used for both classification and regression. However, to its disadvantage KNN will store most if not all the training dataset which will often cause the algorithm to be computationally expensive and slow. 

Before our implementation of the KNN algorithm we found that choosing a value of three to represent our k would best optimize the programs results. In the python file k-nearest, we call and train the KNN algorithm with the NFL combine results from the last 21 years. Using the incoming 2019 NFL rookie’s data as the input data, the program calculates the Euclidean distance between each feature of the input data, and the accumulated combine results of previous years. This calculation yields the three closest veteran players that each NFL rookie performed the most similarly to during the combine. While the results of our implementation are accurate and informative, the speed disadvantage of the KNN algorithm become apparent within our program. Despite making adjustments to speed up the algorithm, such as only running KNN on the instances of the input data called for versus running it on all of the input data and filtering it afterwards to get a tailored output, the program still runs slowly. This is simply due to the KNN algorithm storing the entire dataset before it runs computations on it. Despite our best efforts of optimization, our program still has an unavoidable run speed of about ten seconds. 

Another disadvantage of the KNN algorithm and other machine learning techniques are there tendency to un-intentionally weight certain features of datasets due to size and scale differences in the features. To account for this, we have to normalize the datasets we pass into the algorithm, creating an equal ‘weight’ for the Euclidean distance to calculate a distance to. In Python the program Pandas library, or Python Data Analysis Library, allows us to do just that and easily import the csv’s needed to execute the KNN algorithm. …… to be continued and edited


---
### Technologies Used:

#### K-Nearest Neighbors
#### Pandas
#### Python Design
#### Rest
#### Docker
#### Yaml

## Benchmark

## Conclusion

## Acknowledgement

## Workbreakdown

Only needed if you work in a group.

