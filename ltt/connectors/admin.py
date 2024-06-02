from django.contrib import admin

from .models import Conveyor, Belt, Press, Splice

@admin.register(Conveyor)
class ConveyorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Belt)
class BeltAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Press)
class PressAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Splice)
class SpliceAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'when_made', 'conveyor_machine']
    list_filter = ['owner', 'when_made', 'conveyor_machine', 'press']

