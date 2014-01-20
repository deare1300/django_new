from django.contrib import admin
from test_dj.models import User,Poll,Choice

# Register your models here.

#class UserAdmin(admin.ModelAdmin):
#    fields=['name']


class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3
    
class PollAdmin(admin.ModelAdmin):
    list_display=['question','pub_date','was_pub_recently']
    list_filter=['pub_date']
    search_fields=['question']
    fieldsets=[
               (None,{'fields':['question']}),
               ('Date information',{'fields':['pub_date'],'classes':['collapse']})
               ]
    inlines=[ChoiceInline]
    pass


    
admin.site.register(User)
admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)
