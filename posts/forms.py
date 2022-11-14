from django import forms
from ckeditor.fields import RichTextFormField
  

class Post(forms.Form):
    title = forms.CharField(max_length=20)
    slug = forms.CharField(max_length=20)
    author = forms.IntegerField()
    content = forms.CharField(max_length=20)
    status = forms.IntegerField(choices=STATUS, default=0)
    
#  title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)   
