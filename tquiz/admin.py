from django.contrib import admin
from .models import Question, Choice, Examiner, QuizCatalog

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Examiner)
admin.site.register(QuizCatalog)

