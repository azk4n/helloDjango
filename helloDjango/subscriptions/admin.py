#coding: utf-8
from django.contrib import admin
from helloDjango.subscriptions.models import Subscription
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, gettext as _


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    #cria a sidebar com filtro de data
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    #traduz a short_description do created at
    subscribed_today.short_description = _(u'Inscrito hoje?')
    #cria o sinalizador true e false
    subscribed_today.boolean = True
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        msg = ungettext(
            u'%i inscrição foi marcada como paga!',
            u'%i inscrições foram marcadas como pagas!',
            count
        )
        self.message_user(request, msg % count)
    mark_as_paid.short_description = _('Marcar como pago')

admin.site.register(Subscription, SubscriptionAdmin)
