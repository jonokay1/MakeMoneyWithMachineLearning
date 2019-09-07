#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
	
@app.route('/yoo')
def hello_world1():
    return 'Hello, World! New Route working'

if __name__ == "__main__":
  app.run()


# In[ ]:




