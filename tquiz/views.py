from django.shortcuts import render
from django.views import View
from .models import Question, Choice, QuizCatalog
from .utility_functions import *

# Create your views here.

class Index(View):
	
	quizList = QuizCatalog.objects.all()[:10]
	
	
	def get (self, request):

		self.template = "tquiz/index.html"
		
		self.context = {"quizList" : self.quizList}
		
		return render(request, self.template, self.context)


				
class Results(View):
	
	questions = Question.objects.all()
	
	def post(self, request):
		
		sub_ans = request.POST
		
		results = mark(sub_ans, self.questions)
		
		self.template = 'tquiz/results.html'
		
		self.context = {'results' : results}
		
		return render(request, self.template, self.context)
		
	def get(self, request):
		
		self.template = "tquiz/no-results.html"
			
		self.context = {}
			
		return render(request, self.template, self.context)
			


class StartWork(View):

	def get(self, request, quiz_name):
		quiz = QuizCatalog.objects.get(name=quiz_name)
		questions = quiz.question_set.all()
		qc_dict = {}
		for question in questions:
			choice = question.choice_set.all()
			qc_dict[question.question] = choice

		questionList = shuffler(qc_dict)


		self.template = 'tquiz/start-work.html'
		self.context = {'questionList':questionList}

		return render(request, self.template, self.context)

class SearchResult(View):
	def get(self, request, query):
		quiz_results = quiz_results(query)
		quiz_numbers = len(quiz_results)
		tutorials_results = tutorials_results(query)
		tutorials_number = len(tutorials_results)
		qns_results = qns_results(query)
		quiz_number = len(qns_results)
		query = query
		self.template = 'tquiz/serach-result.html'
		self.context = {'quiz_results': quiz_results, 
						'quiz_number': quiz_number,
						'tutorials_results': tutorials_results, 
						'tutorials_number': tutorials_number,
						'qns_results': qns_results, 
						'qns_number': qns_number,
						 'query': query}
		return render(request, self.template, self.context)


class Quiz(View):
	def get(self, request):
		quizList = QuizCatalog.objects.all()[:10]
		self.template = 'tquiz/quiz.html'
		self.context = {"quizList": quizList}

		return render(request, self.template, self.context)