#-*- coding:Latin-1 -*
#
#               UNIVERSITÉ SHERBROOKE
#           DEPARTEMENT DE GÉOMATIQUE APPLIQUÉE
#
#
# Ce script fait:   crée un point
#                   mettre les coordonées en UTM

#
#Crée par Miguel Blanco, Avril 2013.
#
# ##################################################################
#!/usr/bin/env python

import arcpy

# se rendre sur la mxdCarte actuelle
mxdCarte = arcpy.mapping.MapDocument("CURRENT")
# Paramèetres à remplir pour l'utilisateur
UTM =arcpy.GetParameterAsText(0)
CoordX = arcpy.GetParameterAsText(1)
CoordY = arcpy.GetParameterAsText(2)
Comport = arcpy.GetParameterAsText(3)


# Asignation des coordonées selon le choix.
for coord in UTM:
    if UTM == "UTM 17N":
        coordinate = 26917
    elif UTM == "UTM 18N":
        coordinate = 26918
    elif UTM =="UTM 19N":
        coordinate = 26919
    elif UTM =="UTM 20N":
        coordinate = 26920
    elif UTM =="UTM 21N":
        coordinate = 26921
    elif UTM =="GEO NAD 83":
        coordinate = 4269
    elif UTM =="GEO NAD 27":
        coordinate = 4267
    elif UTM =="GEO WGS 84":
        coordinate = 4326

FieldID = "ID"
chaComp= "Comportement"
chaDist = "Cercle_95"

inPoint = arcpy.Point(CoordX,CoordY)
rowInsert = arcpy.InsertCursor("PI",coordinate)
newInsident = rowInsert.newRow()

newInsident.SHAPE = inPoint
newInsident.setValue(FieldID,"PI")
newInsident.setValue(chaComp,Comport)

if Comport =="Abus de substance Boise":
    newInsident.setValue(chaDist,9700)

elif Comport =="Abus de substance Urbain":
    newInsident.setValue(chaDist,1900)


elif Comport =="Alzheimer Boise-Montagneux":
    newInsident.setValue(chaDist,5100)


elif Comport =="Alzheimer Boise-Plat":
    newInsident.setValue(chaDist,12800)

elif Comport =="Alzheimer Urbaint":
    newInsident.setValue(chaDist,12600)

elif Comport =="Autiste - Boise":
    newInsident.setValue(chaDist,15200)


elif Comport =="Autiste - Urbain":
    newInsident.setValue(chaDist,8000)


elif Comport =="Campeur - Montagneux":
    newInsident.setValue(chaDist,38600)


elif Comport =="Campeur - Plat":
    newInsident.setValue(chaDist,12800)


elif Comport =="Chasseur - Montagneux":
    newInsident.setValue(chaDist,17200)


elif Comport =="Chasseurs - Plat":
    newInsident.setValue(chaDist,13700)


elif Comport =="Coureurs ":
    newInsident.setValue(chaDist,5800)



elif Comport =="Cueilleurs - Montagneux ":
    newInsident.setValue(chaDist,12900)


elif Comport =="Deficient mental - Boise-Montagneux":
    newInsident.setValue(chaDist,11300)

elif Comport =="Deficient mental - Boise-Plat":
    newInsident.setValue(chaDist,11800)

elif Comport =="Deficient menal - Urbain":
    newInsident.setValue(chaDist,9900)

elif Comport =="Depressif ou suicidaire - Boise-Montagneux":
    newInsident.setValue(chaDist,21600)


elif Comport =="Depressif ou suicidaire - Boise-Plat":
    newInsident.setValue(chaDist,17300)

elif Comport =="Depressif ou suicidaire -Urbain":
    newInsident.setValue(chaDist,13100)


elif Comport =="Enfant 1 - 3 ans - Boise-Montagneux":
    newInsident.setValue(chaDist,4500)

elif Comport =="Enfant 1 - 3 ans - Boise-Plat":
    newInsident.setValue(chaDist,3200)

