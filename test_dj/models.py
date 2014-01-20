from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return self.name

class Poll(models.Model):    
    question=models.CharField(max_length=200)
    pub_date=models.DateTimeField('published date')
    
    def was_pub_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
        
    def __unicode__(self):
        return self.question
    
    ##this other is for admin
    #for the order
    was_pub_recently.admin_order_field='pub_date'
    
    #show the result 
    was_pub_recently.boolean=True
    
    #the column name
    
    was_pub_recently.short_description='published recently?'


class Choice(models.Model):
    poll=models.ForeignKey(Poll)
    test=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.test