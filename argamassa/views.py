from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta
import locale
def home_argamassa(request):
    
###############################################################################    Carregamento  Geral ##############################################
    consulta_car_geral_dia = pd.read_sql(f"""
        SELECT 
        GALMCOD,GALMNOME,NFDATAORDEM DATANF,
        ESTQCOD, ESTQNOME,
        SUM((INFQUANT * CASE WHEN ESTQPESO > 0 THEN ESTQPESO ELSE 1 END) / 1000) QUANTIDADETN,
        SUM(INFQUANT) QUANTIDADE,
        SUM((INFTOTAL / NFTOTAL) * NFTOTAL) VALOR

        FROM NOTAFISCAL
        JOIN ITEMNOTAFISCAL ON INFNFCOD = NFCOD
        JOIN ESTOQUE ON ESTQCOD = INFESTQ
        JOIN ESPECIE ON ESPCOD = ESTQESP
        JOIN GRUPOALMOXARIFADO ON GALMCOD = ESTQGALM
        LEFT OUTER JOIN GRUPOPRODUTO ON GRPCOD = ESTQGRP
        JOIN NATUREZAOPERACAO ON NOPCOD = INFNOP


        WHERE CAST(NFDATA as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                        AND CAST (GETDATE() AS DATE)
        AND NFSIT = 1
        AND GALMCOD = 1824
        AND GALMPRODVENDA = 'S'
        AND (SUBSTRING(NOPFLAGNF, 2, 1) = 'S' ) --Flag Circulação de Merc. 'S' 
        AND NFEMP = 1
        AND NFFIL = 0


        GROUP BY GALMCOD,GALMNOME, ESTQCOD, ESTQNOME,NFDATAORDEM
        ORDER BY GALMCOD,GALMNOME,NFDATAORDEM, ESTQCOD
""",connection)

    tot_ton_car_geral_dia = round(consulta_car_geral_dia['QUANTIDADETN'].sum(),1)
    tot_ton_car_geral_dia = locale.format_string("%.2f",tot_ton_car_geral_dia,grouping=True)
################################################--------------------------------------MENSAL----------------------------------------#########################################################################
    consulta_car_geral_mes = pd.read_sql(f"""
        SELECT 
        GALMCOD,GALMNOME,NFDATAORDEM DATANF,
        ESTQCOD, ESTQNOME,
        SUM((INFQUANT * CASE WHEN ESTQPESO > 0 THEN ESTQPESO ELSE 1 END) / 1000) QUANTIDADETN,
        SUM(INFQUANT) QUANTIDADE,
        SUM((INFTOTAL / NFTOTAL) * NFTOTAL) VALOR

        FROM NOTAFISCAL
        JOIN ITEMNOTAFISCAL ON INFNFCOD = NFCOD
        JOIN ESTOQUE ON ESTQCOD = INFESTQ
        JOIN ESPECIE ON ESPCOD = ESTQESP
        JOIN GRUPOALMOXARIFADO ON GALMCOD = ESTQGALM
        LEFT OUTER JOIN GRUPOPRODUTO ON GRPCOD = ESTQGRP
        JOIN NATUREZAOPERACAO ON NOPCOD = INFNOP


        WHERE NFDATA >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND nfDATA < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
                                         
        AND NFSIT = 1
        AND GALMCOD = 1824
        AND GALMPRODVENDA = 'S'
        AND (SUBSTRING(NOPFLAGNF, 2, 1) = 'S' ) --Flag Circulação de Merc. 'S' 
        AND NFEMP = 1
        AND NFFIL = 0


        GROUP BY GALMCOD,GALMNOME, ESTQCOD, ESTQNOME,NFDATAORDEM
        ORDER BY GALMCOD,GALMNOME,NFDATAORDEM, ESTQCOD
""",connection)

    tot_ton_car_geral_mes = round(consulta_car_geral_mes['QUANTIDADETN'].sum(),1)    
    tot_ton_car_geral_mes = locale.format_string("%.2f",tot_ton_car_geral_mes,grouping=True)
    #################################################-----------------------------------------------ANUAL------------------------------####################################################################

    consulta_car_geral_ano = pd.read_sql(f"""
        SELECT 
        GALMCOD,GALMNOME,NFDATAORDEM DATANF,
        ESTQCOD, ESTQNOME,
        SUM((INFQUANT * CASE WHEN ESTQPESO > 0 THEN ESTQPESO ELSE 1 END) / 1000) QUANTIDADETN,
        SUM(INFQUANT) QUANTIDADE,
        SUM((INFTOTAL / NFTOTAL) * NFTOTAL) VALOR

        FROM NOTAFISCAL
        JOIN ITEMNOTAFISCAL ON INFNFCOD = NFCOD
        JOIN ESTOQUE ON ESTQCOD = INFESTQ
        JOIN ESPECIE ON ESPCOD = ESTQESP
        JOIN GRUPOALMOXARIFADO ON GALMCOD = ESTQGALM
        LEFT OUTER JOIN GRUPOPRODUTO ON GRPCOD = ESTQGRP
        JOIN NATUREZAOPERACAO ON NOPCOD = INFNOP


       WHERE NFDATA >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND NFDATA <= GETDATE()
                                         
        AND NFSIT = 1
        AND GALMCOD = 1824
        AND GALMPRODVENDA = 'S'
        AND (SUBSTRING(NOPFLAGNF, 2, 1) = 'S' ) --Flag Circulação de Merc. 'S' 
        AND NFEMP = 1
        AND NFFIL = 0


        GROUP BY GALMCOD,GALMNOME, ESTQCOD, ESTQNOME,NFDATAORDEM
        ORDER BY GALMCOD,GALMNOME,NFDATAORDEM, ESTQCOD
""",connection)
    
    #kpi´s
    tot_ton_car_geral_ano = round(consulta_car_geral_ano['QUANTIDADETN'].sum(),1) 
    tot_ton_car_geral_ano = locale.format_string("%.2f",tot_ton_car_geral_ano,grouping=True)
