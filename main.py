import time
import winsound

while True:
    try:
        time_in_sec = int(input('\nEnter the time in seconds: '))

        for i in reversed(range(0, time_in_sec+1)): 
            seconds = i % 60
            minutes = int(i/60) % 60
            hours = int(i/3600)
            print(f'{hours:02}:{minutes:02}:{seconds:02}')
            time.sleep(1)
            
        for i in range(3):
            winsound.Beep(800, 3000)
        break

    except ValueError:
        print('\nInvalid input please enter a valid number.')
 
# ____________________________________________________________________________________________________

# Created by: Izram Khan
# Date created: 10/Oct/2025
