posts = []


def add_post(json):
    posts.append(json)


def get_post(index):
    return posts[index]


def post_len():
    return len(posts)


def edit_post(pid, body):
    posts[pid]['body'] = body


def delete_post(pid):
    del posts[pid]
