from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)
    admin_name = models.CharField(max_length=200)
    admin_priori = models.IntegerField()

    def __unicode__(self):
        return self.admin_username


class Air(models.Model):
    air_id = models.IntegerField()
    pm25 = models.FloatField()
    cloud = models.FloatField()
    rain = models.FloatField()
    ziwai = models.FloatField()
    guang = models.FloatField()
    clouddir = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __unicode__(self):
        return str(self.air_id)


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=200)
    news_type = models.IntegerField()
    news_content = models.CharField(max_length=10000)
    news_update_time = models.CharField(max_length=200)
    news_priori = models.IntegerField(default=0)
    news_readtime = models.IntegerField(default=0)
    news_author = models.ForeignKey(Admin, related_name='news', null=True)

    def __unicode__(self):
        return self.news_title


class Draft(models.Model):
    draft_id = models.AutoField(primary_key=True)
    draft_title = models.CharField(max_length=200)
    draft_type = models.IntegerField()
    draft_content = models.CharField(max_length=10000)
    draft_update_time = models.CharField(max_length=200)
    draft_author = models.ForeignKey(Admin, related_name='draft', null=True)

    def __unicode__(self):
        return self.draft_id


class Recycle(models.Model):
    recycle_id = models.AutoField(primary_key=True)
    news_id = models.IntegerField()
    recycle_title = models.CharField(max_length=200)
    recycle_type = models.IntegerField()
    recycle_content = models.CharField(max_length=10000)
    recycle_update_time = models.CharField(max_length=200)
    recycle_readtime = models.IntegerField()
    recycle_author = models.ForeignKey(Admin, related_name='recycle', null=True)

    def __unicode__(self):
        return self.recycle_id

# Create your models here.
