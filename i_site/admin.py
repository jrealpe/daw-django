from django.contrib import admin
from .models import *


class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 1


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [RequirementInline,]
    list_display = ('name', 'description', 'date_created', 'date_last_updated', 'is_activated')
    list_display_links = ('name', 'description')


@admin.register(W2W)
class W2WAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'date_created', 'date_last_updated', 'is_activated')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline,]
    list_display = ('name', 'course', 'phone', 'email', 'charge', 'is_activated')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'date_last_updated', 'is_activated')
