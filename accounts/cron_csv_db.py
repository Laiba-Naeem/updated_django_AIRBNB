
from . import Hotel
import csv


def upload():

    with open('hotel_dataset.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model_instance = Hotel(
                hotel_name=row['name'],
                hotel_location=row['host_location'],
                bed_rooms=row['bedrooms'],
                latitude=row['latitude'],
                longitude=row['longitude']

            )
            model_instance.save()
