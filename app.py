from flask import Flask, request

app = Flask(__name__)

posts = []

INDEX = '''
title: <input id="post-title">
body: <input id="post-body">
<button onclick="newPost()">new post!</button>
<script>
const postFormIds = ['post-title', 'post-body']

function newPost() {
    fetch('/posts', {
        body: JSON.stringify({
            'title': document.getElementById('post-title').value,
            'body': document.getElementById('post-body').value
        }),
        headers: {
            'content-type': 'application/json'
        },
        method: 'POST',
    }).then(res => res.text()).then(text => alert(text))
}
</script>
'''

POST = '''
<button onclick="editPost()">edit</button>
<button onclick="deletePost()">delete</button>
<script>
function editPost() {
    fetch('', {
        body: JSON.stringify({
            'body': document.getElementById('post-body').value
        }),
        headers: {
            'content-type': 'application/json'
        },
        method: 'PUT',
    }).then(res => res.text()).then(text => alert(text))
}
function deletePost() {
    fetch('', {
        method: 'DELETE',
    }).then(res => res.text()).then(text => alert(text))
}
</script>
'''


@app.route('/', methods=['GET'])
def index():
    return INDEX


@app.route('/posts', methods=['POST'])
def add_post():
    posts.append(request.json)
    return str(len(posts) - 1)


@app.route('/posts/<int:pid>', methods=['GET'])
def get_post(pid):
    if pid < 0 or pid >= len(posts):
        return 'post not found'
    post = posts[pid]
    return f'<h1>{post["title"]}</h1><input id="post-body" value="{post["body"]}">' + POST


@app.route('/posts/<int:pid>', methods=['PUT'])
def edit_post(pid):
    if pid < 0 or pid >= len(posts):
        return 'post not found'
    posts[pid]['body'] = request.json['body']
    return str(pid)


@app.route('/posts/<int:pid>', methods=['DELETE'])
def delete_post(pid):
    if pid < 0 or pid >= len(posts):
        return 'post not found'
    del posts[pid]
    return str(pid)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
