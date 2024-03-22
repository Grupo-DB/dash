from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta

def home_fertilizantes(request):
    return render(request,'fertilizantes.html')