###################################################################################-----PRODUÇÃO TOTAL TN---------------------########################
    
    consulta_prod_arg_dia = pd.read_sql(f"""

        SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                        AND CAST (GETDATE() AS DATE)

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1
            AND BPROFPRO != 61

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    tot_ton_arg_dia = round(consulta_prod_arg_dia['PESO'].sum(),1)
    tot_ton_arg_dia = locale.format_string("%.2f",tot_ton_arg_dia,grouping=True)
    tot_sc = round(consulta_prod_arg_dia['IBPROQUANT'].sum())
    tot_sc = locale.format_string("%.2f",tot_sc,grouping=True)
###########################---MENSAL-----------###########################################
    
    consulta_prod_arg_mes = pd.read_sql(f"""

        SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE BPRODATA >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND BPRODATA < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1
            AND BPROFPRO != 61                            
            

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_prod_arg_mes = round(consulta_prod_arg_mes['PESO'].sum(),1)
    to_ton_prod_arg_mes = locale.format_string("%.2f",to_ton_prod_arg_mes,grouping=True)
    tot_sc_mes = round(consulta_prod_arg_mes['IBPROQUANT'].sum())
    tot_sc_mes = locale.format_string("%.2f",tot_sc_mes,grouping=True)

############---------ANUAL------------------############################################################
    
    consulta_prod_arg_ano = pd.read_sql(f"""

    SELECT
        BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
        IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

        FROM BAIXAPRODUCAO
        JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
        JOIN ESTOQUE ON ESTQCOD = IBPROREF
        LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

        WHERE BPRODATA >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
        AND BPRODATA <= GETDATE()

        AND BPROEMP = 1
        AND BPROFIL = 0
        AND BPROSIT = 1
        AND IBPROTIPO = 'D'
        AND BPROEP = 1
        AND BPROFPRO != 61                                

        ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

""",connection)
    
    #KPI´S
    to_ton_prod_arg_ano = round(consulta_prod_arg_ano['PESO'].sum(),1)
    to_ton_prod_arg_ano = locale.format_string("%.2f",to_ton_prod_arg_ano,grouping=True)
    tot_sc_ano = round(consulta_prod_arg_ano['IBPROQUANT'].sum())
    tot_sc_ano = locale.format_string("%.2f",tot_sc_ano,grouping=True)
####################################################################-----------------------ARG1===MH-01----------#####################################
    #DIARIO
    consulta_agr_eqp1 = pd.read_sql(f"""
            SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                        AND CAST (GETDATE() AS DATE)

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1 
			AND BPROFPRO != 61
			AND BPROEQP = 264
                                    
        """,connection)

    ##########################################################################-------- soma------unidades -DIA-------#################################
    
    ac3 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==3,['IBPROQUANT']]
    ac3_str= ac3['IBPROQUANT'].values.sum()
    ac3_str = locale.format_string("%.2f",ac3_str,grouping=True)

    ac2 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==2,['IBPROQUANT']]
    ac2_str= ac2['IBPROQUANT'].values.sum()
    ac2_str = locale.format_string("%.2f",ac2_str,grouping=True)

    ac1 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==1,['IBPROQUANT']]
    ac1_str= ac1['IBPROQUANT'].values.sum()
    ac1_str = locale.format_string("%.2f",ac1_str,grouping=True)

    dbm = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==18,['IBPROQUANT']]
    dbm = dbm['IBPROQUANT'].values.sum()
    dbm = locale.format_string("%.2f",dbm,grouping=True)

    ap = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==20,['IBPROQUANT']]
    ap_str= ap['IBPROQUANT'].values.sum()
    ap_str = locale.format_string("%.2f",ap_str,grouping=True)

    ae = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==11,['IBPROQUANT']]
    ae= ae['IBPROQUANT'].values.sum()
    ae = locale.format_string("%.2f",ae,grouping=True)

    ae6 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==12,['IBPROQUANT']]
    ae6= ae6['IBPROQUANT'].values.sum()
    ae6 = locale.format_string("%.2f",ae6,grouping=True)

    ae8 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==13,['IBPROQUANT']]
    ae8= ae8['IBPROQUANT'].values.sum()
    ae8 = locale.format_string("%.2f",ae8,grouping=True)

    ae10 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==14,['IBPROQUANT']]
    ae10= ae10['IBPROQUANT'].values.sum()    
    ae10 = locale.format_string("%.2f",ae10,grouping=True)

    ae12 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==15,['IBPROQUANT']]
    ae12= ae12['IBPROQUANT'].values.sum()
    ae12 = locale.format_string("%.2f",ae12,grouping=True)

    ae15 = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==16,['IBPROQUANT']]
    ae15= ae15['IBPROQUANT'].values.sum()
    ae15 = locale.format_string("%.2f",ae15,grouping=True)

    agf = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==7,['IBPROQUANT']]
    agf= agf['IBPROQUANT'].values.sum()
    agf = locale.format_string("%.2f",agf,grouping=True)

    ag = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==6,['IBPROQUANT']]
    ag= ag['IBPROQUANT'].values.sum()
    ag = locale.format_string("%.2f",ag,grouping=True)

    mf = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==10,['IBPROQUANT']]
    mf= mf['IBPROQUANT'].values.sum()
    mf = locale.format_string("%.2f",mf,grouping=True)

    mdf = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==5,['IBPROQUANT']]
    mdf= mdf['IBPROQUANT'].values.sum()
    mdf = locale.format_string("%.2f",mdf,grouping=True)

    agmed = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==4,['IBPROQUANT']]
    agmed= agmed['IBPROQUANT'].values.sum()
    agmed = locale.format_string("%.2f",agmed,grouping=True)

    mchap = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==19,['IBPROQUANT']]
    mchap= mchap['IBPROQUANT'].values.sum()
    mchap = locale.format_string("%.2f",mchap,grouping=True)

    piso = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==8,['IBPROQUANT']]
    piso= piso['IBPROQUANT'].values.sum()
    piso = locale.format_string("%.2f",piso,grouping=True)

    peva = consulta_agr_eqp1.loc[consulta_agr_eqp1['BPROFPRO']==9,['IBPROQUANT']]
    peva= peva['IBPROQUANT'].values.sum()
    peva = locale.format_string("%.2f",peva,grouping=True)

