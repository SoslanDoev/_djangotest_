from django.core.management.base import BaseCommand
from core.models import Author, Discipline, Group, Student, Testing, Question, Variant, ScheduleTesting

class Command(BaseCommand):
    help = 'Заполнение базы данных тестовыми данными'

    def handle(self, *args, **kwargs):
        author = Author.objects.create(name='Иван', surname='Иванов', patronymic='Иванович')
        discipline = Discipline.objects.create(name='Математика')
        group = Group.objects.create(name='Группа 1')
        
        student = Student.objects.create(
            name='Петр',
            surname='Петров',
            patronymic='Петрович',
            group=group,
            block=False,
            email='petr@example.com',
            login='petr',
            password='securepassword',
            token='unique-token'
        )

        testing = Testing.objects.create(title='Тест по математике', discipline=discipline, author=author)

        question1 = Question.objects.create(testing=testing, title='Что такое интеграл?', ball=10)
        question2 = Question.objects.create(testing=testing, title='Решите уравнение 2x + 3 = 7', ball=5)

        Variant.objects.create(question=question1, title='Определённый интеграл', is_correct=True, ball=10)
        Variant.objects.create(question=question1, title='Неопределённый интеграл', is_correct=False)
        Variant.objects.create(question=question2, title='x = 2', is_correct=True, ball=5)
        Variant.objects.create(question=question2, title='x = 1', is_correct=False)

        ScheduleTesting.objects.create(
            testing=testing,
            group=group,
            time_start='2024-06-01 10:00:00',
            time_end='2024-06-01 12:00:00'
        )

        self.stdout.write(self.style.SUCCESS('Данные успешно заполнены'))
