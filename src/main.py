from bottle import route, run, template
from datetime import datetime


@route('/')
def weeknumber():
    now = datetime.now()
    weeknum = now.isocalendar()[1]
    weekday = now.weekday()
    day = now.day
    month = now.month
    year = now.year
    days_remaining = (datetime(year, 12, 31) - now).days
    weeks_remaining = 52 - weeknum

    return template(
        'weektemplate',
        weeknum=weeknum,
        day=day,
        month=month,
        year=year,
        days_remaining=days_remaining,
        weeks_remaining=weeks_remaining
    )

run(host='localhost', port=8080)