import arcpy
import os

aprx = arcpy.mp.ArcGISProject("CURRENT")
folder = aprx.homeFolder
arcpy.env.workspace = r"{}\brg_mpzp.gdb".format(folder)
arcpy.env.overwriteOutput = True

nr_planu = arcpy.GetParameterAsText(0)
mzPkt = arcpy.GetParameterAsText(1)
mzLin = arcpy.GetParameterAsText(2)
fRast = arcpy.GetParameterAsText(3)

mpzpMap = aprx.listMaps("XXXX_MPZP")[0]
mpzpLyt = aprx.listLayouts("XXXX_WYDRUK_MPZP")[0]
mpzpMap.name = f"{nr_planu}_MPZP"
mpzpLyt.name = f"{nr_planu}_WYDRUK_MPZP"

mpzpMap = aprx.listMaps(f"{nr_planu}_MPZP")[0]

pktMZ = mpzpMap.listLayers("PUNKTY")[1]
linMZ = mpzpMap.listLayers("LINIE")[1]

mapMZ = mpzpMap.listLayers("MAPA_ZASADNICZA")[0]

mpzpMap.addDataFromPath(mzPkt)
pktMz = mpzpMap.listLayers("New Group Layer")[0]
pktMz.name = "PUNKTY_MZ"
mpzpMap.addDataFromPath(mzLin)
linMz = mpzpMap.listLayers("New Group Layer")[0]
linMz.name = "LINIE_MZ"

mpzpMap.addLayerToGroup(mapMZ, pktMz)
mpzpMap.addLayerToGroup(mapMZ, linMz)

pktMZ = mpzpMap.listLayers("PUNKTY")[1]
linMZ = mpzpMap.listLayers("LINIE")[1]
mpzpMap.removeLayer(pktMZ)
mpzpMap.removeLayer(linMZ)

pktMZ = mpzpMap.listLayers("PUNKTY_MZ")[0]
linMZ = mpzpMap.listLayers("LINIE_MZ")[0]
mpzpMap.removeLayer(pktMz)
mpzpMap.removeLayer(linMZ)

rasMzPath = (r"{}\PODKLAD_{}.tif".format(fRast, nr_planu))
mpzpMap.addDataFromPath(rasMzPath)
rasMz = mpzpMap.listLayers(f"PODKLAD_{nr_planu}.tif")[0]

arcpy.management.DefineProjection(rasMz, 'PROJCS["ETRS_1989_Poland_CS2000_Zone_6",GEOGCS["GCS_ETRS_1989",DATUM["D_ETRS_1989",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",6500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",18.0],PARAMETER["Scale_Factor",0.999923],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

powLyr = mpzpMap.listLayers("POWIERZCHNIE")[0]

mpzpMap.moveLayer(powLyr, rasMz, "BEFORE")

rasMz.visible = False

arcpy.AddMessage(nr_planu)
arcpy.AddMessage(mzLin)
arcpy.AddMessage(mzPkt)
arcpy.AddMessage(rasMz)
arcpy.AddMessage("Brawo - mapa zasadnicza w formie rastrowej i wektorowej zaladowana")
