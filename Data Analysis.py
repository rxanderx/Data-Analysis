from re import S
from tkinter import N
import numpy as np
import pandas as pd
# installing the required libraries for concise data analysis


# This code will use numpy and pandas libraries to analyze the data of daily coffee prices within the past 20 years
# using pandas to read and call the csv file
df = pd.read_csv("coffee.csv")

# the important functions for the questions I want to answer will be the usecols() argument :    , #usecols= ["Volume"]
# by using usecols(["name of columns I want here"]) I can get the important object columns from within

# by using .describe() I can retrieve the mean, sd, minimum value, maximum value, and each percentile column
# print(df.describe())

#print(df["Volume"].value_counts())
#print(df[df["Volume"]==0].describe())
print(df["Low"].mean())
uinput = input("|| Welcome! Before we get started- would you like to apply a filter to the data? (Date,Volume,No)\n")
if uinput.upper() == "DATE":
    date_lower = input("|| Understood, please enter the date for the bottom of the range (YYYY-MM-DD)\n")
    df_lower = df["Date"] > date_lower
    date_higher = input("|| Thank you, please enter the date for the top of the range (YYYY-MM-DD)\n")
    df_higher = df["Date"] < date_higher

    print(f"|| Got it! We'll be using the dataset with dates ranging from {date_lower} to {date_higher}")
    df = df[df_lower & df_higher]

elif uinput.upper() == "Volume":
    volume_lower = input("|| Understood, please enter the volume for the bottom of the range \n")
    df_lower = df["Date"] > volume_lower
    volume_higher = input("|| Thank you, please enter the volume for the top of the range \n")
    df_higher = df["Date"] < volume_higher

    print(f"|| Got it! We'll be using the dataset with volumes between {volume_lower} and {volume_higher}")
    df = df[df_lower & df_higher]


uinput = input("|| Is there any variable within the dataset you want to analyze? (Yes/No)\n")
if uinput.upper() == "YES":

    uinput = input("|| What variable would you like to analyze? (High, Close, Volume)\n")
    if uinput.upper() == "HIGH":
        #heres the higher command
        print(f"|| Calculations for the High price point per day in the dataset: \n\
        || The maximum value for daily Highs within the dataset is:")
        print(df["High"].max())
        print(f"|| The minimum value for daily Highs within the dataset is:")
        print(df["High"].min())
        print(f"|| The average value for daily Highs within the dataset is:")
        print(df["High"].mean())

    elif uinput.upper() == "CLOSE":
        #heres the close command
        print(f"|| Calculations for the Closing price point per day in the dataset: \n\
        || The maximum value of daily closing prices within the dataset is:")
        print(df["Close"].max())
        print(f"|| The minimum value for daily closing prices within the dataset is:")
        print(df["Close"].min())
        print(f"|| The average value for daily closing prices within the dataset is:")
        print(df["Close"].mean())

    elif uinput.upper() == "VOLUME":
        #heres the volume command
        print(f"|| Calculations for the Volume of Coffee sold per day (in tons) in the dataset: \n\
        || The maximum volume per day within the dataset is:")
        print(df["Volume"].max())
        print(f"|| The minimum volume per day within the dataset is:")
        print(df["Volume"].min())
        print(f"|| The average volume per day within the dataset is:")
        print(df["Volume"].mean())

    else:
        print("|| Unrecognized input.")
elif uinput.upper() == "NO":
    print("|| Understood- Here is a general overview of the dataset!\n")
    print(df.describe())