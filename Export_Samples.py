# Requires lxml to be added to python
# doesnt check for existence of temp file geodb
# output folder should be a folder
# doesn't have identifications in the xml

import arcpy, os, sys
import datetime, pytz
from lxml import etree


arcpy.env.OverwriteOutput = True
arcpy.env.preserveGlobalIds = True
arcpy.env.qualifiedFieldNames = False
arcpy.SetLogHistory(False)

in_hfs_pts = arcpy.GetParameterAsText(0) # Must be a layer from the ArcGIS Pro table of contents
in_hfs_rel_rows = arcpy.GetParameterAsText(1) # Must be a layer from the ArcGIS Pro table of contents
out_xml_folder = arcpy.GetParameterAsText(2)
now = datetime.datetime.now().strftime('%Y-%m-%dT%H%M%S')
xml_path = os.path.join(out_xml_folder,now + '.xml')
temp_fgdb = r'C:\temp\test.gdb'

PrimaryKeyField = "GlobalID"
ForiegnKeyField = "Sample_GUID"

def buildWhereClauseFromList(table, field, idList):
    valueList = ["'%s'" % value for value in idList]
    whereClause = "%s IN (%s)" % (field, ', '.join(map(str, valueList)))
    return whereClause

def selectRelatedRecords(oTable, dTable, pKeyField, fKeyField):
    # Set the SearchCursor to look through the selection of the OriginTable
    sourceIDs = set([row[0] for row in arcpy.da.SearchCursor(oTable, pKeyField)])

    # Establishes the where clause used to select records from DestinationTable
    whereClause = buildWhereClauseFromList(dTable,fKeyField, sourceIDs)

    # Process: Select Layer By Attribute
    arcpy.SelectLayerByAttribute_management(dTable, "NEW_SELECTION", whereClause)

def changeTimeZone(iTime):
    NZ_tz = pytz.timezone('Pacific/Auckland')
    local_time = NZ_tz.fromutc(iTime).strftime('%Y-%m-%d %H:%M:%S')
    return local_time

def subNull(text):
    # Substitute a null value as otherwise lxml writes "None" to the output vs a blank result
    if text:
        try:
            # Format dates nicely
            return str(text.strftime('%Y-%m-%d'))
        except:
            return str(text)
    else:
        return None


# Process: Select related records between OriginTable and DestinationTable
selectRelatedRecords(in_hfs_pts, in_hfs_rel_rows, PrimaryKeyField, ForiegnKeyField)

# Download Points
arcpy.AddMessage("Copying Sample Points")
sample_fc = arcpy.CopyFeatures_management(in_features = in_hfs_pts, out_feature_class = os.path.join(temp_fgdb, "sample_points"))[0]

# Update timezones
arcpy.AddMessage("Changing Dates and Times from UTC to NZ")
fields = ['SampleDate']
with arcpy.da.UpdateCursor(sample_fc, fields) as cursor:
    for row in cursor:
        if row[0]:
            row[0] = changeTimeZone(row[0])
            cursor.updateRow(row)

# Download records
arcpy.AddMessage("Copying Disorder Records")
disorder_rows = arcpy.CopyRows_management(in_rows = in_hfs_rel_rows, out_table = os.path.join(temp_fgdb, "disorder_records"))[0]

# Export XML
arcpy.AddMessage("Exporting XML")

sample_fields = ['GlobalID','FormID','Owner','Location','Stand','BioRegion','SiteType','SampleDate','Inspector','HostSpec','EstabYear',
                 'Treatment','Diam','Height','InspType','Comments','SHAPE@X','SHAPE@Y','Err1']

disorder_fields = ['Sample_GUID','DisorderDescription','DisorderAgentName','DisorderAspect','DisorderTerrain','DisorderPosition',
                   'DisorderType','DisorderSeverity','DisorderSeverityPer','DisorderExt','DisorderIncid','DisorderComments']

null_txt = None
inspections = etree.Element('inspections')

