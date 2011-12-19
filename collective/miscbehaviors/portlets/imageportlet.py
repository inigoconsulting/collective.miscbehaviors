from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from zope.formlib import form

from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from zope import schema
from collective.miscbehaviors.behavior.leadimage import ILeadImage

class IImagePortlet(IPortletDataProvider):
    width = schema.Int(title=u'Width')
    height = schema.Int(title=u'Height')


class Assignment(base.Assignment):
    """Portlet assignment."""

    implements(IImagePortlet)

    def __init__(self, width=150, height=150):
        super(Assignment, self).__init__()
        self.width = width
        self.height = height

    @property
    def title(self):
        return u"Lead Image Behavior Portlet"


class AddForm(base.AddForm):
    form_fields = form.Fields(IImagePortlet)
    label = u'Add Lead Image Behavior Portlet'
    description = u'This portlet displays lead image of the current content'

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IImagePortlet)
    label = u'Edit Lead Image Behavior Portlet'
    description = u'This portlet displays lead image of the current content'


class Renderer(base.Renderer):
    """ Portlet renderer. """
    render = ViewPageTemplateFile("imageportlet.pt")

    @property
    def available(self):
        if not ILeadImage.providedBy(self.context):
            return False
        if not getattr(self.context, 'image'):
            return False
        return True
