from flask import Flask
from flask_celery import make_celery, uuid_celery
import time
import random
from flask import jsonify

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/1'

celery = make_celery(app)

@app.route('/process/<name>')
def process(name):
    async_result = reverse.apply_async(args=[name])
    print async_result
    response = {
        'uuid': async_result.id,
        'status': 'curl -X GET http://localhost:5000/status/'+async_result.id,  # this is the exception raised
    }
    return jsonify(response)


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = celery.AsyncResult(task_id)
    print task.state
    print task.info
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'status': task.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)

@celery.task(name='celery_example.reverse')
def reverse(string):
    time.sleep(20)
    return string[::-1]

if __name__ == '__main__':
    app.run(debug=True)