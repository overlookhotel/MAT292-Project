# MAT292 Project - Modelling the spread of COVID-19
This project was coded on MATLAB. The purpose of this project is to code and then evaluate the ability of the SIRU and SEIQR models to predict the behaviour of the pandemic in the US. The insights gained from this analysis is used to then inform the creation of our own model, would better account for government interventions through social isolation and vaccinations to better predict the pandemic's behaviour. 

## The Files
Each .mlx file functions independently of the other files. 

### The Data Files
**cases_per_day_2020_2023.csv** [CDC] \
**cleaned_both_vaccinations.csv** [CDC] 

### The Code Files
**SEIQR_final.mlx** ― This file is used to solve SEIQR and evaluate the MAE of the SEIQR model \
**SIRU_final.mlx** ― This file is used to solve SIRU and evaluate the MAE of the SIRU model \
**final_model.mlx** ― This is the code for our model
**daily_vaccinations.py** - Process daily vaccinations to make the date usable by MATLAB
**num_cases.py** - Process the data to convert from unique cases into number of cases per day


## Running the Code Files
1. Either: Create a folder named "MAT292" in MATLAB Drive and input all the files into there \
   Or    : Download the files and change the directories in each .mlx file correspondingly \
   (Ensure that file path at top of document matches currect directory!!)
2. Run the each of the files, which will produce the discussed figures and values



