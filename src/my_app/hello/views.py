from my_app import Blueprint
from my_app.hello.models import MESSAGES

@hello.route('/')
@hello.route('/hello')
def hello_world():
    return MESSAGES['default']


@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key


@hello.route('/add/<key>/<messages>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key