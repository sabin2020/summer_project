from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from sys import argv

# Create your models here.
class Project(models.Model):
    # user
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    unique_name = models.CharField(max_length=50,null=True)
    # proposal
    proposal_file=models.FileField(blank=True,null=True,upload_to='proposals/')
    proposal_reason=models.TextField(null=True)
    condition= [
    ('selected', 'selected'),
    ('not_selected', 'not_selected'),
    ('not_verified','not_verified'),
    ]
    selected_proposal_condition=models.CharField(max_length=12,choices=condition,default='not_verified' )
    # progress
    name = models.CharField(max_length=50,null=True)
    git_url = models.URLField(max_length=200,null=True)
    references = models.TextField(null=True)
    tools = models.TextField(null=True)
    updated_date = models.DateTimeField(auto_now_add=True,null=True)
    # Report
    report_file=models.FileField(blank=True,null=True,upload_to='reports/')
    report_reason=models.TextField(null=True)
    condition= [
    ('selected', 'selected'),
    ('not_selected', 'not_selected'),
    ('not_verified','not_verified'),
    ]
    selected_report_condition=models.CharField(max_length=12,choices=condition,default='not_verified' )

class Watchlist(models.Model):
    # teacher = models.ManyToManyField(User)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,null=True)
