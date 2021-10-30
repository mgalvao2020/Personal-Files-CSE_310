# Overview

"""As a software engineer to further my learning I am trying to work on reading files,
extrac data to work on, calculate things and display results.

Description of the software:
This software will read a database and calculate averages of temperature
I will also to display a graph in a GUI

The purpose of this software is to prepare the way ahead for a prediction software
that will be applied on potato farms



[Software Demo Video](https://youtu.be/79TAMNijtOE)

# Development Environment

Tools and library used: "try / except", math functions, and I used the following libraries: pandas, matplotlib, math


# Useful Websites

* [W3 Schools](https://www.w3schools.com/python/)
* [Python.org](https://wiki.python.org/moin/BeginnersGuide)

# Future Work


* Item 1: Improve the GUI to show the average
* Item 2: Improve the explanation on the video
* Item 3: Fix the output of the average in the user range
""""


import pandas as pd
import matplotlib.pyplot as pyplot
import math



def main():
    try:
        # Read the ProdxYear.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv("potato_prodXyear.csv", parse_dates=["year"])
       
        print(df.dtypes)

        sum_prod(df)
        sum_low_ave(df)
        calc_pearson(df)
        #average_low_temp(df)
       
        #df.plot(kind="bar", x="year", y="production_in_cwt")
        df.plot(kind="scatter", x="low_ave", y="production_in_cwt")
        # Draw and show all production x year plots.
        pyplot.show()
    
        # Receive the input from user: 
        # start and the end year to be analyzed 
        start_year = input("Enter the start year (1990 - 2019): ")
        end_year = input("Enter the end year (1991 - 2020): ")
        

    except RuntimeError as run_err:
        print(type(run_err).__name__, run_err, sep= ": ")

def sum_prod(df):
    total_prod = df["production_in_cwt"].sum()
    print("Total production from 1990 - 2020 is: ", total_prod)
    print("Average production is", round(total_prod / 30, 1))

def sum_low_ave(df):
    total_low_ave = df["low_ave"].sum()
    #return total_low_ave
    print("Total of the average low temperature (1990 - 2020) is: ", total_low_ave)
    print("The average of the Low temperature is: ", round(total_low_ave / 30, 1))


def calc_pearson(df):
    # This function will calculate the Pearson coefficient 
    r = 0
    xi = pd.read_csv("potato_prodXyear.csv", parse_dates=["low_ave"])
    yi = pd.read_csv("potato_prodXyear.csv", parse_dates=["production_in_cwt"])
    total_low_ave = df["low_ave"].sum()
    total_prod = df["production_in_cwt"].sum()
    x_ave = float(total_low_ave) / 30
    y_ave = float(total_prod) / 30
    #numerator = (xi - float(x_ave)) * (yi - float(y_ave)) 
    #denominator = math.sqrt(((xi - x_ave) ** 2) * ((yi - y_ave) ** 2)) 
    #r = numerator / denominator
    #print("Pearson coefficient is: ", r)


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()



