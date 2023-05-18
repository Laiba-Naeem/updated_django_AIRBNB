# import pandas as pd
# from hotel.models import Hotel

# # bulk insertion method


# def upload():
#     csv_file_path = 'hotel_dataset.csv'
#     df = pd.read_csv(csv_file_path)
#     for index, row in df.iterrows():

#         print("updating")
#         model_instance = Hotel(

#             hotel_name=row['name'],
#             hotel_location=row['host_location'],
#             bed_rooms=row['bedrooms'],
#             latitude=row['latitude'],
#             longitude=row['longitude'])

#         model_instance.save()
#     str = 'done'
#     return str

import pandas as pd
from hotel.models import Hotel

# Code below using bulk_create


def upload():
    df = pd.read_csv("hotel_dataset.csv")
    hotels = [
        Hotel(

            hotel_name=row['name'],
            hotel_location=row['host_location'],
            bed_rooms=row['bedrooms'],
            latitude=row['latitude'],
            longitude=row['longitude'])


        for i, row in df.iterrows()
        if not Hotel.objects.filter(hotel_name=row['name']).exists()
    ]
    Hotel.objects.bulk_create(hotels, ignore_conflicts=True)
    msg = "successful"
    return msg
