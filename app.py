from datetime import datetime

# In-memory storage for events
events = []

#Event creation
def add_event(title, description, date, time):
    try:
        event_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        return
    
    new_event = {
        'title': title,
        'description': description,
        'datetime': event_datetime
    }
    
    events.append(new_event)
    print("Event added successfully.")

#Listing events
def list_events():
    if not events:
        print("No events found.")
        return
    
    sorted_events = sorted(events, key=lambda x: x['datetime'])
    
    for event in sorted_events:
        print(f"Title: {event['title']}")
        print(f"Description: {event['description']}")
        print(f"Date and Time: {event['datetime'].strftime('%Y-%m-%d %H:%M')}")
        print("-" * 20)

#Deleting events
def delete_event(title):
    global events
    updated_events = [event for event in events if event['title'] != title]
    
    if len(updated_events) == len(events):
        print(f"No event found with the title '{title}'.")
    else:
        events = updated_events
        print(f"Event with title '{title}' deleted successfully.")

def search_events(keyword):
    matching_events = [event for event in events if keyword.lower() in event['title'].lower() or keyword.lower() in event['description'].lower()]
    
    if not matching_events:
        print(f"No events found with the keyword '{keyword}'.")
    else:
        print(f"Events matching the keyword '{keyword}':")
        for event in matching_events:
            print(f"Title: {event['title']}")
            print(f"Description: {event['description']}")
            print(f"Date and Time: {event['datetime'].strftime('%Y-%m-%d %H:%M')}")
            print("-" * 20)

def edit_event(title):
    global events
    event_to_edit = next((event for event in events if event['title'] == title), None)
    
    if event_to_edit:
        print("Enter new details for the event:")
        new_title = input("New title (press Enter for no changes): ") or event_to_edit['title']
        new_description = input("New description (press Enter for no changes): ") or event_to_edit['description']
        new_date = input("New date (YYYY-MM-DD) (press Enter for no changes): ") or event_to_edit['datetime'].strftime('%Y-%m-%d')
        new_time = input("New time (HH:MM) (press Enter for no changes): ") or event_to_edit['datetime'].strftime('%H:%M')
        
        try:
            new_datetime = datetime.strptime(f"{new_date} {new_time}", "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date or time format. Event not edited.")
            return
        
        event_to_edit['title'] = new_title
        event_to_edit['description'] = new_description
        event_to_edit['datetime'] = new_datetime
        
        print(f"Event with title '{title}' edited successfully.")
    else:
        print(f"No event found with the title '{title}'.")

def main():
    while True:
        print("\nEvent Scheduler Application")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Search Events")
        print("5. Edit Event")
        print("6. Exit")
        
        user_choice = input("Select an option (1/2/3/4/5/6): ")
        
        if user_choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            add_event(title, description, date, time)
        
        elif user_choice == '2':
            list_events()
        
        elif user_choice == '3':
            title = input("Enter the title of the event to delete: ")
            delete_event(title)

        elif user_choice == '4':
            keyword = input("Enter a keyword to search for events: ")
            search_events(keyword)

        elif user_choice == '5':
            tittle = input("Enter the tittle of the event to edit: ")
            edit_event(tittle)

        elif user_choice == '6':
            print("Exiting Event Scheduler. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
