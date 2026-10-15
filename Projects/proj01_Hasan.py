#Program : proj01_hasan.py
#Name :  Md Mridul Hasan
#Convert the distance in chains to several other units of distance, and then calculate the walking time needed to cover this distance by assuming a average walking speed of 3.1 miles per hour.


def main():

    distance_in_chains= float(input("Welcome to the NYC Subway distance converter!"
         "\n" #used "\n " for a blank line, and to break the lines
         "\n" 
         "Enter the distance in Chains: "))

     #store the conversion constant of units
    feet_per_chain= 66 
    meters_per_foot= 0.3048
    feet_per_mile= 5280
    meters_per_kilometer= 1000
       #should be unchanged

     #convert input into other units  
    distance_in_feet= distance_in_chains* feet_per_chain
    distance_in_meter= distance_in_feet * meters_per_foot
    distance_in_miles= distance_in_feet/feet_per_mile       #1mile = 5280 feet
    distance_in_kilometers= distance_in_meter/meters_per_kilometer   

     #calculate the walking distance
    speed_mph= 3.1   #average walking speed in 3.1 miles/hour

    time_hours= distance_in_miles / speed_mph

    #hours to mins, by multiplying 60
    walking_time_in_mins= time_hours * 60

    #now lets print
    print(
         "\n"
         "Distance:", f"{distance_in_chains:.3f}", "chains", "\n"  #used f-string to show only 3 decimals
         "Meters:", f"{distance_in_meter:.3f}" "\n"
         "Feet:", f"{distance_in_feet:.3f}" "\n"
         "Miles:", f"{distance_in_miles:.3f}" "\n"
         "Kilometers:", f"{distance_in_kilometers:.3f}" 
         "\n"
         "\n"
         "Walking time:", f"{walking_time_in_mins:.1f}", "minutes"  #.1f to show only 1 decimal
         "\n" #used "\n " for a blank line, and to break the lines
         "\n"
         "Thank you for using the converter. Goodbye:D")



if __name__ == "__main__":
    main()

#used the def main()
