import arcpy
import os

aprx = arcpy.mp.ArcGISProject("CURRENT")
folder = aprx.homeFolder
arcpy.env.workspace = r"{}\brg_mpzp.gdb".format(folder)
arcpy.env.overwriteOutput = True

nr_planu = arcpy.GetParameterAsText(0)
fMz = arcpy.GetParameterAsText(1)

mpzpMap = aprx.listMaps("XXXX_MPZP")[0]
mpzpLyt = aprx.listLayouts("XXXX_WYDRUK_MPZP")[0]
mpzpMap.name = f"{nr_planu}_MPZP"
mpzpLyt.name = f"{nr_planu}_WYDRUK_MPZP"

mpzpMap = aprx.listMaps(f"{nr_planu}_MPZP")[0]

pktMZ = mpzpMap.listLayers("PUNKTY")[1]
linMZ = mpzpMap.listLayers("LINIE")[1]

mapMZ = mpzpMap.listLayers("MAPA_ZASADNICZA")[0]

pktMzPath = (r"{}\{}_MZ_punkty.lpkx".format(fMz, nr_planu))
mpzpMap.addDataFromPath(pktMzPath)

linMzPath = (r"{}\{}_MZ_linie.lpkx".format(fMz, nr_planu))
mpzpMap.addDataFromPath(linMzPath)

if "BUDOWLE_I_URZADZENIA" in [layer.name for layer in mpzpMap.listLayers()] and "BUDOWLE_I_URZADZENIA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    budIurzP = mpzpMap.listLayers("BUDOWLE_I_URZADZENIA")[0]
    budIurzL = mpzpMap.listLayers("BUDOWLE_I_URZADZENIA_1")[0]
elif "BUDOWLE_I_URZADZENIA" in [layer.name for layer in mpzpMap.listLayers()]:
    budIurzL = mpzpMap.listLayers("BUDOWLE_I_URZADZENIA")[0]
    budIurzL.name = "BUDOWLE_I_URZADZENIA_1"
elif "BUDOWLE_I_URZADZENIA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    budIurzL = mpzpMap.listLayers("BUDOWLE_I_URZADZENIA_1")[0]
else:
    pass
if "BUDYNKI" in [layer.name for layer in mpzpMap.listLayers()] and "BUDYNKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    budP = mpzpMap.listLayers("BUDYNKI")[0]
    budL = mpzpMap.listLayers("BUDYNKI_1")[0]
elif "BUDYNKI" in [layer.name for layer in mpzpMap.listLayers()]:
    budL = mpzpMap.listLayers("BUDYNKI")[0]
    budL.name = "BUDYNKI_1"
elif "BUDYNKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    budL = mpzpMap.listLayers("BUDYNKI_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___DZIALKI" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___DZIALKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewDzP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___DZIALKI")[0]
    ewDzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___DZIALKI_1")[0]
elif "EWIDENCJA_GRUNTOW___DZIALKI" in [layer.name for layer in mpzpMap.listLayers()]:
    ewDzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___DZIALKI")[0]
    ewDzL.name = "EWIDENCJA_GRUNTOW___DZIALKI_1"
elif "EWIDENCJA_GRUNTOW___DZIALKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewDzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___DZIALKI_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___GRANICZNIKI" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___GRANICZNIKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGrP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI")[0]
    ewGrL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI_1")[0]
elif "EWIDENCJA_GRUNTOW___GRANICZNIKI" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGrL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI")[0]
    ewGrL.name = "EWIDENCJA_GRUNTOW___GRANICZNIKI_1"
elif "EWIDENCJA_GRUNTOW___GRANICZNIKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGrL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___GRANICA_OBREBU" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGoP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU")[0]
    ewGoL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1")[0]
elif "EWIDENCJA_GRUNTOW___GRANICA_OBREBU" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGoL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU")[0]
    ewGoL.name = "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1"
elif "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewGoL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___UZYTKI" in [layer.name for layer in mpzpMap.listLayers()] and "EWIDENCJA_GRUNTOW___UZYTKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewUzP = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___UZYTKI")[0]
    ewUzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___UZYTKI_1")[0]
