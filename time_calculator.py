# This function named add_time takes in two required parameters and one optional parameter:
# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive
# The function adds the duration time to the start time and returns the result.

def add_time(start, duration, day=None):  # sourcery no-metrics
    
    # split the inputs into individual useable characters 
    split_start_characters = list(start.split())
    split_time_characters = list(split_start_characters[0].split(":"))
    all_start_time_characters = [split_time_characters[0], split_time_characters[1], split_start_characters[1]]

    duration = list(duration.split(":"))
    duration_in_hours = int(duration[0])
    duration_in_minutes = int(duration[1])  

    # convert input start time into 24hr format
    if "PM" in all_start_time_characters:
        all_start_time_in_24hrs = [int(all_start_time_characters[0]) + 12, int(all_start_time_characters[1])]
    else:
        all_start_time_in_24hrs = all_start_time_characters = [int(split_time_characters[0]), int(split_time_characters[1])]

    # compute the new summed-up hours and minutes
    add_hours = all_start_time_in_24hrs[0] + duration_in_hours
    add_minutes = all_start_time_in_24hrs[1] + duration_in_minutes

    # initialise a set of variables for use later
    new_time_hour_in_24hr = 0
    new_time_minute = 0
    number_of_days_later = 0
    new_day = None

    # set hour, day and week facts ready for use later
    number_of_minutes_in_an_hour = 60
    number_of_hours_in_a_day = 24
    number_of_days_in_a_week = 7

    # seek number of hours in the summed-up minutes
    if add_minutes > number_of_minutes_in_an_hour:
        number_of_hours_in_the_summed_minutes = add_minutes // number_of_minutes_in_an_hour
        new_time_hour_in_24hr = add_hours + number_of_hours_in_the_summed_minutes

        number_of_minutes_in_the_summed_minutes = add_minutes % number_of_minutes_in_an_hour
        new_time_minute = number_of_minutes_in_the_summed_minutes

    else:
        new_time_hour_in_24hr = add_hours
        new_time_minute = add_minutes

    # seek number of days in the summed-up hours
    if new_time_hour_in_24hr > number_of_hours_in_a_day:
        number_of_days_in_the_summed_hours = new_time_hour_in_24hr // number_of_hours_in_a_day
        number_of_days_later = number_of_days_in_the_summed_hours

        number_of_hours_in_the_summed_hours = new_time_hour_in_24hr % number_of_hours_in_a_day
        new_time_hour_in_24hr = number_of_hours_in_the_summed_hours

    else:
        new_time_hour_in_24hr

    # re-arrange days of the week in a list format and let the list always start from the function argument (day), if given in the call
    if day is None:
        number_of_days_later

    else:
        # initialise set of variables for use later including the days of the week list 
        day_case_insensitive = day.capitalize()
        days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        days_of_the_week_rearranged = days_of_the_week.copy()
        current_day_index = days_of_the_week.index(day_case_insensitive)

        # move the given day argument to the begining of the week whilst making the other days follow subsequently
        for _ in range(len(days_of_the_week[:])):
            days_of_the_week_rearranged.insert(_, days_of_the_week_rearranged.pop(current_day_index))
            current_day_index += 1
            if current_day_index == 7:
                break

        # seek the new day from the re-arranged list of days. easier to deal with if the day parameter is at index 0 of the list
        if day_case_insensitive:
            if number_of_days_later <= 6:
                new_day = days_of_the_week_rearranged[days_of_the_week_rearranged.index(day_case_insensitive) + number_of_days_later]
            elif number_of_days_later > 6:
                number_of_weeks = number_of_days_later // number_of_days_in_a_week
                number_of_days_remaining_after_weeks = number_of_days_later % number_of_days_in_a_week
                if number_of_weeks != 0 and number_of_days_remaining_after_weeks <= 6:
                    new_day = days_of_the_week_rearranged[days_of_the_week_rearranged.index(day_case_insensitive) + number_of_days_remaining_after_weeks]
            else:
                number_of_days_later

    # convert the new hour time (obtained in 24hr time format) to a 12hr time format
    if new_time_hour_in_24hr > 12:
        new_time_hour = new_time_hour_in_24hr - 12
    elif new_time_hour_in_24hr == 0:
        new_time_hour = 12
    else:
        new_time_hour = new_time_hour_in_24hr
    
    # printing formats using all the possible combinations that can be given in the function call. if/elif/else statements to help
    if day != None:
        if number_of_days_later > 1:
            print_format = ", " + str(new_day) + " (" + str(number_of_days_later) + " days later)"
        elif number_of_days_later == 0 or number_of_days_later < 1:
            print_format = ", " + str(new_day)
        elif number_of_days_later == 1:
            print_format = ", " + str(new_day) + " (next day)"
        else:
            print_format = " (next day)"
    elif number_of_days_later == 1:
        if day is None:
            print_format =  " (next day)"
        else:
            print_format = " (next day)"
    elif day is None and new_day is None:
        if number_of_days_later == 0:
            print_format = ""
        else:    
            print_format = " (" + str(number_of_days_later) + " days later)"
    else:
        print_format = ""

    new_time = f"{new_time_hour}:{new_time_minute:02}{' PM' if (new_time_hour_in_24hr >= 12) else ' AM'}{print_format}"  

    return print(new_time)
    # return print(f"new time (unformatted) = {new_time_hour_in_24hr:02}:{new_time_minute:02}"+'\n'
    # f"new time (formatted) = {new_time_hour}:{new_time_minute:02}{' PM' if (new_time_hour_in_24hr >= 12) else ' AM'}"+'\n'
    # f"re-arranged days of the week = {'Null' if (day is None) else days_of_the_week_rearranged}"+'\n'
    # f"number of days elapsed = {number_of_days_later}"+'\n'
    # f"new day = {'Null' if (day is None) else new_day}"+'\n'
    # f"{new_time_hour}:{new_time_minute:02}{' PM' if (new_time_hour_in_24hr >= 12) else ' AM'}{print_format}")


