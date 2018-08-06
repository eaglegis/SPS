import datetime
import pytz

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
