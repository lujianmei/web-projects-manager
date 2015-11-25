from django.db import models


class Project(models.Model):
    id = models.CharField(u'唯一标识', max_length=256, primary_key=True, unique=True)
    title = models.CharField(u'名称', max_length=256)
    start = models.DateTimeField(u'开始时间',  editable=True)
    end = models.DateTimeField(u'结束时间',  editable=True)
    #timeFormat = models.CharField(u'时间格式', max_length=10, default='yyyy-MM-dd')
    weekstartsmonday = models.BooleanField(u'周一开始', default=True)

    def __str__(self):
        return self.title

class Resource(models.Model):
    #resource = models.CharField(u'唯一标识', max_length=50, blank=False,null=False)
    #id = models.CharField(u'唯一标识', max_length=256, primary_key=True, unique=True)
    name = models.CharField(u'姓名', max_length=50)
    email = models.CharField(u'邮箱', max_length=50)
    rate = models.IntegerField(u'工价')

    def __str__(self):
        return self.name

class Task(models.Model):
    #id = models.CharField(u'唯一标识', max_length=256)
    #uniqueid = models.CharField(u'任务名称', unique=True, max_length=256, default='taskname')
    title = models.CharField(u'名称', max_length=256)
    projectid = models.ForeignKey(Project)
    #projectid = models.CharField(u'所属项目', max_length=256)
    #allocate = models.CharField(u'资源分配', max_length=256)
    #allocate = models.ForeignKey(Resource)
    allocate = models.ManyToManyField(Resource, through='TaskAssign')
    complete = models.CharField(u'完成情况', max_length=256)
    depends = models.CharField(u'依赖任务', max_length=256)
    duration = models.CharField(u'周期', max_length=256)
    priority = models.CharField(u'优先级', max_length=256)
    start = models.DateTimeField(u'开始时间', editable=True)
    end = models.DateTimeField(u'结束时间', editable=True)

    def __str__(self):
        return self.title

class TaskAssign(models.Model):
    resource = models.ForeignKey(Resource)
    task = models.ForeignKey(Task)
    date_assign = models.DateField()


# Create your models here.
