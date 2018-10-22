import pandas as pd

import datetime as dt

import time
import numpy as np
from scipy.stats import mode





CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = { 'january', 'february', 'march', 'april', 'may', 'june', 'all' }

DAY_DATA = { 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all' }



########################  Applying Filters ###################################################################
def get_filters():
 

          print('Hello! Let\'s explore some US bikeshare data!')
          print('-'*45)
          
          city=input("Please enter a city:")
          
          while city.lower() not in CITY_DATA: 
              city=input("Please enter valid city from chicago, washington, new york city \n") 
          
         
          month=input("Please enter valid month: ") 

          while month.lower() not in MONTH_DATA: 
              month=input("Please enter valid month from 'january', 'february', 'march', 'april', 'may', 'june', 'all' \n") 
          
          day=input("Please enter a day:" )
          while day.lower() not in DAY_DATA: 
              day=input("Please enter valid day from 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all' \n")

          print('Please wait while calculating statistics:.................')
          
          return city.lower(), month.lower(), day.lower()


######################### Loading Data ##########################################################################


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
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    
    data=input('\nWould you like to see the filter data? Enter yes or no.\n')
    if data.lower() == 'yes':
           print(df)
    else:
           print('Ok...')

    return df
    
######################  time_stats ########################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # popular_month = df['month'].mode()[0]
    popular_month=df.loc[:,"month"].mode()[0]
    print('Most Popular Start month:', popular_month)


    # TO DO: display the most common start hour
    # popular_hour = df['hour'].mode()[0]
    popular_hour=df.loc[:,"hour"].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    # TO DO: display the most common day of week
    # popular_day = df['day_of_week'].mode()[0]
    popular_day=df.loc[:,"day_of_week"].mode()[0]
    print('Most Popular Start day:', popular_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

########################### station_stats ################################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
   
    start_station=df.groupby(['Start Station']).size().sort_values(ascending=False).head(1)
   
    print (' Most Popular Start station Total Count:\n', start_station)
    


    # TO DO: display most commonly used end station

    end_station=df.groupby(['End Station']).size().sort_values(ascending=False).head(1)
    
    print(' Most Popular End station Total Count:\n', end_station)



    # TO DO: display most frequent combination of start station and end station trip
    
    
    
    count = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1)
    print("Frequent combination of start station and end station count\n", count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

################ trip_duration_stats ###############################################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total=df['Trip Duration'].sum()
    print("Total Travel Time: " , total)

    # TO DO: display mean travel time
    mean=df['Trip Duration'].mean()
    print("Average Travel Time:" , mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

####################### user_stats #######################################################

def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types= df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city.lower()=='washington':
         print("Gender is not available for washington")
    else:
         gender=df['Gender'].value_counts()
         print(gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    
    if city.lower()=='washington':
         print("Earliest, recent, common birth year is not available for washington")
    else:
         early=df['Birth Year'].min()
         print("Earliest Birth Year:", early)
 
    
         recent=df['Birth Year'].max()
         print("Most Recent Year:", recent)

   
         common=df['Birth Year'].mode()[0]
         print("Common Birth Year:", common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


################## MAIN ######################################################

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



