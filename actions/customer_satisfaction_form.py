from utils import (
    safe_input,
    today,
    get_sales,
    get_feedbacks,
    add_feedback,
)


def customer_satisfaction_form():
    feedback = {
        "date": today()
    }
    print("--- Customer satisfaction form ---\n")
    print('Which is your sale id (it is found on your receipt)?')

    total_sales = len(get_sales())

    sale_id = 0

    while True:
        sale_id = safe_input('int_positive', 'Sale id: ')
        if sale_id > -1 and sale_id < total_sales:
            break
        else:
            print('That sale id is invalid')

    print('\nHow was our service? (1, 2, 3, 4, 5)')
    rating = 0
    while True:
        rating = safe_input('int_positive', 'Rating: ')
        if rating > 0 and rating < 6:
            break
        else:
            print('Please select a number from 1 to 5')

    feedback['sale_id'] = sale_id
    feedback['rating'] = rating
    feedback['id'] = len(get_feedbacks())

    add_feedback(feedback)

    print('\nCool. Thanks for giving us your feedback.')
    print('We hope to see you again')
