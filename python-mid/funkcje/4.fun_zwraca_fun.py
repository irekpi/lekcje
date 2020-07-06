from datetime import datetime


def time_minute(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_hour(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_day(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()


def create_func(span):
    if 'm' == span:
        sec = 60
    if 'h' == span:
        sec = 3600
    if 'd' == span:
        sec = 86400
    source = """
def count_time(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
""".format(sec)
    exec(source, globals())
    return count_time


f_minutes = create_func('m')
f_hours = create_func('h')
f_days = create_func('d')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))