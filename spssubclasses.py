#!/usr/bin/env python

#
# Generated Fri Aug  3 16:48:57 2018 by generateDS.py version 2.29.19.
# Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'c:/zzcloud/dropbox/work/sps/sps/spsclasses.py')
#   ('-s', 'c:/zzcloud/dropbox/work/sps/sps/spssubclasses.py')
#   ('--super', 'spsclasses')
#
# Command line arguments:
#   c:/zzcloud/dropbox/work/sps/sps/inspectionschema.xml
#
# Command line:
#   C:/Users/fsh/AppData/Roaming/Python/Python36/Scripts/generateDS.py -f -o "c:/zzcloud/dropbox/work/sps/sps/spsclasses.py" -s "c:/zzcloud/dropbox/work/sps/sps/spssubclasses.py" --super="spsclasses" c:/zzcloud/dropbox/work/sps/sps/inspectionschema.xml
#
# Current working directory (os.getcwd()):
#   arcgispro-py3
#

import sys
from lxml import etree as etree_

import spsclasses as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class inspectionsSub(supermod.inspections):
    def __init__(self, inspection=None):
        super(inspectionsSub, self).__init__(inspection, )
supermod.inspections.subclass = inspectionsSub
# end class inspectionsSub


class inspectionTypeSub(supermod.inspectionType):
    def __init__(self, serialNumber=None, forestManager=None, location=None, stand=None, siteId=None, subSite=None, bioRegion=None, siteType=None, date=None, inspector=None, hostSpec=None, estabYear=None, treatment=None, stemsPerHa=None, diam=None, height=None, inspType=None, sampleType=None, comments=None, points=None, disorders=None, identifications=None):
        super(inspectionTypeSub, self).__init__(serialNumber, forestManager, location, stand, siteId, subSite, bioRegion, siteType, date, inspector, hostSpec, estabYear, treatment, stemsPerHa, diam, height, inspType, sampleType, comments, points, disorders, identifications, )
supermod.inspectionType.subclass = inspectionTypeSub
# end class inspectionTypeSub


class pointsTypeSub(supermod.pointsType):
    def __init__(self, datum=None, projection=None, comments=None, point=None):
        super(pointsTypeSub, self).__init__(datum, projection, comments, point, )
supermod.pointsType.subclass = pointsTypeSub
# end class pointsTypeSub


class pointTypeSub(supermod.pointType):
    def __init__(self, east=None, north=None, err=None):
        super(pointTypeSub, self).__init__(east, north, err, )
supermod.pointType.subclass = pointTypeSub
# end class pointTypeSub


class disordersTypeSub(supermod.disordersType):
    def __init__(self, disorder=None):
        super(disordersTypeSub, self).__init__(disorder, )
supermod.disordersType.subclass = disordersTypeSub
# end class disordersTypeSub


class disorderTypeSub(supermod.disorderType):
    def __init__(self, name=None, comments=None, agent=None, aspect=None, terrain=None, position=None, type_=None, severity=None, severityPercent=None, extent=None, incidencePercent=None, isSampleTaken=None):
        super(disorderTypeSub, self).__init__(name, comments, agent, aspect, terrain, position, type_, severity, severityPercent, extent, incidencePercent, isSampleTaken, )
supermod.disorderType.subclass = disorderTypeSub
# end class disorderTypeSub


class identificationsTypeSub(supermod.identificationsType):
    def __init__(self, identification=None):
        super(identificationsTypeSub, self).__init__(identification, )
supermod.identificationsType.subclass = identificationsTypeSub
# end class identificationsTypeSub


class identificationTypeSub(supermod.identificationType):
    def __init__(self, name=None, agent=None, family=None, type_=None, labDate=None, dateIdentified=None, person=None, cultureNo=None, retained=None, herbariumNo=None, confidence=None, effect=None, comments=None):
        super(identificationTypeSub, self).__init__(name, agent, family, type_, labDate, dateIdentified, person, cultureNo, retained, herbariumNo, confidence, effect, comments, )
supermod.identificationType.subclass = identificationTypeSub
# end class identificationTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'inspections'
        rootClass = supermod.inspections
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'inspections'
        rootClass = supermod.inspections
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from io import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'inspections'
        rootClass = supermod.inspections
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'inspections'
        rootClass = supermod.inspections
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from spsclasses import *\n\n')
        sys.stdout.write('import spsclasses as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
