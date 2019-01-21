from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    student_id = models.ForeignKey(Student,  on_delete=models.CASCADE)
    task_date = models.DateTimeField('Task Date')
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.student_id.name + ' - '+ str(self.task_date)