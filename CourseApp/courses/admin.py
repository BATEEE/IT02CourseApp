from ctypes.wintypes import tagMSG

from django.contrib import admin
from courses.models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_date', 'category']
    search_fields = ['subject']
    list_filter = ['id', 'created_date']
    list_editable = ['subject']
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=obj.image.name)
            )


    def image_view(self, course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='260' />")


class MyLessonAdmin(admin.ModelAdmin):
    form = LessonForm
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=obj.image.name)
            )


admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)

