from flask import Flask, request, Response, render_template
import json
import pickle
app = Flask(__name__)

def get_all_users():
    data_new = pickle.load(open('data.base', 'rb'))  
    js = json.dumps(data_new)  
    data_new.close
    return Response(js, status=200, mimetype='application/json')

def create_user():
  pass

def update_user(user_id):
  pass

def delete_user(user_id):
  pass

@app.route('/', methods=['GET', 'POST']  )
def users():
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        create_user()

@app.route('/users/<user_id>', methods=['PATCH', 'DELETE'])
def users(user_id):
  if request.method == 'PATCH':
    return update_user(user_id)
  elif request.method == 'DELETE':
    return delete_user(user_id)
  else:
    pass
    

if __name__ == '__main__':
    app.run()
