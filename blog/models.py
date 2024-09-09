from django.db import models

class BlogPost(models.Model):
    title = models.CharField(default='', max_length=200)
    content = models.TextField(default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    def _str_(self):
        return self.title
    
        