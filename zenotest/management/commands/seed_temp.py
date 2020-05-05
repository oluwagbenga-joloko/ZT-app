import csv
import re
from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from zenotest.models import TempMeasurement

def clear_DB():
    TempMeasurement.objects.all().delete()


pattern = r'((?P<days>\d+)\sdays\s)((?P<hours>\d+):)((?P<minutes>\d+):)((?P<seconds>\d+\.\d+))'
regex = re.compile(pattern)


def parse_time(time_str):
    parts = regex.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for (name, param) in parts.items():
        if param and name != "seconds":
            time_params[name] = int(param)
    time_params["seconds"] = float(parts["seconds"])
    return timedelta(**time_params)



class Command(BaseCommand):
    help = 'seeds temperature measurements'
    def handle(self, *args, **options):
        self.stdout.write("seeding data.......")
        clear_DB()
        with open("./data/test_data.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                measurement = TempMeasurement.objects.create(id = row["id"])
                measurement.timestamp = row["timestamp"]
                measurement.duration = parse_time(row["duration"])
                measurement.temperature = row["temperature"]
                measurement.save()
        self.stdout.write(self.style.SUCCESS("Successfully seeded data"))
