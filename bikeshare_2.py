import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    month = "all"
    day = "all"

    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nWhich city data to see? : Chicago, New York, or Washington: ').lower()
            if city  == 'chicago' or city == 'new york' or city == 'washington':
                break
            else:
                print('That\'s not a valid entry!')
        except :
            print('That\'s not a valid entry !')


    while True:
        try:
            filter = input('\nWould you like to filter by day or month? plz type day/month : ').lower()
            if filter  == 'day' or filter == 'month':
                break
            else:
                print('That\'s not a valid entry!')
        except :
            print('That\'s not a valid entry !')



    # get user input for month (all, january, february, ... , june)
    if filter  == 'day':
        while True:
            try:
                day = input('\nwhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all ?. plz type day name / all: ').lower()
                if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
                    break
                else:
                    print('That\'s not a valid entry!')
            except :
                print('That\'s not a valid entry !')
    else:
        while True:
            try:
                month = input('\nWhich month? January, february, march, april, may, June or all ?. Plz type month name / all: ').lower()
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
                    break
                else:
                    print('That\'s not a valid entry!')
            except :
                print('That\'s not a valid entry !')

    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    pop_month = df['month'].mode()[0]
    print('Most Common month is:', pop_month)

    # display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print('Most Common day is:', pop_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('Most common hour is:', pop_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', start_station)

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', end_station)
    # display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost Commonly used combination of start station and end station trip:', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time is: ', total_travel_time/3600, " hours")

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time is: ', average_travel_time/3600, " hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if city == 'chicago' or city == 'new york':
        # Display counts of gender
        user_gender = df['Gender'].value_counts()
        print(user_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_brth_yer = int(df['Birth Year'].min())
        most_recent_brth_yer = int(df['Birth Year'].max())
        most_common_brth_yer = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth is: ",earliest_brth_yer)
        print("most recent year of birth is: ",most_recent_brth_yer)
        print("nothe most common year of birth is: ",most_common_brth_yer)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    # to prevent colomuns from collapsing if the terminal window width is narrow
    #pd.set_option('display.max_columns',200) # to prevent

    while True:
        try:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
            if view_data.lower() == 'yes':
                print('\nPlz stretch the width of your window to accomodate all colomuns in one horizontal row\n')
                break
            else:
                return
        except :
            print('That\'s not a valid entry !')
    start_loc = 0
    while (view_data == 'yes' and start_loc <= (len(df.index)-5)):
        try:
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5
            view_data = input("\nDo you wish to continue viewing more rows?: ").lower()
        except :
            print('That\'s not a valid entry !')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
