from django.contrib import admin
from .models import Author, Discipline, Group, Student, Testing, Question, Variant, Answer, ScheduleTesting

class AuthorAdmin(admin.ModelAdmin):
    """Автор теста"""
    list_display = ['name', 'surname', 'patronymic']
    search_fields = ['name', 'surname', 'patronymic']

class DisciplineAdmin(admin.ModelAdmin):
    """Дисциплина"""
    list_display = ['name']
    search_fields = ['name']

class GroupAdmin(admin.ModelAdmin):
    """Группа"""
    list_display = ['name']
    search_fields = ['name']

class StudentAdmin(admin.ModelAdmin):
    """Студент"""
    list_display = ['surname', 'name', 'patronymic', 'group', 'block', "login", 'email']
    search_fields = ['surname', 'name', 'patronymic', 'email']
    list_filter = ['group', 'block']

class TestingAdmin(admin.ModelAdmin):
    """Тестирование"""
    list_display = ['title', 'discipline', 'author']
    search_fields = ['title']
    list_filter = ['discipline', 'author']

class QuestionAdmin(admin.ModelAdmin):
    """Вопрос"""
    list_display = ['title', 'testing', 'ball']
    search_fields = ['title']
    list_filter = ['testing']

class VariantAdmin(admin.ModelAdmin):
    """Вариант ответа"""
    list_display = ['title', 'question', 'is_correct', 'ball']
    search_fields = ['title']
    list_filter = ['question', 'is_correct']

class AnswerAdmin(admin.ModelAdmin):
    """Ответ студента"""
    list_display = ['student', 'variant', 'open_text_response', 'host']
    search_fields = ['student__surname', 'student__name', 'variant__title', 'open_text_response']
    list_filter = ['student', 'variant']

class ScheduleTestingAdmin(admin.ModelAdmin):
    """Настройки работы теста"""
    list_display = ['testing', 'group', 'time_start', 'time_end']
    list_filter = ['testing', 'group', 'time_start', 'time_end']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Testing, TestingAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ScheduleTesting, ScheduleTestingAdmin)
