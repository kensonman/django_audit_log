from django.contrib import admin

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
   list_display=('contenttype', 'action', 'timestamp')
