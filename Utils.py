import datetime
import pytz
import lxml
from lxml import etree
import io

class Utils(object):

    @staticmethod
    def change_time_zone(time=None):
        if not time:
            return time
        dttime = datetime.datetime.fromtimestamp(time/1000)
        return dttime.strftime('%Y-%m-%d')
        # originally time wasn't correct - seems to be ok when getting directly from ArcGIS Online
        # NZ_tz = pytz.timezone('Pacific/Auckland')
        # local_time = NZ_tz.fromutc(dttime).strftime('%Y-%m-%d %H:%M:%S')
        # return local_time

    @staticmethod
    def valid_xml(file,xmlschema,log=None):
        try:
            if log:
                log("Validating {0} against {1}".format(file,xmlschema))
            xmlschema_doc = etree.parse(xmlschema)
            xmlschema = etree.XMLSchema(xmlschema_doc)
            doc = etree.parse(file)
            xmlschema.assertValid(doc)
        # check for XML syntax errors
        except etree.XMLSyntaxError as err:
            print('XML Syntax Error')
            if log:
                log(str(err))


