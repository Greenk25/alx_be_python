from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    # Print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Prompt the user to enter a number of days
    days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display the future date
    calculate_future_date(days)

if __name__ == "__main__":
    main()

