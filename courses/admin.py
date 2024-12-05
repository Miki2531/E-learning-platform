from django.contrib import admin
from .models import Subject, Modules, Course

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    
class ModuleInline(admin.StackedInline):
    model = Modules

@admin.register(Course) 
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'created']
    list_filter = ['created', 'subject']
    search_fields= ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
    
    