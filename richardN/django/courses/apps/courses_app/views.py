# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'courses_app/index.html')

def process(request):
    if request.method == 'POST':
        form_data = request.POST
        request.session['name'] = form_data['name']
        request.session['location'] = form_data['location']
        request.session['language'] = form_data['language']

    return redirect('/results')

def result(request):
    return render(request, 'courses_app/results.html')