elif "EWIDENCJA_GRUNTOW___UZYTKI" in [layer.name for layer in mpzpMap.listLayers()]:
    ewUzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___UZYTKI")[0]
    ewUzL.name = "EWIDENCJA_GRUNTOW___UZYTKI_1"
elif "EWIDENCJA_GRUNTOW___UZYTKI_1" in [layer.name for layer in mpzpMap.listLayers()]:
    ewUzL = mpzpMap.listLayers("EWIDENCJA_GRUNTOW___UZYTKI_1")[0]
else:
    pass
if "KOMUNIKACJA_I_TRANSPORT" in [layer.name for layer in mpzpMap.listLayers()] and "KOMUNIKACJA_I_TRANSPORT_1" in [layer.name for layer in mpzpMap.listLayers()]:
    kItrP = mpzpMap.listLayers("KOMUNIKACJA_I_TRANSPORT")[0]
    kItrL = mpzpMap.listLayers("KOMUNIKACJA_I_TRANSPORT_1")[0]
elif "KOMUNIKACJA_I_TRANSPORT" in [layer.name for layer in mpzpMap.listLayers()]:
    kItrL = mpzpMap.listLayers("KOMUNIKACJA_I_TRANSPORT")[0]
    kItrL.name = "KOMUNIKACJA_I_TRANSPORT_1"
elif "KOMUNIKACJA_I_TRANSPORT_1" in [layer.name for layer in mpzpMap.listLayers()]:
    kItrL = mpzpMap.listLayers("KOMUNIKACJA_I_TRANSPORT_1")[0]
else:
    pass
if "OBIEKTY_INNE" in [layer.name for layer in mpzpMap.listLayers()] and "OBIEKTY_INNE_1" in [layer.name for layer in mpzpMap.listLayers()]:
    oInP = mpzpMap.listLayers("OBIEKTY_INNE")[0]
    oInL = mpzpMap.listLayers("OBIEKTY_INNE_1")[0]
elif "OBIEKTY_INNE" in [layer.name for layer in mpzpMap.listLayers()]:
    oInL = mpzpMap.listLayers("OBIEKTY_INNE")[0]
    oInL.name = "OBIEKTY_INNE_1"
elif "OBIEKTY_INNE_1" in [layer.name for layer in mpzpMap.listLayers()]:
    oInL = mpzpMap.listLayers("OBIEKTY_INNE_1")[0]
else:
    pass
if "OBSZAR_OPRACOWANIA" in [layer.name for layer in mpzpMap.listLayers()] and "OBSZAR_OPRACOWANIA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    oOpP = mpzpMap.listLayers("OBSZAR_OPRACOWANIA")[0]
    oOpL = mpzpMap.listLayers("OBSZAR_OPRACOWANIA_1")[0]
elif "OBSZAR_OPRACOWANIA" in [layer.name for layer in mpzpMap.listLayers()]:
    oOpL = mpzpMap.listLayers("OBSZAR_OPRACOWANIA")[0]
    oOpL.name = "OBSZAR_OPRACOWANIA_1"
elif "OBSZAR_OPRACOWANIA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    oOpL = mpzpMap.listLayers("OBSZAR_OPRACOWANIA_1")[0]
else:
    pass
if "OSNOWA" in [layer.name for layer in mpzpMap.listLayers()] and "OSNOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    osP = mpzpMap.listLayers("OSNOWA")[0]
    osL = mpzpMap.listLayers("OSNOWA_1")[0]
elif "OSNOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    osL = mpzpMap.listLayers("OSNOWA")[0]
    osL.name = "OSNOWA_1"
elif "OSNOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    osL = mpzpMap.listLayers("OSNOWA_1")[0]
else:
    pass
if "POKRYCIE_TERENU" in [layer.name for layer in mpzpMap.listLayers()] and "POKRYCIE_TERENU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    pTeP = mpzpMap.listLayers("POKRYCIE_TERENU")[0]
    pTeL = mpzpMap.listLayers("POKRYCIE_TERENU_1")[0]
elif "POKRYCIE_TERENU" in [layer.name for layer in mpzpMap.listLayers()]:
    pTeL = mpzpMap.listLayers("POKRYCIE_TERENU")[0]
    pTeL.name = "POKRYCIE_TERENU_1"
