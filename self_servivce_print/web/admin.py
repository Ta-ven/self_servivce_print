from django.contrib import admin
from web import models
from status import models as m


admin.site.register(models.Time)
admin.site.register(models.Project)
admin.site.register(models.Content)
admin.site.register(m.Department)
admin.site.register(m.User)

