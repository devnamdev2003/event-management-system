import pytz
from datetime import datetime
import json
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'event_management_system.settings')

# Initialize Django
django.setup()

# Now you can import your models
from event_management_system_app.models import Category, Event


def import_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for category_data in data['categories']:
        category_name = category_data['name']
        category, created = Category.objects.get_or_create(name=category_name)

        for event_data in category_data['events']:
            event_name = event_data['name']
            start_date_str = event_data['start_date']
            end_date_str = event_data['end_date']
            priority = event_data['priority']
            description = event_data['description']
            location = event_data['location']
            organizer = event_data['organizer']

            # Parse datetime strings and convert to UTC timezone
            start_date = datetime.strptime(
                start_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
            end_date = datetime.strptime(
                end_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)

            # Create the event
            Event.objects.create(
                name=event_name,
                category=category,
                start_date=start_date,
                end_date=end_date,
                priority=priority,
                description=description,
                location=location,
                organizer=organizer
            )


if __name__ == "__main__":
    file_path = "data.json"  # Update with your JSON file path
    import_data_from_json(file_path)
