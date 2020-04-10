from django.contrib import admin

# Register your models here.
from.models import *
admin.site.register(meter_data)

admin.site.register(helpline_data)
admin.site.register(donation_data)
admin.site.register(news_data)