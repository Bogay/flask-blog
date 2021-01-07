'''
Each post's structure:
{
    'title': str,
    'body': str
}
'''
posts = []


def add_post(json):
    posts.append(json)


def get_post(pid):
    return posts[pid]


def get_posts():
    return posts


def post_len():
    return len(posts)


def edit_post(pid, body):
    posts[pid]['body'] = body


def delete_post(pid):
    del posts[pid]
