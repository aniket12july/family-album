from django.contrib import admin
from album.models import Event, Photo

class PhotoInEvent(admin.TabularInline):
	model = Photo
	extra = 3

class EventAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['title', 'description']}),
		('Date information', 	{'fields': ['event_time'], 'classes': ['collapse']})
	]
	inlines = [PhotoInEvent]
	list_display = ('title', 'event_time')
	list_filter = ['event_time']
	search_fields = ['title']
	date_hierarchy = 'event_time'

admin.site.register(Event, EventAdmin)
