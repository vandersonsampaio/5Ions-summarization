import logging

from datetime import date
from flask import Flask
from flask_restful import Api

from controller.summarization_controller import Summarize

app = Flask(__name__)
api = Api(app)

api.add_resource(Summarize, "/summarization/summarize")

if __name__ == "__main__":
    logFileName = "logs/5ions-summarization_" + date.today().strftime("%Y-%m-%d") + ".log"

    a_logger = logging.getLogger()
    a_logger.setLevel(logging.ERROR)

    output_file_handler = logging.FileHandler(logFileName, 'a', "utf-8")
    a_logger.addHandler(output_file_handler)

    app.run(host="127.0.0.1", port=5000)
