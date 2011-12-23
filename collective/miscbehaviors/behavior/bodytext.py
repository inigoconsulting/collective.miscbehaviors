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

class IBodyText(form.Schema):
    """
        Marker/Form interface for Body Text
    """
   
    # -*- Your Zope schema definitions here ... -*-

    dexteritytextindexer.searchable('text')
    form.widget(text="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    text = schema.Text(
        title=_(u'label_body_text', u"Body Text"),
        description=u'',
        required=False,
    )

alsoProvides(IBodyText,IFormFieldProvider)


class BodyText(object):
    """
      Adapter for Body Text
    """
    implements(IBodyText)
    adapts(IDexterityContent)

    def __init__(self,context):
       self.context = context

    # -*- Your behavior property setters & getters here ... -*-

    text = context_property('text')
