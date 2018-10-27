from django.contrib import admin

# Register your models here.
from cfg.models import Activity, Sense, Review


admin.site.register(Activity)
admin.site.register(Sense)
admin.site.register(Review)