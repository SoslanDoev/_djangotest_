from django.db import models

class Author(models.Model):
    """Автор теста"""
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["surname", "name", "patronymic"]

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

class Discipline(models.Model):
    """Дисциплина"""
    name = models.CharField(unique=True, max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Group(models.Model):
    """Группа"""
    name = models.CharField(unique=True, max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Student(models.Model):
    """Студент"""
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    block = models.BooleanField(default=False, verbose_name="Заблокирован")
    email = models.EmailField(unique=True, verbose_name="Почта")
    login = models.CharField(unique=True, max_length=100, verbose_name="Логин")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    token = models.CharField(max_length=255, unique=True, blank=True, verbose_name="Токен")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["surname", "name", "patronymic"]

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

class Testing(models.Model):
    """Тестирование"""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Дисциплина")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")

    class Meta:
        verbose_name = "Тестирование"
        verbose_name_plural = "Тестирования"
        ordering = ["discipline", "title"]

    def __str__(self):
        return self.title

class Question(models.Model):
    """Вопрос"""
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE, verbose_name="Тестирование")
    title = models.TextField(verbose_name="Текст вопроса")
    ball = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Балл за правильный ответ")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["title"]

    def __str__(self):
        return self.title

class Variant(models.Model):
    """Вариант ответа"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    title = models.TextField(verbose_name="Текст варианта ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")
    ball = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Балл за правильный ответ", null=True, blank=True)

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"
        ordering = ["title"]

    def __str__(self):
        return self.title

class Answer(models.Model):
    """Ответ студента"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, verbose_name="Вариант", null=True, blank=True)
    open_text_response = models.TextField(verbose_name="Открытый ответ", blank=True, null=True)
    host = models.CharField(max_length=255, verbose_name="Хост")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["student"]

    def __str__(self):
        return f"{self.student} - {self.variant or self.open_text_response}"

class ScheduleTesting(models.Model):
    """Настройки работы теста"""
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE, verbose_name="Тестирование")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    time_start = models.DateTimeField(verbose_name="Начало тестирования")
    time_end = models.DateTimeField(verbose_name="Конец тестирования")

    class Meta:
        verbose_name = "Настройка тестирования"
        verbose_name_plural = "Настройки тестирования"
        ordering = ["testing", "time_start"]

    def __str__(self):
        return f"{self.testing} для {self.group} с {self.time_start} до {self.time_end}"