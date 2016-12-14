__author__ = 'shaur'
import pusher


def send_log_signal(message):
    pusher_client = pusher.Pusher(
        app_id='280345',
        key='e64252df238c8822e820',
        secret='d9370b1a7f2571afa019',
        ssl=True
    )
    pusher_client.trigger('inventory', 'user-note', {'message': message})