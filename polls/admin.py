from django.contrib import admin
from .models import Question, Choice, UserChoice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


class UserChoiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'choice', ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserChoice, UserChoiceAdmin)
