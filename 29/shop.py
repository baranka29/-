from flask import Flask, request

app = Flask(__name__)

ids=[]
@app.route('/shoppinglist/new/', methods=['POST'])
def new():
    u = request.json['new_list']
    print(u)
    if u not in ids:
        id = {'list':u}
        ids.append(id)
        print(u)
        print(id)
        print(ids)
        return {'status': 'ok'}
    else:
        return {'status': 'fail'}

@app.route('/shoppinglist/add/', methods=['POST'])
def add():
    k=request.json['data']
    id=request.json['list']
    print(k, '-----', id)


app.run(host='0.0.0.0', port=5000)