elif "POKRYCIE_TERENU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    pTeL = mpzpMap.listLayers("POKRYCIE_TERENU_1")[0]
else:
    pass
if "RZEZBA_TERENU" in [layer.name for layer in mpzpMap.listLayers()] and "RZEZBA_TERENU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    rTeP = mpzpMap.listLayers("RZEZBA_TERENU")[0]
    rTeL = mpzpMap.listLayers("RZEZBA_TERENU_1")[0]
elif "RZEZBA_TERENU" in [layer.name for layer in mpzpMap.listLayers()]:
    rTeL = mpzpMap.listLayers("RZEZBA_TERENU")[0]
    rTeL.name = "RZEZBA_TERENU_1"
elif "RZEZBA_TERENU_1" in [layer.name for layer in mpzpMap.listLayers()]:
    rTeL = mpzpMap.listLayers("RZEZBA_TERENU_1")[0]
else:
    pass
if "SIATKA_KRZYZY" in [layer.name for layer in mpzpMap.listLayers()] and "SIATKA_KRZYZY_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sKrP = mpzpMap.listLayers("SIATKA_KRZYZY")[0]
    sKrL = mpzpMap.listLayers("SIATKA_KRZYZY_1")[0]
elif "SIATKA_KRZYZY" in [layer.name for layer in mpzpMap.listLayers()]:
    sKrL = mpzpMap.listLayers("SIATKA_KRZYZY")[0]
    sKrL.name = "SIATKA_KRZYZY_1"
elif "SIATKA_KRZYZY_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sKrL = mpzpMap.listLayers("SIATKA_KRZYZY_1")[0]
else:
    pass
if "SIEC_CIEPLOWNICZA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_CIEPLOWNICZA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sCpP = mpzpMap.listLayers("SIEC_CIEPLOWNICZA")[0]
    sCpL = mpzpMap.listLayers("SIEC_CIEPLOWNICZA_1")[0]
elif "SIEC_CIEPLOWNICZA" in [layer.name for layer in mpzpMap.listLayers()]:
    sCpL = mpzpMap.listLayers("SIEC_CIEPLOWNICZA")[0]
    sCpL.name = "SIEC_CIEPLOWNICZA_1"
elif "SIEC_CIEPLOWNICZA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sCpL = mpzpMap.listLayers("SIEC_CIEPLOWNICZA_1")[0]
else:
    pass
if "SIEC_ELEKTROENERGETYCZNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_ELEKTROENERGETYCZNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sElP = mpzpMap.listLayers("SIEC_ELEKTROENERGETYCZNA")[0]
    sElL = mpzpMap.listLayers("SIEC_ELEKTROENERGETYCZNA_1")[0]
elif "SIEC_ELEKTROENERGETYCZNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sElL = mpzpMap.listLayers("SIEC_ELEKTROENERGETYCZNA")[0]
    sElL.name = "SIEC_ELEKTROENERGETYCZNA_1"
elif "SIEC_ELEKTROENERGETYCZNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sElL = mpzpMap.listLayers("SIEC_ELEKTROENERGETYCZNA_1")[0]
else:
    pass
if "SIEC_GAZOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_GAZOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sGaP = mpzpMap.listLayers("SIEC_GAZOWA")[0]
    sGaL = mpzpMap.listLayers("SIEC_GAZOWA_1")[0]
elif "SIEC_GAZOWA" in [layer.name for layer in mapx.listLayers()]:
    sGaL = mpzpMap.listLayers("SIEC_GAZOWA")[0]
    sGaL.name = "SIEC_GAZOWA_1"
elif "SIEC_GAZOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sGaL = mpzpMap.listLayers("SIEC_GAZOWA_1")[0]
else:
    pass
if "SIEC_INNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_INNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sInP = mpzpMap.listLayers("SIEC_INNA")[0]
    sInL = mpzpMap.listLayers("SIEC_INNA_1")[0]
elif "SIEC_INNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sInL = mpzpMap.listLayers("SIEC_INNA")[0]
    sInL.name = "SIEC_INNA_1"
elif "SIEC_INNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sInL = mpzpMap.listLayers("SIEC_INNA_1")[0]  
else:
    pass
