from utils import (
    dict_to_csv_line,
    dict_from_entries
)

keys = ('id', 'date', 'sale_id', 'rating')


def get_feedbacks():
    """
    Read and return the feedback from feedbacks.csv.

    Returns:
        - feedbacks (tuple): dictionary tuple with feedback data

    Sample dictionary:
    ```
    feedback = {
        "id": 0,
        "date": "01/02/20",
        "sale_id": 0,
        "rating": 5
    }
    """

    feedbacks = []

    file = open('feedbacks.csv')
    for line in file:
        # using unpacking syntax
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
    """
    Append a single feedback to feedbacks.csv

    Parameters: 
        - feedback (dictionary): feedback data

    Sample dictionary:
    ```
    feedback = {
        "id": 0,
        "date": "01/02/20",
        "sale_id": 0,
        "rating": 5
    }
    """
    # append, not destructive write
    file = open('feedbacks.csv', 'a')
    line = dict_to_csv_line(feedback, keys)
    file.write(line)
    file.close()
