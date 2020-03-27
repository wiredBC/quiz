import random


# functions for getting query result
def quiz_result(query):

	quiz_by_name = QuizCatalog.objects.filter(name=query)
	quiz_by_course = QuizCatalog.objects.filter(course=query)
	quiz_by_level = QuizCatalog.objects.filter(level=query)
	quiz_by_subject = QuizCatalog.objects.filter(programme=query)

def tutorial_result():
	pass

def q_n_s_result(query):
	pass

# funtion to mark submitted answers

def mark(sub_ans, questions):
	results = {}
	
	marking_scheme = {}
	
	correct_ans = 0
	
	wrong_ans = 0
	
	missing_question = 0
	
	for question in questions:
		
		marking_scheme.update({question.question : question.answer})
		
	
	for key , value in marking_scheme.items() :
		
		submitted_ans = sub_ans.get(key, 0)
		
		if submitted_ans != 0:
			ms_ans = value
			
			if submitted_ans == ms_ans :
				print(f"ans is correct : {submitted_ans}")
				correct_ans +=1
				
			else:
				print(f"ans is wrong	 : {submitted_ans}")
				wrong_ans +=1
				continue	
		else:
			print(f"question is missing : {key}")
			
			missing_question += 1
			
			continue
			
	results.update({"correct" : correct_ans, "wrong" : wrong_ans, "miss" : missing_question , "marking_scheme" :marking_scheme})
	
	return results
		
		  	

# function to shuffle question order

def shuffler(d2) :

	d1 = dict()

	d2_k = list(d2.keys())

	random.shuffle(d2_k)

	for key in d2_k :
	
		d1.update({
		
		key : d2[key]
		
		})
		
	return d1
