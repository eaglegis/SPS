#from __future__ import print_function

import pyxb
import pyxb.binding.datatypes as xs
import spsb
import spsbiota
import urllib
# pyxbgen -m x -u file://c:/Windows/My%20Documents/x.xsd
#
# C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python.exe  C:/Users/fsh/AppData/Roaming/Python/Python36/Scripts/pyxbgen --version
# pyxbgen from PyXB 1.2.6

# C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python.exe  C:/Users/fsh/AppData/Roaming/Python/Python36/Scripts/pyxbgen --module spsbiota -u file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml --binding-root c:/zzcloud/dropbox/work/sps/sps/
# Python for URN:spsbiota requires 1 modules
# C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python.exe  C:/Users/fsh/AppData/Roaming/Python/Python36/Scripts/pyxbgen --module spsbiota -u file:///c:/zzcloud/dropbox/work/sps/sps/nsspsbiota.xsd --binding-root c:/zzcloud/dropbox/work/sps/sps/
# Python for URN:sps requires 1 modules
#

# C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python.exe  C:/Users/fsh/AppData/Roaming/Python/Python36/Scripts/pyxbgen -u file:///c:/zzcloud/dropbox/work/sps/sps/spsschema.xml -m spsbiota -u file:///c:/zzcloud/dropbox/work/sps/sps/nsspsbiota.xsd -m spsb --binding-root c:/zzcloud/dropbox/work/sps/sps/
# Python for URN:spsb requires 2 modules

#
#
# d = spsbiota.inspections
# print("dd")
# d.append(pyxb.BIND(pyxb.BIND(serialNumber="wank",forestManager="pooiuyp",location="poooop",stand="poop"),pyxb.BIND(serialNumber="wank",forestManager="pooiuyp",location="poooop",stand="poop")))
#
# print(d.toxml("utf-8").decode('utf-8'))


# C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python.exe C:/Users/fsh/AppData/Roaming/Python/Python36/Scripts/generateDS.py -f -o c:/zzcloud/dropbox/work/sps/sps/spsclasses.py -s c:/zzcloud/dropbox/work/sps/sps/spssubclasses.py --super=spsclasses c:/zzcloud/dropbox/work/sps/sps/inspectionschema.xml
#
#requires generateDS and lxml
import sys
import spsclasses
import spssubclasses
from lxml import etree
from ArcGISOnlineHelper import ArcGISOnlineHelper
from ArcGISOnlineHelper import ArcGISOnlineTypesEnum
from Utils import Utils
from SPSXMLExport import SPSXMLExport
from SPSClassEnum import SPSClassEnum

func_lookups = {"SampleDate":Utils.changeTimeZone}
lookups = {"FormID":"serialNumber","Owner":"forestManager","SampleDate":"date"}

# with open('c:/temp/out.xml','w') as outfile:
#     outfile.write('<?xml version="1.0" encoding="utf-8"?>\n')
#     insps = spsclasses.inspections()


agol = ArcGISOnlineHelper()
agol.get_gis('https://spsbiota.maps.arcgis.com', 'roganb', 'kelly10')
item = agol.get_item_by_id('656ac46be12e420fa7ccc8674beb6574')  # ,ArcGISOnlineTypesEnum.FEATURELAYER.value)
    # if item and item.type == ArcGISOnlineTypesEnum.FEATURESERVICE.value:
    #     # make the assumption that we are getting the data from the first layer
    #     feat_set = agol.get_feat_set(item, 0)
    #     func = lambda s: s[:1].lower() + s[1:] if s else ''
    #     #couple of look ups
    #
    #     for feat in feat_set:
    #         insp = spssubclasses.inspectionTypeSub()
    #         for an_att,value in feat.attributes.items():
    #             print(an_att,value)
    #             # do a getattr to see if it exists
    #             try:
    #                 print(an_att,",",func(an_att))
    #                 getattr(insp,func(an_att)) # this throws an error so effectively an if
    #                 setattr(insp,func(an_att),value)
    #             except AttributeError as ae:
    #                 print(ae)
    #                 if an_att in lookups.keys():
    #                     if an_att in func_lookups:
    #                         setattr(insp, lookups[an_att], func_lookups[an_att](value))
    #                     else:
    #                         setattr(insp, lookups[an_att], value)
    #                 continue
    #
    #         # get related disorders
    #         # we are assuming that we already have the layer id and the relationship id assumes that we are dealing with the first layer and first relationship
    #
    #         insps.add_inspection(insp)
    #     print(len(feat_set))
    #     # if item.layers[0].type == ArcGISOnlineTypesEnum.FEATURELAYER.value:
    #     print("quack " * 3)
    # print(item.layers)
recs = item.layers[0].query()
ids = item.layers[0].query(return_ids_only=True)
print("----------->",ids)
str_ids = ",".join([str(i) for i in ids['objectIds']])
releated_recs = item.layers[0].query_related_records(object_ids=str_ids, relationship_id="0",out_fields="*")
print("k")

xml_exp = SPSXMLExport('c:/temp/')
xml_exp.export_feats_to_XML(recs, {SPSClassEnum.DISORDERS: releated_recs})

