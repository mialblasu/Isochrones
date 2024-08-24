#-*- coding:Latin-1 -*
#
#               UNIVERSITÉ SHERBROOKE
#           DEPARTEMENT DE GÉOMATIQUE APPLIQUÉE
#
#
# Ce script fait:   Cartes d'isochrones de marche
#                   à partir du point initial (PI)

#
#Crée par Miguel Blanco, Avril 2013.
#
# ##################################################################
#!/usr/bin/env python

import arcpy, os, math
from arcpy.sa import *
arcpy.env.overwriteOutput = True

# Se rendre sur la Carte actuelle
mxdCarte = arcpy.mapping.MapDocument("CURRENT")
# Paramètres à remplir pour l'utilisateur
UTM =arcpy.GetParameterAsText(0)
CoordX = arcpy.GetParameterAsText(1)
CoordY = arcpy.GetParameterAsText(2)

# Paramètres du comportement
Comport = arcpy.GetParameterAsText(3)

# Paramètres de l'individu
inage= arcpy.GetParameterAsText(4)
insexe = arcpy.GetParameterAsText(5)
intaille= arcpy.GetParameterAsText(6)
inpoids = arcpy.GetParameterAsText(7)
inactPhysique = arcpy.GetParameterAsText(8)

#  Variables de la méteo

intemperature = arcpy.GetParameterAsText(9)
inprecipitation = arcpy.GetParameterAsText(10)
invents = arcpy.GetParameterAsText(11)
inHauteurneige = arcpy.GetParameterAsText(12)

# Heure disparition
inheureDisparition = arcpy.GetParameterAsText(13)




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
        coordinate = 4267
    elif UTM =="GEO NAD 27":
        coordinate = 4267
    elif UTM =="GEO WGS 84":
        coordinate = 4326


FieldID = "ID"
chaComp= "Comportement"
chaDist = "Cercle_95"
chaAge = "Age"
chaSexe = "Sexe"
chaTaille = "Taille"
chaPoids = "Poids"
chaActivitePhysique = "Activite_Physique"
chaHeureDisparition = "Heure_disparition"
chaPrecipitation = "Precipitation"
chaTemperature = "Temperature"
chaVents = "Vents"
chaHauterneige = "Hauteur_neige"



#  pointer les coordonnées

inPoint = arcpy.Point(CoordX,CoordY)
rowInsert = arcpy.InsertCursor("PI",coordinate)
newInsident = rowInsert.newRow()


# Mettre les valeurs entrées par l'utilisateur dans la table PI
newInsident.SHAPE = inPoint
newInsident.setValue(FieldID,"PI")
newInsident.setValue(chaComp,Comport)
newInsident.setValue(chaAge,inage)
newInsident.setValue(chaSexe,insexe)
newInsident.setValue(chaTaille,intaille)
newInsident.setValue(chaPoids,inpoids)
newInsident.setValue(chaActivitePhysique,inactPhysique)
newInsident.setValue(chaPrecipitation,inprecipitation)
newInsident.setValue(chaTemperature,intemperature)
newInsident.setValue(chaHeureDisparition,inheureDisparition)
newInsident.setValue(chaVents,invents)
newInsident.setValue(chaHauterneige,inHauteurneige)



# Choisir la distance selon le comportement
if Comport =="Abus de substance Boise":   # Abus de substance Boise
    newInsident.setValue(chaDist,9700)

elif Comport =="Abus de substance Urbain":
    newInsident.setValue(chaDist,1900)


elif Comport =="Alzheimer Boise-Montagneux":
    newInsident.setValue(chaDist,8300)


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

elif Comport =="Deficient mental - Urbain":
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
    arcpy.AddMessage("Il n'y a pas de distance, revoir le code")


rowInsert.insertRow(newInsident)





# Zone tampon donnée par la distance maximale selon la categorie du sujet disparu
# #############

# Path de l'actuel mxd
path1 = mxdCarte.filePath
# Ouvrir le fichier
Fichier = open(path1)
#Arriver au dossier
Dossier = os.path.dirname(Fichier.name)

# Arriver à la godatabase
repertoire = "\\GDB\isochrones.gdb"  # "/GDB/isochrones.gdb"   #

Geodatabase =  "D:/MAITRISE/isochrones/Recherche/GDB/isochrones.gdb"  #  metre ca si l'autre plainte  Dossier+repertoire

arcpy.AddMessage(Geodatabase)
arcpy.env.workspace = Geodatabase

