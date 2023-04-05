# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:25:35 2023

@author: Shreya Thekkiniyedath Kudalvalli
"""

# importing requiredpackages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    """
    Read the file from the local directory and load it into a dataframe.
    Then transpose the dataframe and returns both the dataframes. It 
    Also, set the header for the transposed dataframe.
    
    Parameters
    ----------
    file_name : string
        Name of the file tobe read into the datarame.
    Returns
    -------
    A dataframe loaded from the file and it's transpose.
    
    """

    
    address = "C:\\Users\\user\\OneDrive\\ASD1 Assignment 2\\" + file_name
    df = pd.read_excel(address)
    df_transpose = pd.DataFrame.transpose(df)
    # Header setting
    header = df_transpose.iloc[0].values.tolist()
    df_transpose.columns = header
    return(df, df_transpose)


def clean_df(df):
    """
    Clean the dataframe to get only the required columns and convert 
    index as int.
    
    Parameters
    ----------
    df : dataframe
        Dataframe that needs to be cleaned and index converted.
        
    Returns
    -------
    df : dataframe
        dataframe with required columns and index as int.
        
    """

   
    # Cleaning the dataframe
    df = df.iloc[1:]
    df = df.iloc[11:55]
    
    # Converting index ot int
    df.index = df.index.astype(int)
    df = df[df.index > 1989]

    # Cleaning empty cells
    df = df.dropna(axis = 'columns')
    return df


# Read the files
df_fertility_total, df_fertility_countries = read_file("Fertility.xls")
df_mortality_total, df_mortality_countries = read_file("Mortality.xls")
df_staff_total, df_staff_countries = read_file("Births.xls")
df_anemia_total, df_anemia_countries = read_file("Anemia.xls")
df_under_total, df_under_countries = read_file("Undernourishment.xls")

# Create a list of countries and years to use in the plots
countries =['Bangladesh',
            'China',
            'Germany', 
            'France',  
            'United Kingdom',
            'India',
            'Kenya', 
            'Saudi Arabia',
            'United States'
            ]
countries_label =['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US']
years = [1990, 1994, 1998, 2002, 2006, 2010, 2014]


"""

Adolescent Fertility Rate Bar graph
Creating a bar graph of Adolescent Fertility Rate
(births per 1,000 women ages 15-19) of mutiple countries
from 1990-2014

