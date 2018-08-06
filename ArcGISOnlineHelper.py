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

if __name__ == "__main__":
    agol = ArcGISOnlineHelper()
    agol.get_gis('https://spsbiota.maps.arcgis.com', 'roganb', 'kelly10')
    item = agol.get_item_by_id('656ac46be12e420fa7ccc8674beb6574')#,ArcGISOnlineTypesEnum.FEATURELAYER.value)
    if item and item.type == ArcGISOnlineTypesEnum.FEATURESERVICE.value:
        #make the assumption that we are getting the data from the first layer
        feat_set = agol.get_feat_set(item,0)
        for feat in feat_set:
            # loop over xml class and capitalise the field and apply to arcgisonline

            print(feat)
        print(len(feat_set))
        #if item.layers[0].type == ArcGISOnlineTypesEnum.FEATURELAYER.value:
        print("quack "*3)


        fs_url = 'http://sampleserver3.arcgisonline.com/ArcGIS/rest/services/SanFrancisco/311Incidents/FeatureServer'

    print(item.layers)