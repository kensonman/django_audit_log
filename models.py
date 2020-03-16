# -*- coding: utf-8 -*-
# File: django_audit_logs/models.py
# Date: 2020-03-16 13:32
# Author: Kenson Man <kenson@breakthrough.org.hk>
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from webframe.CurrentUserMiddleware import get_current_user

class AuditLog(models.Model):
   class Meta(object):
      verbose_name         = _('django_audit_logs.AuditLog')
      verbose_name_plural  = _('django_audit_logs.AuditLogs')

   ACTION_INSERT     = 0
   ACTION_UPDATE     = 1
   ACTION_DELETE     = 2
   ACTIONS           = (
      (ACTION_INSERT, _('django_audit_logs.AuditLog.ACTION_INSERT'),
      (ACTION_UPDATE, _('django_audit_logs.AuditLog.ACTION_UPDATE'),
      (ACTION_DELETE, _('django_audit_logs.AuditLog.ACTION_DELETE'),
   )
   contenttype       = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   action            = models.IntegerField(
      choices=ACTIONS, 
      default=ACTION_UPDATE, 
      verbose_name=_('django_audit_logs.AuditLog.action'),
      help_text=_('django_audit_logs.AuditLog.action.help'),
   )
   b4save            = models.TextField(
      null=True,
      empty=True,
      verbose_name=_('django_audit_logs.AuditLog.b4save'),
      help_text=_('django_audit_logs.AuditLog.b4save.help'),
   )
   afsave            = models.TextField(
      verbose_name=_('django_audit_logs.AuditLog.afsave'),
      help_text=_('django_audit_logs.AuditLog.afsave.help'),
   )
   timestamp         = models.DateTimeField(
      auto_now=True, 
      verbose_name=_('django_audit_logs.AuditLog.timestamp'),
      help_text=_('django_audit_logs.AuditLog.timestamp.help'),
   )
   user              = models.ForeignKey(
     settings.AUTH_USER_MODEL,
     default=get_current_user,
     on_delete=models.PROTECTED, #Since Django 2.0, the on_delete field is required.
     verbose_name=_('django_audit_logs.AuditLog.user'),
     help_text=_('django_audit_logs.AuditLog.user.helptext'),
   )

class Config(models.Model):
   class Meta(object):
      verbose_name         = _('django_audit_logs.Config')
      verbose_name_plural  = _('django_audit_logs.Configs')


   contenttype       = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   insert_ind        = models.BooleanField(default=True, verbose_name=_('django_audit_logs.Config.insert_ind'), help_text=_('django_audit_logs.Config.insert_ind.help'))
   update_ind        = models.BooleanField(default=True, verbose_name=_('django_audit_logs.Config.update_ind'), help_text=_('django_audit_logs.Config.update_ind.help'))
   delete_ind        = models.BooleanField(default=True, verbose_name=_('django_audit_logs.Config.delete_ind'), help_text=_('django_audit_logs.Config.delete_ind.help'))
   
