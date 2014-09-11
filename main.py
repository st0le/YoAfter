import webapp2, urllib, jinja2, os
from google.appengine.api import taskqueue
from google.appengine.api import urlfetch

from apikeys import *  # contains api key for YOAFTER15MIN,YOAFTER30MIN,YOAFTERANHOUR 

SINGLE_YO_API = "http://api.justyo.co/yo/"

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class BaseScheduleHandler(webapp2.RequestHandler):
    
    def __init__(self, request=None, response=None, apitoken=None, delay=None):
        self.initialize(request, response)
        self.apitoken = apitoken
        self.delay = delay
    
    def get(self):
        username = self.request.get("username")
        if username:
            taskqueue.add(url="/yo", params={"username":username.upper(), "api_token":self.apitoken}, method="POST", countdown=self.delay)

    
class FifteenMinuteHandler(BaseScheduleHandler):
    def __init__(self, request=None, response=None):
        BaseScheduleHandler.__init__(self, request, response, YOAFTER15MIN, 15 * 60)
    
class ThirtyMinuteHandler(BaseScheduleHandler):
    def __init__(self, request=None, response=None):
        BaseScheduleHandler.__init__(self, request, response, YOAFTER30MIN, 30 * 60)

class OneHourHandler(BaseScheduleHandler):
    def __init__(self, request=None, response=None):
        BaseScheduleHandler.__init__(self, request, response, YOAFTERANHOUR, 60 * 60)
        
class YoHandler(webapp2.RequestHandler):
    
    def post(self):
        params = {field:self.request.get(field) for field in self.request.arguments()}
        if "username" in params and "api_token" in params:
            form_data = urllib.urlencode(params)
            urlfetch.fetch(url=SINGLE_YO_API,
                                    payload=form_data,
                                    method=urlfetch.POST,
                                    headers={'Content-Type': 'application/x-www-form-urlencoded'})

class HomePageHandler(webapp2.RequestHandler):
    
    def get(self):
        template = jinja_environment.get_template("index.html")
        self.response.write(template.render({}))

app = webapp2.WSGIApplication([ ("/", HomePageHandler),
                                (YOAFTERANHOUR_CALLBACK, OneHourHandler),
                                (YOAFTER30MIN_CALLBACK, ThirtyMinuteHandler),
                                (YOAFTER15MIN_CALLBACK, FifteenMinuteHandler),
                                ("/yo", YoHandler) ], debug=True)

