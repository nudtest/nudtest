from flask import Flask, request, make_response
import uuid

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'], defaults={'path': ''})
@app.route('/<path:path>', methods=['POST', 'GET'])
def hello_world(path):
    app.logger.warning(f'{request.data}, {request.headers}')
    # Respond with another event (optional)
    res = {'msg': f'Hi from helloworld-python app! your path is /{path}'}
#    res.update(request)
    response = make_response(res)
    response.headers["Ce-Id"] = str(uuid.uuid4())
    response.headers["Ce-specversion"] = "0.3"
    response.headers["Ce-Source"] = "knative/eventing/samples/hello-world"
    response.headers["Ce-Type"] = "dev.knative.samples.hifromknative"
    return response



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