# Build XML from search cursor - Inspection records
with arcpy.da.SearchCursor(sample_fc, sample_fields) as sample_cursor:
    for sRow in sample_cursor:
        arcpy.AddMessage('Sample GlobalID: ' + str(sRow[0]))
        inspection = etree.SubElement(inspections, "inspection")
        insp_serialNumber = etree.SubElement(inspection, "serialNumber")
        insp_serialNumber.text = subNull(sRow[1])
        insp_forestManager = etree.SubElement(inspection, "forestManager")
        insp_forestManager.text = subNull(sRow[2])
        insp_location = etree.SubElement(inspection, "location")
        insp_location.text = subNull(sRow[3])
        insp_stand = etree.SubElement(inspection, "stand")
        insp_stand.text = subNull(sRow[4])
        insp_bioRegion = etree.SubElement(inspection, "bioRegion")
        insp_bioRegion.text = subNull(sRow[5])
        insp_siteId = etree.SubElement(inspection, "siteId")
        insp_siteId.text = null_txt
        insp_subSiteId = etree.SubElement(inspection, "subSiteId")
        insp_subSiteId.text = null_txt
        insp_siteType = etree.SubElement(inspection, "siteType")
        insp_siteType.text = subNull(sRow[6])
        insp_date = etree.SubElement(inspection, "date")
        insp_date.text = subNull(sRow[7])
        insp_inspector = etree.SubElement(inspection, "inspector")
        insp_inspector.text = subNull(sRow[8])
        insp_hostSpec = etree.SubElement(inspection, "hostSpec")
        insp_hostSpec.text = subNull(sRow[9])
        insp_estabYear = etree.SubElement(inspection, "estabYear")
        insp_estabYear.text = subNull(sRow[10])
        insp_stemsPerHa = etree.SubElement(inspection, "stemsPerHa")
        insp_stemsPerHa.text = null_txt
        insp_treatment = etree.SubElement(inspection, "treatment")
        insp_treatment.text = subNull(sRow[11])
        insp_diam = etree.SubElement(inspection, "diam")
        insp_diam.text = subNull(sRow[12])
        insp_height = etree.SubElement(inspection, "height")
        insp_height.text = subNull(sRow[13])
        insp_inspType = etree.SubElement(inspection, "inspType")
        insp_inspType.text = subNull(sRow[14])
        insp_comments = etree.SubElement(inspection, "comments")
        insp_comments.text = subNull(sRow[15])
        insp_points = etree.SubElement(inspection, "points")
        pts_datum = etree.SubElement(insp_points, "datum")
        pts_datum.text = 'NZGD2000'
        pts_projection = etree.SubElement(insp_points, "projection")
        pts_projection.text = 'NZTM'
        pts_point = etree.SubElement(insp_points, "point")
        pt_east = etree.SubElement(pts_point, "east")
        pt_east.text = subNull(sRow[16])
        pt_err = etree.SubElement(pts_point, "err")
        pt_err.text = subNull(sRow[18])
        pt_north = etree.SubElement(pts_point, "north")
        pt_north.text = subNull(sRow[17])
        insp_disorders = etree.SubElement(inspection, "disorders")
        
        # Each inspection record has 0-N Disorders.  Related using globalids
        expression = u"{0} = '{1}'".format('Sample_GUID', sRow[0])
        with arcpy.da.SearchCursor(disorder_rows, disorder_fields, where_clause=expression) as disorder_cursor:
            for dRow in disorder_cursor:
                arcpy.AddMessage('Disorder Sample GUID: ' + str(sRow[0]))
                dis_disorder = etree.SubElement(insp_disorders, "disorder")
                dis_name = etree.SubElement(dis_disorder, "name")
                dis_name.text = subNull(dRow[1])
                dis_comments = etree.SubElement(dis_disorder, "comments")
                dis_comments.text = subNull(dRow[11])
                dis_agent = etree.SubElement(dis_disorder, "agent")
                dis_agent.text = subNull(dRow[2])
                dis_aspect = etree.SubElement(dis_disorder, "aspect")
                dis_aspect.text = subNull(dRow[3])
                dis_terrain = etree.SubElement(dis_disorder, "terrain")
                dis_terrain.text = subNull(dRow[4])
                dis_position = etree.SubElement(dis_disorder, "position")
                dis_position.text = subNull(dRow[5])
                dis_type = etree.SubElement(dis_disorder, "type")
                dis_type.text = subNull(dRow[6])
                dis_severity = etree.SubElement(dis_disorder, "severity")
                dis_severity.text = subNull(dRow[7])
                dis_severityPercent = etree.SubElement(dis_disorder, "severityPercent")
                dis_severityPercent.text = subNull(dRow[8])
                dis_extent = etree.SubElement(dis_disorder, "extent")
                dis_extent.text = subNull(dRow[9])
                dis_incidencePercent = etree.SubElement(dis_disorder, "incidencePercent")
                dis_incidencePercent.text = subNull(dRow[10])

# Write out xml file to folder specified in arcgis pro
xmlDoc = etree.ElementTree(inspections)
arcpy.AddMessage(xml_path)

xmlDoc.write(xml_path, pretty_print=True, xml_declaration=True, encoding="utf-8")