###### WORKING TEST BENCH AREA ######
if __name__ == '__main__':
    add_time("8:16 PM", "466:02", "tuesday")
    # Returns: 6:18 AM, Monday (20 days later)

    add_time("2:59 AM", "24:00", "saturDay")
    # Returns: 2:59 AM, Sunday (next day)

    add_time("3:00 PM", "3:10")
    # Returns: 6:10 PM
    
    add_time("11:30 AM", "2:32", "Monday")
    # Returns: 2:02 PM, Monday
    
    add_time("11:43 AM", "00:20")
    # Returns: 12:03 PM
    
    add_time("10:10 PM", "3:30")
    # Returns: 1:40 AM (next day)
    
    add_time("11:43 PM", "24:20", "tueSday")
    # Returns: 12:03 AM, Thursday (2 days later)

    add_time("6:30 PM", "205:12")
    # Returns: 7:42 AM (9 days later)

    add_time("8:16 PM", "1199:02", "tuesday")

    add_time("10:30 AM", "39674:50", "WedNesDay")

    # return print(f"new time (unformatted) = {new_time_hour_in_24hr:02}:{new_time_minute:02}"+'\n'
    #     f"new time (formatted) = {new_time_hour}:{new_time_minute:02}{' PM' if (new_time_hour_in_24hr >= 12) else ' AM'}"+'\n'
    #     f"re-arranged days of the week = {'Null' if (day is None) else days_of_the_week_rearranged}"+'\n'
    #     f"number of days elapsed = {number_of_days_later}"+'\n'
    #     f"new day = {'Null' if (day is None) else new_day}"+'\n'
    #     f"{new_time_hour}:{new_time_minute:02}{' PM' if (new_time_hour_in_24hr >= 12) else ' AM'}{print_format}")

    add_time("5:32 PM", "67:50", "thursday")