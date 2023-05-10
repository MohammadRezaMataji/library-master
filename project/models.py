from datetime import datetime,timedelta
from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=400, null=True, blank=True)
    book_image = models.ImageField(null=True, blank=True, default="cover-default--book.svg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Is_borrowed = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up Vote'),
        ('down', 'Down Vote'),
    )
    #owner = 
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name
    
def get_returndate():
    return datetime.today() + timedelta(days=8)

#class Book_Issue(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    book_instance = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True,help_text="Date the book is issued")
    due_date = models.DateTimeField(default=get_returndate(),help_text="Date the book is due to")
    date_returned=models.DateField(null=True, blank=True,help_text="Date the book is returned")
    remarks_on_issue = models.CharField(max_length=100, default="Book in good condition", help_text="Book remarks/condition during issue")
    remarks_on_return = models.CharField(max_length=100, default="Book in good condition", help_text="Book remarks/condition during return")

    def __str__(self):
        return self.student.fullname + " borrowed " + self.book.book_title

