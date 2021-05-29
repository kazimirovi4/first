from django.contrib.auth.models import AbstractUser
from django.db import models

MARKS = list(enumerate(range(1, 11)))


class PerformanceModel(models.Model):
    active = models.PositiveIntegerField(choices=MARKS)
    mark_for_practice = models.PositiveIntegerField(choices=MARKS)
    mark_for_theories = models.PositiveIntegerField(choices=MARKS)
    visits = [('offline', 1), ('online', 2), ('exited', 0)]
    visiting = models.PositiveIntegerField(choices=visits)
    # person = models.ForeignKey('PersonModel', on_delete=models.CASCADE)


class CoursePerformanceModel(models.Model):
    performance = models.ForeignKey("PerformanceModel", on_delete=models.CASCADE)
    course = models.ForeignKey("CourseModel", on_delete=models.CASCADE)
    person = models.ForeignKey("PersonModel", on_delete=models.CASCADE)


class AddressModel(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    flat = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100, blank=True)


class CourseModel(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    hours = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ManyToManyField('PersonModel', limit_choices_to=models.Q(status__title="teacher"))


class StatusModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class PersonModel(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.ForeignKey('AddressModel', on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField('CourseModel', through_fields=("person","course"),
                                     through='CoursePerformanceModel')
    status = models.ManyToManyField('StatusModel')
    changed = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name},,, {self.last_name}'