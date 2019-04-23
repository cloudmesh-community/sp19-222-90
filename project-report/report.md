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

We worked to create a REST service that predicts which NFL Rookies will score the most fantasy football points based on their position and list them. 

## Introduction

Who should be my top draft picks in this years fantasy football draft? This is a question that has plagued Americans since the creation of fantasy football, especially when it comes to drafting rookies due to their inexperience. For those trying to make an educated pick on an untested rookie, our project, the Rookie Fantasy Football Point Predictor will finally provide some guidance on who is likely to perform for your team.	 
    Our project utilizes information from three data sets consisting of the 2000-18 NFL Combine stats for all participants, 2019 NFL Combine stats for this years rookies, and 2001-18 Fantasy Football Data for current players. From this data, it was our goal to be able to predict any rookie combine participants fantasy football points per season and per game and rank which rookies will score the most points based on their position. 
    We employed the K-Nearest Neighbor machine learning algorithm to compare the combine stats of each incoming rookies to current players combine stats and determine who they are most similar to. After finding the current player that is most like each rookie, we average the current players fantasy football points. This gives us a prediction of how many points a rookie while score in the season and per game.  These rookies are then sorted by their football position and ranked by most predicted points to allow one to quickly, and easily decide who the best pick is for a given position.


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

