
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.DO_NOTHING)
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.DO_NOTHING)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.DO_NOTHING)
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

class CompanyTable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField("Company Name",max_length=100)

class ComapnySchedule(models.Model):
    companyName=models.ForeignKey(CompanyTable,on_delete=models.DO_NOTHING)
    eligibleBranches=models.CharField("Eligible Branches",max_length=300,blank=False) 
    offers=models.IntegerField(blank=False)
    lastdateofregistration=models.DateTimeField(auto_now=False)

class CompanyCriteriaAndOffer(models.Model):
    recruitmentType=models.CharField("Recruitment Type",max_length=100)
    jobType=models.CharField("Job Type",max_length=20)
    eligibleBranches=models.CharField("Eligible Branches",max_length=300,blank=False)
    minimum_Gpa_Mtech=models.IntegerField("Minimum GPA 1st Sem Mtech",blank=False)
    minimum_Cgpa_Btech=models.IntegerField("Minimum CGPA in Undergrad",blank=False)
    maximumBackLog=models.IntegerField("Maximum Backlog")
    minimum_12_marks=models.IntegerField("Minimum Class 12 Marks")
    minimum_10_marks=models.IntegerField("Minimum Class 10 Marks")
    minimum_Dimploma_marks=models.IntegerField("Minimum Diploma Marks")
    stipend=models.CharField("Stipend",max_length=500,blank=False)
    location=models.CharField("Location",max_length=100)
    on_conversion=models.CharField("On Conversion CTC",max_length=100)
