import arcpy
import ArcGISOnlineHelper
import importlib
import SPSXMLExport
import webbrowser
from SPSClassEnum import SPSClassEnum
import Utils
import spsclasses
import spssubclasses
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "FBS Samples Export"
        self.alias = "FBSSamplesExport"
        # List of tool classes associated with this toolbox
        self.tools = [SamplesExportTool]# ,ReloadModules] # uncomment to update code and test from Pro

class CommonTool(object):
    def __init__(self):
        self.log = lambda msg : arcpy.AddMessage(str(msg))
        self.error_log = lambda msg : arcpy.AddError(str(msg))
        arcpy.SetLogHistory(False)

class SamplesExportTool(CommonTool):
    def __init__(self):
        super().__init__()
        """Define the tool (tool name is the name of the class)."""
        self.label = "Export samples to XML"
        self.description = "Export selected features / features (based in ArcGIS Online) from the map to XML"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        param0 = arcpy.Parameter(
            displayName="User Name",
            name="user",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        param0.value = "roganb"

        param1 = arcpy.Parameter(
            displayName="Password",
            name="password",
            datatype="GPStringHidden",
            parameterType="Required",
            direction="Input")

        param2 = arcpy.Parameter(
            displayName="Features",
            name="features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        param3 = arcpy.Parameter(
            displayName="Output Folder",
            name="out_folder",
            datatype="DEFolder",
            direction="Input",
            parameterType="Required"
        )

        param4 = arcpy.Parameter(
            displayName="Validation File",
            name="val_file",
            datatype="DEFile",
            direction="Input",
            parameterType="Required"
        )
        param4.value = os.path.join(os.path.dirname(os.path.realpath(__file__)),"InspectionSchema.xml")


        return [param0, param1, param2, param3, param4]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        try:
            self.log("Running Export Tool")
            user_name, password, feat_layer, out_loc, val_file  = parameters
            ids = feat_layer.value.getSelectionSet()
            agol = ArcGISOnlineHelper.ArcGISOnlineHelper()
            agol.get_gis(arcpy.GetActivePortalURL(),user_name.value,password.value)
            self.log("Logged into %s got GIS object" % arcpy.GetActivePortalURL())
            agol_feat_layer = agol.get_feature_layer(feat_layer.value.dataSource)
            self.log("Got feature layer %s from ArcGIS Online" % feat_layer.value.dataSource)
            if ids:
                str_ids = ",".join([ str(t) for t in ids])
                feats = agol_feat_layer.query(object_ids=str_ids)
                self.log("Exporting a selection set")
            else:
                feats = agol_feat_layer.query()
                ids = agol_feat_layer.query(return_ids_only=True)
                str_ids = ",".join([str(i) for i in ids['objectIds']])
                self.log("Exporting all features")
            try:
                # assumption is that the relationship id 0 - will need to update this as we go forward - i.e. inspections
                releated_recs = agol_feat_layer.query_related_records(object_ids=str_ids,relationship_id="1")

                xml_exp = SPSXMLExport.SPSXMLExport(out_loc.valueAsText,self.log)

                for feat in feats.features:
                    new_geom = agol.project_geom([feat.geometry], 4326, 2193)
                    feat.geometry['x'] = new_geom[0]['x']
                    feat.geometry['y'] = new_geom[0]['y']

                xml_exp.export_feats_to_XML(feats,{SPSClassEnum.DISORDERS:releated_recs})

                Utils.Utils.valid_xml(xml_exp.out_file,val_file.valueAsText,self.log)
                self.log("XML Validated ok.")
                self.log("Exported file to {0}".format(xml_exp.out_file))
                webbrowser.open("file://{0}".format(xml_exp.out_file))
            except Exception as e:
                self.error_log(str(e))
        except Exception as e:
            self.error_log(str(e))
        return

class ReloadModules(CommonTool):
    def __init__(self):
        super().__init__()
        """Define the tool (tool name is the name of the class)."""
        self.label = "Reload Modules"
        self.description = "Reload Modules"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        self.log("Reloading modules")
        modules = [ArcGISOnlineHelper,SPSXMLExport,Utils,spsclasses,spssubclasses]
        for x in modules:
            self.log("reloading {0}".format(str(x)))
            importlib.reload(x)