######################################################################---------------eqp1-----------mensal------------###############@@@@@@@@@@@
    
    #DIARIO
    consulta_agr_eqp1_mes = pd.read_sql(f"""
            SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE BPRODATA >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND BPRODATA < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
                                        
            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1 
			AND BPROFPRO != 61
			AND BPROEQP = 264
                                    
        """,connection)


    mac3 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==3,['IBPROQUANT']]
    mac3_str= mac3['IBPROQUANT'].values.sum()
    mac3_str = locale.format_string("%.2f",mac3_str,grouping=True)

    mac2 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==2,['IBPROQUANT']]
    mac2_str= mac2['IBPROQUANT'].values.sum()
    mac2_str = locale.format_string("%.2f",mac2_str,grouping=True)

    mac1 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==1,['IBPROQUANT']]
    mac1_str= mac1['IBPROQUANT'].values.sum()
    mac1_str = locale.format_string("%.2f",mac1_str,grouping=True)
   
    mdbm = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==18,['IBPROQUANT']]
    mdbm = mdbm['IBPROQUANT'].values.sum()
    mdbm = locale.format_string("%.2f",mdbm,grouping=True)
      
    apm = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==20,['IBPROQUANT']]
    apm_str= apm['IBPROQUANT'].values.sum()
    apm_str = locale.format_string("%.2f",apm_str,grouping=True)

    mae = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==11,['IBPROQUANT']]
    mae= mae['IBPROQUANT'].values.sum()
    mae = locale.format_string("%.2f",mae,grouping=True)

    mae6 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==12,['IBPROQUANT']]
    mae6= mae6['IBPROQUANT'].values.sum()
    mae6 = locale.format_string("%.2f",mae6,grouping=True)

    mae8 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==13,['IBPROQUANT']]
    mae8= mae8['IBPROQUANT'].values.sum()
    mae8 = locale.format_string("%.2f",mae8,grouping=True)

    mae10 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==14,['IBPROQUANT']]
    mae10= mae10['IBPROQUANT'].values.sum()
    mae10 = locale.format_string("%.2f",mae10,grouping=True)    

    mae12 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==15,['IBPROQUANT']]
    mae12= mae12['IBPROQUANT'].values.sum()
    mae12 = locale.format_string("%.2f",mae12,grouping=True)

    mae15 = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==16,['IBPROQUANT']]
    mae15= mae15['IBPROQUANT'].values.sum()
    mae15 = locale.format_string("%.2f",mae15,grouping=True)

    magf = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==7,['IBPROQUANT']]
    magf= magf['IBPROQUANT'].values.sum()
    magf = locale.format_string("%.2f",magf,grouping=True)

    mmag = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==6,['IBPROQUANT']]
    mmag= mmag['IBPROQUANT'].values.sum()
    mmag = locale.format_string("%.2f",mmag,grouping=True)

    mmf = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==10,['IBPROQUANT']]
    mmf= mmf['IBPROQUANT'].values.sum()
    mmf = locale.format_string("%.2f",mmf,grouping=True)

    mmdf = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==5,['IBPROQUANT']]
    mmdf= mmdf['IBPROQUANT'].values.sum()
    mmdf = locale.format_string("%.2f",mmdf,grouping=True)

    magmed = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==4,['IBPROQUANT']]
    magmed= magmed['IBPROQUANT'].values.sum()
    magmed = locale.format_string("%.2f",magmed,grouping=True)

    mmchap = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==19,['IBPROQUANT']]
    mmchap= mmchap['IBPROQUANT'].values.sum()
    mmchap = locale.format_string("%.2f",mmchap,grouping=True)

    mpiso = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==8,['IBPROQUANT']]
    mpiso= mpiso['IBPROQUANT'].values.sum()
    mpiso = locale.format_string("%.2f",mpiso,grouping=True)

    mpeva = consulta_agr_eqp1_mes.loc[consulta_agr_eqp1_mes['BPROFPRO']==9,['IBPROQUANT']]
    mpeva= mpeva['IBPROQUANT'].values.sum()
    mpeva = locale.format_string("%.2f",mpeva,grouping=True)

