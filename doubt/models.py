from django.db import models

# Create your models here.
class DoubtQuestion(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='doubt/post', default ="" )
    date = models.DateField()
    

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250 , default="")
    phone = models.CharField(max_length=13, default="")
    email = models.CharField(max_length=100, default="")
    time = models.DateTimeField(auto_now=True,  blank=True )
    message = models.TextField()

    def __str__(self):
        return "Message from" + self.email

class LiveClass(models.Model):
    sno = models.AutoField(primary_key= True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13, default="")
    std = models.CharField(max_length=4)
    subject = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=250, default="")
    stream = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='doubt/images', default ="" )

    def __str__(self):
        return self.name
        