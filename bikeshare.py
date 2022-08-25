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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chikago, New York, or Washington? ')
    while city.lower() not in ['chikago', 'new york', 'washington']:
        city = input('Invalid! choose correct one again please.. ')
    city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Would you like to filter the data for {} by what month? (all, january, february, ... , june)'.format(city))
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Invalid! choose correct one again please.. ')
    month = month.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Would you like to filter by what day? (all, monday, tuesday, ... sunday) '.format(city))
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Invalid! choose correct one again please.. ')
    day = day.lower()


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
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (pandas dataframe) df - the dataset to analyze  // df - Pandas DataFrame containing dataset to analyze
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    x = df['Start Time'].dt.month_name().mode()[0]
    print('The most commom month - of data you chose to analize - is {}'.format(x))

    # TO DO: display the most common day of week
    y = df['Start Time'].dt.day_name().mode()[0]
    print('The most commom day is {}'.format(y))

    # TO DO: display the most common start hour
    z = df['Start Time'].apply(lambda x: x.hour).mode()[0]
    print('The most commom start hour is {}'.format(z))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    Args:
        df - Pandas DataFrame containing dataset to analyze
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    a = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(a))

    # TO DO: display most commonly used end station
    b = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(b))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is from {} to {}'.format(a, b))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing dataset to analyze
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time = {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time = {}'.format(df['Trip Duration'].mean()))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.

    Args:
        df - Pandas DataFrame containing dataset to analyze
        (str) city - name of the city to analyze
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('There are {} types of users, their counts:'.format(df['User Type'].nunique()))
    print(df['User Type'].value_counts())

    if city != 'washington':
        # TO DO: Display counts of gender
        print('counts of gender:')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth of users is {}'.format(int(df['Birth Year'].min())))
        print('And the most recent year of birth of them is {}'.format(int(df['Birth Year'].max())))
        print('Most common year of birth is {}'.format(int(df['Birth Year'].mean())))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        i = 0
        while True:
            restart = input('\nWould you like to display 5 rows of the data to explore? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
            print(df.iloc[i:i+5])
            i += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
