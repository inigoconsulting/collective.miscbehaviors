from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective.miscbehaviors import _
from collective.miscbehaviors.behavior.utils import context_property

class IFileAttachment(form.Schema):
    """
       Marker/Form interface for File Attachment
    """
   
    # -*- Your Zope schema definitions here ... -*-

    file = namedfile.NamedBlobFile(
        title=_(u"File Attachment"),
        description=u"",
        required=False,
    )



alsoProvides(IFileAttachment,IFormFieldProvider)


class FileAttachment(object):
    """
       Adapter for File Attachment
    """
    implements(IFileAttachment)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    file = context_property('file')
