from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from zope.formlib import form

from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from zope import schema
from collective.miscbehaviors.behavior.paypal import IPayPal
import hashlib
import random


PAYPAL_COMMAND={
    'donation': '_donations',
    'buynow': '_xclick'
}


PAYPAL_BN = {
    'donation': 'PP-DonationsBF:btn_donateCC_LG.gif:NonHostedGuest',
    'buynow': 'PP-BuyNowBF:btn_buynowCC_LG.gif:NonHostedGuest'
}

BUTTON_IMAGES={
    'donation': 'https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif',
    'buynow': 'https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif'
}

BUTTON_SUBTYPE={
    'buynow': 'services'
}


class IPayPalPortlet(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    """Portlet assignment."""

    implements(IPayPalPortlet)

    @property
    def title(self):
        return u"PayPal Behavior Portlet"


class AddForm(base.NullAddForm):
    
    def create(self):
        return Assignment()

class Renderer(base.Renderer):
    """ Portlet renderer. """
    render = ViewPageTemplateFile("paypal.pt")

    @property
    def available(self):
        if not IPayPal.providedBy(self.context):
            return False
        if not (
            getattr(self.context, 'paypal_type', None) and
            getattr(self.context, 'paypal_email', None) and 
            getattr(self.context, 'paypal_currency', None) and
            getattr(self.context, 'paypal_itemname', None)
            ):
            return False
        return True

    def image_url(self):
        return BUTTON_IMAGES[self.context.paypal_type]

    def paypal_command(self):
        return PAYPAL_COMMAND[self.context.paypal_type]

    def paypal_bn(self):
        return PAYPAL_BN[self.context.paypal_type]

    def button_subtype(self):
        return BUTTON_SUBTYPE.get(self.context.paypal_type, '')
