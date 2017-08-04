import webapp2
import jinja2
import os
import json
import random
import logging
import urllib2
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


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

        my_vars = {}
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(my_vars))


    def post(self):
        # my_vars = {
        #     'noun1': self.request.get('noun1'),
        #     'activity': self.request.get('activity'),
        #     'teacher': self.request.get('teacher'),
        #     'celebrity': self.request.get('celebrity'),
        #     'show': self.request.get('show'),
        #     'fun': self.request.get('fun')
        # }

        loc = {
            'long': self.request.get('long'),
            'lat': self.request.get('lat')
        }

        template = jinja_environment.get_template('templates/temp.html')
        self.response.out.write(template.render(loc))

class AdminPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            if users.is_current_user_admin():
                self.response.write('You are an administrator.')
            else:
                self.response.write('You are not an administrator.')
        else:
            self.response.write('You are not logged in.')



class Api(webapp2.RequestHandler):
    def get(self):
        noun1s = ['car', 'plane', 'sandwich']
        activities = ['swim', 'surf', 'rollerblade']
        teachers = ['yasser', 'kim', 'josh', 'zack']
        celebrities = ['beyonce', 'usher', 'justin bieber', 'drake']
        shows = ['modern family', 'csi', 'gossip girl']
        funs = ['FUN!', 'FUNNNNNNN!!!', 'FUNNNNNNNNNN!!!!!!!']

        answer = {
            'noun1': random.choice(noun1s),
            'activitiy': random.choice(activities),
            'teacher': random.choice(teachers),
            'celebrity': random.choice(celebrities),
            'show': random.choice(shows),
            'fun': random.choice(funs)
        }
        self.response.out.write(json.dumps(answer))


class Artist(ndb.Model):
    name = ndb.StringProperty()
    genre = ndb.StringProperty()
    age = ndb.IntegerProperty()

class Song(ndb.Model):
    title = ndb.StringProperty()
    lyrics = ndb.StringProperty()
    duration = ndb.IntegerProperty()
    release = ndb.DateProperty()

class UserLocation(ndb.Model):
    username = ndb.StringProperty()
    lat = ndb.StringProperty()
    lng = ndb.StringProperty()

class Birthplace(ndb.Model):
    name = ndb.StringProperty()
    lat = ndb.StringProperty()
    lng = ndb.StringProperty()


class Story(webapp2.RequestHandler):
    def get(self):
        ans = urllib2.urlopen('http://cssi-kir.appspot.com/api')
        ans = ans.read()
        f = json.loads(ans)

        template = jinja_environment.get_template('templates/story.html')
        self.response.out.write(template.render(f))

class PositionHandler(webapp2.RequestHandler):
    def post(self):
        logging.info('got a request')
        name = self.request.get('name')
        lng = self.request.get('lng')
        lat = self.request.get('lat')

        if name and lat and lng:
            b = Birthplace(name = name, lat = lat, lng = lng)
            b.put()
            logging.info('just put a birthplace')

class GetPosHandler(webapp2.RequestHandler):
    def get(self):
        results = Birthplace.query().fetch()
        dresult = [i.to_dict() for i in results]
        self.response.write(json.dumps(dresult))

class MapPage(webapp2.RequestHandler):
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

        my_vars = {}
        template = jinja_environment.get_template('templates/map.html')
        self.response.out.write(template.render(my_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/api', Api),
    ('/story', Story),
    ('/admin', AdminPage),
    ('/postpos', PositionHandler),
    ('/getpos', GetPosHandler),
    ('/map', MapPage)
], debug=True)
