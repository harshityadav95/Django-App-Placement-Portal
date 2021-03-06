# Generated by Django 3.0.6 on 2020-05-29 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyCriteriaAndOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruitmentType', models.CharField(max_length=100, verbose_name='Recruitment Type')),
                ('jobType', models.CharField(max_length=20, verbose_name='Job Type')),
                ('eligibleBranches', models.CharField(max_length=300, verbose_name='Eligible Branches')),
                ('minimum_Gpa_Mtech', models.IntegerField(verbose_name='Minimum GPA 1st Sem Mtech')),
                ('minimum_Cgpa_Btech', models.IntegerField(verbose_name='Minimum CGPA in Undergrad')),
                ('maximumBackLog', models.IntegerField(verbose_name='Maximum Backlog')),
                ('minimum_12_marks', models.IntegerField(verbose_name='Minimum Class 12 Marks')),
                ('minimum_10_marks', models.IntegerField(verbose_name='Minimum Class 10 Marks')),
                ('minimum_Dimploma_marks', models.IntegerField(verbose_name='Minimum Diploma Marks')),
                ('stipend', models.CharField(max_length=500, verbose_name='Stipend')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('on_conversion', models.CharField(max_length=100, verbose_name='On Conversion CTC')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Company Name')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topics', to='boards.Board')),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='boards.Topic')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComapnySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eligibleBranches', models.CharField(max_length=300, verbose_name='Eligible Branches')),
                ('offers', models.IntegerField()),
                ('lastdateofregistration', models.DateTimeField()),
                ('companyName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='boards.CompanyTable')),
            ],
        ),
    ]
