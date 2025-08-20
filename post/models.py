from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length = 50)
    txt = models.TextField(max_length = 7000)
    is_enable = models.BooleanField(default = False)
    publish_date = models.DateField(null = True, blank = True)
    created_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}, {}'.format(self.pk, self.title)

class comment(models.Model):
    post = models.ForeignKey(post, on_delete = models.CASCADE)
    txt = models.TextField (max_length = 7000)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateField(auto_now = True)
