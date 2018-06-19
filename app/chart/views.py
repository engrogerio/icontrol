# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import render
from app.chart.models import Chart 

# Create your views here.

class ChartShow(ListView):
    model = Chart
    template_name = 'chart_show.html'
