from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    category=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category 
    
status_choices=[
    ('Published','Published'),
    ('Draft','Draft')
]  
class Articles(models.Model):
    title=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=1000)
    image=models.ImageField(upload_to='media')
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    short_description=models.TextField()
    detail_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=status_choices)
    is_treanding=models.BooleanField(default=False)







