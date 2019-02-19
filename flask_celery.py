from celery import Celery, uuid
#from celery.result import AsyncResult


def uuid_celery():
    task_id = uuid()
    return task_id

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    #TaskBase = celery.Task
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


# def check_task_timeout(request):
#     async_result = Celery.result.AsyncResult(request.POST['task_id'])
#     try:
#         result = async_result.get(timeout=5, propagate=False)
#     except Exception, e:
#         result = None
#     status = async_result.status
#     traceback = async_result.traceback
#     if isinstance(result, Exception):
#         return HttpResponse(json.dumps({
#             'status': status,
#             'error': str(result),
#             'traceback': traceback,
#         }), content_type='application/json')
#     else:
#         return HttpResponse(json.dumps({
#             'status': status,
#             'result': result,
#         }), content_type='application/json')
#

