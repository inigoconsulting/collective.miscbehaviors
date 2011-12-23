from plone.indexer import indexer
from collective.miscbehaviors.behavior.bodytext import IBodyText

@indexer(IBodyText)
def bodytext(obj):
    return obj.text
