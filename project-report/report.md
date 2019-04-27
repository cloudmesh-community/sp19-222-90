# Rookie Fantasy Football Point Prediction

:warning: in review 

:wave: I want to see the equations for knn...i can help you with the math syntax if you tell me what they are.


| Andrew Gotts, Ethan Japundza, Brian Schwantes  
| adgotts@iu.edu, ejapundz@iu.edu, bschwant@iu.edu  
| Indiana University

| hid: sp19-222-94, sp19-222-90, sp19-222-92  
| github: [:cloud:](https://github.com/cloudmesh-community/proceedings-fa18/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/proceedings-fa18/blob/master/project-code)


---

Keywords: KNN, Fantasy Football, REST, Docker, Yaml

---

## Abstract

The number of fantasy football player increases dramatically every year. We wanted to create a service that will help users draft better teams. We decided to focus on incoming NFL rookies, as they have no professional sports experience making it hard to decide who will be the most succesful. To solve this problem, we implemeted a REST service that gets data from Goodle drive, then utilizes the K-Nearest Neighbor machine learning algorithm on the data set then predicts which 2019 NFL Rookies will score the most fantasy football points based on their position allowing users to make more educated picks.

## Introduction

Who should be my top draft picks in this years fantasy football draft?  This is a question that has plagued fantasy football enthusiast since its creation in 1962, especially when it comes to drafting rookies due to their inexperience. But why does it even matter, isn't fantasy football is just a game?  According to Joris Drayer, "more than 29 million Americans and Canadians participate in some kind of fantasy sports league." He goes on to explain that fantasy sports leagues have an, "economic impact estimated at $4.48 billion across the sport industry" @brian1. Fantasy sports players are always looking for a way to get an edge over their competion. With that many people and that much money involved, technologies created to help players be successful could revolutionize fantasy football. Because of that, we utilized the the power of machine learning to create the 'Rookie Fantasy Football Point Predictor' for those trying to make an educated pick, on untested rookie players. Our service will finally provide some data points to assist end users in making more informed decisions.

Our project utilizes information from three data sets consisting of the 2000-18 NFL Combine stats for all participants, 2019 NFL Combine stats for this years rookies, and 2001-18 Fantasy Football Data for current players. From this data, it was our goal to be able to predict any rookie players fantasy football points per season and per game. We also wanted to be able to show how these rookies stacked up against other rookies that play the same postion. 

We employed the K-Nearest Neighbor machine learning algorithm for our service. We needed to compare the combine stats of each incoming rookies to current players combine stats and determined who they are most similar to. After finding the rookies three nearest neighbors, or the current players they are most similar to, we averaged the players past fantasy football points. We then had a prediction of how many fantasy football points each rookie would score throughtout the season and during each game.  The rookies were then sorted by their football position and ranked in order of predicted points. With this data, one can quickly and efficently decide who the best rookie pick is for a given position.

## Implementation and Design

The machine learning technique KNN (k nearest neighbors) is a technique often used for classification or linear regression predictive problems. The algorithm relies on feature similarity, or the process of checking how an input sample will resemble the training set. Using the Euclidean distance, KNN calculates which features of the input sample are nearest to the training set. Choosing the value of k is dependent on the training datasets used, and the desired outcome. To get the optimal value of k, you can segregate the training and validation from the initial dataset, and plot the validation error curve to visualize the optimal value of K. Compared to other machine learning algorithms KNN has an advantage as it does not make assumptions about the data it uses, it is simple and highly effective, and it is versatile, as it can be used for both classification and regression. However, to its disadvantage KNN will store most if not all the training dataset which will often cause the algorithm to be computationally expensive and slow. 

Before our implementation of the KNN algorithm we found that choosing a value of three to represent our k would best optimize the programs results. In the python file k-nearest, we call and train the KNN algorithm with the NFL combine results from the last 21 years. Using the incoming 2019 NFL rookie’s data as the input data, the program calculates the Euclidean distance between each feature of the input data, and the accumulated combine results of previous years. This calculation yields the three closest veteran players that each NFL rookie performed the most similarly to during the combine. While the results of our implementation are accurate and informative, the speed disadvantage of the KNN algorithm become apparent within our program. Despite making adjustments to speed up the algorithm, such as only running KNN on the instances of the input data called for versus running it on all of the input data and filtering it afterwards to get a tailored output, the program still runs slowly. This is simply due to the KNN algorithm storing the entire dataset before it runs computations on it. Despite our best efforts of optimization, our program still has an unavoidable run speed of about ten seconds. 

Another disadvantage of the KNN algorithm and other machine learning techniques are there tendency to un-intentionally weight certain features of datasets due to size and scale differences in the features. To account for this, we have to normalize the datasets we pass into the algorithm, creating an equal ‘weight’ for the Euclidean distance to calculate a distance to. In Python the program Pandas library, or Python Data Analysis Library, allows us to do just that and easily import the csv’s needed to execute the KNN algorithm. …… to be continued and edited

## Architecture and Technologies Used:

#### REST
Representational State Transfer or REST is an architectural style used when creating web services. From the textbook, REST is desribed as being, "based on stateless, client-server, cacheable communications protocol.” REST applications typically use HTTP protocol and basic methods like GET, PUT, POST, etc. Because of this, REST can preform the four CRUD operations: Create resources, Read resources, Update resources, and Delete resources. Functions created a user can be combined with REST to create a cloud service that completes predefined tasks. 

We used REST in conjuction with a YAML document within our project, to create a REST service that runs on ones local machine. The service can be connected to through any internet broswer. Within the YAML document, there are predefined paths a user can use for different purposes. For our project the path can be alterd from /results/{position} to view fantasy football point predictions based on a given postion. When a postion is entered, our service gets the dataset from a google drive, then runs the K-Nearest neighbors algorithim on the data, then prints the result.

Excerpt From: Gregor von Laszewski. “Cloud Computing.” iBooks.  

#### Docker
Docker is a tool that allows users to create, deploy and run applications within virtual containers. This technology is extremely useful when developing applications because it allows one to combine all needed components into one package. Because of these containers, developers are also certain these applications will work on all other Linux machines and don't have to worry about the individual machines their programs will run on. We utilized Docker within our project to created a robust, self-contained, and easy to use REST service for users on any Linux machine. 

#### Yaml
YAML is the type of file that is used to configure the endpoints for the server. Endpoints are used to dictate what URLs are valid in the server and what data and data type will be displayed for a particular path. YAML also allows specifications to be added to endpoints such as operations, HTML responses, and HTTP methods. This provides a lot of flexibility that is complemented by an easy to read syntax. Our YAML takes advantage of the operations feature along with URL paths acting as variables to a function, and also displays a .csv table that is translated into an HTML table.


#### Python
???

## Dataset

We got all of our datasets from Pro Football Reference (https://www.pro-football-reference.com). The data we utilized is 2019 NFL combine stats of current incoming rookies, 2000-2018 NFL combine stats which is needed to compare rookie players to current players, and 2001-2018 Fantasy Football player results which we used when predicting Fantasy Football points.

## Limitations

The NFL combine has only six tests of speed, agility and stregth, 40 yard dash, vertical leap, bench press reps, broad jump, three cone drill, and 20 yard shuttle run. We used that data in conjuction with each players height and weight when finding their "nearest neighbors." However, not all players, rookies and current, completed all of these tests in the combine, which could result in inaccurate comparisons between players. While we accurately found the most similar players based on combine data when all parameters were availabe, success in the NFL most likely can not be fully determined based on these stats. Another limitation is that we do not know what NFL team each rookie will join, and what role they will play on the team, (starter, first string, second string?) based on the players each team already has. Going forawd, one way we could attempt to increase accraucy of predictions in focusing on the weight of each parameter of the data and the correlation that has to success in fantasy football. For example, vertical leap may have no correlation to the number of fantasy points a player scores, while the three cone drill may have a very strong correlation to the number of points scored.  One way we wanted to increase the accuracy of prediction, was utilizing rookies in game college football stats. However, we ulimatly decided that the differences in conferance and division could provided skewed data resulting in inaccurate predictions. 

## Conclusion

As the number of Fantasy Football players continues to increase, we set out to answer the age old question, who should be my top draft picks in this years fantasy football draft? We wanted to provide users a way to make eduecated picks on rookies that are likely to succeed in Fantasy Football. To accomplish this, with the used nearly 18 years worth of NFL combine data and Fantasy Football results and created a service using REST, Python, Yaml, and Docker to predict how well NFL rookies will do. Utilizing artifical intelligence to provide educated sports picks could revolutionize fantasy sport; and in a market that has a nearly $4.5 billion impact across the sports industry, this information could be extremly valuable as well. We successfully made a service that ranked rookies by postion, and predicted how many points they would score in Fantasy Football.



