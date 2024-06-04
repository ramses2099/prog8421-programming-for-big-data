#!/env/bin/ python3
import os
from style import Style

# -----------------------------------------------------------------------------------------
# Question-2. Write a program that reads a sound level in decibels from the user. If the user enters a decibel level
# that matches one of the noises in the table, then your program should display a message containing only that
# noise. If the user enters a number of decibels between the noises listed, then your program should display a
# message indicating which noises the level is between. Ensure that your program also generates reasonable output
# for a value smaller than the quietest noise in the table, and for a value larger than the loudest noise in the table.
# -----------------------------------------------------------------------------------------

# Define the noise levels in decibels
noise_levels = {
    "Jackhammer": 130,
    "Gas Lawnmower": 106,
    "Alarm Clock": 70,
    "Quiet Room": 40
}

def main():
    os.system("clear")
    print(Style.BLUE + "[--------------------QUESTION 2----------------------]")
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
    # Read the sound level in decibels from the user
    decibel_level = int(input("Enter the sound level in decibels: "))
    print(Style.BLUE + "[---------------------INPUT--------------------------]")
        
    print()
    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    
    # Determine the appropriate message to display
    if decibel_level < min(noise_levels.values()):
        print(Style.GREEN + "The sound level is quieter than a Quiet Room.")
    elif decibel_level > max(noise_levels.values()):
        print(Style.GREEN + "The sound level is louder than a Jackhammer.")
    else:
        matching_noise = None
        lower_noise = None
        higher_noise = None

        for noise, level in noise_levels.items():
            if decibel_level == level:
                matching_noise = noise
                break
            elif decibel_level < level:
                if higher_noise is None or level < noise_levels[higher_noise]:
                    higher_noise = noise
            elif decibel_level > level:
                if lower_noise is None or level > noise_levels[lower_noise]:
                    lower_noise = noise

        if matching_noise:
            print(Style.GREEN + f"The sound level matches that of a {matching_noise}.")
        else:
            print(Style.GREEN + f"The sound level is between a {lower_noise} and a {higher_noise}.")

    print(Style.YELLOW + "[---------------------OUTPUT-------------------------]")
    print()   
    
if __name__ == "__main__":
    main()