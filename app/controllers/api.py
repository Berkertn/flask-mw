from flask_restx import Api
from app.controllers.analysis_controller import analysis_ns

api = Api(
    title="AI-MW API",
    version="1.0",
    description="API documentation for AI-MW",
    doc="/swagger-ui"
)

api.add_namespace(analysis_ns)

"""namespaces = [analysis_ns, user_ns, product_ns]

# use with for
for namespace in namespaces:
    api.add_namespace(namespace)"""
