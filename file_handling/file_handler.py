""" class for reading from and writing to CSV file used for training of the classifier """

import pandas
import csv
import pkg_resources
import os
import booking_classifier

class FileHandler():
    def __init__(self):
        self.filepath = str(booking_classifier.ROOT_DIR + '/resources/Labeled_transactions.csv')

    def read_csv(self, file):
        if file:
            return pandas.read_csv(filepath_or_buffer=file, encoding='ISO-8859-1', delimiter=',')
        else:
            return pandas.read_csv(self.filepath, encoding='ISO-8859-1', delimiter=',')

    def write_csv(self, booking):
        #booking_props = booking.to_array()
        #booking_props = booking.to_small_array()
        with open(self.filepath, 'a') as file:
            file.write('\n'+booking.category+','+booking.text+','+booking.usage+','+booking.owner)
            #writer = csv.writer(file)
            #writer.writerow(booking_props)
