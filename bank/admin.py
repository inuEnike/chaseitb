from django.contrib import admin
from .models import *



admin.site.register([Profile, Deposit,Card, Accountnumber, Transfer, Withdraw, Pin,Transaction])