# Data-Analysis-Proj--Explore-US-Bike-Share-Data
The code imports the data from the cities bikeshare data files ( chicago, new york, washington), and using interactive command lines, it prompts the user to choose what data to filter and what stats to calculate, then perform some descriptive data analysis based on user choices and print back the stats. it can also display snippets of the csv files if the user wants.

This projects is part of Udacity Data analysis Nano degree

## Project Details
Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

## The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

    Start Time (e.g., 2017-01-01 00:07:57)
    End Time (e.g., 2017-01-01 00:20:53)
    Trip Duration (in seconds - e.g., 776)
    Start Station (e.g., Broadway & Barry Ave)
    End Station (e.g., Sedgwick St & North Ave)
    User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

    Gender
    Birth Year
![Data for the first 10 rides in the new_york_city.csv file
Close](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)[Data for the first 10 rides in the new_york_city.csv file
Close]


## Statistics Computed

1. Popular times of travel (i.e., occurs most often in the start time)

   - most common month
   - most common day of week
   - most common hour of day

2. Popular stations and trip

   - most common start station
   - most common end station
   - most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

   - total travel time
   - average travel time

4. User info

   - counts of each user type
   - counts of each gender (only available for NYC and Chicago)
   - earliest, most recent, most common year of birth (only available for NYC and Chicago)




## Software Needs
- You should have Python 3, NumPy, and pandas installed using Anaconda.
- A text editor, like Sublime or Atom.
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).


## Udacity data analyst Bikeshare data
This project explores Bike share data from 3 differents cities; it uses data from csv files to compute staticts from those 3 cities, also takes user inputs to create an interactive experience.

## Built with
- Python
- Pandas
- Numpy
- atom
- Git Bash

## Files used
- chicago.csv
- new_york_city.csv
- washington.csv

