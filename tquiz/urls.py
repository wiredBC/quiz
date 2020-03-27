from django.urls import path

from . import views


app_name = 'tquiz'

urlpatterns = [

	path("", views.Index.as_view(), name ='index'),
	
	path("results/", views.Results.as_view(), name ='results'),

	path("startwork/<quiz_name>", views.StartWork.as_view(), name ='startwork'),

	path("search/<query>", views.SearchResult.as_view(), name ='search'),

	path("quiz/", views.Quiz.as_view(), name ='quiz'),

]
