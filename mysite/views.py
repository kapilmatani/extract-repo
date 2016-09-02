from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import JsonResponse
import datetime
import json
import requests
from pprint import pprint


def hello(request):
	return HttpResponse("Hello world")


def my_homepage_view(request):
	return HttpResponse("This is the homepage :D")


def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)


def hours_ahead(request, offset):
    try:
       offset = int(offset)
    except ValueError:
       raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def abc(request):
	return render(request, 'current_datetime.html')


def github(request):
	t = get_template('github.html')
	url = "https://api.github.com"
	url_repo_person = "https://api.github.com/users/AnshikaMittal/repos"
	url_repos = "https://api.github.com/repositories"
	response = requests.get(url_repos)
	d = response.json()
	repos_name = []
	for r in d:
		repos_name.append(r['name'])
	html = t.render(Context({'repos': repos_name}))
	return HttpResponse(html)


# def github_new(request):
# 	# if request.is_ajax():
# 		url = "https://api.github.com"
# 		url_repo_person = "https://api.github.com/users/AnshikaMittal/repos"
# 		url_repos = "https://api.github.com/repositories"
# 		response = requests.get(url_repos)
# 		d = response.json()
# 		repos_name = []
# 		for r in d:
# 			repos_name.append(r['name'])
# 		data = json.dumps(repos_name)
# 	# else:
# 	# 	data = "fail"
# 	return HttpResponse(data)

def github_new(request):
	url = "https://api.github.com"
	url_repo_person = "https://api.github.com/users/AnshikaMittal/repos"
	url_repos = "https://api.github.com/repositories"
	response = requests.get(url_repos)
	d = response.json()
	repos_name = []
	for r in d:
		repos_name.append(r['name'])
	data = json.dumps(repos_name)
	return JsonResponse(data, safe=False)



	
	
