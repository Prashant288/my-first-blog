from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Contents(models.Model):
    title = models.CharField(max_length=2000)
    textarea = models.TextField()
    link_site = models.TextField()
    pub_date = models.DateTimeField('date published')
    id = models.AutoField(primary_key=True)
    upload_image_to = models.FileField(upload_to='media/blog/images',blank=True)
    upload_video_to = models.FileField(upload_to='media/polls/videos',blank=True)
    BUSINESS = 'bu'
    CULTURE = 'cu'
    DESIGN = 'de'
    HEALTH = 'he'
    INDIA = 'in'
    OPINION = 'op'
    POLITICS = 'po'
    SCIENCE = 'sc'
    STYLE = 'st'
    TECHNOLOGY  = 'te'
    TRAVEL = 'tr'
    WORLD = 'wo'
    TOPPING_CHOICES = (
        (CULTURE, 'Culture'),
        (BUSINESS, 'Business'),
        (DESIGN, 'Design'),
        (HEALTH, 'Health'),
        (INDIA,'India'),
        (OPINION,'Opinion'),
        (POLITICS,'Politics'),
        (SCIENCE,'Science'),
        (STYLE,'Style'),
        (TECHNOLOGY,'Technology'),
        (TRAVEL,'Travel'),
        (WORLD,'World'),
    )

    toppings = models.CharField(
        max_length=10,
        choices=TOPPING_CHOICES
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id,])

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Comment(models.Model):
    post = models.ForeignKey(Contents, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))
