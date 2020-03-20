from pymongo import MongoClient
client = MongoClient()
db = client['library-db']


class user_info:
    collection = db['users-collection']
    def __init__(self, id):
        posts = db.posts
        self.user = posts.find_one({'id': id})
        if self.user is None:
            self.create_user(id)

    def create_user(self, id):
        posts = db.posts
        new_user = {'id': id,
                    'book': -1,
                    'chapt': -1,
                    'skip_chars': 0,
                    'timer': 0}
        self.user = posts.insert_one(new_user)

    def get_info(self):
        return self.user

class book_info:
    collection = db['books-collection']
    def __init__(self, book_name):
        posts = db.posts

