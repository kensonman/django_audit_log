# -*- coding: utf-8 -*-
# File: django_audit_logs/models.py
# Date: 2020-03-16 13:32
# Author: Kenson Man <kenson@breakthrough.org.hk>

from django.contrib.contenttypes.models import ContentType
from django.db import models

class AuditLog(models.Model):
   ACTION_INSERT     = 0
   ACTION_UPDATE     = 1
   ACTION_DELETE     = 2
   ACTIONS           = (
      (ACTION_INSERT, _('django_audit_logs.AuditLog.ACTION_INSERT'),
      (ACTION_UPDATE, _('django_audit_logs.AuditLog.ACTION_UPDATE'),
      (ACTION_DELETE, _('django_audit_logs.AuditLog.ACTION_DELETE'),
   )
   contenttype       = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   action            = models.IntegerField(choices=ACTION, default=ACTION_UPDATE, verbose_name=_('django_audit_logs.AuditLog.action'))
   b4save            = models.TextField(null=True,empty=True,verbose_name=_('django_audit_logs.AuditLog.b4save'))
   afsave            = models.TextField(verbose_name=_('django_audit_logs.AuditLog.afsave'))
   timestamp         = models.DateTimeField(auto_now=True, verbose_name=_('django_audit_logs.AuditLog.timestamp'))
   user              = models.ForeignKey(
     settings.AUTH_USER_MODEL,
     default=get_current_user,
     null=True,
     blank=True,
     on_delete=models.PROTECTED, #Since Django 2.0, the on_delete field is required.
     verbose_name=_('django_audit_logs.AuditLog.user'),
     help_text=_('django_audit_logs.AuditLog.user.helptext'),
   )
