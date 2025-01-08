import pywhatkit
import csv
import time

'''Function to send a message to an individual contact '''
def send_message(contact, message, hour, minute):
    """
    Args:
        contact (str): Phone number of the contact in international format (e.g., '+92XXXXXXXXXX').
        message (str): The message to send.
        hour (int): Hour in 24-hour format for scheduled message.
        minute (int): Minute of the scheduled message.
    """
    try:
        pywhatkit.sendwhatmsg(contact, message, hour, minute)
        print(f"Message successfully sent to {contact}")
    except Exception as e:
        print(f"Failed to send message to {contact}: {e}")

'''Function to send messages in bulk from a CSV file '''
def bulk_send(file, hour, minute):
    """
    Args:
        file (str): Path to the CSV file containing 'Contact' and 'Message' columns.
        hour (int): Hour in 24-hour format for scheduled message.
        minute (int): Minute of the scheduled message.
    """
    try:
        with open(file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = row['Contact']
                message = row['Message']
                send_message(contact, message, hour, minute)
                time.sleep(10)  # Wait 10 seconds to avoid rate-limiting
    except Exception as e:
        print(f"Error while sending bulk messages: {e}")

''' Function to send a message to a group'''
def send_group_message(group_name, message):
    """
    Args:
        group_name (str): Name of the WhatsApp group.
        message (str): The message to send.
    """
    try:
        pywhatkit.sendwhatmsg_to_group(group_name, message, 16, 24)  # Adjust time at the time of use
        print(f"Message successfully sent to group {group_name}")
    except Exception as e:
        print(f"Failed to send message to group {group_name}: {e}")

'''Main logic'''
try:
    print("What would you like to do?")
    print("1. Send a message to an individual")
    print("2. Send a message to a group")
    print("3. Send messages in bulk from a CSV file")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        contact = input("Please enter the contact number (in international format): ")
        message = input("Please type your message here: ")
        hour = int(input("Enter the hour (24-hour format): "))
        minute = int(input("Enter the minute: "))
        send_message(contact, message, hour, minute)

    elif choice == "2":
        group_name = input("Please enter the group name: ")
        message = input("Please type your message here: ")
        send_group_message(group_name, message)

    elif choice == "3":
        file_path = input("Please enter your file location (CSV with 'Contact' and 'Message' columns): ")
        hour = int(input("Enter the hour (24-hour format): "))
        minute = int(input("Enter the minute: "))
        bulk_send(file_path, hour, minute)

    else:
        print("Invalid choice. Please run the script again and select a valid option.")

except Exception as e:
    print(f"An error occurred: {e}")