#####################################################################---------------anual-----------############################################
#ANUAL
    consulta_agr_eqp1_ano = pd.read_sql(f"""
            SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE BPRODATA >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND BPRODATA <= GETDATE()
                                        
            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1 
			AND BPROFPRO != 61
			AND BPROEQP = 264
                                    
        """,connection)

    yac3 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==3,['IBPROQUANT']]
    yac3_str= yac3['IBPROQUANT'].values.sum()
    yac3_str = locale.format_string("%.2f",yac3_str,grouping=True)

    yac2 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==2,['IBPROQUANT']]
    yac2_str= yac2['IBPROQUANT'].values.sum()
    yac2_str = locale.format_string("%.2f",yac2_str,grouping=True)

    yac1 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==1,['IBPROQUANT']]
    yac1_str= yac1['IBPROQUANT'].values.sum()
    yac1_str = locale.format_string("%.2f",yac1_str,grouping=True)

    ydbm = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==18,['IBPROQUANT']]
    ydbm = ydbm['IBPROQUANT'].values.sum()
    ydbm = locale.format_string("%.2f",ydbm,grouping=True)
      
    yap = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==20,['IBPROQUANT']]
    yap_str= yap['IBPROQUANT'].values.sum()
    yap_str = locale.format_string("%.2f",yap_str,grouping=True)

    yae = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==11,['IBPROQUANT']]
    yae= yae['IBPROQUANT'].values.sum()
    yae = locale.format_string("%.2f",yae,grouping=True)

    yae6 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==12,['IBPROQUANT']]
    yae6= yae6['IBPROQUANT'].values.sum()
    yae6 = locale.format_string("%.2f",yae6,grouping=True)

    yae8 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==13,['IBPROQUANT']]
    yae8= yae8['IBPROQUANT'].values.sum()
    yae8 = locale.format_string("%.2f",yae8,grouping=True)

    yae10 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==14,['IBPROQUANT']]
    yae10= yae10['IBPROQUANT'].values.sum()    
    yae10 = locale.format_string("%.2f",yae10,grouping=True)

    yae12 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==15,['IBPROQUANT']]
    yae12= yae12['IBPROQUANT'].values.sum()
    yae12 = locale.format_string("%.2f",yae12,grouping=True)

    yae15 = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==16,['IBPROQUANT']]
    yae15= yae15['IBPROQUANT'].values.sum()
    yae15 = locale.format_string("%.2f",yae15,grouping=True)

    yagf = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==7,['IBPROQUANT']]
    yagf= yagf['IBPROQUANT'].values.sum()
    yagf = locale.format_string("%.2f",yagf,grouping=True)

    yag = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==6,['IBPROQUANT']]
    yag= yag['IBPROQUANT'].values.sum()
    yag = locale.format_string("%.2f",yag,grouping=True)

    ymf = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==10,['IBPROQUANT']]
    ymf= ymf['IBPROQUANT'].values.sum()
    ymf = locale.format_string("%.2f",ymf,grouping=True)

    ymdf = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==5,['IBPROQUANT']]
    ymdf= ymdf['IBPROQUANT'].values.sum()
    ymdf = locale.format_string("%.2f",ymdf,grouping=True)

    yagmed = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==4,['IBPROQUANT']]
    yagmed= yagmed['IBPROQUANT'].values.sum()
    yagmed = locale.format_string("%.2f",yagmed,grouping=True)

    ychap = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==19,['IBPROQUANT']]
    ychap= ychap['IBPROQUANT'].values.sum()
    ychap = locale.format_string("%.2f",ychap,grouping=True)

    ypiso = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==8,['IBPROQUANT']]
    ypiso= ypiso['IBPROQUANT'].values.sum()
    ypiso = locale.format_string("%.2f",ypiso,grouping=True)

    ypeva = consulta_agr_eqp1_ano.loc[consulta_agr_eqp1_ano['BPROFPRO']==9,['IBPROQUANT']]
    ypeva= ypeva['IBPROQUANT'].values.sum()
    ypeva = locale.format_string("%.2f",ypeva,grouping=True)
