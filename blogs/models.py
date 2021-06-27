from django.db import models

# Create your models here.
class Blogpost(models.Model):
    
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=50, default="")
    chead0 = models.TextField(max_length=5000, default="",blank=True)
    head1 = models.CharField(max_length=50, default="")
    chead1 = models.TextField(max_length=5000, default="")
    head2 = models.CharField(max_length=50, default="")
    chead2 = models.TextField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', default="")

    def __str__(self):
        return self.title