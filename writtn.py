# -*- encoding: utf-8 -*-
import os
import urllib

from data import *
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
  def get(self):
    data = {
      'quote': getquote(),
      'title': "Writtn",
      'content': "templates/index.html",
    }
    path = os.path.join(os.path.dirname(__file__), 'main.html')
    self.response.out.write(template.render(path, data))
    

class AddPage(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if not user:
      self.redirect(users.create_login_url(self.request.uri))
    else:
      if users.is_current_user_admin():
        data = {
          'title': "Add Quote",
          'content': "templates/add.html",
        }
        path = os.path.join(os.path.dirname(__file__), 'main.html')
        self.response.out.write(template.render(path, data))
      else:
        self.redirect('/')

class AddSavePage(webapp.RequestHandler):
  def post(self):
    save(self.request);
    self.redirect('/add');

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/add', AddPage),
                                      ('/addsave', AddSavePage),
                                      ],
                                     debug=False)

def real_main():
    run_wsgi_app(application)

def profile_main():
    # This is the main function for profiling
    # We've renamed our original main() above to real_main()
    import cProfile, pstats
    prof = cProfile.Profile()
    prof = prof.runctx("real_main()", globals(), locals())
    print "<pre>"
    stats = pstats.Stats(prof)
    stats.sort_stats("time")  # Or cumulative
    stats.print_stats(80)  # 80 = how many to print
    # The rest is optional.
    # stats.print_callees()
    # stats.print_callers()
    print "</pre>"

def real_main():
    run_wsgi_app(application)

main = real_main

if __name__ == "__main__":
    main()