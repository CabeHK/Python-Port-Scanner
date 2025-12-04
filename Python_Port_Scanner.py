import socket
import logging
import os
from datetime import datetime

# Logging configuration


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Port_Scanner(IP, start_Port, end_Port): # Function for scanning a range of ports
    time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") # String formatting the time for filename
    
    logging.basicConfig(
    filename = f"{time} portscans.log", # Filename
    level = logging.INFO, # What level of results to log
    format = "%(asctime)s - %(levelname)s - %(message)s" 
    )

    # For loop to go through each port in a range
    for port in range(start_Port, end_Port + 1):
        # Configuring the socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 and TCP config
        sock.settimeout(0.5) # Stop checking after 0.5 Seconds
        
        result = sock.connect_ex((IP, port)) # Save port scan result to a variable
        print(f"Scanning port {port}") # Write to console so the user knows things are happening

        # Log results of this port to file
        if result == 0:
            logging.info(f"Port {port} is open on {IP}")
        else:
            logging.info(f"Port {port} is closed on {IP}")
        sock.close() # Close the socket to preserve system resources.
    input("Scan Complete. Press enter ton continue")



def Program(): # Main Program Logic
    clear_console() 
    verified = False # Bool for handling user input validity
    valid_Port = False # Bool for handling port number validity (Do these ports exist?)
    
    print("Welcome to Digicore's Port Scanner")
    # Gather target device from user
    target_Device = input("What is the IP or hostname of the device you would like to scan?")

    # While loop for determining ports to scan
    while not valid_Port:
        try:
            valid_Port = False # Reset validation variable

            # Gathering User Inputs related to port scanning range
            start_Port = input("What port would you like to start scanning from? (Inclusive)")
            end_Port = input("What port would you like to stop scanning from? (Inclusive)")
        
            start_Port = int(start_Port)
            end_Port = int(end_Port)
            if (start_Port > 65535 or start_Port < 0) or (end_Port > 65535 or end_Port < 0) or end_Port <= start_Port:
                print("Invalid Port Range. Only Ports between 0 and 65535 can be scanned")
                print("and the ending port must be greater than the starting port.")
                input("Press Enter to try again...")
            else: 
                valid_Port = True

        except ValueError: # Error catching for if the user doesnt enter a valid int
            print("Please only enter whole numbers")
            input("Press enter to try again")

    # Get user confirmation before proceeding
    while not verified:
        print("Does this information look correct? (Y/N)")
        print(f"Hostname: {target_Device}")
        print(f"Starting Port: {start_Port}")
        print(f"Ending Port: {end_Port}")

        user_input = input().upper() # Var to actually captureuser confirmation

    
        if user_input == "Y": # If yes, continue to the port scanner function.
            verified = True
        elif user_input == "N": # If NO, return to home page. This works because the Program function is in a loop
            verified = True
            print("Okay. Returning to Home Page...")
            input("Press Enter to continue")
            return 
        else: # If invalid Input, prompt user again.
            print("Invalid Input. Press Enter to try again")
            input()

    Port_Scanner(target_Device, start_Port, end_Port)

while True:
    Program()
