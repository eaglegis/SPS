from arcgis.gis import GIS
from enum import Enum
from arcgis.features import FeatureLayer

class ArcGISOnlineTypesEnum(Enum):
    # this can easily be extended going forward
    FEATURELAYER = 'Feature Layer',
    FEATURESERVICE = 'Feature Service'

class ArcGISOnlineHelper(object):

    def get_gis(self,url,username,password):
        self._gis = GIS(url,username,password)

    def get_item_by_id(self,id):
        result = None
        if self._gis:
            result = self._gis.content.get(id)
        else:
            raise Exception("GIS is not set")
        return result

    def get_items_by_title(self,title,type):
        results = None
        if self._gis:
            results = self._gis.content.search('title: {0}'.format(title), type)
        else:
            raise Exception("GIS is not set")
        return results

    def get_feat_set(self,item,layer_id):
        return item.layers[layer_id].query()

    def get_feature_layer(self,url):
        return FeatureLayer(url,self._gis)

    def get_releated_recs(self,item,layer_id,object_ids,relationship_id):
        # this is on the layer -> properties -> relationships
        # object ids are comma separated
        return item.layers[layer_id].query_related_records(object_ids,relationship_id)