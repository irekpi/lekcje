import datetime as dt


class Trip:

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self. start = start
        self.end = end

    def check_data(self):
        # if len(self.title) == 0:
        #     raise Exception('Title is empty')
        assert len(self.title) > 0, "Title is empty!!!!"
        if self.start > self.end:
            raise ValueError('End needs to be later than start')

    @classmethod
    def publish_offer(cls, trips):
        list_of_error = []
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_error.append('{}: {}'.format(trip.symbol, str(e)))
            except Exception as e:
                list_of_error.append('{}: {}'.format(trip.symbol, str(e)))

        if list_of_error:
            raise Exception('List of errors: {}'.format(list_of_error))
        else:
            print('the offer will be published.')


trips = [
    Trip('IT-VNC', 'Spain', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),          #No Errors
    # Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),   #Errors
    # Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))          #Errors
]

try:
    print('----=== Check process begins ===----')
    Trip.publish_offer(trips)
    print('==Done==')
except Exception as e:
    print(e)