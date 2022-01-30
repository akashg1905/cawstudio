from django.contrib import admin

# Register your models here.
from boxoffice.models import City,Theatre,Movie,Show,Booking

admin.site.register(City),
admin.site.register(Theatre),
admin.site.register(Movie),
admin.site.register(Show),
admin.site.register(Booking),