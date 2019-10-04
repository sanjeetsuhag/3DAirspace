import json
import pymap3d
import xml.etree.ElementTree

# Load GLTF template.
GLTF = None
with open('GLTF.json') as GLTF_file:
    GLTF = json.load(GLTF_file)

# Load KML data source.
PlacemarkKML = xml.etree.ElementTree.parse('Placemark.kml')
coordinates = PlacemarkKML.getroot().find('Polygon/outerBoundaryIs/LinearRing/coordinates').text.split(' ')
ceiling = 4300 # float(PlacemarkKML.getroot().find('ExtendedData/SchemaData').text.split(' '))
base = 1000
for coordinate in coordinates:
    print(coordinate)