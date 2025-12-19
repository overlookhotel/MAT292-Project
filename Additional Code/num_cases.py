#CDC data was provided as every case being an individual data points
#(e.g. not how many cases per day, just listing all cases and their dates)
#data sets were also extremely large and had to be downloaded in seperate batches
#files are too large to upload to github and only results were included
#but are available to download from CDC website here: 
# https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf/about_data

#this code counts number of each date from downloaded dataset
#and combines them into a form able to be used by the MATLAB code

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('20200301_20210616_dates_only.csv') #read csv
date_column = 'cdc_case_earliest_dt ' #column name want to select
date_counts = df[date_column].value_counts().sort_index() #sort by chosen column
date_counts.to_csv('cases_per_day_20200301_20210616.csv', header=['num_cases']) #same to new csv


#repeat for all other CSV files:

#1
df = pd.read_csv('20210616_20211231_dates_only.csv')
date_column = 'cdc_case_earliest_dt '
date_counts = df[date_column].value_counts().sort_index()
date_counts.to_csv('cases_per_day_20210616_20211231.csv', header=['num_cases'])

#2
df = pd.read_csv('20220101_20220630_dates_only.csv')
date_column = 'cdc_case_earliest_dt ' 
date_counts = df[date_column].value_counts().sort_index()
date_counts.to_csv('cases_per_day_20220101_20220630.csv', header=['num_cases'])

#3
df = pd.read_csv('20220701_20221231_dates_only.csv')
date_column = 'cdc_case_earliest_dt '
date_counts = df[date_column].value_counts().sort_index()
date_counts.to_csv('cases_per_day_20220701_20221231.csv', header=['num_cases'])


#4
df = pd.read_csv('20230101_20231231_dates_only.csv')
date_column = 'cdc_case_earliest_dt '  
date_counts = df[date_column].value_counts().sort_index()
date_counts.to_csv('cases_per_day_20230101_20231231.csv', header=['num_cases'])



#combine all csv files

# Read all CSV files
df1 = pd.read_csv('cases_per_day_20200301_20210616.csv')
df2 = pd.read_csv('cases_per_day_20210616_20211231.csv')
df3 = pd.read_csv('cases_per_day_20220101_20220630.csv')
df4 = pd.read_csv('cases_per_day_20220701_20221231.csv')
df5 = pd.read_csv('cases_per_day_20230101_20231231.csv')

# Combine all dataframes
combined_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# Save to new CSV
combined_df.to_csv('cases_per_day_2020_2023.csv', index=False)


#plot to check for correctness (does graph from CSV match actual daily number of cases graph)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cases_per_day_2020_2023.csv')

# print("Column names:", df.columns.tolist())

x_col = df.columns[0]  
y_col = df.columns[1]  

plt.figure(figsize=(10, 6))
plt.scatter(df[x_col], df[y_col], alpha=0.6)
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title(f'Scatter Plot: {y_col} vs {x_col}')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()