from flask import Flask
app = Flask(__name__)

def hello_world(order2, blogId):
   return 'Hello World %d %d' % (blogId, order2)

if __name__ == '__main__':
   app.run(debug = True)