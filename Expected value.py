#-----------------------Importing libraries-------------------------------

# Import the NumPy library
import numpy as np
# Import the Matplotlib library for plotting
import matplotlib.pyplot as plt
# Import the os and platform libraries
import os , platform
# Import the colorama library for colored text
from colorama import Fore

# -------------------------------BAnner --------------------------------------

# Check the platform and clear the screen
plat = platform.uname()[0]
if plat == "Linux":
     os.system("clear")
else:
      os.system("cls")

# Define a function to print the banner
def banner():
    # Define the banner text
    font =f"""{Fore.CYAN} 

███████╗██╗  ██╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗     ██╗   ██╗ █████╗ ██╗     ██╗   ██╗███████╗    
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██║   ██║██╔══██╗██║     ██║   ██║██╔════╝    
█████╗   ╚███╔╝ ██████╔╝█████╗  ██║        ██║   █████╗  ██║  ██║    ██║   ██║███████║██║     ██║   ██║█████╗      
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██║  ██║    ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══╝      
███████╗██╔╝ ██╗██║     ███████╗╚██████╗   ██║   ███████╗██████╔╝     ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗    
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═════╝       ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝

                                         Developed by Abolfazl ilka                                                                       
                                                                                                                                                                                                                                                                                                                                                             
"""
    # Print the banner text
    print(font)
# Call the banner function to print the banner
banner()

# ----------------------- Input data by user using three methods ---------------------

# Prompt the user for their preferred data input method
show_data = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Hello, do you enter the data manually or use the txt file or the default data? [ 1-manually , 2-txt file 3-default ] '+Fore.LIGHTGREEN_EX )
# Default data for fallback or user selection
default_data = np.array([75,75,73,71,71,70,67,75,79,78,78,78,78,77,75,80,87,86,86,83,82,82,81,91])

# Define an empty list to store user-entered data
user_data = []

#------------------------Process User Input with Robust Error Handling----------------

try:
    # Manual data entry
    if show_data == "1":
        while True:
            value = input("Enter your data one by one and when finished type 'End'")
            if value.upper() == "END":
                break
            user_data.append(float(value))
        print(f"Your entered data: {user_data}")

    # Data from a text file    
    elif show_data == "2":
        with open('data.txt', 'r') as file:
            user_data = [float(line) for line in file]
        print(f"Data loaded from text file: {user_data}")
    
    # Use default data    
    elif show_data == "3":
        user_data = default_data
    else:
        raise ValueError("Invalid input! Please enter 1, 2 or 3")
except Exception as e:
    print(f"{Fore.RED} An error occurred during data input:", e)
    print(f"{Fore.BLUE} Using default data as a fallback.")
    user_data = default_data

#-------------------------Calculate Descriptive Statistics----------------------

# Calculate the mean of the data
def calculate_mean(data):
    """
    Calculates the mean of a given dataset.

    Args:
        data: A list of numerical values.

    Returns:
        The mean of the data.
    """
    return sum(data) / len(data)
# Calculate the variance of the data
def calculate_variance(data):
    """
    Calculates the variance of a given dataset.

    Args:
        data: A list of numerical values.

    Returns:
        The variance of the data.
    """
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

# Calculate the standard deviation of the data
def calculate_std_dev(variance):
    """
    Calculates the standard deviation of a given dataset.

    Args:
        variance: The variance of the data.

    Returns:
        The standard deviation of the data.
    """
    return variance ** 0.5

mean = calculate_mean(user_data)
variance = calculate_variance(user_data)
std_dev = calculate_std_dev(variance)

#------------------------Display Descriptive Statistics----------------------
print(f"\n{Fore.YELLOW}Data Summary: ")
print(f"{Fore.LIGHTGREEN_EX}Mean: {mean : .2f}")
print(f"{Fore.LIGHTGREEN_EX}Variance: {variance : .2f}")
print(f"{Fore.LIGHTGREEN_EX}Standard Deviation: {std_dev : .2f} \n")

#---------------------------Prompt User for Plotting Options-------------------

