from django.contrib import admin

from .models import Contents , Question ,Comment




class ContentsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Text area', {'fields': ['textarea']}),
        ('Site link', {'fields':['link_site']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Images Upload', {'fields':['upload_image_to']}),
        ('Videos Upload', {'fields':['upload_video_to']}),
        ('Select Tag', {'fields':['toppings']}),



    ]

    list_display = ('title','textarea','link_site','pub_date', 'was_published_recently','id','toppings')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Contents, ContentsAdmin)



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment)
