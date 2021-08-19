import logging

from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from model.summary import SummaryFields
from service.summarize_service import SummarizeService as Service


class Summarize(Resource):

    @staticmethod
    def get():
        return Summarize.post()

    @staticmethod
    def post():
        try:
            content_list = request.json
            schema = SummaryFields()

            for content in content_list:
                try:
                    schema.load(content)
                except ValidationError as err:
                    logging.error("Document error: " + content["id"])
                    logging.error(err.messages)
                    return err.messages, 400

                content["summary"] = Service.summarize(content["content"], content["language"])

            return jsonify(content_list)
        except Exception as err:
            logging.error(err)
