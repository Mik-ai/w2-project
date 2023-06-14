from django.contrib import admin

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from .models import Skill, User, Project


class SkillsInLineProject(admin.TabularInline):
    model = Skill.projects_with.through
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [SkillsInLineProject]


class SkillsInLineUser(admin.TabularInline):
    model = Skill.users_with.through
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [SkillsInLineUser]


admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)

# Register your models here.
app_models = apps.get_app_config("w2core").get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