if "SIEC_KANALIZACYJNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_KANALIZACYJNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sKaP = mpzpMap.listLayers("SIEC_KANALIZACYJNA")[0]
    sKaL = mpzpMap.listLayers("SIEC_KANALIZACYJNA_1")[0]
elif "SIEC_KANALIZACYJNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sKaL = mpzpMap.listLayers("SIEC_KANALIZACYJNA")[0]
    sKaL.name = "SIEC_KANALIZACYJNA_1"
elif "SIEC_KANALIZACYJNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sKaL = mpzpMap.listLayers("SIEC_KANALIZACYJNA_1")[0]
else:
    pass
if "SIEC_NIEZIDENTYFIKOWANA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_NIEZIDENTYFIKOWANA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sNiP = mpzpMap.listLayers("SIEC_NIEZIDENTYFIKOWANA")[0]
    sNiL = mpzpMap.listLayers("SIEC_NIEZIDENTYFIKOWANA_1")[0]
elif "SIEC_NIEZIDENTYFIKOWANA" in [layer.name for layer in mpzpMap.listLayers()]:
    sNiL = mpzpMap.listLayers("SIEC_NIEZIDENTYFIKOWANA")[0]
    sNiL.name = "SIEC_NIEZIDENTYFIKOWANA_1"
elif "SIEC_NIEZIDENTYFIKOWANA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sNiL = mpzpMap.listLayers("SIEC_NIEZIDENTYFIKOWANA_1")[0]
else:
    pass
if "SIEC_TELEKOMUNIKACYJNA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_TELEKOMUNIKACYJNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sTeP = mpzpMap.listLayers("SIEC_TELEKOMUNIKACYJNA")[0]
    sTeL = mpzpMap.listLayers("SIEC_TELEKOMUNIKACYJNA_1")[0]
elif "SIEC_TELEKOMUNIKACYJNA" in [layer.name for layer in mpzpMap.listLayers()]:
    sTeL = mpzpMap.listLayers("SIEC_TELEKOMUNIKACYJNA")[0]
    sTeL.name = "SIEC_TELEKOMUNIKACYJNA_1"
elif "SIEC_TELEKOMUNIKACYJNA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sTeL = mpzpMap.listLayers("SIEC_TELEKOMUNIKACYJNA_1")[0]
else:
    pass
if "SIEC_WODOCIAGOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_WODOCIAGOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sWoP = mpzpMap.listLayers("SIEC_WODOCIAGOWA")[0]
    sWoL = mpzpMap.listLayers("SIEC_WODOCIAGOWA_1")[0]
elif "SIEC_WODOCIAGOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    sWoL = mpzpMap.listLayers("SIEC_WODOCIAGOWA")[0]
    sWoL.name = "SIEC_WODOCIAGOWA_1"
elif "SIEC_WODOCIAGOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sWoL = mpzpMap.listLayers("SIEC_WODOCIAGOWA_1")[0]
else:
    pass
if "SIEC_NAFTOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_NAFTOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sNaP = mpzpMap.listLayers("SIEC_NAFTOWA")[0]
    sNaL = mpzpMap.listLayers("SIEC_NAFTOWA_1")[0]
elif "SIEC_NAFTOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    sNaL = mpzpMap.listLayers("SIEC_NAFTOWA")[0]
    sNaL.name = "SIEC_NAFTOWA_1"
elif "SIEC_NAFTOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sNaL = mpzpMap.listLayers("SIEC_NAFTOWA_1")[0]
else:
    pass
if "SIEC_BENZYNOWA" in [layer.name for layer in mpzpMap.listLayers()] and "SIEC_BENZYNOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sBeP = mpzpMap.listLayers("SIEC_BENZYNOWA")[0]
    sBeL = mpzpMap.listLayers("SIEC_BENZYNOWA_1")[0]
elif "SIEC_BENZYNOWA" in [layer.name for layer in mpzpMap.listLayers()]:
    sBeL = mpzpMap.listLayers("SIEC_BENZYNOWA")[0]
    sBeL.name = "SIEC_BENZYNOWA_1"
