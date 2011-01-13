from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective.miscbehaviors import _
from collective.miscbehaviors.behavior.utils import context_property

import urlparse
from urllib import quote

class IRemoteURL(form.Schema):
    """
       Marker/Form interface for Remote URL
    """
   
    # -*- Your Zope schema definitions here ... -*-

    remoteUrl = schema.TextLine(
        title=_(u"Link"),
        default=u'http://',
        description=u"",
        required=False,
    )



alsoProvides(IRemoteURL,IFormFieldProvider)


class RemoteURL(object):
    """
       Adapter for Remote URL
    """
    implements(IRemoteURL)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    def _setRemoteUrl(self, value):
        if value:
            value = urlparse.urlunparse(urlparse.urlparse(value))
        self.context.remoteUrl = value

    def _getRemoteUrl(self):
        value = self.context.remoteUrl
        if not value: value = '' # ensure we have a string
        return quote(value, safe='?$#@/:=+;$,&%')

    remoteUrl = property(_getRemoteUrl, _setRemoteUrl)