elif Comport =="Enfant 1 - 3 ans - Urbain":
    newInsident.setValue(chaDist,1100)

elif Comport =="Enfant 4 - 6 ans - Boise-Montagneux":
    newInsident.setValue(chaDist,3700)

elif Comport =="Enfant 4 - 6 ans - Boise-Plat":
    newInsident.setValue(chaDist,6600)

elif Comport =="Enfant 4 - 6 ans - Urbain":
    newInsident.setValue(chaDist,3400)

elif Comport =="Enfant 7 - 9 ans - Boise-Montagneux":
    newInsident.setValue(chaDist,11300)

elif Comport =="Enfant 7 - 9 ans - Boise-Plat":
    newInsident.setValue(chaDist,8000)

elif Comport =="Enfant 7 - 9 ans Urbain":
    newInsident.setValue(chaDist,5200)

elif Comport =="Enfant 10 - 12 ans - Boise-Montagneux":
    newInsident.setValue(chaDist,9000)

elif Comport =="Enfant 10 - 12 ans - Boise-Plat":
    newInsident.setValue(chaDist,10000)

elif Comport =="Enfant 10 - 12 ans - Urbain":
    newInsident.setValue(chaDist,5800)

elif Comport =="Enfant 13 - 15 ans - Boise-Montagneux":
    newInsident.setValue(chaDist,21400)

elif Comport =="Enfant 13 - 15 ans - Boise-Plat":
    newInsident.setValue(chaDist,10000)

elif Comport =="Enlevement":
    newInsident.setValue(chaDist,19300)

elif Comport =="Motoneigiste disparu - Montagneux":
    newInsident.setValue(chaDist,16100)

elif Comport =="Motoneigistes disparu - Plat":
    newInsident.setValue(chaDist,96100)

elif Comport =="Pecheur - Montagneux":
    newInsident.setValue(chaDist,9900)

elif Comport =="Pecheur - Plat":
    newInsident.setValue(chaDist,14900)

elif Comport =="Planchiste":
    newInsident.setValue(chaDist,15400)

elif Comport =="Quadiste ":
    newInsident.setValue(chaDist,8000)

elif Comport =="Randonneur - Boise-Montagneux":
    newInsident.setValue(chaDist,18300)

elif Comport =="Randonneur - Boise-Plat":
    newInsident.setValue(chaDist,9900)

elif Comport =="Randonneur - Urbain":
    newInsident.setValue(chaDist,2600)

elif Comport =="schizophrene - Boise-Montagneux":
    newInsident.setValue(chaDist,14600)

elif Comport =="schizophrene - Boise-Plat":
    newInsident.setValue(chaDist,8100)

elif Comport =="schizophrene - Urbain":
    newInsident.setValue(chaDist,12500)

elif Comport =="Skieur alpin ":
    newInsident.setValue(chaDist,15200)

elif Comport =="Skieur de fond ":
    newInsident.setValue(chaDist,19600)

elif Comport =="Velo de montagne ":
    newInsident.setValue(chaDist,25000)


else:
    newInsident.setValue(chaDist,0000)


rowInsert.insertRow(newInsident)






# #################################################################
# créer rayons
# #################################################################

import arcpy

from math import radians, sin, cos

#  Coordonnées de l'origen = Point Initial

origin_x =float(CoordX)
origin_y = float(CoordY)

# Chercher la distance du rayon dans l'entité PI
curs = arcpy.SearchCursor("PI",coordinate)
rang = curs.next()
# Pointer sur les champs contenant la valeur du rayon
actuDist = rang.Cercle_95



distance = actuDist
angle = 0 # cette variale va changer sa valeur chaque 5 dégrées

# Fonction pour faire la ligne à partir du PI et jusqu'a la limite de la zone tampon
# établie selon le comportement du disparu.

def rayons():

    arcpy.AddMessage(angle)
    arcpy.AddMessage(distance)

    # Calculer le delta Dx et delta Dy
    Dx = (distance * sin(radians(angle)))
    Dy = (distance * cos(radians(angle)))
    # Calculer les coordonnées du point final (limite de zone tampon)
    finalX = float(origin_x) + Dx
    finalY = float(origin_y) + Dy

