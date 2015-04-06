from google.appengine.ext import db
import random

__author__="aquilax"
__date__ ="$Feb 20, 2010 8:15:35 AM$"


class MyQuote(db.Model):
  author = db.StringProperty(verbose_name="Author")
  quote = db.StringProperty(verbose_name="Quote", multiline=True)
  created = db.DateTimeProperty(verbose_name="Addred", auto_now_add=True)
  status = db.IntegerProperty(default=1)

class MyHash(db.Model):
  name = db.StringProperty(verbose_name="Name")
  val = db.IntegerProperty(default=0)

def getnum():
  num = MyHash.all();
  num.filter("name =", 'count')
  nums = num.fetch(1)
  if (nums):
    num = nums[0]
    return num.val
  else:
    return 0
  

def setnum():
  n = getnum();
  if (not n):
    n = 0
    num = MyHash()
    num.name = 'count'
  else:
    num = MyHash.all();
    num.filter("name =", 'count')
    num = num.fetch(1)[0]
  num.val = n+1;
  num.put();

def getquote():
  quote = MyQuote.all()
  randNum = random.randrange(1, getnum(), 1)
  quote = MyQuote.all().fetch(limit = 1, offset = randNum)[0]
  return quote

def save(data):
  quote = MyQuote();
  quote.author= data.get('author')
  quote.quote = data.get('quote')
  quote.put()
  setnum()