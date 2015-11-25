from django.contrib import admin
from .models import Project
from .models import Resource
from .models import Task


class TaskInline(admin.StackedInline):
    classes = ('grp-collapse grp-open',)
    model = Task
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    fieldSets= [(None,{'fields': ['id', 'title', 'start', 'end']}),
                ('属性', {'fields': ['timeFormat', 'weekstartsmonday']})
    ]

    def project_period(self):
        return self.end - self.start

    #inlines = [TaskInline]
    list_filter = ['start']
    list_display = ('title', 'start', 'end', project_period)


class TaskAdmin(admin.ModelAdmin):
    def get_projectname(self):
        return 0
    fieldSets = (get_projectname,'title', 'start', 'end', 'allocate', 'duration', 'priority', 'complete')
    def task_list(self):
        tasklist = self.objects.all()

    def task_period(self):
        return self.endDate - self.startDate
    list_filter=['start']
    list_display = ('title', 'start', 'end',  'duration', 'priority', 'complete')
    search_fields=['title']



admin.site.register(Project, ProjectAdmin)
admin.site.register(Resource)
admin.site.register(Task, TaskAdmin)





# Register your models here.
