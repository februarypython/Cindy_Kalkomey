from django.shortcuts import render, HttpResponse, redirect

#/surveys - display "placeholder to display all the surveys created"
def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)
#/surveys/new - display "placeholder for users to add a new survey
def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)