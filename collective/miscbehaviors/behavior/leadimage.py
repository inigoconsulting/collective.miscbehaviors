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

class ILeadImage(form.Schema):
    """
       Marker/Form interface for Lead Image
    """
   
    # -*- Your Zope schema definitions here ... -*-

    image = namedfile.NamedBlobImage(
        title=_(u"Lead Image"),
        description=u"",
        required=False,
    )

    imageCaption = schema.TextLine(
        title=_(u"Lead Image Caption"),
        description=u"",
        required=False,
    )




alsoProvides(ILeadImage,IFormFieldProvider)

class LeadImage(object):
    """
       Adapter for Lead Image
    """
    implements(ILeadImage)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    imageCaption = context_property('imageCaption')
    image = context_property('image')
