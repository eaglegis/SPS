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
* arcgis (1.4.2) - uses the ArcGIS Python API to query the data directly

These need to be added to the ArcGIS Pro installation via the Python back stage.
[ArcGIS Pro Python packages](http://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-conda.htm)

### Installing

To install:

* Add required Python packages
* Copy toolbox folder (with supporting modules) to a location on disk
* Add this folder to ArcGIS pro Catalog view
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
* [generateDs overview](https://bitbucket.org/dkuhlman/generateds/overview)
* [generateDS at source forge](https://sourceforge.net/projects/generateds/)
* [Dave Kuhlman](https://davekuhlman.org)
* [Dave Kulhman generateDS](http://www.davekuhlman.org/generateDS.html)

This can be installed via pip.
Once it is available generate the Python classes based on the supplied xml schema.
Something like
> C:/../Python/Python36/Scripts/generateDS.py -f -o "c:/../work/sps/sps/spsclasses.py" -s "c:/../work/sps/sps/spssubclasses.py" --super="spsclasses" c:/../work/sps/sps/inspectionschema.xml

This will allow you to override any functions you need in the sub classes script.

## Authors

Fraser Hand (Python toolbox, not generateDS or ArcGIS python API)

## Acknowledgments

* Esri Python API team
* Dave Kuhlman
