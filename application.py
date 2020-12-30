# @Author  : Edlison
# @Date    : 12/28/20 18:08
from backend.api import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()