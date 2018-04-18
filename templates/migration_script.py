import csv
import django
django.setup()
from pages.models import Student
with open('0_Final Registrations - All.csv','r') as csvfile:
    spamreader =csv.DictReader(csvfile)
    for row in spamreader:
        Student.objects.create(name=row['Name'],programme=row['Programme'],allowed_entries=int(row['Count']),last_name=" ",middle_name=" ",remaining_entries=int(row['Count']))