"""

# Clean the dataframe
df_fertility_countries = clean_df(df_fertility_countries)

# select only the required data
df_fertility_time = pd.DataFrame.transpose(df_fertility_countries)
df_fertility_subset_time = df_fertility_time[years].copy()
df_fertility_subset_time = df_fertility_subset_time.loc[df_fertility_subset_time.index.isin(countries)]


# plotting the data
n = len(countries)
r =np.arange(n)
width = 0.1
plt.bar(r-0.3, 
        df_fertility_subset_time[1990],
        color = 'tomato',
        width = width,
        edgecolor = 'black',
        label='1990'
        )
plt.bar(r-0.2,
        df_fertility_subset_time[1994],
        color = 'cadetblue',
        width = width,
        edgecolor = 'black',
        label='1994'
        )         
plt.bar(r-0.1, 
        df_fertility_subset_time[1998], 
        color = 'limegreen',
        width = width, 
        edgecolor = 'black',
        label='1998'
        )         
plt.bar(r,
        df_fertility_subset_time[2002],
        color = 'purple',
        width = width,
        edgecolor = 'black',
        label='2002'
        )         
plt.bar(r+0.1, 
        df_fertility_subset_time[2006],
        color = 'plum',
        width = width,
        edgecolor = 'black',
        label='2006'
        )
plt.bar(r+0.2, 
        df_fertility_subset_time[2010],
        color = 'palevioletred',
        width = width,
        edgecolor = 'black',
        label='2010'
        )
plt.bar(r+0.3, 
        df_fertility_subset_time[2014],
        color = 'darkorchid',
        width = width,
        edgecolor = 'black',
        label='2014')

plt.xlabel("Countries", fontsize = 12)
plt.ylabel("Number of births", fontsize = 12)
plt.xticks(width+r, countries_label)
plt.legend()
plt.title("Adolescent Fertility Rate (births per 1,000 women aged 15-19)")
plt.savefig("Adolescent.png", dpi=300, bbox_inches='tight')


# Calculate the mean, median and mode
fertility_rate_mean = df_fertility_subset_time.mean()
fertility_rate_median = df_fertility_subset_time.median()
fertility_rate_mode = df_fertility_subset_time.mode()

print("Mean of Adolescent Fertility Rate:\n", fertility_rate_mean)
print("Median of Adolescent Fertility Rate:\n", fertility_rate_median)
print("Mode of Adolescent Fertility Rate:\n", fertility_rate_mode)

# Generate Descriptive Statistics using describe() method.
df_fertility_describe = df_fertility_subset_time.describe()
print(df_fertility_describe)

# Display the plot
plt.show()


"""
Neonatal Mortality Rate Bar graph
Creating a bar chart of Neonatal Mortality Rate(per 1,000 live births) 
of multiple countries during 1990-2014
"""

# Cleaning the dataframe
df_mortality_countries = clean_df(df_mortality_countries)

# selecting only required data
df_mortality_time = pd.DataFrame.transpose(df_mortality_countries)
df_mortality_subset_time = df_mortality_time[years].copy()
df_mortality_subset_time = df_mortality_subset_time.loc[df_mortality_subset_time.index.isin(countries)]


# plotting the data
plt.bar(r-0.3, 
        df_mortality_subset_time[1990],
        color = 'teal',
        width = width,
        edgecolor = 'black',
        label='1990'
        )
plt.bar(r-0.2,
        df_mortality_subset_time[1994],
        color = 'pink',
        width = width,
        edgecolor = 'black',
        label='1994'
        )
plt.bar(r-0.1,
        df_mortality_subset_time[1998],
        color = 'thistle',
        width = width,
        edgecolor = 'black',
        label='1998'
        )
plt.bar(r,
        df_mortality_subset_time[2002], 
        color = 'steelblue',
        width = width, 
        edgecolor = 'black', 
        label='2002'
        )
plt.bar(r+0.1,
        df_mortality_subset_time[2006], 
        color = 'tan',
        width = width, 
        edgecolor = 'black', 
        label='2006'
        )
plt.bar(r+0.2, 
        df_mortality_subset_time[2010], 
        color = 'violet',
        width = width, 
        edgecolor = 'black',
        label='2010'
        )
plt.bar(r+0.3,
        df_mortality_subset_time[2014], 
        color = 'mediumpurple',
        width = width, 
        edgecolor = 'black',
        label='2014'
        )

plt.xlabel("Countries",fontsize = 12)
plt.ylabel("percentage of mortality",fontsize = 12)
plt.xticks(width+r, countries_label)
plt.legend()
plt.title("Neonatal Mortality Rate (per 1,000 live births)")
plt.savefig("Neonatal.png", dpi=300, bbox_inches='tight')
plt.show()


"""
skilled health staff bar graph
Creates a bar chart of the percentage of total births attended by
skilled health staff in multiple countries during 1990-2014.

"""

#Cleaning the dataframe
df_staff_countries = clean_df(df_staff_countries)

#selecting only required data
df_staff_time = pd.DataFrame.transpose(df_staff_countries)
df_staff_subset_time = df_staff_time[years].copy()
df_staff_subset_time = df_staff_subset_time.loc[df_staff_subset_time.index.isin(countries)]


#plotting the data
plt.bar(r-0.3, 
        df_staff_subset_time[1990], 
        color = 'thistle',
        width = width,
        edgecolor = 'black',
        label='1990'
)
plt.bar(r-0.2,
        df_staff_subset_time[1994], 
        color = 'palevioletred',
        width = width,
        edgecolor = 'black', 
        label='1994'
)
plt.bar(r-0.1, 
        df_staff_subset_time[1998],
        color = 'steelblue',
        width = width, 
        edgecolor = 'black',
        label='1998'
)
plt.bar(r, 
        df_staff_subset_time[2002],
        color = 'pink',
        width = width, 
        edgecolor = 'black',
        label='2002'
)
plt.bar(r+0.1,
        df_staff_subset_time[2006], 
        color = 'lightseagreen',
        width = width,
        edgecolor = 'black',
        label='2006'
)
plt.bar(r+0.2, 
        df_staff_subset_time[2010],
        color = 'purple',
        width = width,
        edgecolor = 'black',
        label='2010'
)
plt.bar(r+0.3,
        df_staff_subset_time[2014],
        color = 'wheat',
        width = width, 
        edgecolor = 'black',
        label='2014'
)

plt.xlabel("Countries", fontsize = 12)
plt.ylabel("Births attended", fontsize = 12)
plt.xticks(width+r, countries_label)
plt.legend()
plt.title("Births attended by skilled health staff(% of total)")
plt.savefig("Staff.png", dpi=300, bbox_inches='tight')
plt.show()


"""
Lineplot - prevalence of Anemia
Creates a lineplot of the prevalence of Anemia among pregnant women
in multiple countries during 1990-2014.
Used mean to fill empty cells of Israel.

