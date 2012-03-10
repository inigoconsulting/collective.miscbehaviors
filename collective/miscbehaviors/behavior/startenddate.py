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

from collective import dexteritytextindexer

class IStartEndDate(form.Schema):
    """
        Marker/Form interface for Start/End Dates
    """
   
    # -*- Your Zope schema definitions here ... -*-

    startDate = schema.Datetime(
        title=_(u"Start Date"),
        description=u'',
        required=True,
    )

    endDate = schema.Datetime(
        title=_(u"End Date"),
        description=u'',
        required=True,
    )


alsoProvides(IStartEndDate,IFormFieldProvider)


class StartEndDate(object):
    """
      Adapter for Start/End Dates
    """
    implements(IStartEndDate)
    adapts(IDexterityContent)

    def __init__(self,context):
       self.context = context

    # -*- Your behavior property setters & getters here ... -*-

    startDate = context_property('startDate')
    endDate = context_property('endDate')
