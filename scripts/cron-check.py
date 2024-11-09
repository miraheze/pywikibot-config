#!/usr/bin/env python3
# Script to validate the contents of cron.yaml in Miraheze's pywikibot-config repo
# Copyright (C) 2024 Alex <alex@blueselene.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import yaml
import re
# This list defines the keys every cron entry must have in the YAML
musthave = ["name", "ensure", "script", "scriptparams", "hour", "minute", "month", "monthday", "weekday"]
def isValidCronTime(cronValue: str, minValue: int, maxValue: int) -> bool:
    if cronValue == "*":
        return True
    try:
        if int(cronValue) < minValue or int(cronValue) > maxValue:
            return False
        else:
            return True
    except ValueError:
        return False
with open("cron.yaml", "r") as file:
    data = yaml.safe_load(file)
    for dbname in data.keys():
        if re.search("^[a-z0-9]*$", dbname) is None:
            print(f"Invalid dbname {dbname}, must consist of only lowercase letters with numbers optionally")
            exit(1)
        nameList = []
        for i, dict in enumerate(data[dbname]):
            if all(a == b for a, b in zip(musthave, dict.keys())) is False:
                print(f"Missing keys in dict {i} of wiki {dbname}, have: {dict.keys()}, expected: {musthave}")
                exit(1)
            if dict["name"] in nameList:
                print(f"Cron entry with name {dict['name']} on wiki {dbname} defined twice")
                exit(1)
            nameList.append(dict["name"])
            if dict["ensure"] != "present" and dict["ensure"] != "absent":
                print(f"Invalid value for ensure in dict {i} of dbname {dbname}, have: {dict['ensure']}, expected: either present or absent")
                exit(1)
            if isValidCronTime(dict["hour"], 0, 23) is False:
                print(f"Invalid value for hour in dict {i} of dbname {dbname}, have: {dict['hour']}, expected: either * or a number between 0 and 23 inclusive")
                exit(1)
            if isValidCronTime(dict["minute"], 0, 59) is False:
                print(f"Invalid value for minute in dict {i} of dbname {dbname}, have: {dict['minute']}, expected: either * or a number between 0 and 59 inclusive")
                exit(1)
            if isValidCronTime(dict["month"], 1, 12) is False:
                print(f"Invalid value for month in dict {i} of dbname {dbname}, have: {dict['month']}, expected: either * or a number between 1 and 12 inclusive")
                exit(1)
            if isValidCronTime(dict["monthday"], 1, 31) is False:
                print(f"Invalid value for monthday in dict {i} of dbname {dbname}, have: {dict['monthday']}, expected: either * or a number between 1 and 31 inclusive")
                exit(1)
            if isValidCronTime(dict["weekday"], 0, 6) is False:
                print(f"Invalid value for weekday in dict {i} of dbname {dbname}, have: {dict['weekday']}, expected: either * or a number between 0 and 6 inclusive")
                exit(1)
print("No issues detected with cron.yaml.")
exit(0)