"""

#Cleaning the dataframe
#Clean function is not used here because it will remove entirety of Israel column

df_anemia_countries = df_anemia_countries.iloc[1:]
df_anemia_countries = df_anemia_countries.iloc[11:55]

df_anemia_countries.index = df_anemia_countries.index.astype(int)
df_anemia_countries = df_anemia_countries[df_anemia_countries.index > 1990]

#using mean() function of pandas to fill empty cells of Israel
df_anemia_countries["Israel"] = df_anemia_countries["Israel"].interpolate(method='nearest', axis=0).ffill().bfill()

#plotting the data
plt.figure()
plt.plot(df_anemia_countries.index, df_anemia_countries["Bangladesh"])
plt.plot(df_anemia_countries.index, df_anemia_countries["China"] )
plt.plot(df_anemia_countries.index, df_anemia_countries["Germany"])
plt.plot(df_anemia_countries.index, df_anemia_countries["France"])
plt.plot(df_anemia_countries.index, df_anemia_countries["United Kingdom"])
plt.plot(df_anemia_countries.index, df_anemia_countries["India"])
plt.plot(df_anemia_countries.index, df_anemia_countries["Kenya"])
plt.plot(df_anemia_countries.index, df_anemia_countries["Saudi Arabia"])
plt.plot(df_anemia_countries.index, df_anemia_countries["United States"])
plt.plot(df_anemia_countries.index, df_anemia_countries["Israel"])
plt.xlim(1991,2014)
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Number of pregnant women", fontsize = 12)
plt.legend(['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US', 'IL'],
            prop = {'size': 8}
)
plt.title(" Prevalence of Anemia among pregnant women")
plt.savefig("Anemia.png", dpi = 300, bbox_inches='tight')
plt.show()



"""
Lineplot- prevalence of undernourishment
Creates a lineplot of the prevalence of undernourishment among
pregnant women in multiple countries during 1990-2014.
 
"""

# Cleaning the dataframe
# Clean function is not used here because it will remove entirety of Israel 
df_under_countries = df_under_countries.iloc[1:]
df_under_countries = df_under_countries.iloc[11:55]

df_under_countries.index = df_under_countries.index.astype(int)
df_under_countries = df_under_countries[df_under_countries.index > 1990]



#using mean() function of pandas to fill empty cells of Israel
df_under_countries["Israel"] = df_under_countries["Israel"].interpolate(method='nearest', axis=0).ffill().bfill()


#plotting the data
plt.figure()
plt.plot(df_under_countries.index, df_under_countries["Bangladesh"])
plt.plot(df_under_countries.index, df_under_countries["China"])
plt.plot(df_under_countries.index, df_under_countries["Germany"])
plt.plot(df_under_countries.index, df_under_countries["France"])
plt.plot(df_under_countries.index, df_under_countries["United Kingdom"])
plt.plot(df_under_countries.index, df_under_countries["India"])
plt.plot(df_under_countries.index, df_under_countries["Kenya"])
plt.plot(df_under_countries.index, df_under_countries["Saudi Arabia"])
plt.plot(df_under_countries.index, df_under_countries["United States"])
plt.plot(df_under_countries.index, df_under_countries["Israel"])



plt.xlim(1991, 2014)
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Population", fontsize = 12)
plt.legend(['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US', 'IL'], prop = {'size': 8})

plt.title(" Prevalence of Undernourishment( % of population)")
plt.savefig("Undernourishment.png", dpi = 300, bbox_inches='tight')
plt.show()








