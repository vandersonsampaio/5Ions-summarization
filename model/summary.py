from marshmallow import Schema, fields


class SummaryFields(Schema):
    id = fields.Str(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    language = fields.Str(required=True)
