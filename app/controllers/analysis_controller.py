from flask_restx import Resource
from flask import request

from app.exceptions.error_handler import APIException
from app.models.requests.analysis_request import analysis_get_request_model
from app.models.responses.analysis_response import analysis_get_response_model
from app.namespace.namespaces import analysis_ns
from app.services.analyse_service import get_all_analyses, get_analysis_with_filtered


@analysis_ns.route('/get_all')
class AnalysisList(Resource):
    @analysis_ns.doc('list_analyses')
    @analysis_ns.param('task_keys', 'Comma-separated list of task keys to filter by')
    @analysis_ns.marshal_list_with(analysis_get_response_model)
    def get(self):
        task_keys = request.args.get('task_keys')
        if task_keys:
            task_keys = task_keys.split(',')
        analyses = get_all_analyses(task_keys)

        return analyses


@analysis_ns.route('/get-analysis')
class AnalysisList(Resource):
    @analysis_ns.expect(analysis_get_request_model, validate=True)
    @analysis_ns.marshal_list_with(analysis_get_response_model)
    def post(self):
        allowed_keys = {'filters'}
        extra_keys = set(request.get_json().keys()) - allowed_keys

        if extra_keys:
            raise APIException(
                message="Unexpected fields in request body",
                status_code=400,
                details={"unexpected_fields": list(extra_keys)}
            )

        data = request.get_json()
        filters = data.get('filters', [])
        return get_analysis_with_filtered(filters)


"""
    @analysis_ns.doc('add_analysis')
    @analysis_ns.expect(analysis_get_request_model)
    @analysis_ns.marshal_with(analysis_get_response_model, code=201)
    def post(self):
        # TODO: implement
        data = analysis_ns.payload
        return {"id": 3, **data}, 201"""
