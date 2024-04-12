import datetime

en_sv_translation = {
    "Monday": "Måndag",
    "Tuesday": "Tisdag",
    "Wednesday": "Onsdag",
    "Thursday": "Torsdag",
    "Friday": "Fredag",
    "Saturday": "Lördag",
    "Sunday": "Söndag",
    "January": "Januari",
    "February": "February",
    "March": "Mars",
    "April": "April",
    "May": "Maj",
    "June": "Juni",
    "July": "Juli",
    "August": "Augusti",
    "September": "September",
    "October": "Oktober",
    "November": "November",
    "December": "December"
}

now = datetime.datetime.now()

for i in range(365):
    date = now + datetime.timedelta(days=i)
    date_representation_parts = f"{date:%-d %B %Y %A}".split()

    weekday = en_sv_translation[date_representation_parts[3]]
    month = en_sv_translation[date_representation_parts[1]]

    date_representation_parts[3] = weekday
    date_representation_parts[1] = month

    print(" ".join(date_representation_parts))