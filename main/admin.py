from django.contrib import admin
from django.contrib.auth import models
from .models import Blog,Certificate,ContactProfile,Media,Portfolio,Skill,Testimonial,UserProfile,User

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user',)

# class UserProfilee(admin.ModelAdmin):
#     list_display_links=('id','user','email')

# admin.site.register(UserProfile,UserProfilee)

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')