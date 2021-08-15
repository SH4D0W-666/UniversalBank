from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class customer(admin.ModelAdmin):
    list_display = ['id','name','email','bal']

@admin.register(Transfer)
class Transfer(admin.ModelAdmin):
    list_display = ['sender','reciever','amount','date']