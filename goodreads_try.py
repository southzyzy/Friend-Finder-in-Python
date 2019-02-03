import goodreads, time
from goodreads import client
import random


class GoodreadsBook(object):

    def __init__(self, key, secret):
        self.client_key = key
        self.client_secret = secret

    def authenticate(self):
        self.auth_client = client.GoodreadsClient(self.client_key, self.client_secret)

    def book(self):
        """ Get info about a random book """
        max_book_num = 10000000
        index = random.randint(1, max_book_num)
        book = self.auth_client.book(index)

        return book

    def book_search(self, b, page=1, search_field='all'):
        """ Get the most popular books for the given query. This will search all
            books in the title/author/ISBN fields and show matches, sorted by
            popularity on Goodreads.
            :param q: query text
            :param page: which page to return (default 1)
            :param search_fields: field to search, one of 'title', 'author' or
            'genre' (default is 'all')
        """
        books = self.auth_client.search_books(str(b), page, search_field)

        return books


if __name__ == '__main__':
    start_time = time.time()
    gc = client.GoodreadsClient("key", "secret")
    # print gc.search_books("Christian reflections")
    print("\n--- Program Runtime: ---\n %s seconds " % (time.time() - start_time))