# Chercher l'entité poliligne dnas la carte
    cur = arcpy.InsertCursor("Zone Tampon l", coordinate)
    pLigneArray = arcpy.Array()

    p1 = arcpy.Point()
    (p1.ID, p1.X, p1.Y) = (1, origin_x, origin_y)
    pLigneArray.add(p1)


    # Point final
    p2 = arcpy.Point()
    (p2.ID, p2.X, p2.Y) = (2, finalX, finalY)
    pLigneArray.add(p2)

    # créer la poliligne
    pligne = cur.newRow()
    pligne.shape = pLigneArray
    cur.insertRow(pligne)
##
##    # yes, this shouldn't really be necessary...
##    pLigneArray.removeAll()
##    del cur

# Boucle pour miner le rayon à travers le 360 dégrées du cercle avec un
# intervalle de 5 dégrées par ligne.
for angle in range (0, 360,5):
    angle
    rayons()







# ##################################################################





arcpy.RefreshActiveView()

mxdCarte.save()

del CoordX, CoordY, UTM, coordinate, FieldID,  inPoint, newInsident,   rowInsert, curs



# ####################################################################
# PROJETER LA COORDONNÉE UTM DU LIEU OÙ EST PLACÉ LE POINT INITIAL
# #####################################################################



##
###Créer la variable "df" du data frame "COUCHES"
##
##df = arcpy.mapping.ListDataFrames(mxdCarte,"COUCHES")[0]
### Indiquer le groupe de layers "Waypoints" auquel s'ajoute le layer "Grille UTM.lyr"
##GroupDessins = arcpy.mapping.ListLayers(mxdCarte,"Waypoints",df)[0]
### Source de la couche "Grille UTM.lyr"
##addLayer = arcpy.mapping.Layer(r"C:\GEOMATIQUE\mxdCarteS\AUTRES\Lyr\INDIVIDUEL\COUCHES D INFORMATION\Autres couches d informations\Grille UTM.lyr")
##arcpy.mapping.AddLayerToGroup(df,GroupDessins,addLayer,"TOP")
##
### Sélectionner le fuseau UTM d'accord a la position du "Point Initial"
##
##arcpy.SelectLayerByLocation_management("Waypoints\Grille UTM","INTERSECT","Waypoints\Point initial","","NEW_SELECTION")
##
### Pointer sur la table de la Grille UTM
### Malheuresement el ne prends pas le code (EPSG)  associée à la coordonnée, donc s'il y a changements
### de version d'arcgis, il foudré repointer dans la table 'Grille UTM' la source placée
### sur le champ "PRJ_TEXT"
##
##rows = arcpy.SearchCursor("Waypoints\Grille UTM","","","PRJ_TEXT","")
##
### Changer les coordonnées du dataframe pour les coordonnées UTM du point initial
##for rows in rows:
##    mxdCarte = arcpy.mapping.MapDocument("CURRENT")
##    prj = rows.getValue("PRJ_TEXT")
##    sr = arcpy.SpatialReference(prj)
##    df = arcpy.mapping.ListDataFrames(mxdCarte)[0] # il me semble qu'ici il y a un erreur
##    df.spatialReference = sr
##
##
### Effacer le layer "Grille UTM" du Dataframe "COUCHES"
##
##mxdCarte = arcpy.mapping.MapDocument("CURRENT")
##for COUCHES in arcpy.mapping.ListDataFrames(mxdCarte):
##    for lyr in arcpy.mapping.ListLayers(mxdCarte, "", COUCHES):
##        if lyr.name == "Grille UTM":
##            arcpy.mapping.RemoveLayer(COUCHES,lyr)
##
##arcpy.RefreshTOC()
##arcpy.RefreshActiveView
##mxdCarte.save()
##
##del mxdCarte, prj, sr, df, GroupDessins, addLayer, rows
##
##

