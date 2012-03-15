from plone.indexer import indexer
from collective.miscbehaviors.behavior.bodytext import IBodyText
from collective.miscbehaviors.behavior.startenddate import IStartEndDate

@indexer(IStartEndDate)
def startDate(obj):
    return obj.startDate

@indexer(IStartEndDate)
def endDate(obj):
    return obj.endDate