elif "SIEC_BENZYNOWA_1" in [layer.name for layer in mpzpMap.listLayers()]:
    sBeL = mpzpMap.listLayers("SIEC_BENZYNOWA_1")[0]
else:
    pass

camera = aprx.activeView.camera
camera.setExtent(arcpy.Describe(ewDzL).extent)

try:
    if budIurzL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, budIurzL)
        mpzpMap.removeLayer(budIurzL)
    elif budIurzL.isFeatureLayer == False and budIurzP == True:
        mpzpMap.addLayerToGroup(linMZ, budIurzP)
        mpzpMap.removeLayer(budIurzP)
    else:
        arcpy.AddMessage("Brak warstwy budIurzL lub cos poszlo nie tak") 
except NameError:
    pass
try:
    if budIurzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, budIurzP)
        mpzpMap.removeLayer(budIurzP)
    else:
        arcpy.AddMessage("Brak warstwy budIurzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if budL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, budL)
        mpzpMap.removeLayer(budL)
    elif budL.isFeatureLayer == False and budP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, budP)
        mpzpMap.removeLayer(budP)
    else:
        arcpy.AddMessage("Brak warstwy budL lub cos poszlo nie tak")  
except NameError:
    pass
try:
    if budP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, budP)
        mpzpMap.removeLayer(budP)
    else:
        arcpy.AddMessage("Brak warstwy budP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewDzL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewDzL)
        mpzpMap.removeLayer(ewDzL)
    elif ewDzL.isFeatureLayer == False and ewDzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewDzP)
        mpzpMap.removeLayer(ewDzP)
    else:
        arcpy.AddMessage("Brak warstwy ewDzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewDzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewDzP)
        mpzpMap.removeLayer(ewDzP)
    else:
        arcpy.AddMessage("Brak warstwy ewDzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGrL)
        mpzpMap.removeLayer(ewGrL)
    elif ewGrL.isFeatureLayer == False and ewGrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGrP)
        mpzpMap.removeLayer(ewGrP)
    else:
        arcpy.AddMessage("Brak warstwy ewGrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewGrP)
        mpzpMap.removeLayer(ewGrP)
    else:
        arcpy.AddMessage("Brak warstwy ewGrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGoL)
        mpzpMap.removeLayer(ewGoL)
    elif ewGoL.isFeatureLayer == False and ewGoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewGoP)
        mpzpMap.removeLayer(ewGoP)
    else:
        arcpy.AddMessage("Brak warstwy ewGoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewGoP)
        mpzpMap.removeLayer(ewGoP)
    else:
        arcpy.AddMessage("Brak warstwy ewGoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewUzL)
        mpzpMap.removeLayer(ewUzL)
    elif ewUzL.isFeatureLayer == False and ewUzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, ewUzP)
        mpzpMap.removeLayer(ewUzP)
    else:
        arcpy.AddMessage("Brak warstwy ewUzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, ewUzP)
        mpzpMap.removeLayer(ewUzP)
    else:
        arcpy.AddMessage("Brak warstwy ewUzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, kItrL)
        mpzpMap.removeLayer(kItrL)
    elif kItrL.isFeatureLayer == False and kItrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, kItrP)
        mpzpMap.removeLayer(kItrP)
    else:
        arcpy.AddMessage("Brak warstwy kItrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, kItrP)
        mpzpMap.removeLayer(kItrP)
    else:
        arcpy.AddMessage("Brak warstwy kItrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oInL)
        mpzpMap.removeLayer(oInL)
    elif oInL.isFeatureLayer == False and oInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oInP)
        mpzpMap.removeLayer(oInP)
    else:
        arcpy.AddMessage("Brak warstwy oInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, oInP)
        mpzpMap.removeLayer(oInP)
    else:
        arcpy.AddMessage("Brak warstwy oInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oOpL)
        mpzpMap.removeLayer(oOpL)
    elif oOpL.isFeatureLayer == False and oOpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, oOpP)
        mpzpMap.removeLayer(oOpP)
    else:
        arcpy.AddMessage("Brak warstwy oOpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, oOpP)
        mpzpMap.removeLayer(oOpP)
    else:
        arcpy.AddMessage("Brak warstwy oOpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, osL)
        mpzpMap.removeLayer(osL)
    elif osL.isFeatureLayer == False and osP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, osP)
        mpzpMap.removeLayer(osP)
    else:
        arcpy.AddMessage("Brak warstwy osL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, osP)
        mpzpMap.removeLayer(osP)
    else:
        arcpy.AddMessage("Brak warstwy osP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, pTeL)
        mpzpMap.removeLayer(pTeL)
    elif pTeL.isFeatureLayer == False and pTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, pTeP)
        mpzpMap.removeLayer(pTeP)
    else:
        arcpy.AddMessage("Brak warstwy pTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, pTeP)
        mpzpMap.removeLayer(pTeP)
    else:
        arcpy.AddMessage("Brak warstwy pTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, rTeL)
        mpzpMap.removeLayer(rTeL)
    elif rTeL.isFeatureLayer == False and rTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, rTeP)
        mpzpMap.removeLayer(rTeP)
    else:
        arcpy.AddMessage("Brak warstwy rTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, rTeP)
        mpzpMap.removeLayer(rTeP)
    else:
        arcpy.AddMessage("Brak warstwy rTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKrL)
        mpzpMap.removeLayer(sKrL)
    elif sKrL.isFeatureLayer == False and sKrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKrP)
        mpzpMap.removeLayer(sKrP)
    else:
        arcpy.AddMessage("Brak warstwy sKrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sKrP)
        mpzpMap.removeLayer(sKrP)
    else:
        arcpy.AddMessage("Brak warstwy sKrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sCpL)
        mpzpMap.removeLayer(sCpL)
    elif sCpL.isFeatureLayer == False and sCpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sCpP)
        mpzpMap.removeLayer(sCpP)
    else:
        arcpy.AddMessage("Brak warstwy sCpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sCpP)
        mpzpMap.removeLayer(sCpP)
    else:
        arcpy.AddMessage("Brak warstwy sCpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sElL)
        mpzpMap.removeLayer(sElL)
    elif sElL.isFeatureLayer == False and sElP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sElP)
        mpzpMap.removeLayer(sElP)
    else:
        arcpy.AddMessage("Brak warstwy sElL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sElP)
        mpzpMap.removeLayer(sElP)
    else:
        arcpy.AddMessage("Brak warstwy sElP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sGaL)
        mpzpMap.removeLayer(sGaL)
    elif sGaL.isFeatureLayer == False and sGaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sGaP)
        mpzpMap.removeLayer(sGaP)
    else:
        arcpy.AddMessage("Brak warstwy sGaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sGaP)
        mpzpMap.removeLayer(sGaP)
    else:
        arcpy.AddMessage("Brak warstwy sGaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sInL)
        mpzpMap.removeLayer(sInL)
    elif sInL.isFeatureLayer == False and sInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sInP)
        mpzpMap.removeLayer(sInP)
    else:
        arcpy.AddMessage("Brak warstwy sInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sInP)
        mpzpMap.removeLayer(sInP)
    else:
        arcpy.AddMessage("Brak warstwy sInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKaL)
        mpzpMap.removeLayer(sKaL)
    elif sKaL.isFeatureLayer == False and sKaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sKaP)
        mpzpMap.removeLayer(sKaP)
    else:
        arcpy.AddMessage("Brak warstwy sKaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sKaP)
        mpzpMap.removeLayer(sKaP)
    else:
        arcpy.AddMessage("Brak warstwy sKaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNiL)
        mpzpMap.removeLayer(sNiL)
    elif sNiL.isFeatureLayer == False and sNiP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNiP)
        mpzpMap.removeLayer(sNiP)
    else:
        arcpy.AddMessage("Brak warstwy sNiL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sNiP)
        mpzpMap.removeLayer(sNiP)
    else:
        arcpy.AddMessage("Brak warstwy sNiP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sTeL)
        mpzpMap.removeLayer(sTeL)
    elif sTeL.isFeatureLayer == False and sTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sTeP)
        mpzpMap.removeLayer(sTeP)
    else:
        arcpy.AddMessage("Brak warstwy sTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sTeP)
        mpzpMap.removeLayer(sTeP)
    else:
        arcpy.AddMessage("Brak warstwy sTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sWoL)
        mpzpMap.removeLayer(sWoL)
    elif sWoL.isFeatureLayer == False and sWoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sWoP)
        mpzpMap.removeLayer(sWoP)
    else:
        arcpy.AddMessage("Brak warstwy sWoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sWoP)
        mpzpMap.removeLayer(sWoP)
    else:
        arcpy.AddMessage("Brak warstwy sWoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNaL)
        mpzpMap.removeLayer(sNaL)
    elif sNaL.isFeatureLayer == False and sNaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sNaP)
        mpzpMap.removeLayer(sNaP)
    else:
        arcpy.AddMessage("Brak warstwy sNaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sNaP)
        mpzpMap.removeLayer(sNaP)
    else:
        arcpy.AddMessage("Brak warstwy sNaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeL.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sBeL)
        mpzpMap.removeLayer(sBeL)
    elif sBeL.isFeatureLayer == False and sBeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(linMZ, sBeP)
        mpzpMap.removeLayer(sBeP)
    else:
        arcpy.AddMessage("Brak warstwy sBeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeP.isFeatureLayer == True:
        mpzpMap.addLayerToGroup(pktMZ, sBeP)
        mpzpMap.removeLayer(sBeP)
    else:
        arcpy.AddMessage("Brak warstwy sBeP lub cos poszlo nie tak")
except NameError:
    pass

pktMZ.name = "PUNKTY_MZ"
linMZ.name = "LINIE_MZ"

pktMZ = mpzpMap.listLayers("PUNKTY_MZ")[0]
linMZ = mpzpMap.listLayers("LINIE_MZ")[0]

pktMap = mpzpMap.listLayers("PUNKTY")[0]
linMap = mpzpMap.listLayers("LINIE")[0]

try:
    if arcpy.Exists(mpzpMap.listLayers("PUNKTY")[1]):
        punktyLyr = mpzpMap.listLayers("PUNKTY")[0]
        mpzpMap.removeLayer(punktyLyr)
    else:
        pass
except IndexError:
    pass
try:
    if arcpy.Exists(mpzpMap.listLayers("LINIE")[1]):
        linieLyr = mpzpMap.listLayers("LINIE")[0]
        mpzpMap.removeLayer(linieLyr)
    else:
        pass
except IndexError:
    pass

try:
    if arcpy.Exists(mpzpMap.listLayers("Nowa warstwa grupowa")[0]):
        nowaWar = mpzpMap.listLayers("Nowa warstwa grupowa")[0]
        mpzpMap.removeLayer(nowaWar)
    else:
        pass
except IndexError:
    pass

rasMzPath = (r"{}\PODKLAD_{}.tif".format(fMz, nr_planu))
mpzpMap.addDataFromPath(rasMzPath)
rasMz = mpzpMap.listLayers(f"PODKLAD_{nr_planu}.tif")[0]
rasMz.name = f"PODKLAD_{nr_planu}"
rasMz = mpzpMap.listLayers(f"PODKLAD_{nr_planu}")[0]

arcpy.management.DefineProjection(rasMz, 'PROJCS["ETRS_1989_Poland_CS2000_Zone_6",GEOGCS["GCS_ETRS_1989",DATUM["D_ETRS_1989",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",6500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",18.0],PARAMETER["Scale_Factor",0.999923],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

with arcpy.EnvManager(outputCoordinateSystem='PROJCS["ETRS_1989_Poland_CS2000_Zone_6",GEOGCS["GCS_ETRS_1989",DATUM["D_ETRS_1989",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",6500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",18.0],PARAMETER["Scale_Factor",0.999923],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'):
    arcpy.conversion.RasterToGeodatabase(rasMz, r"{}\brg_mpzp.gdb".format(folder), '')

powLyr = mpzpMap.listLayers("POWIERZCHNIE")[0]

mpzpMap.moveLayer(powLyr, rasMz, "AFTER")

rasMz.visible = False

arcpy.AddMessage(nr_planu)
arcpy.AddMessage(fMz)

arcpy.AddMessage("Luzik arbuzik - mapa zasadnicza w formie rastrowej i wektorowej załadowana")

