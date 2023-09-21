from flask import Flask
from controller import home_controller


def createApp():
    app = Flask(__name__)
    app.add_url_rule("/", view_func=home_controller.home_index)

    return app

if __name__ == "__main__":
    app = createApp()
    app.run(host="0.0.0.0", port=8080, debug=True)
