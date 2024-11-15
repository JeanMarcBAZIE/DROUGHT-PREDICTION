from pathlib import Path

class Config:

    # Construction des dossiers de travail
    ASSETS_PATH = Path('../ASSETS')
    DATASET_PATH = ASSETS_PATH / 'DATA'
    PLUIE_ETP_PATH = DATASET_PATH / 'RAW' / 'ETP_PLUIE'
    SPEI_PATH = DATASET_PATH / 'RAW' / 'SPEI'
    ERA5_PATH = DATASET_PATH / 'RAW' / 'ERA5'
    
    
    SST_LEF_DEK=ERA5_PATH /'SST_LEF' #Emplacement des données de SST de LEF d'ERA5
    SST_NINO_DEK=ERA5_PATH /'SST_NINO'
    TEMP_ROS_DEK=ERA5_PATH /'TEMP_ROS'  #Emplacement des données de temperature point de rosée d'ERA5
    SOL_EAU_DEK=ERA5_PATH /'SOL_EAU'  #Emplacement des données volume d'eau dans le sol d'ERA5
    PREC_EAU_DEK=ERA5_PATH /'PREC_EAU'  #Emplacement des données d'eau precipitable d'ERA5
    U_WIND_975_DEK=ERA5_PATH /'U_WIND_975'  #Emplacement des données de la composante nord du vent à la 975 hPa d'ERA5
    U_WIND_925_DEK=ERA5_PATH /'U_WIND_925'  #Emplacement des données de la composante nord du vent à la 925 hPa d'ERA5
    U_WIND_850_DEK=ERA5_PATH /'U_WIND_850'  #Emplacement des données de la composante nord du vent à la 850 hPa d'ERA5
    U_WIND_700_DEK=ERA5_PATH /'U_WIND_700'  #Emplacement des données de la composante nord du vent à la 700 hPa d'ERA5
    U_WIND_200_DEK=ERA5_PATH /'U_WIND_200'  #Emplacement des données de la composante nord du vent à la 200 hPa d'ERA5
    V_WIND_975_DEK=ERA5_PATH /'V_WIND_975'  #Emplacement des données de la composante Est du vent à la 975 hPa d'ERA5
    V_WIND_925_DEK=ERA5_PATH /'V_WIND_925'  #Emplacement des données de la composante Est du vent à la 925 hPa d'ERA5
    V_WIND_850_DEK=ERA5_PATH /'V_WIND_850'  #Emplacement des données de la composante Est du vent à la 850 hPa d'ERA5
    V_WIND_700_DEK=ERA5_PATH /'V_WIND_700'  #Emplacement des données de la composante Est du vent à la 700 hPa d'ERA5
    V_WIND_200_DEK=ERA5_PATH /'V_WIND_200'  #Emplacement des données de la composante Est du vent à la 200 hPa d'ERVAL

    SST_LEF_VAL=ERA5_PATH /'SST_LEF_VAL' #Emplacement des données de SST de LEF d'ERA5
    SST_NINO_VAL=ERA5_PATH /'SST_NINO_VAL'
    TEMP_ROS_VAL=ERA5_PATH /'TEMP_ROS_VAL'  #Emplacement des données de temperature point de rosée d'ERA5
    SOL_EAU_VAL=ERA5_PATH /'SOL_EAU_VAL'  #Emplacement des données volume d'eau dans le sol d'ERA5
    PREC_EAU_VAL=ERA5_PATH /'PREC_EAU_VAL'  #Emplacement des données d'eau precipitable d'ERA5
    U_WIND_975_VAL=ERA5_PATH /'U_WIND_975_VAL'  #Emplacement des données de la composante nord du vent à la 975 hPa d'ERA5
    U_WIND_925_DEK=ERA5_PATH /'U_WIND_925_VAL'  #Emplacement des données de la composante nord du vent à la 925 hPa d'ERA5
    U_WIND_850_VAL=ERA5_PATH /'U_WIND_850_VAL'  #Emplacement des données de la composante nord du vent à la 850 hPa d'ERA5
    U_WIND_700_VAL=ERA5_PATH /'U_WIND_700_VAL'  #Emplacement des données de la composante nord du vent à la 700 hPa d'ERA5
    U_WIND_200_VAL=ERA5_PATH /'U_WIND_200_VAL'  #Emplacement des données de la composante nord du vent à la 200 hPa d'ERA5
    V_WIND_975_VAL=ERA5_PATH /'V_WIND_975_VAL'  #Emplacement des données de la composante Est du vent à la 975 hPa d'ERA5
    V_WIND_925_VAL=ERA5_PATH /'V_WIND_925_VAL'  #Emplacement des données de la composante Est du vent à la 925 hPa d'ERA5
    V_WIND_850_VAL=ERA5_PATH /'V_WIND_850_VAL'  #Emplacement des données de la composante Est du vent à la 850 hPa d'ERA5
    V_WIND_700_VAL=ERA5_PATH /'V_WIND_700_VAL'  #Emplacement des données de la composante Est du vent à la 700 hPa d'ERA5
    V_WIND_200_VAL=ERA5_PATH /'V_WIND_200_VAL'  #Emplacement des données de la composante Est du vent à la 200 hPa d'ERA5

    
    STATION_PATH = DATASET_PATH / 'RAW' / 'INFO_STATIONS'
    MODELS_PATH = ASSETS_PATH / 'models'
    FEATURES_PATH = ASSETS_PATH / 'features'
    METRICS_FILE_PATH = ASSETS_PATH / 'metrics'
    FILES_TRAITED_PATH=DATASET_PATH / 'PREPARED'
    ERA5_DATA_PATH = DATASET_PATH / 'ERA5'
    DATASET_DIR=DATASET_PATH / 'DATASET'
    RESULT_DIR= ASSETS_PATH / 'RESULTAT'
    RESULT_COMPILE_DIR= ASSETS_PATH / 'RESULTAT_COMPILE'
    RESULT_LATEX_DIR=ASSETS_PATH / 'RESULTAT_LATEX'
    RESULT_DIR_SEL_VAR= ASSETS_PATH / 'RESULTAT_SEL_VAR'
    RESULT_COMPILE_DIR_SEL_VAR= ASSETS_PATH / 'RESULTAT_COMPILE_SEL_VAR'
    RESULT_LATEX_DIR_SEL_VAR=ASSETS_PATH / 'RESULTAT_LATEX_SEL_VAR'

    #Partie liée au processing des données de era5
    #Fichier de coordonnées des stations
    
    #Fichiers
    PLUIE_FILE_NAME='pluie_jour.xls'           #Données journalières de pluies
    ETP_FILE_NAME='etp_jour.xls'
    STAT_COORD_FILE_NAME='station_coord.xlsx'  #Coordonnées des stations
    SPEI_1DEK_FILE_NAME='SPEI_1dek.csv'
    SPEI_1MON_FILE_NAME='SPEI_1mon.csv'
    SPEI_3MON_FILE_NAME='SPEI_3mon.csv'
    SPEI_6MON_FILE_NAME='SPEI_6mon.csv'              #Données journalières de l'evapotranspiration
    PLUIE_ETP_FILE_NAME='merged_data.csv'      #Fusionner les deux fichiers en un après traitement
    STATION_TEST='boromo.csv'                  #Permettre de sauvegarder une station test pour controle
    STATION_ALL='all_station.csv'
    DATA_1DEK='data_1dek.csv'
    #DATA_1DEK_EXTR='data_ext_1dek.csv'
    #DATA_1DEK_SEV='data_sev_1dek.csv'
    DATA_1MON='data_1mon.csv'
    #DATA_1MON_EXTR='data_ext_1mon.csv'
    #DATA_1MON_SEV='data_sev_1mon.csv'
    DATA_3MON='data_3mon.csv'
    #DATA_3MON_EXTR='data_ext_3mon.csv'
    #DATA_3MON_SEV='data_sev_3mon.csv'
    DATA_6MON='data_6mon.csv'
    #DATA_6MON_EXTR='data_ext_6mon.csv'
    #DATA_6MON_SEV='data_sev_6mon.csv'
    #Les fichiers dans era5
    WIND_V_975='v_wind_975.nc' #'v_wind_1.nc'
    WIND_V_975_CSV='v_wind_975.csv' # 'v_wind_1.csv'
    WIND_V_975_DEK='v_wind_975_dek.csv'
    WIND_V_975_MON='v_wind_975_mon.csv'
    
    WIND_V_925='v_wind_925.nc' #'v_wind_1.nc'
    WIND_V_925_CSV='v_wind_925.csv' # 'v_wind_1.csv'
    WIND_V_925_DEK='v_wind_925_dek.csv'
    WIND_V_925_MON='v_wind_925_mon.csv'
    
    WIND_U_850='u_wind_850.nc' #'v_wind_1.nc'
    WIND_U_850_CSV='u_wind_850.csv' # 'v_wind_1.csv'
    WIND_U_850_DEK='u_wind_850_dek.csv'
    WIND_U_850_MON='u_wind_850_mon.csv'
    
    WIND_U_700='u_wind_700.nc' #'v_wind_1.nc'
    WIND_U_700_CSV='u_wind_700.csv' # 'v_wind_1.csv'
    WIND_U_700_DEK='u_wind_700_dek.csv'
    WIND_U_700_MON='u_wind_700_mon.csv'  
    
    
    WIND_U_200='u_wind_200.nc' #'v_wind_1.nc'
    WIND_U_200_CSV='u_wind_200.csv' # 'v_wind_1.csv'
    WIND_U_200_DEK='u_wind_200_dek.csv'
    WIND_U_200_MON='u_wind_200_mon.csv'  
    
    WIND_U_100='u_wind_100.nc' #'v_wind_1.nc'
    WIND_U_100_CSV='u_wind_100.csv' # 'v_wind_1.csv'
    WIND_U_100_DEK='u_wind_100_dek.csv'
    WIND_U_100_MON='u_wind_100_mon.csv' 
    
    #EAU_PREC='cloud_liquid_water_flux.nc' #'v_wind_1.nc'
    EAU_PREC='eau_precipitable.nc'
    EAU_PREC_CSV='eau_prec.csv' # 'v_wind_1.csv'
    EAU_PREC_CSV_DEK='eau_prec_dek.csv'
    EAU_PREC_CSV_MON='eau_prec_mon.csv'    
    
    #POINT_ROSEE='drew_point.nc' #'v_wind_1.nc'
    POINT_ROSEE='point_rosee.nc'
    POINT_ROSEE_CSV='point_rosee.csv' # 'v_wind_1.csv'
    POINT_ROSEE_CSV_DEK='point_rosee_dek.csv'
    POINT_ROSEE_CSV_MON='point_rosee_mon.csv' 
    
    SOL_WATERPOINT='vol_soil_water.nc'
    SOL_WATERPOINT_CSV='vol_soil_water.csv' # 'v_wind_1.csv'
    SOL_WATERPOINT_CSV_DEK='vol_soil_water_dek.csv'
    SOL_WATERPOINT_CSV_MON='vol_soil_water_mon.csv'      
    
    #Dossiers de données de temperature de mer
    SST_LEF_PATH= ERA5_PATH / 'SST_LEF_DEK'
    SST_NINO_PATH= ERA5_PATH / 'SST_NINO_DEK'
    SST_LEF_SP_MN_PATH= ERA5_PATH / 'SST_LEF_FLDMEAN'   # Recupère les fichiers temp langue d'eau froide avec les moyennes spatiales
    SST_NINO_SP_MN_PATH=ERA5_PATH / 'SST_NINO_FLDMEAN'
    SST_LEF_MERGE='sst_leg_merged.nc'
    SST_NINO_MERGE='sst_nino_merged.nc'
    
    #Fichier pour sauvegarder les parametres issus de ERA5
    ERA_FUSION_DEK='era_decade.csv'
    ERA_FUSION_MON='era_mensuel.csv'
    
    
class Constant:
    #Labels secheresse
    LABEL_1='Humidité extrême'
    LABEL_2='Humidité sévère'
    LABEL_3='Humidité modérée'
    LABEL_4='Normale'
    LABEL_5='Sécheresse modérée'
    LABEL_6='Sécheresse sévère'
    LABEL_7='Sécheresse extrême'
    LABEL_II='Sécheresse extr_sev'
    #Seuils secheresse 
    SEUIL_1=-1.0
    SEUIL_2=-1.5
    SEUIL_3=-1.99
    SEUIL_4=-2.0
    # Partage des datasets avant l'apprentissage 
    TEST_SIZE=0.2
    RANDOM_SEED=42
    
    # Mois d'avance pour la prediction
    MONTH_AVANT=2


