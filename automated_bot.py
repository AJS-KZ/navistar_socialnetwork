import json
import requests
import string
import random
from datetime import date


tokens = []
posts = []
file = open('bot_config_file.json', 'r')
data = json.load(file)

url_create_user = 'http://127.0.0.1:8000/api/users/'
url_create_post = 'http://127.0.0.1:8000/api/posts/create/'
url_create_likes_dislikes = 'http://127.0.0.1:8000/api/posts/like_dislike/'


def randomword(length):
   letters = string.ascii_lowercase
   result = ''.join(random.choice(letters) for i in range(length))
   return result


def get_token(value):
    value = json.loads(value)
    token = value['tokens']['access']
    return token


def get_post_uuid(value):
    global posts
    value = json.loads(value)
    posts.append(value['uuid'])


def create_data_to_likes_request():
    global posts
    start_date = date(day=1, month=1, year=2021).toordinal()
    end_date = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))

    kinds = ['LIKE', 'DISLIKE']
    result = random.choice(kinds)

    post_uuid = random.choice(posts)
    return random_day, result, post_uuid


def create_users():
    global url_create_user, url_create_post, tokens, data

    for user in range(data['number_of_user']):
        new_phone = str(random.randint(100000, 9999999))
        new_name = randomword(5)
        new_surname = randomword(5)
        new_user = requests.post(
            url_create_user,
            data={
                'phone': new_phone,
                'password': 'Password_123',
                'first_name': new_name,
                'last_name': new_surname
            }
        )
        tokens.append(get_token(new_user.content))
        posts_random_count = random.randint(1, data['max_posts_per_user'])
        for post in range(posts_random_count):
            new_post_title = randomword(5)
            new_post_text = randomword(25)
            new_post = requests.post(
                url_create_post,
                headers={'Authorization': 'Bearer ' + tokens[len(tokens)-1]},
                data={'title': new_post_title,
                      'text': new_post_text},
            )
            get_post_uuid(new_post.content)


def like_dislike_posts():
    global data, tokens

    for i in range(len(tokens)):
        token = tokens.pop()

        likes_count = random.randint(1, data['max_likes_per_user'])
        for j in range(likes_count):
            some_date, like, post_id = create_data_to_likes_request()

            requests.put(
                url_create_likes_dislikes + post_id + '/',
                headers={'Authorization': 'Bearer ' + token},
                data={'like': like,
                      'date': str(some_date)},
            )


if __name__ == '__main__':
    create_users()
    like_dislike_posts()


