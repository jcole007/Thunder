# The calculated time traveled project.
# Date 3/22/2021
# CTI-110 P3HW2 - DistanceTraveled
# Jerry Cole
##### Flowchart #####
# Start
# Input the car speed.
# Input the time traveled. (true display calculated output)
# False Display Error.
# Calculate the distance traveled.
# Display the output.
# End
##### Pseudocode ##### 
# Ask user to enter the car speed
# Ask user to enter time traveled (if user enter 0 or -number error)
# Calculate distance ( speed x time)
# Display the following:
# The Speed Entered
# The Time entered
# The Output Display Distance Traveled in mile
# Display error if enter 0 or -number.

speed = int(input('Enter the car speed: '))
time = float(input('Enter the time traveled: '))
distance = (speed * time)
if time > 0:
    print('Speed entered:', speed)  
    print('Time :', time)
    print()
    print('Distance Traveled', distance, 'miles.')
else:
        print('Error ! time entered should be > 0.')
        
input('Press Enter to Exit. ')



