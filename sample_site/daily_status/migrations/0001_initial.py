# Generated by Django 2.1.5 on 2019-01-21 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_date', models.DateTimeField(verbose_name='Task Date')),
                ('comment_text', models.CharField(max_length=200)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_status.Student')),
            ],
        ),
    ]
