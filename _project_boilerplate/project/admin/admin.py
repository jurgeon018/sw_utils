from django.contrib import admin
from sw_utils.sw_auth.admin import BoxUserAdmin
from project.models import ProjectUser 

class ProjectUserAdmin(BoxUserAdmin):
    pass 


admin.site.register(ProjectUser, ProjectUserAdmin)