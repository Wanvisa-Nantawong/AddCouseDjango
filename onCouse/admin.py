from django.contrib import admin

from .models import AddCouse,Student,AddCouseTimeline

# Register your models here.
class AddCouseTimelineInline(admin.TabularInline) :
    model = AddCouseTimeline



class ActivityAdmin(admin.ModelAdmin) :
    list_display = ['id',
                    'activity_name',
                    'act_type',
                    'activity_type',
                    'activity_date']
    list_display_links = ['id',
                          'activity_name']

    inlines = [
        AddCouseTimelineInline
    ]

    COLORDICT = {
        'AV' : 'red',
        'UV' : 'green',
    }
    save_as = True

    fields = ('activity_name',
              'activity_type',
              'activity_desc',
              'participant')


admin.site.register(AddCouse,ActivityAdmin)
admin.site.register(Student)
admin.site.register(AddCouseTimeline)
