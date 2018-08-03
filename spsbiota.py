# c:/zzcloud/dropbox/work/sps/sps/spsbiota.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e6e2cef30043af3592b0c3c54d3fc8bd15294198
# Generated 2018-07-30 17:22:38.908263 by PyXB version 1.2.6 using Python 3.6.5.final.0
# Namespace URN:sps-inspection

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:92a9158a-93b8-11e8-a907-9cb6d0da5030')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('URN:sps-inspection', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}inspection uses Python identifier inspection
    __inspection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inspection'), 'inspection', '__URNsps_inspection_CTD_ANON_URNsps_inspectioninspection', True, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 6, 8), )

    
    inspection = property(__inspection.value, __inspection.set, None, None)

    _ElementMap.update({
        __inspection.name() : __inspection
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 7, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}serialNumber uses Python identifier serialNumber
    __serialNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serialNumber'), 'serialNumber', '__URNsps_inspection_CTD_ANON__URNsps_inspectionserialNumber', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 9, 14), )

    
    serialNumber = property(__serialNumber.value, __serialNumber.set, None, None)

    
    # Element {URN:sps-inspection}forestManager uses Python identifier forestManager
    __forestManager = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'forestManager'), 'forestManager', '__URNsps_inspection_CTD_ANON__URNsps_inspectionforestManager', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 10, 14), )

    
    forestManager = property(__forestManager.value, __forestManager.set, None, None)

    
    # Element {URN:sps-inspection}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__URNsps_inspection_CTD_ANON__URNsps_inspectionlocation', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 11, 14), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element {URN:sps-inspection}stand uses Python identifier stand
    __stand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stand'), 'stand', '__URNsps_inspection_CTD_ANON__URNsps_inspectionstand', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 12, 14), )

    
    stand = property(__stand.value, __stand.set, None, None)

    
    # Element {URN:sps-inspection}siteId uses Python identifier siteId
    __siteId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'siteId'), 'siteId', '__URNsps_inspection_CTD_ANON__URNsps_inspectionsiteId', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 13, 14), )

    
    siteId = property(__siteId.value, __siteId.set, None, None)

    
    # Element {URN:sps-inspection}subSite uses Python identifier subSite
    __subSite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSite'), 'subSite', '__URNsps_inspection_CTD_ANON__URNsps_inspectionsubSite', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 14, 14), )

    
    subSite = property(__subSite.value, __subSite.set, None, None)

    
    # Element {URN:sps-inspection}bioRegion uses Python identifier bioRegion
    __bioRegion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bioRegion'), 'bioRegion', '__URNsps_inspection_CTD_ANON__URNsps_inspectionbioRegion', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 15, 14), )

    
    bioRegion = property(__bioRegion.value, __bioRegion.set, None, None)

    
    # Element {URN:sps-inspection}siteType uses Python identifier siteType
    __siteType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'siteType'), 'siteType', '__URNsps_inspection_CTD_ANON__URNsps_inspectionsiteType', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 16, 14), )

    
    siteType = property(__siteType.value, __siteType.set, None, None)

    
    # Element {URN:sps-inspection}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'date'), 'date', '__URNsps_inspection_CTD_ANON__URNsps_inspectiondate', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 17, 14), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {URN:sps-inspection}inspector uses Python identifier inspector
    __inspector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inspector'), 'inspector', '__URNsps_inspection_CTD_ANON__URNsps_inspectioninspector', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 18, 14), )

    
    inspector = property(__inspector.value, __inspector.set, None, None)

    
    # Element {URN:sps-inspection}hostSpec uses Python identifier hostSpec
    __hostSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hostSpec'), 'hostSpec', '__URNsps_inspection_CTD_ANON__URNsps_inspectionhostSpec', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 19, 14), )

    
    hostSpec = property(__hostSpec.value, __hostSpec.set, None, None)

    
    # Element {URN:sps-inspection}estabYear uses Python identifier estabYear
    __estabYear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'estabYear'), 'estabYear', '__URNsps_inspection_CTD_ANON__URNsps_inspectionestabYear', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 20, 14), )

    
    estabYear = property(__estabYear.value, __estabYear.set, None, None)

    
    # Element {URN:sps-inspection}treatment uses Python identifier treatment
    __treatment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'treatment'), 'treatment', '__URNsps_inspection_CTD_ANON__URNsps_inspectiontreatment', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 21, 14), )

    
    treatment = property(__treatment.value, __treatment.set, None, None)

    
    # Element {URN:sps-inspection}stemsPerHa uses Python identifier stemsPerHa
    __stemsPerHa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stemsPerHa'), 'stemsPerHa', '__URNsps_inspection_CTD_ANON__URNsps_inspectionstemsPerHa', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 22, 14), )

    
    stemsPerHa = property(__stemsPerHa.value, __stemsPerHa.set, None, None)

    
    # Element {URN:sps-inspection}diam uses Python identifier diam
    __diam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'diam'), 'diam', '__URNsps_inspection_CTD_ANON__URNsps_inspectiondiam', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 23, 14), )

    
    diam = property(__diam.value, __diam.set, None, None)

    
    # Element {URN:sps-inspection}height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'height'), 'height', '__URNsps_inspection_CTD_ANON__URNsps_inspectionheight', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 24, 14), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element {URN:sps-inspection}inspType uses Python identifier inspType
    __inspType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inspType'), 'inspType', '__URNsps_inspection_CTD_ANON__URNsps_inspectioninspType', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 25, 14), )

    
    inspType = property(__inspType.value, __inspType.set, None, None)

    
    # Element {URN:sps-inspection}sampleType uses Python identifier sampleType
    __sampleType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sampleType'), 'sampleType', '__URNsps_inspection_CTD_ANON__URNsps_inspectionsampleType', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 26, 14), )

    
    sampleType = property(__sampleType.value, __sampleType.set, None, None)

    
    # Element {URN:sps-inspection}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comments'), 'comments', '__URNsps_inspection_CTD_ANON__URNsps_inspectioncomments', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 27, 14), )

    
    comments = property(__comments.value, __comments.set, None, None)

    
    # Element {URN:sps-inspection}points uses Python identifier points
    __points = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'points'), 'points', '__URNsps_inspection_CTD_ANON__URNsps_inspectionpoints', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 28, 14), )

    
    points = property(__points.value, __points.set, None, None)

    
    # Element {URN:sps-inspection}disorders uses Python identifier disorders
    __disorders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'disorders'), 'disorders', '__URNsps_inspection_CTD_ANON__URNsps_inspectiondisorders', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 47, 14), )

    
    disorders = property(__disorders.value, __disorders.set, None, None)

    
    # Element {URN:sps-inspection}identifications uses Python identifier identifications
    __identifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifications'), 'identifications', '__URNsps_inspection_CTD_ANON__URNsps_inspectionidentifications', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 70, 14), )

    
    identifications = property(__identifications.value, __identifications.set, None, None)

    _ElementMap.update({
        __serialNumber.name() : __serialNumber,
        __forestManager.name() : __forestManager,
        __location.name() : __location,
        __stand.name() : __stand,
        __siteId.name() : __siteId,
        __subSite.name() : __subSite,
        __bioRegion.name() : __bioRegion,
        __siteType.name() : __siteType,
        __date.name() : __date,
        __inspector.name() : __inspector,
        __hostSpec.name() : __hostSpec,
        __estabYear.name() : __estabYear,
        __treatment.name() : __treatment,
        __stemsPerHa.name() : __stemsPerHa,
        __diam.name() : __diam,
        __height.name() : __height,
        __inspType.name() : __inspType,
        __sampleType.name() : __sampleType,
        __comments.name() : __comments,
        __points.name() : __points,
        __disorders.name() : __disorders,
        __identifications.name() : __identifications
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 29, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}datum uses Python identifier datum
    __datum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'datum'), 'datum', '__URNsps_inspection_CTD_ANON_2_URNsps_inspectiondatum', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 31, 20), )

    
    datum = property(__datum.value, __datum.set, None, None)

    
    # Element {URN:sps-inspection}projection uses Python identifier projection
    __projection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'projection'), 'projection', '__URNsps_inspection_CTD_ANON_2_URNsps_inspectionprojection', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 32, 20), )

    
    projection = property(__projection.value, __projection.set, None, None)

    
    # Element {URN:sps-inspection}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comments'), 'comments', '__URNsps_inspection_CTD_ANON_2_URNsps_inspectioncomments', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 33, 20), )

    
    comments = property(__comments.value, __comments.set, None, None)

    
    # Element {URN:sps-inspection}point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'point'), 'point', '__URNsps_inspection_CTD_ANON_2_URNsps_inspectionpoint', True, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 34, 20), )

    
    point = property(__point.value, __point.set, None, None)

    _ElementMap.update({
        __datum.name() : __datum,
        __projection.name() : __projection,
        __comments.name() : __comments,
        __point.name() : __point
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 35, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}east uses Python identifier east
    __east = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'east'), 'east', '__URNsps_inspection_CTD_ANON_3_URNsps_inspectioneast', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 37, 26), )

    
    east = property(__east.value, __east.set, None, None)

    
    # Element {URN:sps-inspection}north uses Python identifier north
    __north = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'north'), 'north', '__URNsps_inspection_CTD_ANON_3_URNsps_inspectionnorth', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 38, 26), )

    
    north = property(__north.value, __north.set, None, None)

    
    # Element {URN:sps-inspection}err uses Python identifier err
    __err = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'err'), 'err', '__URNsps_inspection_CTD_ANON_3_URNsps_inspectionerr', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 39, 26), )

    
    err = property(__err.value, __err.set, None, None)

    _ElementMap.update({
        __east.name() : __east,
        __north.name() : __north,
        __err.name() : __err
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 48, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}disorder uses Python identifier disorder
    __disorder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'disorder'), 'disorder', '__URNsps_inspection_CTD_ANON_4_URNsps_inspectiondisorder', True, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 50, 20), )

    
    disorder = property(__disorder.value, __disorder.set, None, None)

    _ElementMap.update({
        __disorder.name() : __disorder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 51, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionname', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 53, 26), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {URN:sps-inspection}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comments'), 'comments', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectioncomments', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 54, 26), )

    
    comments = property(__comments.value, __comments.set, None, None)

    
    # Element {URN:sps-inspection}agent uses Python identifier agent
    __agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agent'), 'agent', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionagent', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 55, 26), )

    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Element {URN:sps-inspection}aspect uses Python identifier aspect
    __aspect = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aspect'), 'aspect', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionaspect', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 56, 26), )

    
    aspect = property(__aspect.value, __aspect.set, None, None)

    
    # Element {URN:sps-inspection}terrain uses Python identifier terrain
    __terrain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'terrain'), 'terrain', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionterrain', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 57, 26), )

    
    terrain = property(__terrain.value, __terrain.set, None, None)

    
    # Element {URN:sps-inspection}position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'position'), 'position', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionposition', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 58, 26), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Element {URN:sps-inspection}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectiontype', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 59, 26), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {URN:sps-inspection}severity uses Python identifier severity
    __severity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'severity'), 'severity', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionseverity', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 60, 26), )

    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Element {URN:sps-inspection}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extent'), 'extent', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionextent', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 61, 26), )

    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Element {URN:sps-inspection}incidencePercent uses Python identifier incidencePercent
    __incidencePercent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'incidencePercent'), 'incidencePercent', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionincidencePercent', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 62, 26), )

    
    incidencePercent = property(__incidencePercent.value, __incidencePercent.set, None, None)

    
    # Element {URN:sps-inspection}isSampleTaken uses Python identifier isSampleTaken
    __isSampleTaken = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isSampleTaken'), 'isSampleTaken', '__URNsps_inspection_CTD_ANON_5_URNsps_inspectionisSampleTaken', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 63, 26), )

    
    isSampleTaken = property(__isSampleTaken.value, __isSampleTaken.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __comments.name() : __comments,
        __agent.name() : __agent,
        __aspect.name() : __aspect,
        __terrain.name() : __terrain,
        __position.name() : __position,
        __type.name() : __type,
        __severity.name() : __severity,
        __extent.name() : __extent,
        __incidencePercent.name() : __incidencePercent,
        __isSampleTaken.name() : __isSampleTaken
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 71, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}identification uses Python identifier identification
    __identification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identification'), 'identification', '__URNsps_inspection_CTD_ANON_6_URNsps_inspectionidentification', True, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 73, 26), )

    
    identification = property(__identification.value, __identification.set, None, None)

    _ElementMap.update({
        __identification.name() : __identification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 74, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:sps-inspection}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionname', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 76, 32), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {URN:sps-inspection}agent uses Python identifier agent
    __agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agent'), 'agent', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionagent', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 77, 32), )

    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Element {URN:sps-inspection}family uses Python identifier family
    __family = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'family'), 'family', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionfamily', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 78, 32), )

    
    family = property(__family.value, __family.set, None, None)

    
    # Element {URN:sps-inspection}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectiontype', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 79, 32), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {URN:sps-inspection}labDate uses Python identifier labDate
    __labDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'labDate'), 'labDate', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionlabDate', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 80, 32), )

    
    labDate = property(__labDate.value, __labDate.set, None, None)

    
    # Element {URN:sps-inspection}dateIdentified uses Python identifier dateIdentified
    __dateIdentified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateIdentified'), 'dateIdentified', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectiondateIdentified', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 81, 32), )

    
    dateIdentified = property(__dateIdentified.value, __dateIdentified.set, None, None)

    
    # Element {URN:sps-inspection}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionperson', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 82, 32), )

    
    person = property(__person.value, __person.set, None, None)

    
    # Element {URN:sps-inspection}cultureNo uses Python identifier cultureNo
    __cultureNo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cultureNo'), 'cultureNo', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectioncultureNo', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 83, 32), )

    
    cultureNo = property(__cultureNo.value, __cultureNo.set, None, None)

    
    # Element {URN:sps-inspection}retained uses Python identifier retained
    __retained = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'retained'), 'retained', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionretained', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 84, 32), )

    
    retained = property(__retained.value, __retained.set, None, None)

    
    # Element {URN:sps-inspection}herbariumNo uses Python identifier herbariumNo
    __herbariumNo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'herbariumNo'), 'herbariumNo', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionherbariumNo', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 85, 32), )

    
    herbariumNo = property(__herbariumNo.value, __herbariumNo.set, None, None)

    
    # Element {URN:sps-inspection}confidence uses Python identifier confidence
    __confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'confidence'), 'confidence', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectionconfidence', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 86, 32), )

    
    confidence = property(__confidence.value, __confidence.set, None, None)

    
    # Element {URN:sps-inspection}effect uses Python identifier effect
    __effect = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'effect'), 'effect', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectioneffect', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 87, 32), )

    
    effect = property(__effect.value, __effect.set, None, None)

    
    # Element {URN:sps-inspection}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comments'), 'comments', '__URNsps_inspection_CTD_ANON_7_URNsps_inspectioncomments', False, pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 88, 32), )

    
    comments = property(__comments.value, __comments.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __agent.name() : __agent,
        __family.name() : __family,
        __type.name() : __type,
        __labDate.name() : __labDate,
        __dateIdentified.name() : __dateIdentified,
        __person.name() : __person,
        __cultureNo.name() : __cultureNo,
        __retained.name() : __retained,
        __herbariumNo.name() : __herbariumNo,
        __confidence.name() : __confidence,
        __effect.name() : __effect,
        __comments.name() : __comments
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


inspections = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inspections'), CTD_ANON, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 3, 2))
Namespace.addCategoryObject('elementBinding', inspections.name().localName(), inspections)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inspection'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 6, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inspection')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 6, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serialNumber'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 9, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forestManager'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 10, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 11, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stand'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 12, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'siteId'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 13, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSite'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 14, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bioRegion'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 15, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'siteType'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 16, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 17, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inspector'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 18, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hostSpec'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 19, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'estabYear'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 20, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'treatment'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 21, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stemsPerHa'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 22, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'diam'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 23, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 24, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inspType'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 25, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sampleType'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 26, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comments'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 27, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'points'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 28, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'disorders'), CTD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 47, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifications'), CTD_ANON_6, scope=CTD_ANON_, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 70, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 13, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 16, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 18, 14))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 19, 14))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 20, 14))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 21, 14))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 22, 14))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 23, 14))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 24, 14))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 25, 14))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 26, 14))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 27, 14))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 70, 14))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serialNumber')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 9, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'forestManager')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 10, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 11, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stand')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 12, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'siteId')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 13, 14))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSite')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 14, 14))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bioRegion')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 15, 14))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'siteType')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 16, 14))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'date')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 17, 14))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inspector')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 18, 14))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hostSpec')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 19, 14))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'estabYear')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 20, 14))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'treatment')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 21, 14))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stemsPerHa')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 22, 14))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'diam')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 23, 14))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'height')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 24, 14))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inspType')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 25, 14))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sampleType')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 26, 14))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comments')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 27, 14))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'points')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 28, 14))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'disorders')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 47, 14))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifications')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 70, 14))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_21._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'datum'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 31, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'projection'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 32, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comments'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 33, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'point'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 34, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 33, 20))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'datum')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 31, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'projection')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 32, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comments')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 33, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'point')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 34, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'east'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 37, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'north'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 38, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'err'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 39, 26)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 39, 26))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'east')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 37, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'north')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 38, 26))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'err')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 39, 26))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'disorder'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 50, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'disorder')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 50, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 53, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comments'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 54, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agent'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 55, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aspect'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 56, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'terrain'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 57, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'position'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 58, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 59, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'severity'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 60, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extent'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 61, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'incidencePercent'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 62, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isSampleTaken'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 63, 26)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 54, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 55, 26))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 56, 26))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 57, 26))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 58, 26))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 59, 26))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 60, 26))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 61, 26))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 62, 26))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 63, 26))
    counters.add(cc_9)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 53, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comments')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 54, 26))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agent')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 55, 26))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aspect')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 56, 26))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'terrain')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 57, 26))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'position')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 58, 26))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 59, 26))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'severity')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 60, 26))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 61, 26))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'incidencePercent')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 62, 26))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isSampleTaken')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 63, 26))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identification'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 73, 26)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identification')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 73, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 76, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agent'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 77, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'family'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 78, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 79, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'labDate'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 80, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateIdentified'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 81, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 82, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cultureNo'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 83, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'retained'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 84, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'herbariumNo'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 85, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confidence'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 86, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'effect'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 87, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comments'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 88, 32)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 77, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 78, 32))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 79, 32))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 80, 32))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 81, 32))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 82, 32))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 83, 32))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 85, 32))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 86, 32))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 87, 32))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 88, 32))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 76, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agent')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 77, 32))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'family')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 78, 32))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 79, 32))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'labDate')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 80, 32))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateIdentified')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 81, 32))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 82, 32))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cultureNo')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 83, 32))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'retained')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 84, 32))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'herbariumNo')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 85, 32))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'confidence')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 86, 32))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effect')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 87, 32))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comments')), pyxb.utils.utility.Location('file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml', 88, 32))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()

