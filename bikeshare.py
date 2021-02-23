import time
import pandas as pd
import numpy as np

print("Starting the Project....")
print("this part is used in the third Project of the course....")

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    print("\nWelcome to this program. Please choose your city:")
    print("\n1. Chicago 2. New York City 3. Washington")
    city = input().lower()
    while city not in CITY_DATA.keys() :
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nPlease check your input")
            print("\nRestarting...")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                                    'may': 5, 'june':6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month, between January to June, for which you're    seeking the data:")
        print("\n(You may also opt to view data for all months, please type 'all' or 'All' or 'ALL' for that.)")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. Please try again in the accepted input format.")
            print("\nRestarting...")


    #Creating a list to store all the days including the 'all' option
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',                                                                          'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
        day = input().lower()

        if day not in DAY_LIST:
            print("\nInvalid input. Please try again in one of the accepted input formats.")
            print("\nRestarting...")

    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")

   
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
    df = pd.read_csv(CITY_DATA[city])
    
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['week'].mode()[0]
    print('Most Popular Weekday:', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.week
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most common start station is : ",start_station)
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most common end station is : ",end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Stations'] = df['Start Station']+' '+df['End Station'] 
    combined = df['Combined Stations'].mode()[0]
    print("The most common Combined stations is : ",combined)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time = ',df['Trip Duration'].sum(),' hours')

    # TO DO: display mean travel time
    print('Mean of travel time = ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("No data available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The oldest year is :',df['Birth Year'].min())
        print('The smallest year is :',df['Birth Year'].max())
        print('The most common year is :',df['Birth Year'].mode()[0])
    else:
        print("No data available for this city")
           
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    start_time = time.time()
    sample = input("Do you want to see a sample of the data? (yes or no) ")
    start_loc = 0
    while sample == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        sample = input("Do you wish to continue?: ").lower()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
