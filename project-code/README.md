
# Fantasy Football Point Predictor - Tutorial
---
#### 1) Clone Repository into Local Directory
```
$ git clone https://github.com/cloudmesh-community/sp19-222-90.git 
```
#### 2) Enter Project-Code Directory
```
$ cd sp19 cd sp19-222-90/project-code/
```

#### 3) Build and Run Docker Container and Start Service
```
$ make docker-all
```

#### 4) Open Server in Browser
```
https://localhost:8080/cloudmesh/nfl-analysis/v1/home
```

### 5) View Predictions by Postion
* Postion options are QB, TE, RB, WR, and ALL
```
https://localhost:8080/cloudmesh/nfl-analysis/v1/results/QB
https://localhost:8080/cloudmesh/nfl-analysis/v1/results/TE
https://localhost:8080/cloudmesh/nfl-analysis/v1/results/RB
https://localhost:8080/cloudmesh/nfl-analysis/v1/results/WR
https://localhost:8080/cloudmesh/nfl-analysis/v1/results/ALL
```