###############################################################----------------------EQUIPAMENTO 02---------------#################################
     #DIARIO
    consulta_agr_eqp2 = pd.read_sql(f"""
            SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                        AND CAST (GETDATE() AS DATE)

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1 
			AND BPROFPRO != 61
			AND BPROEQP = 265
                                    
        """,connection)

    ##########################################################################-------- soma------unidades -DIA-------#################################
    
    ac3mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==3,['IBPROQUANT']]
    ac3mh2_str= ac3mh2['IBPROQUANT'].values.sum()
    ac3mh2_str = locale.format_string("%.2f",ac3mh2_str,grouping=True)

    ac2mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==2,['IBPROQUANT']]
    ac2mh2_str= ac2mh2['IBPROQUANT'].values.sum()
    ac2mh2_str = locale.format_string("%.2f",ac2mh2_str,grouping=True)

    ac1mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==1,['IBPROQUANT']]
    ac1mh2_str= ac1mh2['IBPROQUANT'].values.sum()
    ac1mh2_str = locale.format_string("%.2f",ac1mh2_str,grouping=True)

    dbmmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==18,['IBPROQUANT']]
    dbmmh2 = dbmmh2['IBPROQUANT'].values.sum()
    dbmmh2 = locale.format_string("%.2f",dbmmh2,grouping=True)  

    apmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==20,['IBPROQUANT']]
    apmh2_str= apmh2['IBPROQUANT'].values.sum()
    apmh2_str = locale.format_string("%.2f",apmh2_str,grouping=True)
    

    aemh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==11,['IBPROQUANT']]
    aemh2= aemh2['IBPROQUANT'].values.sum()
    aemh2 = locale.format_string("%.2f",aemh2,grouping=True)

    ae6mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==12,['IBPROQUANT']]
    ae6mh2= ae6mh2['IBPROQUANT'].values.sum()
    ae6mh2 = locale.format_string("%.2f",ae6mh2,grouping=True)

    ae8mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==13,['IBPROQUANT']]
    ae8mh2= ae8mh2['IBPROQUANT'].values.sum()
    ae8mh2 = locale.format_string("%.2f",ae8mh2,grouping=True)

    ae10mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==14,['IBPROQUANT']]
    ae10mh2= ae10mh2['IBPROQUANT'].values.sum()    
    ae10mh2 = locale.format_string("%.2f",ae10mh2,grouping=True)

    ae12mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==15,['IBPROQUANT']]
    ae12mh2= ae12mh2['IBPROQUANT'].values.sum()
    ae12mh2 = locale.format_string("%.2f",ae12mh2,grouping=True)

    ae15mh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==16,['IBPROQUANT']]
    ae15mh2= ae15mh2['IBPROQUANT'].values.sum()
    ae15mh2 = locale.format_string("%.2f",ae15mh2,grouping=True)

    agfmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==7,['IBPROQUANT']]
    agfmh2= agfmh2['IBPROQUANT'].values.sum()
    agfmh2 = locale.format_string("%.2f",agfmh2,grouping=True)

    agmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==6,['IBPROQUANT']]
    agmh2= agmh2['IBPROQUANT'].values.sum()
    agmh2 = locale.format_string("%.2f",agmh2,grouping=True)

    mfmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==10,['IBPROQUANT']]
    mfmh2= mfmh2['IBPROQUANT'].values.sum()
    mfmh2 = locale.format_string("%.2f",mfmh2,grouping=True)

    mdfmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==5,['IBPROQUANT']]
    mdfmh2= mdfmh2['IBPROQUANT'].values.sum()
    mdfmh2 = locale.format_string("%.2f",mdfmh2,grouping=True)

    agmedmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==4,['IBPROQUANT']]
    agmedmh2= agmedmh2['IBPROQUANT'].values.sum()
    agmedmh2 = locale.format_string("%.2f",agmedmh2,grouping=True)

    mchapmh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==19,['IBPROQUANT']]
    mchapmh2= mchapmh2['IBPROQUANT'].values.sum()
    mchapmh2 = locale.format_string("%.2f",mchapmh2,grouping=True)

    pisomh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==8,['IBPROQUANT']]
    pisomh2= pisomh2['IBPROQUANT'].values.sum()
    pisomh2 = locale.format_string("%.2f",pisomh2,grouping=True)

    pevamh2 = consulta_agr_eqp2.loc[consulta_agr_eqp2['BPROFPRO']==9,['IBPROQUANT']]
    pevamh2= pevamh2['IBPROQUANT'].values.sum()
    pevamh2 = locale.format_string("%.2f",pevamh2,grouping=True)
   


