from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField('Tag')
    photo = models.ImageField(blank=True, null=True, default='fah.jpg')    
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    
    def __str__(self) -> str:
        return self.title
      
# class Review(models.Model):
#     # author
#     VOTES = (
#         ('up', 'Up Vote'), 
#         ('down', 'Down Vote')
#     )
#     content = models.CharField(max_length=300)
#     vote = models.CharField(max_length=20, choices=VOTES, null=True, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

#     def __str__(self) -> str:
#         return self.content
    
    

class tag(models.Model):
    name = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name




