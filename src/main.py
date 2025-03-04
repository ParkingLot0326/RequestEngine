import sys
import requests
import re
from PyQt5.QtWidgets import QApplication

from Method import Method
from app import App


def init_session(org:str, ref:str) -> requests.Session:
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Origin': org,
        "Referer": ref
    })
    return session

def check_url(org:str) -> bool:
    url_pattern = re.compile(
        r'^(https?://)?'  # http:// or https:// (optional)
        r'([a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}'  # domain like example.com
        r'(/\S*)?$'  # optional path
    )

    return bool(url_pattern.match(org))

def send(session:requests.Session, method:Method, url:str, data:dict=None) -> requests.Response:
    match method:
        case Method.HEAD:
            return session.head(url)
        case Method.GET:
            return session.get(url)
        case Method.POST:
            return session.post(url, data=data)
        case Method.PUT:
            return session.put(url, data=data)
        case Method.DELETE:
            return session.delete(url)
        case _:
            pass
    pass

def set_global_timeout():
    pass

if __name__ == '__main__':
    print("Hello World!")
    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec_())