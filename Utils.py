import datetime, pytz

class Utils(object):

    @staticmethod
    def changeTimeZone(time=None):
        if not time:
            return time
        dttime = datetime.datetime.fromtimestamp(time/1000)
        return dttime.strftime('%Y-%m-%d')
        # NZ_tz = pytz.timezone('Pacific/Auckland')
        # local_time = NZ_tz.fromutc(dttime).strftime('%Y-%m-%d %H:%M:%S')
        # return local_time
