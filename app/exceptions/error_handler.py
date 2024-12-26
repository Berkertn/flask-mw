from flask import jsonify
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import DataError



class APIException(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, details=None):
        super().__init__()
        self.message = message
        self.details = details or {}  # information about the error maybe extra data or detail
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return {
            'error': self.message,
            'status_code': self.status_code,
            'details': self.details
        }


def register_error_handlers(app):
    @app.errorhandler(APIException)
    def handle_api_exception(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(BadRequest)
    def handle_validation_error(error):
        return jsonify({
            "error": "Validation error",
            "status_code": 400,
            "details": error.data.get('errors') if hasattr(error, 'data') else str(error)
        }), 400


    @app.errorhandler(DataError)
    def handle_data_error(error1):
        return jsonify({
            "error": "Database query error",
            "status_code": 400,
            "details": "Query error"
        }), 400

    @app.errorhandler(404)
    def handle_404(error):
        return jsonify({
            "error": "Resource not found",
            "status_code": 404,
            "details": {}
        }), 404

    @app.errorhandler(500)
    def handle_500(error):
        return jsonify({
            "error": "Internal server error",
            "status_code": 500,
            "details": {}
        }), 500


"""  custom error example to use in services !!
 raise APIException(
        "This is a custom error",
        status_code=400,
        details={"reason": "Invalid input", "expected": "JSON payload"}
    )"""