arcpy.env.overwriteOutput = True
#arcpy.env.outputCoordinateSystem = r"C:\Program Files\ArcGIS\Desktop10.0\Coordinate Systems\Projected Coordinate Systems\National Grids\Canada\NAD 1983 Quebec Lambert.prj"




curs = arcpy.SearchCursor("PI")
rang = curs.next()

actuDist = rang.Cercle_95


# Appellation des variables

df = arcpy.mapping.ListDataFrames(mxdCarte,"Layers")[0]
arcpy.env.outputCoordinateSystem = df.spatialReference # est necesaire, si non les distances des cercles seront elles créées en dégrée décimale
Point_initial = arcpy.mapping.ListLayers(mxdCarte,"PI",df)[0] # Point initial


arcpy.Buffer_analysis(Point_initial,"Zone_tampon_p",actuDist)  # Zone tampon   Zone_tampon_p

# ############################################################################
#

arcpy.RefreshActiveView()

arcpy.RefreshTOC()

mxdCarte.save()



raster =   "\\raster"  #  "/raster"   #
dossierRaster = Dossier + raster
rasters =  "\\rasters.gdb"   #  "/rasters.gdb"  #

couchesRasters =  "D:/MAITRISE/isochrones/Recherche/raster/rasters.gdb"      #   dossierRaster + rasters
arcpy.AddMessage(couchesRasters)





zoneTampon ="Zone_tampon_p"


# ##############################################################################

#  Couper Carte de impedance  par la zone tampon  (anterieur matric_circa)
# ######################################################
arcpy.env.workspace = couchesRasters

arcpy.Clip_management("RastImpe","","Imp_coupe","Zone_tampon_p","0","")  #  ClippingGeometry a implementer ******************


# ################################
# clip modèle numérique du terrain (mnt) *** Clip de la carte de pente "mnt_coupe" a implementer ******************
# ###############################

arcpy.Clip_management("Slope_mnt","","CartePente","Zone_tampon_p","0","")  #  ClippingGeometry



# ################################
# Calculer pente en degrees
# ###############################



# #################################################################################
#  Calculer Carte de superficie de viteses base sur la pente et la vitesse de l individu
# #################################################################################


# Mettre les valeurs entrés par l'utilisateur dans la table du PI


# ###

arcpy.AddMessage(u"Âge:  "+ str(inage) + "  ans")
arcpy.AddMessage(u"Sexe:   " + str(insexe))

#  hommes

if int(inage) >= 1 and int(inage) < 4 and insexe == "Masculin":
    VITESSE = 3.5040

elif int(inage) >= 4 and int(inage) < 7 and insexe == "Masculin":
    VITESSE = 3.3120


elif int(inage) >= 7 and int(inage) < 10 and insexe == "Masculin":
    VITESSE = 3.4200


elif int(inage) >= 10 and int(inage) < 15 and insexe == "Masculin":
    VITESSE = 4.7628

elif int(inage) >= 15 and int(inage) < 20 and insexe == "Masculin":
    VITESSE = 4.8636


elif int(inage) >= 20 and int(inage) < 30 and insexe == "Masculin":
    VITESSE = 4.8888

elif int(inage) >= 30 and int(inage) < 40 and insexe == "Masculin":
    VITESSE = 5.1588


elif int(inage) >= 40 and int(inage) < 50 and insexe == "Masculin":
    VITESSE = 5.1624


elif int(inage) >= 50 and int(inage) < 60 and insexe == "Masculin":
    VITESSE = 5.1588

elif int(inage) >= 60 and int(inage) < 70 and insexe == "Masculin":
    VITESSE = 4.8204

elif int(inage) >= 70 and int(inage) < 80 and insexe == "Masculin":
    VITESSE = 4.5432

elif int(inage) >= 80 and int(inage) < 120 and insexe == "Masculin":
    VITESSE = 3.4848


# femmes

if int(inage) >= 1 and int(inage) < 4 and insexe == "Femenin":
    VITESSE = 3.5040

elif int(inage) >= 4 and int(inage) < 7 and insexe == "Femenin":
    VITESSE = 3.3120


elif int(inage) >= 7 and int(inage) < 10 and insexe == "Femenin":
    VITESSE = 3.4200


elif int(inage) >= 10 and int(inage) < 15 and insexe == "Femenin":
    VITESSE = 3.9096

elif int(inage) >= 15 and int(inage) < 20 and insexe == "Femenin":
    VITESSE = 4.4604