######################################################################---------------eqp2-----------mensal------------###############@@@@@@@@@@@
    
    #DIARIO
    consulta_agr_eqp2_mes = pd.read_sql(f"""
            SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE BPRODATA >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND BPRODATA < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
                                        
            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1 
			AND BPROFPRO != 61
			AND BPROEQP = 265
                                    
        """,connection)


    mac3mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==3,['IBPROQUANT']]
    mac3mh2_str= mac3mh2['IBPROQUANT'].values.sum()
    mac3mh2_str = locale.format_string("%.2f",mac3mh2_str,grouping=True)

    mac2mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==2,['IBPROQUANT']]
    mac2mh2_str= mac2mh2['IBPROQUANT'].values.sum()
    mac2mh2_str = locale.format_string("%.2f",mac2mh2_str,grouping=True)

    mac1mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==1,['IBPROQUANT']]
    mac1mh2_str= mac1mh2['IBPROQUANT'].values.sum()
    mac1mh2_str = locale.format_string("%.2f",mac1mh2_str,grouping=True)

    mdbmmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==18,['IBPROQUANT']]
    mdbmmh2 = mdbmmh2['IBPROQUANT'].values.sum()
    mdbmmh2 = locale.format_string("%.2f",mdbmmh2,grouping=True)  

    apmmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==20,['IBPROQUANT']]
    apmmh2_str= apmmh2['IBPROQUANT'].values.sum()
    apmmh2_str = locale.format_string("%.2f",apmmh2_str,grouping=True)

    maemh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==11,['IBPROQUANT']]
    maemh2= maemh2['IBPROQUANT'].values.sum()
    maemh2 = locale.format_string("%.2f",maemh2,grouping=True)

    mae6mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==12,['IBPROQUANT']]
    mae6mh2= mae6mh2['IBPROQUANT'].values.sum()
    mae6mh2 = locale.format_string("%.2f",mae6mh2,grouping=True)

    mae8mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==13,['IBPROQUANT']]
    mae8mh2= mae8mh2['IBPROQUANT'].values.sum()
    mae8mh2 = locale.format_string("%.2f",mae8mh2,grouping=True)

    mae10mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==14,['IBPROQUANT']]
    mae10mh2= mae10mh2['IBPROQUANT'].values.sum()    
    mae10mh2 = locale.format_string("%.2f",mae10mh2,grouping=True)

    mae12mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==15,['IBPROQUANT']]
    mae12mh2= mae12mh2['IBPROQUANT'].values.sum()
    mae12mh2 = locale.format_string("%.2f",mae12mh2,grouping=True)

    mae15mh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==16,['IBPROQUANT']]
    mae15mh2= mae15mh2['IBPROQUANT'].values.sum()
    mae15mh2 = locale.format_string("%.2f",mae15mh2,grouping=True)

    magfmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==7,['IBPROQUANT']]
    magfmh2= magfmh2['IBPROQUANT'].values.sum()
    magfmh2 = locale.format_string("%.2f",magfmh2,grouping=True)

    mmagmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==6,['IBPROQUANT']]
    mmagmh2= mmagmh2['IBPROQUANT'].values.sum()
    mmagmh2 = locale.format_string("%.2f",mmagmh2,grouping=True)

    mmfmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==10,['IBPROQUANT']]
    mmfmh2= mmfmh2['IBPROQUANT'].values.sum()
    mmfmh2 = locale.format_string("%.2f",mmfmh2,grouping=True)

    mmdfmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==5,['IBPROQUANT']]
    mmdfmh2= mmdfmh2['IBPROQUANT'].values.sum()
    mmdfmh2 = locale.format_string("%.2f",mmdfmh2,grouping=True)

    magmedmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==4,['IBPROQUANT']]
    magmedmh2= magmedmh2['IBPROQUANT'].values.sum()
    magmedmh2 = locale.format_string("%.2f",magmedmh2,grouping=True)

    mmchapmh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==19,['IBPROQUANT']]
    mmchapmh2= mmchapmh2['IBPROQUANT'].values.sum()
    mmchapmh2 = locale.format_string("%.2f",mmchapmh2,grouping=True)

    mpisomh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==8,['IBPROQUANT']]
    mpisomh2= mpisomh2['IBPROQUANT'].values.sum()
    mpisomh2 = locale.format_string("%.2f",mpisomh2,grouping=True)

    mpevamh2 = consulta_agr_eqp2_mes.loc[consulta_agr_eqp2_mes['BPROFPRO']==9,['IBPROQUANT']]
    mpevamh2= mpevamh2['IBPROQUANT'].values.sum()
    mpevamh2 = locale.format_string("%.2f",mpevamh2,grouping=True)

