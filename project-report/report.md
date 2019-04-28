# Rookie Fantasy Football Point Prediction

:warning: in review 

:warning: lets create a bib entry for the profootball website where we got the data from instead of showing the link.

:wave: I want to see the equations for knn...i can help you with the math syntax if you tell me what they are.

:question: Is the KNN section better now, any tips for rest of paper? :smiley: check how i seeded and referenced the figure.

:smiley: Paris Campbell :smiley: Great pick

| Andrew Gotts, Ethan Japundza, Brian Schwantes  
| adgotts@iu.edu, ejapundz@iu.edu, bschwant@iu.edu  
| Indiana University

| hid: sp19-222-94, sp19-222-90, sp19-222-92  
| github: [:cloud:](https://github.com/cloudmesh-community/sp19-222-90/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/sp19-222-90/tree/master/project-code)


---

Keywords: KNN, Fantasy Football, REST, Docker, Yaml

---

## Abstract

As the number of fantasy football players increases dramatically every year, we saw an opportunity to create a service that will help users draft better teams. While NFL veterans have gameplay for fantasy enthusiasts to evaluate, incoming rookies with a lack of professional experience makes it difficult for fans to evaluate whether or not their teams picks will be successful in the NFL. To solve this problem, we implemented a REST service that gets an aggregate of combine and fantasy football data from Google-Drive. Our service then utilizes the K-Nearest Neighbor machine learning algorithm on our data set, outputting our projections for which 2019 NFL Rookies will score the most fantasy football points based on their metrics from the combine.

## Introduction

Who should be the top pick in this years fantasy football draft? This is a question that has plagued fantasy football enthusiasts since its creation in 1962. But why does it even matter, isn't fantasy football just a game? According to a report on the effects of fantasy football participation on NFL consumption, "more than 29 million Americans and Canadians participate in some kind of fantasy sports league." He goes on to explain that fantasy sports leagues have an, "economic impact estimated at $4.48 billion across the sports industry" @ref1. Fantasy sports players are always looking for a way to get an edge over their competition. With such a large amount of people and money involved, the technologies created to help players be successful are in a position to revolutionize the market of fantasy football. Utilizing the power of machine learning, we were able to create the 'Rookie Fantasy Football Point Predictor'. A service for those trying to make an educated pick on rookie players with no professional experience. 

Our project utilizes information from three data sets consisting of the 2000-2018 NFL Combine statistics, the 2019 NFL Combine statistics for this year's rookies, and the 2001-2018 Fantasy Football Data for every active NFL player. From this data, our goal was to both rank and predict the average fantasy points-per-game for the incoming rookie class based on comparisons within the data sets. In order to properly see the correlation between combine measurables and rookies’ average fantasy points-per-game, we needed to create comparisons of each combine drill with those of past and present NFL athletes. We found the best way to achieve this was to employ the K-Nearest Neighbor machine learning algorithm for our service.


## KNN Algorithm

The machine learning technique KNN (K-Nearest Neighbors) is a technique often used for classification or linear regression predictive problems. The algorithm relies on feature similarity, or the process of checking how an input sample will resemble the training set. Using the Euclidean distance formula, KNN calculates which features of the input sample are nearest to the training set. @fig:knn is a graphical illustration of this process.

![Euclidean distance formula](images/KNN_Euclidean.jpg){#fig:knn}

As seen above the Euclidean distance formula is used within KNN to calculate the distance between a feature of the input data, blue helmet, and k instances of that same feature within the training data, red helmets. Choosing the value of k is dependent on the training datasets used and the desired outcome. To get the optimal value of k, you can segregate the training and validation from the initial dataset, and plot the validation error curve to visualize the optimal value of k. Compared to other machine learning algorithms KNN has an advantage as it does not make assumptions about the data it uses, it is simple, highly effective, and it is versatile. However to its disadvantage, the KNN algorithm requires that we store all of the training dataset, which will often cause the algorithm to be computationally expensive and slow.

Before our implementation of the KNN algorithm, we found that choosing a value of three to represent our k would best optimize the results of the program. In the python file k-nearest, we call and train the KNN algorithm with the NFL combine results from the last 21 years. Using the incoming 2019 NFL rookie statistics as the input data, the program calculates the Euclidean distance between each feature of the input data and the accumulated combine results of previous years. This calculation yields the three closest veteran players that each NFL rookie performed the most similar to during the combine. While the results of our implementation are accurate and informative, the speed disadvantage of the KNN algorithm becomes apparent within our program. Despite making adjustments to speed up the algorithm, such as only running KNN on the instances of the input data called for opposed to running it on all of the input data and filtering it afterward to get a tailored output, the program still runs slowly. This is due to the KNN algorithm requiring us to store the entire dataset before it runs computations on it. Despite our best efforts of optimization, our program still has a run speed of about five seconds.

Another disadvantage of the KNN algorithm and other machine learning techniques are there tendency to un-intentionally weight certain features of datasets due to size and scale differences. To account for this, we have to normalize the datasets we pass into the algorithm, creating an equal ‘weight’ for the Euclidean distance to calculate. In Python using the PANDAS library, or Python Data Analysis Library, allows us to do just that, and easily import the csv’s needed to execute the KNN algorithm. 

From this library we use the read.csv function to read the NFL comma-separated values (csv) file into data frame. A data frame is a two-dimensional tabular data structure with labeled axes, in which arithmetic operations align on both row and column labels. We use this data frame to isolate only our numeric features within the dataset, allowing us to quickly use only the features from the NFL combine that are measurables. As discussed earlier, in order for our output to be accurate the numeric features within each dataset must be normalized to create an equal weight for each combine measurement. Using the PANDAS data frame we achieved this by taking the numeric features and subtracting them from their mean. Once this was done we divide them by the standard deviation of the dataset, resulting in a very neat and evenly weighted data frame to pass into the KNN module. 


## Implementation

![REST Service](images/RESTdiagram.jpg){#fig:REST}

#### REST
Representational State Transfer or REST is an architectural style used when creating web services. From the textbook, REST is desribed as being, "based on stateless, client-server, cacheable communications protocol.” REST applications typically use HTTP protocol and basic methods like GET, PUT, POST, etc. Because of this, REST can preform the four CRUD operations: Create resources, Read resources, Update resources, and Delete resources. Functions created a user can be combined with REST to create a cloud service that completes predefined tasks. 

We used REST in conjuction with a YAML document within our project, to create a REST service that runs on ones local machine. The service can be connected to through any internet broswer. Within the YAML document, there are predefined paths a user can use for different purposes. For our project the path can be alterd from /results/{position} to view fantasy football point predictions based on a given postion. When a postion is entered, our service gets the dataset from a google drive, then runs the K-Nearest neighbors algorithim on the data, then prints the result.

Excerpt From: Gregor von Laszewski. “Cloud Computing.” iBooks.  

#### Docker
Docker is a tool that allows users to create, deploy and run applications within virtual containers. This technology is extremely useful when developing applications because it allows one to combine all needed components into one package. Because of these containers, developers are also certain these applications will work on all other Linux machines and don't have to worry about the individual machines their programs will run on. We utilized Docker within our project to created a robust, self-contained, and easy to use REST service for users on any Linux machine. 

#### Yaml
YAML is the type of file that is used to configure the endpoints for the server. Endpoints are used to dictate what URLs are valid in the server and what data and data type will be displayed for a particular path. YAML also allows specifications to be added to endpoints such as operations, HTML responses, and HTTP methods. This provides a lot of flexibility that is complemented by an easy to read syntax. Our YAML takes advantage of the operations feature along with URL paths acting as variables to a function, and also displays a .csv table that is translated into an HTML table. Future additions to endpoints are simple to add without affecting current endpoints which makes future updates straight forward with few worries about breaking past versions.


#### Python
The core of this project is written in Python which allows us to package all components needed to run our service easily. The use of "__init__" files creates a sensible directory structure that ensures a user can import our functions if they see them as useful for personal applications. The versatility of python enabled us to create functions that perform our main service along with a server that hosts them and ties everything together in a clean REST service, which uses a YAML file to create a direct link between the server and the python functions and presents an easy to understand flow in terms of the overall structure of the project.

## Dataset

We got all of our datasets from Pro Football Reference @data. The data we utilized is 2019 NFL combine stats of current incoming rookies, 2000-2018 NFL combine stats which is needed to compare rookie players to current players, and 2001-2018 Fantasy Football player results which we used when predicting Fantasy Football points.

## Limitations

The NFL combine has only six tests of speed, agility and stregth, 40 yard dash, vertical leap, bench press reps, broad jump, three cone drill, and 20 yard shuttle run. We used that data in conjuction with each players height and weight when finding their "nearest neighbors." However, not all players, rookies and current, completed all of these tests in the combine, which could result in inaccurate comparisons between players. While we accurately found the most similar players based on combine data when all parameters were availabe, success in the NFL most likely can not be fully determined based on these stats. Another limitation is that we do not know what NFL team each rookie will join, and what role they will play on the team, (starter, first string, second string?) based on the players each team already has. Going forawd, one way we could attempt to increase accraucy of predictions in focusing on the weight of each parameter of the data and the correlation that has to success in fantasy football. For example, vertical leap may have no correlation to the number of fantasy points a player scores, while the three cone drill may have a very strong correlation to the number of points scored.  One way we wanted to increase the accuracy of prediction, was utilizing rookies in game college football stats. However, we ulimatly decided that the differences in conferance and division could provided skewed data resulting in inaccurate predictions. 

## Conclusion

As the number of Fantasy Football players continues to increase, we set out to answer the age old question, who should be my top draft picks in this years fantasy football draft? We wanted to provide users a way to make eduecated picks on rookies that are likely to succeed in Fantasy Football. To accomplish this, with the used nearly 18 years worth of NFL combine data and Fantasy Football results and created a service using REST, Python, Yaml, and Docker to predict how well NFL rookies will do. Utilizing artifical intelligence to provide educated sports picks could revolutionize fantasy sport; and in a market that has a nearly $4.5 billion impact across the sports industry, this information could be extremly valuable as well. We successfully made a service that ranked rookies by postion, and predicted how many points they would score in Fantasy Football.


## Specification

```
swagger: "2.0"
info: 
  version: "0.0.1"
  title: "NFL FF Points"
  description: "A service that provides Fantasy Football point predictions for upcoming NFL rookies"
  termsOfService: "http://swagger.io/terms/"
  contact: 
    name: "NFL FF Prediction Service"
  license: 
    name: "Apache"
host: "localhost:8080"
basePath: "/cloudmesh/nfl-analysis/v1"
paths: 
  /results/{position}:
    get:
      tags:
        - NFL
      parameters:
        - name: position
          in: path
          description: position
          type: string
          required: true
      operationId: nfl-analysis.ff_prediction
      produces:
        - text/html
      responses: 
        "200":
          description: "FF data"
          schema:
            $ref: "#/definitions/NFL"
definitions:
  NFL:
    type: "string"
    properties: 
      model:
        type: "string"
```
