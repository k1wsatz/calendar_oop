from datetime import datetime
from event import Event, Workshop, Meeting
from planner import Planner


def main():
    e = Event('piwko', datetime.strptime('01-03-2022 17:50', '%d-%m-%Y %H:%M'), 6, 'better world', 'mikolaj',
              ['bodzio', 'seba', 'tomek'])
    w = Workshop('python', datetime.strptime('01-03-2022 17:15', '%d-%m-%Y %H:%M'), 60, 'better world', 'mikolaj',
                 ['bodzio', 'seba', 'tomek'], 'online')
    m = Meeting('piwko', datetime.strptime('01-03-2022 17:15', '%d-%m-%Y %H:%M'), 60, 'better world', 'mikolaj',
                ['bodzio', 'seba', 'tomek'], 'arctovsky')
    e.start_time = datetime.strptime('01-03-2022 17:50', '%d-%m-%Y %H:%M')
    print(repr(w))
    # planner = Planner([])
    # print(repr(planner))
    print(w.duration)
    print(w.start_time)
    print(w.end_of_meeting())
    print(w.end_of_meeting() - w.start_time)


if __name__ == '__main__':
    main()

# check_dt = e.check_date(datetime.strptime('01-03-2022 11:40', '%d-%m-%Y %H:%M'))
# print(check_dt)
# def check_event(event):
#     if not isinstance(event, Meeting):
#         raise TypeError(f'{event} is not real event')
#
#     return event.__dict__


# result = check_event(e)
# print(result)
