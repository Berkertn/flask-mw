from flask_restx import fields

from app.namespace.namespaces import analysis_ns

analysis_get_response_model = analysis_ns.model('AnalysisGetResponse', {
    'id': fields.Integer(readOnly=True, attribute='row_id', description='The unique identifier of an analysis'),
    'task_key': fields.String(required=True, description='The task key of the analysis'),
    'description': fields.String(description='The description of the analysis'),
})
