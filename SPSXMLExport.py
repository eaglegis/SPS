
import datetime
import os
import spsclasses
import spssubclasses
from Utils import Utils
from SPSClassEnum import SPSClassEnum

class SPSXMLExport(object):

    def __init__(self,out_location,log=None):
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H%M%S')
        self._out = os.path.join(out_location,'%s.xml' % now)
        self._func_lookups = {"SampleDate": Utils.change_time_zone}
        self._default_lookups = {"datum":"NZGD2000","projection":"NZTM2000"} # add a function for the "default fields"
        self._lookups = {"FormID": "serialNumber", "Owner": "forestManager",
                         "SampleDate": "date","Description":"name",
                         "AgentName":"agent","Type":"type_",
                         "Ext":"extent","Incid":"incidencePercent",
                         "SeverityPer":"severityPercent",
                         "x":"east","y":"north","Err1":"err"}
        self._lower_first = lambda s: s[:1].lower() + s[1:] if s else ''
        self._log = log
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
                        points = spssubclasses.pointsTypeSub()
                        self.set_feature_defaults(points)
                        # we know that there will only be only point
                        point = spssubclasses.pointTypeSub()
                        self.set_feature_attribute(point,feat.geometry)
                        # an we have a case where a point attr is stored on the feature
                        self.set_feature_attribute(point,feat.attributes)
                        points.add_point(point)
                        insp.set_points(points)
                        disorders = spssubclasses.disordersTypeSub()

                        if related_recs:
                            if SPSClassEnum.DISORDERS in related_recs.keys():
                                # disorders = spssubclasses.disordersTypeSub()
                                #loop here
                                for rec in self.get_realted_records_for_object_id(related_recs[SPSClassEnum.DISORDERS],feat.attributes['objectid']):
                                    # strip off Disorder off keys - would be easier if AGOL used the same schema
                                    new = dict((k.replace("Disorder",""), v) for k, v in rec['attributes'].items())
                                    disorder = spssubclasses.disorderTypeSub()
                                    self.set_feature_attribute(disorder,new)
                                    disorders.add_disorder(disorder)
                                if disorders:
                                    insp.set_disorders(disorders)

                            if SPSClassEnum.IDENTIFICATIONS in related_recs.keys():
                                pass # not implemented - no identifications as yet

                        # if we haven't got any related recs so we have create some empty ones.
                        # if self._log: self._log(str(insp.get_disorders().disorder))
                        if not insp.get_disorders().disorder:
                            # disorder is a minoccurs=1 so we need at least one empty record
                            disorders.add_disorder(spssubclasses.disorderTypeSub())
                            insp.set_disorders(disorders)
                        insps.add_inspection(insp)
                    insps.export(outfile, 0)
                except Exception:
                    raise

    def get_realted_records_for_object_id(self,related_records,object_id):
        for a_grp in related_records['relatedRecordGroups']:
            if a_grp['objectId'] == object_id:
                return a_grp['relatedRecords']
        return []

    def set_feature_defaults(self,an_object):
        #we have cases where there is no corresponding field in the arcgis feat.
        for k,v in self._default_lookups.items():
            setattr(an_object, k, self._default_lookups[k])

    def set_feature_attribute(self, an_object,some_atts):
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