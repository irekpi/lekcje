projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Dolan Trump and Bill Clinton']

dates = ['2016-06-23', '2016-08-29', '1994-01-01']
combo = zip(projects, leaders, dates)
for project, leader, date in combo:
    print('{} project name, created by {} on {}'.format(project, leader, date))