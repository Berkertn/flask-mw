from app.data.analysis_entity import Analysis

def get_all_analyses(task_keys=None):
    query = Analysis.query

    # task_keys is a list of strings will be filtered by task_key
    if task_keys:
        query = query.filter(Analysis.task_key.in_(task_keys))

    return query.all()


def get_analysis_with_filtered(filters):
    query = Analysis.query
    for filter_item in filters:
        filter_type = filter_item['type']
        values = filter_item['values']

        if filter_type == 'row_id':
            query = query.filter(Analysis.row_id.in_(values))
        elif filter_type == 'task_key':
            query = query.filter(Analysis.task_key.in_(values))

    analyses = query.all()
    return analyses
