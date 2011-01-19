from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective.miscbehaviors.behavior.utils import context_property

from collective.miscbehaviors import _


class IContactInfo(form.Schema):
    """
       Marker/Form interface for Contact Info
    """
   
    # -*- Your Zope schema definitions here ... -*-



    contactName = schema.TextLine(
        title=_(u"Contact Name"),
        description=u"",
        required=False,
    )

    contactEmail = schema.TextLine(
        title=_(u"Contact Email"),
        description=u"",
        required=False,
    )

    contactPhone = schema.TextLine(
        title=_(u"Contact Phone"),
        description=u"",
        required=False,
    )



alsoProvides(IContactInfo,IFormFieldProvider)

class ContactInfo(object):
    """
       Adapter for Contact Info
    """
    implements(IContactInfo)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    contactPhone = context_property('contactPhone')
    contactEmail = context_property('contactEmail')
    contactName = context_property('contactName')
