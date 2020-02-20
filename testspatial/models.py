from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom =models.PointField(null =True)

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name
