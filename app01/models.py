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
    label_type_choices = [
        (1, '42区'),
        (2, '段子'),
        (3, '图片'),
        (4, '挨踢1024'),
        (5, '你问我答'),
    ]
    title = models.CharField('热点标题', max_length=1024)
    url = models.CharField('热点路径', max_length=10240)
    source = models.CharField('热点来源', max_length=3200)
    content = models.CharField('热点简介', max_length=3200)
    img_url = models.CharField('热点图片地址', max_length=3200)
    praises = models.IntegerField('热点获赞数量', default=0)
    comments = models.IntegerField('热点评论数量', default=0)
    label = models.IntegerField('热点标签', choices=label_type_choices)
    storage_time = models.DateTimeField('热点入库时间', auto_now_add=True)
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE, to_field='id', related_name='u')
    praise_user = models.ManyToManyField(to='UserInfo', related_name='user_praise')


class Comment(models.Model):
    news = models.ForeignKey(to='AllHot', to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(to='UserInfo', to_field='id', on_delete=models.CASCADE)
    content = models.CharField(max_length=1280)
    device = models.CharField(max_length=160, null=True)
    ctime = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(to='self', to_field='id', null=True, related_name='pc', on_delete=models.CASCADE)


