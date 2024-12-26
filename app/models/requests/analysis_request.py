# Request body model
from flask_restx import fields

from app.namespace.namespaces import analysis_ns

filter_field = analysis_ns.model('FilterField', {
    'type': fields.String(required=True, description='Filter type (row_id or task_key)', enum=['row_id', 'task_key']),
    'values': fields.List(fields.String, required=True, description='List of values for filtering'),
})

analysis_get_request_model = analysis_ns.model('AnalysisGetRequest', {
    'filters': fields.List(fields.Nested(filter_field), required=False, description='Optional filters for the query'),
})
