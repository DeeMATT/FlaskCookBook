from flask import Flask

app = Flask(__name__)

import my_app.hello.views import hello

app = Flask(__name__)
app.register_blueprint(hello)