# Ask the user if they want to draw a histogram
draw_histogram = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Would you like to draw a histogram? [Y/N] '+Fore.LIGHTGREEN_EX )
# --------- check user input  for draw plot ------------
if draw_histogram.upper() == 'Y':
    try:
        # Plot the histogram
        plt.hist(user_data, bins='auto', color='skyblue', edgecolor='black')
        # Calculate and plot the probability density function
        breaks = np.histogram_bin_edges(user_data , bins='auto')
        # draw plygon plot
        plt.plot([min(breaks)] + [(breaks[i] + breaks[i + 1]) / 2 for i in range(len(breaks) - 1)] + [max(breaks)], [0] + np.histogram(user_data, bins=breaks)[0].tolist() + [0], linestyle='dashed', linewidth=1.75, color='green')
        # Add a title and labels to the plot
        plt.title('Histogram of Data')
        plt.xlabel('Data Value')
        plt.ylabel('Frequency')
        # Show the plot
        plt.show()
    except Exception as e:
       # Handle errors during plot drawing
        print(f"{Fore.RED} An error occurred while drawing the chart:", e)

# --------- ask to user for draw normal plot ------------
draw_normal_plot = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Would you like to draw a normal probability plot? [Y/N]'+Fore.LIGHTGREEN_EX )
# --------- check user input  for draw normal plot ------------
if draw_normal_plot.upper() == 'Y':
    try:
        # input by user for normal sample size
        sample_size = int(input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Enter the size of the normal sample:  '+Fore.LIGHTGREEN_EX ))
        # great normal data 
        data = np.random.normal(mean, std_dev, sample_size)
        # calculate breaks of histogram plot
        breaks_n = np.histogram_bin_edges(data , bins='auto')
        # draw histogam plot
        plt.hist(data, bins='auto', color='skyblue', edgecolor='black')
        # draw plygon plot
        plt.plot([min(breaks_n)] + [(breaks_n[i] + breaks_n[i + 1]) / 2 for i in range(len(breaks_n) - 1)] + [max(breaks_n)], [0] + np.histogram(data, bins=breaks_n)[0].tolist() + [0], linestyle='dashed', linewidth=1.75, color='green')
        # Add a title and labels to the plot
        plt.title('draw normal plot of Data')
        plt.xlabel('Data Value')
        plt.ylabel('Frequency')

        # show plots
        plt.show()
    except Exception as e:
        # Handle errors during plot drawing
        print(f"{Fore.RED} An error occurred while drawing the histogram:", e)

# --------- ask to user for draw sample averages plot ------------
draw_sample_averages = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Would you like to draw a sample averages plot? [Y/N]'+Fore.LIGHTGREEN_EX )
# --------- check user input  for draw sample averages plot ------------
if draw_sample_averages.upper() == 'Y':
    try:
        # input by user for sample averages size
        num_samples= int(input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Enter size sample averages :   '+Fore.LIGHTGREEN_EX ))
        # The list sample_means is used to store the mean of each sample.
        sample_means = []
        # This for loop calculates the mean of 10 random samples from the user data.
        for _ in range(num_samples):
            # The variable sample_mean stores the mean of the sample.
            sample = np.random.choice(user_data, size=len(user_data), replace=True)
            # The variable sample_mean stores the mean of the sample.
            sample_mean = calculate_mean(sample)
            # The mean of the sample is appended to the list sample_means.
            sample_means.append(sample_mean)
        # draw histogam plot    
        plt.hist(sample_means, bins='auto', color='skyblue', edgecolor='black')
        # calculate breaks of histogram plot
        breaks_s = np.histogram_bin_edges(sample_means , bins='auto')
        # Draw polygon plot along the histogram
        plt.plot([min(breaks_s)] + [(breaks_s[i] + breaks_s[i + 1]) / 2 for i in range(len(breaks_s) - 1)] + [max(breaks_s)], [0] + np.histogram(sample_means, bins=breaks_s)[0].tolist() + [0], linestyle='dashed', linewidth=1.75, color='green')
        # calculate means of data
        mean_data = calculate_mean(sample_means)
        # draw means plot
        plt.axvline(mean_data, color='blue', linestyle='dashed', linewidth=2)
        # Add text as a label at the top of the page
        textstr = '\n'.join(( r'Mean sample =%.2f' % (mean_data),r'Mean data =%.2f' % (mean)))
        # add text to plot
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10 ,verticalalignment='top', bbox=props)
        # draw and show plots
        plt.show()
    except Exception as e:
        # Handle errors during plot drawing
        print(f"{Fore.RED} An error occurred while drawing the chart:", e)




# ------------- enter to exit ----------
while True:
    # user can control code with 'Enter' key
    user_input = input("for exit click Enter : ")
    if user_input == "":
        break
#-------------- End ---------------
