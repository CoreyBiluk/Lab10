# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 10 | Part 4
# March 8, 2021

# Import Modules
import serial
import matplotlib.pyplot as plt
from drawnow import *

# Create lists to hold values being transmitted by Arduino
Data1 = []
Data2 = []

# This function is responsible for ploting the incoming values on the graph
def PlotSignal():
    # Set y axis limit to 1200
    plt.ylim(0,1200)
    # Title of graph
    plt.title('Ploting in Streaming AD0 from Arduino')
    # Show grid lines
    plt.grid(True)
    # Label Y axis
    plt.ylabel('Analog Input Value')
    # Plot 1st set of data, format - red dashed line, label data as A0 input
    plt.plot(Data1, 'r--', label='A0 Input')
    # Plot 2nd set of data, format - blue dotted line, label data as A1 input
    plt.plot(Data2, 'b:', label='A1 Input')
    # Create legend and place in upper right
    plt.legend(loc='upper right')

# Main Function
if __name__ == '__main__':

    # Create serial communicaton object at 9600 baudrate
    ser = serial.Serial('COM5', 9600)
    # Turn on interactive mode
    plt.ion()
    # Initialize a data counter variable
    Dcounter=0
    # Fluse Serial comms line
    ser.flush()

    # Loop program
    while True:
        # If no data is being recieved:
        while (ser.inWaiting()==0):
            # Do nothing
            pass 
        # Decode and read data from Arduino
        ardData = ser.readline().decode('utf-8')
        # Split incoming string at each "," to get each individual data value        
        InputData = ardData.split(',')
        # Convert input data value 1 to float and store in variable
        temp_val1 = float(InputData[0])
        # Convert input data value 2 to float and store in variable
        temp_val2 = float(InputData[1])
        # Add input data1 values to data1 list by appending
        Data1.append(temp_val1)
        # Add input data2 values to data2 list by appending
        Data2.append(temp_val2)

        #  Call drawnow function for PlotSignal
        drawnow(PlotSignal)
        # Short pause
        plt.pause(0.000001)
        # Increment data counter variable by 1
        Dcounter=Dcounter+1
        # if data counter variable is greater than 60:
        if(Dcounter>60):
            # Reset data counter variable to 0
            Dcounter=0
            # Clear data from lists
            Data1.pop(0)
            Data2.pop(0)
    # Close Serial communication
    ser.close()