
import datetime
import os
import spsclasses
import spssubclasses
from lxml import etree
from ArcGISOnlineHelper import ArcGISOnlineHelper
from ArcGISOnlineHelper import ArcGISOnlineTypesEnum
from Utils import Utils
from SPSClassEnum import SPSClassEnum

class SPSXMLExport(object):

    def __init__(self,out_location):
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H%M%S')
        self._out = os.path.join(out_location,'%s.xml' % now)
        self._func_lookups = {"SampleDate": Utils.changeTimeZone}
        self._lookups = {"FormID": "serialNumber", "Owner": "forestManager", "SampleDate": "date","Description":"name","AgentName":"agent","Type":"type_","Ext":"extent","Incid":"incidencePercent","SeverityPer":"severityPercent"}
        self._lower_first = lambda s: s[:1].lower() + s[1:] if s else ''

    @property
    def out_file(self):
        if self._out:
            return self._out
        else:
            return None

    def export_feats_to_XML(self,feats,related_recs=None):
        if self._out:
            with open(self._out, 'w') as outfile:
                try:
                    outfile.write('<?xml version="1.0" encoding="utf-8"?>\n')
                    insps = spsclasses.inspections()
                    for feat in feats:
                        insp = spssubclasses.inspectionTypeSub()
                        self.set_feature_attribute(insp, feat.attributes)
                        if related_recs:
                            if SPSClassEnum.DISORDERS in related_recs.keys():
                                disorders = spssubclasses.disordersTypeSub()
                                #loop here
                                for rec in self.get_realted_records_for_object_id(related_recs[SPSClassEnum.DISORDERS],feat.attributes['OBJECTID']):
                                    # strip off Disorder off keys - would be easier if AGOL used the same schema
                                    new = dict((k.replace("Disorder",""),v) for k,v in rec['attributes'].items())
                                    disorder = spssubclasses.disorderTypeSub()
                                    self.set_feature_attribute(disorder,new)

                                    disorders.add_disorder(disorder)
                                if disorders:
                                    insp.set_disorders(disorders)
                            if SPSClassEnum.INSPECTIONS in related_recs.keys():
                                pass

                        insps.add_inspection(insp)
                    insps.export(outfile, 0)
                except Exception as e:
                    raise

    def get_realted_records_for_object_id(self,related_records,object_id):
        for a_grp in related_records['relatedRecordGroups']:
            if a_grp['objectId'] == object_id:
                return a_grp['relatedRecords']
        return []


    def set_feature_attribute(self,an_object,some_atts):
        for an_att, value in some_atts.items():
            print(an_att, value)
            # do a getattr to see if it exists
            try:
                print(an_att, ",", self._lower_first(an_att))
                getattr(an_object, self._lower_first(an_att))  # this throws an error so effectively an if
                setattr(an_object, self._lower_first(an_att), value)
            except AttributeError as ae:
                print(ae)
                if an_att in self._lookups.keys():
                    if an_att in self._func_lookups:
                        setattr(an_object, self._lookups[an_att], self._func_lookups[an_att](value))
                    else:
                        setattr(an_object, self._lookups[an_att], value)
                continue