if int(inage) >= 20 and int(inage) < 30 and insexe == "Femenin":
    VITESSE = 4.8276

elif int(inage) >= 30 and int(inage) < 40 and insexe == "Femenin":
    VITESSE = 4.8132


elif int(inage) >= 40 and int(inage) < 50 and insexe == "Femenin":
    VITESSE = 5.0040


elif int(inage) >= 50 and int(inage) < 60 and insexe == "Femenin":
    VITESSE = 4.7268

elif int(inage) >= 60 and int(inage) < 70 and insexe == "Femenin":
    VITESSE = 4.4676

elif int(inage) >= 70 and int(inage) < 80 and insexe == "Femenin":
    VITESSE = 4.0752

elif int(inage) >= 80 and int(inage) < 120 and insexe == "Femenin":
    VITESSE = 3.3948



vit = VITESSE # vitese selon age et sexe


arcpy.AddMessage(u"Vitesse selon l'âge et le sexe: " + str(VITESSE) + "km/h")

#  indice de masse corporal et facteur d activite physique
# Fp = Facteur du au poid
# imc = indice de masse corporelle


imc = (float(inpoids) / ((float(intaille)/100)**2))

arcpy.AddMessage (u"Indice de masse corporelle:  " + str(imc) )


if float(imc) <= 24.9:
    Fp = 1.0


elif float(imc)> 25 and float(imc) <= 29.9:
    Fp = 0.94

elif float(imc)> 30 and float(imc) <= 34.9:
    Fp = 0.93

elif float(imc)> 35 and float(imc) <= 39.9:
    Fp = 0.80

elif float(imc)> 40 :
    Fp = 0.82


arcpy.AddMessage (u"Facteur de vitesse dû au IMC.  " + str(Fp))

#  Facteur d'activité phisique  (Sédentaire, légère, Modérée,  Modérée à vigoureuse,  Vigoureuse)

Fa = 5  #  POUR PASSER L ESCRIPT

arcpy.AddMessage(u"L'activité physique est:  " + inactPhysique)

if inactPhysique == u"Sédentaire":
    Fa = 1.0

elif inactPhysique == u"Légère":
    Fa = 1.05

elif inactPhysique == u"Modérée":
    Fa = 1.2

elif inactPhysique == u"Modérée à vigoureuse":
    Fa = 1.4

elif inactPhysique == "Vigoureuse":
    Fa = 2.0

arcpy.AddMessage(u"Le facteur dû à l'activité physique est:  " + str(Fa))


#  ################################################
#  Facteur poids et activitée physique  FVpa

FVpa  =Fp * Fa

arcpy.AddMessage(u"Facteur de taille, poids et activité physique:  " + str(FVpa))


# ###########################################
#   Facteurs meteorologiques
# ###############################################

#  Facteur précipitation  Fmp



# inprecipitation = u"Modérée"



if inprecipitation == u"Absent":
    Fmp = 0.0

elif inprecipitation == u"Légère":
    Fmp = 0.015

elif inprecipitation == u"Modérée":
    Fmp = 0.025

elif inprecipitation == u"Intense":
    Fmp = 0.10

elif inprecipitation == u"forte":
    Fmp = 0.50


arcpy.AddMessage (u"Facteur de vitesse dû à la précipitation:  " + str(Fmp))

#  Facteur Vents  Fmv

# invents = u"Intense"



if invents == u"Calme":
    Fmv = 0.00

elif invents == u"Léger":
    Fmv = 0.012

elif invents == u"Modéré":
    Fmv = 0.02

elif invents == u"Intense":
    Fmv = 0.04

elif invents == u"Forte":
    Fmv = 0.10

elif invents == u"Ouragan":
    Fmv = 0.50

arcpy.AddMessage (u"Facteur de vitesse dû aux vents:  " + str(Fmv))

#  Facteur hauteur neige  Fmn

# inHauteurneige = u"Absent"



if inHauteurneige == u"Absent":
    Fmn = 0.00

elif inHauteurneige == u"légère":
    Fmn = 0.013

elif inHauteurneige == u"modérée":
    Fmn = 0.10  # 0.02

elif inHauteurneige == u"Haute":
    Fmn = 0.20

elif inHauteurneige == u"Très haute":
    Fmn = 0.50


arcpy.AddMessage(u"Facteur de vitesse dû à la neige:  " + str(Fmn))


#  Facteur Temperature  Fmt

# intemperature = 40



if int(intemperature) <= -20.0 :
    Fmt = 0.30

