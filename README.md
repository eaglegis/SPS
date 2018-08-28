# SPS Biosecurity

This is a Python toolbox which will enable the user to export an added web layer (within ArcGIS Pro) to XML based on the SPS XML schema. Note that this is currently for the following objects:
* Inspections
* Disorders
* Points

It does not currently support identifications though these could be added easily.
It is based on the SPS FBS Samples: Multi Disorders web layer.

## Getting Started

This is supplied as a Python Toolbox and accompanying scripts and can be copied to any directory.
This needs to be added as a folder within the ArcGIS Pro project. Note that modules will be loaded from the same directory automatically.
If supporting modules are moved the location will need to be added to the Python path or an appropriate pth file will need to be added to the Python repository.
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The Python toolbox requires
* lxml (lxml 4.2.3)- used by the generated Pyhon classes
* arcgis (1.4.2) - uses the ArcGIS Python API to query the data directly from ArcGIS Online

These need to be added to the ArcGIS Pro installation via the Python back stage.
[ArcGIS Pro Python packages](http://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-conda.htm)

### Installing

To install:

* Add required Python packages to ArcGIS Pro via the Python backstage
* Copy toolbox folder (with supporting modules) to a location on disk
* Add this folder to ArcGIS Pro Catalog view
* Test toolbox


## Running the tool in ArcGIS pro

Note you will need the following:

A current signed in connection to ArcGIS Online
The web layer added to the current map view
Valid credentials to log into ArcGIS Online that is a member of a group that has the web layer shared to it.


## Built With

The Python classes are built with generateDS based on the supplied schema.

* [Parse and export to xml](http://www.davekuhlman.org/generateds_tutorial.html#using-the-generated-code-to-parse-and-export-an-xml-document)
* [Export method](http://www.davekuhlman.org/generateDS.html#method-export)
* [generateDS](https://bitbucket.org/dkuhlman/generateds)
* [generateDS overview](https://bitbucket.org/dkuhlman/generateds/overview)
* [generateDS at source forge](https://sourceforge.net/projects/generateds/)
* [Dave Kuhlman](https://davekuhlman.org)
* [Dave Kulhman generateDS](http://www.davekuhlman.org/generateDS.html)

This can be installed via pip.
Once it is available generate the Python classes based on the supplied xml schema.
Something like
> C:/../Python/Python36/Scripts/generateDS.py -f -o "c:/../work/sps/sps/spsclasses.py" -s "c:/../work/sps/sps/spssubclasses.py" --super="spsclasses" --always-export-default  c:/../work/sps/sps/inspectionschema.xml

See the documentation for more detail
http://www.davekuhlman.org/generateDS.html#the-command-line-interface-how-to-use-it


This will allow you to override any functions you need in the sub classes script.

**Note:** You only require generateDS if you need to _**recreate**_ the Python classes (from an updated schema file) or generate new classes.

**_Big Note_ on generateDS.py**
Note that a few changes were made to this file for the sake of this project.
SPS need all elements with minOccurs=1 (or no present as the default) written to the XML to ensure validation. By default the generateDS code ignores elements with no value or children elements with no content. I have made changes to the following functions to support this:
* generateHascontentMethod
* generateExportFn_1

The generateDS.py file is included as part of this project and can be reviewed against the latest version of generateDS if required in the future. If installing on a machine to regenerate classes then review this file against the current version and make the same chnages if neccessary. Note these changes have not been pushed back to the main generateDS repository.
This will be somewhere like C:\Users\ ..\AppData\Roaming\Python\Python36\Scripts


## Authors

Fraser Hand (Python toolbox only, not generateDS or ArcGIS Python API)

## Acknowledgments

* Esri Python API team
* Dave Kuhlman

:dromedary_camel:
