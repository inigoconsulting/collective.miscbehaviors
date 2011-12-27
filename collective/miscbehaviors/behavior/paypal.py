from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from collective.miscbehaviors import _
from collective.miscbehaviors.behavior.utils import context_property


CURRENCIES=[
    'USD',
    'EUR'
]


class IPayPal(form.Schema):

    form.fieldset('paypal',
        label=_(u'Paypal'),
        fields=['paypal_type',
                'paypal_email',
                'paypal_currency',
                'paypal_itemname',
                'paypal_itemnumber',
                'paypal_amount',
                'paypal_shipping',
                'paypal_tax']
    )


    paypal_type = schema.Choice(
        title=_(u'Button Type'),
        values=[
            'donation',  
            'buynow'
        ],
        required=False,
    )

    paypal_email = schema.TextLine(
        title=_(u'Email'),
        required=False,
    )

    paypal_currency = schema.Choice(
        title=_(u'Currency'),
        values=CURRENCIES,
        required=False,
        default='USD'
    )

    paypal_itemname = schema.TextLine(
        title=_(u'Item Name / Organization'),
        required=False
    )

    paypal_itemnumber = schema.TextLine(
        title=_(u'Item Number / Donation ID'),
        required=False
    )

    paypal_amount = schema.Float(
        title=_(u'Amount'),
        description=_(u'Enter the amount. Set to -1 to allow user to enter their own amount'),
        required=False,
        default=0.0
    )

    paypal_shipping = schema.Float(
        title=_(u'Shipping'),
        description=_(u'Enter the shipping amount. Not needed for donation'),
        required=False,
        default=0.0
    )

    paypal_tax = schema.Float(
        title=_(u'Tax'),
        description=_(u'Enter the tax rate in %. Not needed for donation'),
        required=False,
        default=0.0
    )

alsoProvides(IPayPal, IFormFieldProvider)

class PayPal(object):

    implements(IPayPal)
    adapts(IDexterityContent)

    paypal_type = context_property('paypal_type')
    paypal_email = context_property('paypal_email')
    paypal_currency = context_property('paypal_currency')
    paypal_itemname = context_property('paypal_itemname')
    paypal_itemnumber = context_property('paypal_itemnumber')
    paypal_amount = context_property('paypal_amount')
    paypal_shipping = context_property('paypal_shipping')
    paypal_tax = context_property('paypal_tax')

    def __init__(self,context):
        self.context = context
