from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField('用户昵称', max_length=32, db_index=True)
    telephone = models.CharField('用户手机号', max_length=32, unique=True)
    pwd = models.CharField('用户密码', max_length=64)
    cTime = models.DateTimeField('用户注册时间', auto_now_add=True)
    sex = models.CharField('用户性别，0为女性，1为男性', max_length=32, default=0)
    sign = models.CharField('用户签名文档', max_length=32, default='')

    class Meta:
        index_together = [
            ('username', 'pwd')
        ]

        # unique_together = [
        #     ('username', 'pwd')
        # ]

class TelCode(models.Model):
    telephone = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=64)
    times = models.IntegerField(default=0)
    cTime = models.DateTimeField(auto_now_add=True)

class AllHot(models.Model):
    title = models.CharField('热点标题', max_length=32)
    url = models.CharField('热点路径', max_length=32)
    source = models.CharField('热点来源', max_length=32)
    content = models.CharField('热点简介', max_length=32)
    img_url = models.CharField('热点图片地址', max_length=32)
    praise = models.IntegerField('热点获赞数量', default=0)
    comments = models.IntegerField('热点评论数量', default=0)
    label = models.CharField('热点标签', max_length=32)
    storage_time = models.DateTimeField('热点入库时间', auto_now_add=True)