from django.db import models

# Create your models here.

class MainPageInfo(models.Model):
    faculty_name = models.CharField(
        "Назва факультету",
        max_length=255,
        default="Факультет природничих наук"
    )
    description = models.TextField(
        "Опис факультету",
        help_text="Основний текст про місію, лабораторії та наукові дослідження факультету"
    )
    address = models.CharField(
        "Адреса деканату",
        max_length=255,
        default="04070, м. Київ, вул. Григорія Сковороди, 2, корпус 3, кімн. 216"
    )
    phone = models.CharField(
        "Телефон",
        max_length=50,
        default="+38 (044) 425-60-57"
    )
    email = models.EmailField(
        "Email",
        default="fprn@ukma.edu.ua"
    )
    working_hours = models.CharField(
        "Графік роботи",
        max_length=255,
        default="Пн–Пт: 09:00 – 17:00"
    )

class Department(models.Model):
    name = models.CharField(
        "Назва кафедри",
        max_length=255
    )
    head = models.CharField(
        "Завідувач кафедри",
        max_length=255
    )

class Program(models.Model):
    code = models.IntegerField(
        "Код спеціальності"
    )
    name = models.CharField(
        "Назва спеціальності",
        max_length=255
    )
    description = models.TextField(
        "Опис спеціальності"
    )
    coordinator_name = models.CharField(
        "Ім'я координатору набору",
        max_length=255
    )
    coordinator_contact = models.CharField(
        "Контакт координатору набору",
        max_length=255
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs"
    )
    disciplines = models.JSONField(
        "Список дисциплін",
        default=list
    )

class Lecturer(models.Model):
    name = models.CharField(
        "Ім'я викладача",
        max_length=255
    )
    position = models.CharField(
        "Посада",
        max_length=255
    )
    degree = models.CharField(
        "Вчене звання",
        max_length=255
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="lecturers"
    )