elif int(intemperature) <= -10.0 and int(intemperature) > -20.0  :
    Fmt = 0.20

elif int(intemperature) >= -9.0 and int(intemperature)< 35.0  :
    Fmt = 0.00

elif int(intemperature) >= 35.0 :
    Fmt = 0.20

arcpy.AddMessage(u"Facteur de vitesse dû à la température:  " + str(Fmt))


Fmeteo = 1-(Fmp + Fmv + Fmn + Fmt)

arcpy.AddMessage(u"Facteur de vitesse dû aux conditions météorologiques:  " + str(Fmeteo))



# ######################
# Calculs finaux
# ########################



#  Facteur de vitese age del individu, poids, taille et activité physique  (Fvipa)

Fvipa = (vit*FVpa) * Fmeteo

# Fvf = (6*Fvipa)/5  # normalization de la vitesse à la pente de moins 5 dégrees

#  le calcul en bas remplace la constante 6 de la formule originale de Tobler W.

Fvf = (-1.0*Fvipa)/(-math.exp(-0.175))


arcpy.AddMessage(u"Vitesse selon âge, sexe, poids, taille et conditions environnementales:  " + str(Fvipa)+ "km/h")
arcpy.AddMessage(u"Vitesse maximale:  " + str(Fvf) + "Km/h")

# formule Tobler modifie pour calculer vitesse sur pente

nPi = math.pi  # numéro pi pour convertre les degrés en radians


varvitese = (Fvf *Exp(-3.5* (Abs((Tan((((Raster("CartePente"))*(nPi/180.0)))+0.05))))))  # tester cette formule plutôt




vitmetsec = (varvitese*1000.00)/3600.00   #  vitesse en mts/sec



vitmetsec.save("CarteViteseSup")

# # #########################################################################
# Carte de vitesse finale:  Carte de vitesse seloin le relief et selon la couverture du sol

# On fera une multiplication de la carte de « Vitesse par surface » (CarteViteseSup)
# par la carte de « Coût de traversée de la surface » (matric_circa)
# pour obtenir la carte « Cout de Voyage (Cv)
#                                                (dans le texte   Cv = W * Fc)
# Cv = CarteViteseSup * matric_circa

# ####################################################################################


#  Multiplication

#  Exemple:  Par une celulle (CarteViteseSup = 6 km/h) et carte  Circa = 80% d'impedance à la marche.
# Alor:   (6*(80/100) = 4.8 km/h

Cvmult = (Raster("CarteViteseSup") * (Raster("Imp_coupe")/100.000)) #

Cvmult.save("CoutTraversee")

#  inverser la valeur por calculer le cost en s/m

inCumul = Power(Cvmult,-1)  # Ainsi le cost est ok

# un autre formule pour inverser la vitesse.  prouvée et testée mais ne marche pas


inCumul.save("CrtVitVoyMul")  # cvaleur anterior a inverse donc Power

#

# cost distance module


# ##############################################################################
#  CALCUL DE ISOCHORONES UTILISANT PATH DISTANCE OUTIL
# ##############################################################################

VFa = r"D:\MAITRISE\isochrones\Recherche\raster\FV.txt"  # table des facteurs verticals


vFACTOR =  VfTable(VFa)  # cette table augmente la vitese en 30% quand le marcheur descend sur la pente


# Distance = 100000.00

# Execute PathDistance
PathDist = PathDistance("PI", Raster("CrtVitVoyMul"), Raster("mnt"), "", "", Raster("mnt"),vFACTOR,"","")  #



# Sauvergarder la sortie
PathDist.save("ISOCvf")  # si tout est bonne apres j efface ca

IsoPahtH = PathDist/3600.00

IsoPahtH.save("ISOCvfHrs")

# #####


arcpy.RefreshActiveView()

arcpy.RefreshTOC()

# ##########


mxdCarte.save()

del CoordX, CoordY, UTM, coordinate, FieldID
del inPoint, newInsident,   rowInsert, raster, rasters, mxdCarte,
del actuDist, couchesRasters, chaActivitePhysique, chaAge
del  chaComp, chaDist, chaHauterneige, chaPoids, chaPrecipitation, chaSexe
del  chaTaille, chaTemperature, chaVents, path1, repertoire, dossierRaster, df
del  rang, Point_initial, inactPhysique, inage, inHauteurneige
del  inheureDisparition, inpoids, inprecipitation, insexe, intemperature
del intaille, invents, Comport, Fichier, varvitese
del Fa



