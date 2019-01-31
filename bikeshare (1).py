
# coding: utf-8

# In[5]:


'''
Sources
https://github.com/philribbens/udacity-bikeshare-project/blob/master/bikeshare.py
Quora
https://github.com/scientificharsha/Udacity-DA_Nanodegree--US-BikeShare/blob/master/bikeshare.py
Stack Overflow
pandas.pydata.org
(Pandas Documentation)
'''
import pandas as pd
import numpy as np
import calendar
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(file_name):
    # load data file into a dataframe
    df = pd.read_csv(file_name)
    return df

def input_city():
    city=input("Please enter city whose bikeshare data is to be viewed (chicago or new york city or washington) : ")
    return city_check(city)
    
def city_check(city):
    if(city in CITY_DATA):
        return CITY_DATA[city]
    else:
        print("Invalid city. Please enter again.")
        input_city()
def start_date_time(df):
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['start_hour']=df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

def get_filter():
    
    #asks the user for a filter and and then asks for the corresponding time choice
    
    #args: none
    #return: list having a returnable function as an element
    
    filter1=input("Would you like to filter by month or day or not at all? Write \"none\" for no filter. : ").lower()
    if(filter1=='month'):
        return [filter1, get_month()]
    elif(filter1=='day'):
        return [filter1, get_day()]
    elif(filter1=='none'):
        return [filter1,'No filter']
    else:
        print("Invalid input. Please enter again.")
        return get_filter()
def get_month():
    month=input("Input a month-Jan, Feb, Mar, Apr, May, Jun? : ")
    if(month=='Jan'):
        return 1
    elif(month=='Feb'):
        return 2
    elif(month=='Mar'):
        return 3
    elif(month=='Apr'):
        return 4
    elif(month=='May'):
        return 5
    elif(month=="Jun"):
        return 6
    else:
        print("Invalid input. Please enter again.")
        return get_month
def get_day():
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day=input("Enter a day-'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday' : \n")
    if(day in days):
        return day
    else:
        print("Invalid input. Please enter again.")
        return get_day()
def pop_mon(df):
    
    #Finds the most popular month for bikesharing according to filters
    
    #args: pandas dataframe
    #return: string
    
    trips_monthly=df.groupby('month')['Start Time'].count()
    return "Most popular month is {}".format(calendar.month_name[trips_monthly.sort_values(ascending=False).index[0]])

def pop_day(df):
    trips_daily=df.groupby('day_of_week')['Start Time'].count()
    return "Most popular day is {}".format(trips_daily.sort_values(ascending=False).index[0])

def pop_hour(df):
    trips_hourly = df.groupby('start_hour')['Start Time'].count()
    return "Most Popular Hour is : {}".format(trips_hourly.sort_values(ascending=False).index[0])

def trip_duration(df):
    
    #Finds the total and mean trip duration
    
    #args: pandas dataframe
    #return: list
    total_duration=df['Trip Duration'].sum()
    mean_duration=df['Trip Duration'].mean()
    mins, secs = divmod(total_duration, 60)
    hrs, mins = divmod(mins, 60)
    days, hrs = divmod(hrs, 24)
    yrs, days = divmod(days, 365)
    total_trip_duration = "\nTotal trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (yrs, days, hrs, mins, secs)
    mins, seconds = divmod(mean_duration, 60)
    hrs, mins = divmod(mins, 60)
    avg_trip_duration = "Average trip duration: %d hrs %02d min %02d sec" % (hrs, mins, secs)
    return [total_trip_duration, avg_trip_duration]

def pop_stat(df):
    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    most_popular_start_station = "\nMost popular start station: " + sorted_start_stations.index[0] + " (" + str(sorted_start_stations[0]) + " trips) "
    most_popular_end_station = "Most popular end station: " + sorted_end_stations.index[0] + " (" + str(sorted_end_stations[0]) + " trips) " 
    return [most_popular_start_station, most_popular_end_station]

def pop_trip(df):
    most_pop_trip = df['journey'].mode().to_string(index = False)
    return ('The most popular trip is {}.'.format(most_pop_trip))

                                                                                           
def users(df):
    
    #Finds no. of customers of each user type
    
    #args: pandas dataframe
    #return: pandas Series
    
    user_type = df.groupby('User Type')['User Type'].count()
    return user_type

def gender(df):
    gender_counts = df.groupby('Gender')['Gender'].count()
    return gender_counts
                                
def birth_years(df):
    earliest_birth_year = "Earliest birth year: " + str(int(df['Birth Year'].min()))
    most_recent_birth_year = "Most recent birth year: " + str(int(df['Birth Year'].max()))
    birth_year_counts = df.groupby('Birth Year')['Birth Year'].count()
    sorted_birth_years = birth_year_counts.sort_values(ascending=False)
    most_common_birth_year = "Most common birth year: " + str(int(sorted_birth_years.index[0])) + " (" + str(sorted_birth_years.iloc[0]) + " trips) " 
    return [earliest_birth_year, most_recent_birth_year, most_common_birth_year]
    
def display_data(df, N):
    
    #displays five lines of dataframe if the user says yes. Then prompts the user again.
    #if user says no, stops printing.
    
    #args: dataframe, integer index to start from
    #return: pandas dataframe with only five entries
    
    inp=input("Do you wanna see individual data? \'yes\' or \'no\'? \n").lower()
    if(inp=='yes'):
        print(df.iloc[N:N+5])
        N+=5
        return display_data(df, N)
    if inp == 'no':
        return 
    else:
        print("\nInvalid input. Please enter again")
        return display_data(df, N)
    
def ask_restart():
    inp=input("\nDo you want to restart? : ").lower()
    if (inp=='yes'):
        main()
    elif(inp=='no'):
        return
    else:
        print("Invalid input. Please enter again.")
        return ask_restart()

def main():
    #filter by city
    city=input_city()
    df=load_data(city)
    df['journey'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    start_date_time(df)
    df_filter=get_filter()
    df_filter1=df_filter[0]
    df_filter_value=df_filter[1]
    df_filter_heading='No filter'
    
    if(df_filter1=='month'):
        filtered_df=df.loc[df['month']==df_filter_value]
        df_filter_heading=calendar.month_name[df_filter_value].upper()
    elif(df_filter1=='day'):
        filtered_df=df.loc[df['day_of_week']==df_filter_value]
        df_filter_heading=df_filter_value.upper()
    elif(df_filter1=='none'):
        filtered_df=df
    print("\n")
    print(city[:-4].replace("_"," ").upper()+" -- "+ df_filter_heading)
    print("-----------------------------------")
    print("Total trips : {}".format(filtered_df['Start Time'].count()))
    if (df_filter1!="month"):
        print(pop_mon(filtered_df))
    if(df_filter1!="day"):
        print(pop_day(filtered_df))
    print(pop_hour(filtered_df))
    trip_duration_stats = trip_duration(filtered_df)
    print(trip_duration_stats[0])
    print(trip_duration_stats[1])
    popular_stations = pop_stat(filtered_df)
    print(popular_stations[0])
    print(popular_stations[1])
    print(pop_trip(filtered_df))
    print("\n")
    print(users(filtered_df))                                                                                       
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print('\n')
        print(gender(filtered_df))
        birth_years_data = birth_years(filtered_df)
        print('\n')
        print(birth_years_data[0])
        print(birth_years_data[1])
        print(birth_years_data[2])
    display_data(filtered_df, 0)
    ask_restart()
    
if(__name__=='__main__'):
    main()