#####################################################################---------------anual-----------############################################
#ANUAL
    consulta_agr_eqp2_ano = pd.read_sql(f"""
            SELECT
            BPROCOD, BPRODATA, ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE BPRODATA >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND BPRODATA <= GETDATE()
                                        
            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 1 
			AND BPROFPRO != 61
			AND BPROEQP = 265
                                    
        """,connection)

    yac3mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==3,['IBPROQUANT']]
    yac3mh2_str= yac3mh2['IBPROQUANT'].values.sum()
    yac3mh2_str = locale.format_string("%.2f",yac3mh2_str,grouping=True)

    yac2mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==2,['IBPROQUANT']]
    yac2mh2_str= yac2mh2['IBPROQUANT'].values.sum()
    yac2mh2_str = locale.format_string("%.2f",yac2mh2_str,grouping=True)

    yac1mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==1,['IBPROQUANT']]
    yac1mh2_str= yac1mh2['IBPROQUANT'].values.sum()
    yac1mh2_str = locale.format_string("%.2f",yac1mh2_str,grouping=True)

    ydbmmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==18,['IBPROQUANT']]
    ydbmmh2 = ydbmmh2['IBPROQUANT'].values.sum()
    ydbmmh2 = locale.format_string("%.2f",ydbmmh2,grouping=True)
      
    yapmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==20,['IBPROQUANT']]
    yapmh2_str= yapmh2['IBPROQUANT'].values.sum()
    yapmh2_str = locale.format_string("%.2f",yapmh2_str,grouping=True)

    yaemh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==11,['IBPROQUANT']]
    yaemh2= yaemh2['IBPROQUANT'].values.sum()
    yaemh2 = locale.format_string("%.2f",yaemh2,grouping=True)

    yae6mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==12,['IBPROQUANT']]
    yae6mh2= yae6mh2['IBPROQUANT'].values.sum()
    yae6mh2 = locale.format_string("%.2f",yae6mh2,grouping=True)

    yae8mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==13,['IBPROQUANT']]
    yae8mh2= yae8mh2['IBPROQUANT'].values.sum()
    yae8mh2 = locale.format_string("%.2f",yae8mh2,grouping=True)

    yae10mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==14,['IBPROQUANT']]
    yae10mh2= yae10mh2['IBPROQUANT'].values.sum()
    yae10mh2 = locale.format_string("%.2f",yae10mh2,grouping=True)    

    yae12mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==15,['IBPROQUANT']]
    yae12mh2= yae12mh2['IBPROQUANT'].values.sum()
    yae12mh2 = locale.format_string("%.2f",yae12mh2,grouping=True)

    yae15mh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==16,['IBPROQUANT']]
    yae15mh2= yae15mh2['IBPROQUANT'].values.sum()
    yae15mh2 = locale.format_string("%.2f",yae15mh2,grouping=True)

    yagfmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==7,['IBPROQUANT']]
    yagfmh2= yagfmh2['IBPROQUANT'].values.sum()
    yagfmh2 = locale.format_string("%.2f",yagfmh2,grouping=True)

    yagmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==6,['IBPROQUANT']]
    yagmh2= yagmh2['IBPROQUANT'].values.sum()
    yagmh2 = locale.format_string("%.2f",yagmh2,grouping=True)

    ymfmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==10,['IBPROQUANT']]
    ymfmh2= ymfmh2['IBPROQUANT'].values.sum()
    ymfmh2 = locale.format_string("%.2f",ymfmh2,grouping=True)

    ymdfmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==5,['IBPROQUANT']]
    ymdfmh2= ymdfmh2['IBPROQUANT'].values.sum()
    ymdfmh2 = locale.format_string("%.2f",ymdfmh2,grouping=True)

    yagmedmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==4,['IBPROQUANT']]
    yagmedmh2= yagmedmh2['IBPROQUANT'].values.sum()
    yagmedmh2 = locale.format_string("%.2f",yagmedmh2,grouping=True)

    ychapmh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==19,['IBPROQUANT']]
    ychapmh2= ychapmh2['IBPROQUANT'].values.sum()
    ychapmh2 = locale.format_string("%.2f",ychapmh2,grouping=True)

    ypisomh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==8,['IBPROQUANT']]
    ypisomh2= ypisomh2['IBPROQUANT'].values.sum()
    ypisomh2 = locale.format_string("%.2f",ypisomh2,grouping=True)

    ypevamh2 = consulta_agr_eqp2_ano.loc[consulta_agr_eqp2_ano['BPROFPRO']==9,['IBPROQUANT']]
    ypevamh2= ypevamh2['IBPROQUANT'].values.sum()
    ypevamh2 = locale.format_string("%.2f",ypevamh2,grouping=True)

    context = {
        'mac3mh2_str':mac3mh2_str,
        'mac2mh2_str':mac2mh2_str,
        'mac1mh2_str':mac1mh2_str,
        'mdbmmh2':mdbmmh2,
        'apmmh2_str':apmmh2_str,
        'maemh2':maemh2,
        'mae6mh2':mae6mh2,
        'mae8mh2': mae8mh2,
        'mae10mh2':mae10mh2,
        'mae12mh2':mae12mh2,
        'mae15mh2':mae15mh2,
        'magfmh2':magfmh2,
        'mmagmh2':mmagmh2,
        'mmfmh2':mmfmh2,
        'mmdfmh2': mmdfmh2,
        'magmedmh2':magmedmh2,
        'mchapmh2':mchapmh2,
        'mpisomh2':mpisomh2,
        'mpevamh2':mpevamh2,
        'yac3mh2_str':yac3mh2_str,
        'yac2mh2_str':yac2mh2_str,
        'yac1mh2_str':yac1mh2_str,
        'ydbmmh2':ydbmmh2,
        'yapmh2_str':yapmh2_str,
        'yaemh2':yaemh2,
        'yae6mh2':yae6mh2,
        'yae8mh2': yae8mh2,
        'yae10mh2':yae10mh2,
        'yae12mh2':yae12mh2,
        'yae15mh2':yae15mh2,
        'yagfmh2':yagfmh2,
        'yagmh2':yagmh2,
        'ymfmh2':ymfmh2,
        'ymdfmh2': ymdfmh2,
        'yagmedmh2':yagmedmh2,
        'ychapmh2':ychapmh2,
        'ypisomh2':ypisomh2,
        'ypevamh2':ypevamh2,
        'tot_ton_car_geral_dia':tot_ton_car_geral_dia,
        'tot_ton_car_geral_mes':tot_ton_car_geral_mes,
        'tot_ton_car_geral_ano':tot_ton_car_geral_ano,
        'tot_ton_prod_arg_ano':to_ton_prod_arg_ano,
        'tot_ton_prod_arg_mes':to_ton_prod_arg_mes,
        'tot_ton_arg_dia':tot_ton_arg_dia,
        'tot_sc':tot_sc,
        'tot_sc_mes':tot_sc_mes,
        'tot_sc_ano':tot_sc_ano,
        'ac3_str':ac3_str,
        'ac2_str':ac2_str,
        'ac1_str':ac1_str,
        'dbm':dbm,
        'ap_str':ap_str,
        'ae':ae,
        'ae6':ae6,
        'ae8':ae8,
        'ae10':ae10,
        'ae12':ae12,
        'ae15':ae15,
        'peva':peva,
        'piso':piso,
        'mchap':mchap,
        'agmed':agmed,
        'mdf':mdf,
        'ag':ag,
        'agf':agf,
        'mf':mf,
        'mac3_str':mac3_str,
        'mac2_str':mac2_str,
        'mac1_str':mac1_str,
        'mdbm':mdbm,
        'apm_str':apm_str,
        'mae':mae,
        'mae6':mae6,
        'mae8':mae8,
        'mae10':mae10,
        'mae12':mae12,
        'mae15':mae15,
        'mpeva':mpeva,
        'mpiso':mpiso,
        'mmchap':mmchap,
        'magmed':magmed,
        'mmdf':mmdf,
        'mmag':mmag,
        'magf':magf,
        'mmf':mmf,
        'yac3_str':yac3_str,
        'yac2_str':yac2_str,
        'yac1_str':yac1_str,
        'ydbm':ydbm,
        'yap_str':yap_str,
        'yae':yae,
        'yae6':yae6,
        'yae8':yae8,
        'yae10':yae10,
        'yae12':yae12,
        'yae15':yae15,
        'ypeva':ypeva,
        'ypiso':ypiso,
        'ychap':ychap,
        'yagmed':yagmed,
        'ymdf':ymdf,
        'yag':yag,
        'yagf':yagf,
        'ymf':ymf,
        'ac3mh2_str':ac3mh2_str,
        'ac2mh2_str':ac2mh2_str,
        'ac1mh2_str':ac1mh2_str,
        'dbmmh2':dbmmh2,
        'aemh2':aemh2,
        'ae6mh2':ae6mh2,
        'ae8mh2':ae8mh2,
        'ae10mh2':ae10mh2,
        'ae12mh2':ae12mh2,
        'ae15mh2':ae15mh2,
        'agfmh2':agfmh2,
        'ac3mh2_str':ac3mh2_str,
        'pevamh2':pevamh2,
        'pisomh2':pisomh2,
        'mmchapmh2':mmchapmh2,
        'agmedmh2':agmedmh2,
        'mdfmh2':mdfmh2,
        'mfmh2':mfmh2,
        'agmh2':agmh2,
        'apmh2_str':apmh2_str,

    }

    return render(request,'argamassa.html',context)