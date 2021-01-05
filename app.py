from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/posts', methods=['POST'])
def add_post():
    model.add_post(request.json)
    return str(model.post_len() - 1)


@app.route('/posts/<int:pid>', methods=['GET'])
def get_post(pid):
    if pid < 0 or pid >= model.post_len():
        return 'post not found'
    post = model.get_post(pid)
    return render_template('post.html', **post)


@app.route('/posts/<int:pid>', methods=['PUT'])
def edit_post(pid):
    if pid < 0 or pid >= model.post_len():
        return 'post not found'
    model.edit_post(pid, request.json['body'])
    return str(pid)


@app.route('/posts/<int:pid>', methods=['DELETE'])
def delete_post(pid):
    if pid < 0 or pid >= model.post_len():
        return 'post not found'
    model.delete_post(pid)
    return str(pid)


if __name__ == '__main__':
    app.run()
