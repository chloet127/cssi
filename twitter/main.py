import webapp2
import jinja2
import os
import json
import random
import logging
import urllib2
from google.appengine.api import users
from google.appengine.ext import ndb


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))



class Author(ndb.Model):
    nickname = ndb.StringProperty()
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()


class Tweet(ndb.Model):
    message = ndb.StringProperty()
    length = ndb.IntegerProperty()
    timestamp = ndb.DateProperty()
    media = ndb.BlobProperty()
    author_key = ndb.KeyProperty()


class NewAuthor(webapp2.RequestHandler):
    def post(self):
        nickname = user.nickname()
        name = self.request.get('name')
        age = self.request.get('age')

        if name and age:
            a = Author(name = name, age = age, nickname = nickname)
            a.put()



class NewTweet(webapp2.RequestHandler):
    def post(self):
        message = self.request.get('message')
        media = self.request.get('media')
        length = 40
        timestamp = 7
        a_get = Author.query(Author.name == user.nickname()).get()
        a_key = a.key

        if message and media and a_key:
            t = Tweet(message = message, media = media, length = length,
                        timestamp = timestamp, a_key = a_key)
            t.put()






app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/author', NewAuthor),
    ('/tweet', TweetHandler)
], debug=True)
