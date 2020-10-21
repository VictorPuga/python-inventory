from utils import (
    dict_to_csv_line,
    dict_from_entries
)

keys = ('id', 'date', 'sale_id', 'rating')


def get_feedbacks():
    feedbacks = []
    file = open('feedbacks.csv')
    for line in file:
        id, date, sale_id, rating = line.split(',')

        feedbacks.append(dict_from_entries(keys, (
            int(id),
            date,
            int(sale_id),
            int(rating.rstrip()),
        )))

    file.close()
    return tuple(feedbacks)


def add_feedback(feedback):
    file = open('feedbacks.csv', 'a')
    line = dict_to_csv_line(feedback, keys)
    file.write(line)
    file.close()
