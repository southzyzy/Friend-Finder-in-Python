import sys
import requests
import AES


class G_BOOKS():
    googleapikey = sys.argv[1]

    def search(self, value):
        parms = {"q": value, 'key': self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print r.url
        rj = r.json()
        print rj["totalItems"]
        for i in rj["items"]:
            try:
                print repr(i["volumeInfo"]["description"])
            except:
                pass
            try:
                print repr(i["volumeInfo"]["imageLinks"]["thumbnail"])
            except:
                pass


if __name__ == "__main__":
    bk = G_BOOKS()
    bk.search("Christian reflections")
