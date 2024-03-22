from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta
import locale
def home_cal(request):
###################################################################------------------AZBE---------------------------##################################################################################
    consulta_ultimo_dia_azbe = pd.read_sql(f"""

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
            AND BPROEP = 2
            AND BPROFPRO = 27

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_azbe = round(consulta_ultimo_dia_azbe['PESO'].sum(),1)
    to_ton_azbe = locale.format_string("%.2f",to_ton_azbe,grouping=True)
########-----------MES-----------------------------------
    consulta_ultimo_mes_azbe = pd.read_sql(f"""

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
    AND BPROEP = 2
    AND BPROFPRO = 27

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    to_ton_azbe_mes = round(consulta_ultimo_mes_azbe['PESO'].sum(),1)
    to_ton_azbe_mes = locale.format_string("%.2f",to_ton_azbe_mes,grouping=True)
########---------------ano----------------------------------------
    
    consulta_ultimo_ano_azbe = pd.read_sql(f"""

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
        AND BPROEP = 2
        AND BPROFPRO = 27

        ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

""",connection)

     #KPI´S
    to_ton_ano_azbe = round(consulta_ultimo_ano_azbe['PESO'].sum(),1)
    to_ton_ano_azbe = locale.format_string("%.2f",to_ton_ano_azbe,grouping=True)
#######################################---------------------METÀLICOS-----------------------------------------------############################################################
    #DIA
    consulta_ultimo_dia_met = pd.read_sql(f"""

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
            AND BPROEP = 2
            AND BPROFPRO IN (28,29,30,31,32,33)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_met = round(consulta_ultimo_dia_met['PESO'].sum(),1)
    to_ton_met = locale.format_string("%.2f",to_ton_met,grouping=True)
    #M##############----------MÊS----------------------###############################

    consulta_ultimo_mes_met = pd.read_sql(f"""

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
    AND BPROEP = 2
    AND BPROFPRO IN (28,29,30,31,32,33)

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
    to_ton_met_mes = round(consulta_ultimo_mes_met['PESO'].sum(),1)
    to_ton_met_mes = locale.format_string("%.2f",to_ton_met_mes,grouping=True)
    ##-----------KTPI----------------------------------------

    consulta_ultimo_ano_met = pd.read_sql(f"""

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
        AND BPROEP = 2
        AND BPROFPRO IN (28,29,30,31,32,33)

        ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

""",connection)

     #KPI´S
    to_ton_ano_met = round(consulta_ultimo_ano_met['PESO'].sum(),1)
    to_ton_ano_met = locale.format_string("%.2f",to_ton_ano_met,grouping=True)
####################################################-----------------------TOTAIS--DOS--FORNOS------------------------#######################################
       
    consulta_ultimo_fornos_dia = pd.read_sql(f"""

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
            AND BPROEP = 2
            

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_fornos_dia = round(consulta_ultimo_fornos_dia['PESO'].sum(),1)
    to_ton_fornos_dia = locale.format_string("%.2f",to_ton_fornos_dia,grouping=True)
###########################---MENSAL-----------###########################################
    
    consulta_ultimo_fornos_mes = pd.read_sql(f"""

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
            AND BPROEP = 2
            

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_fornos_mes = round(consulta_ultimo_fornos_mes['PESO'].sum(),1)
    to_ton_fornos_mes = locale.format_string("%.2f",to_ton_fornos_mes,grouping=True)

############---------ANUAL------------------############################################################
    
    consulta_ultimo_fornos_ano = pd.read_sql(f"""

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
        AND BPROEP = 2
        

        ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

""",connection)
    
    #KPI´S
    to_ton_fornos_ano = round(consulta_ultimo_fornos_ano['PESO'].sum(),1)
    to_ton_fornos_ano = locale.format_string("%.2f",to_ton_fornos_ano,grouping=True)
####################################----------BENEFICIAMENTO---------------------###################################################################
    
    consulta_ultimo_dia_benef = pd.read_sql(f"""

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
            AND BPROEP = 3
            AND BPROFPRO = 39

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_dia_benef = round(consulta_ultimo_dia_benef['PESO'].sum(),1)
    to_ton_dia_benef = locale.format_string("%.2f",to_ton_dia_benef,grouping=True)
##################################----------------MENSAL------------------------###################################################################
    
    consulta_ultimo_mes_benef = pd.read_sql(f"""

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
    AND BPROEP = 3
    AND BPROFPRO = 39

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
     #KPI´S
    to_ton_mes_benef = round(consulta_ultimo_mes_benef['PESO'].sum(),1)
    to_ton_mes_benef = locale.format_string("%.2f",to_ton_mes_benef,grouping=True)
#########################----------------ANUAL--------------------------------------#################################################################
    consulta_ultimo_ano_benef = pd.read_sql(f"""

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
        AND BPROEP = 3
        AND BPROFPRO = 39
        

        ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

""",connection)
    
    #KPI´S
    to_ton_ano_benef = round(consulta_ultimo_ano_benef['PESO'].sum(),1)
    to_ton_ano_benef = locale.format_string("%.2f",to_ton_ano_benef,grouping=True)
######################--------------------------------------------------------ENSACADOS----------------------------------------------#######################################################
    
    consulta_ultimo_dia_benef_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (44,38,221)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_dia_benef_ens = round(consulta_ultimo_dia_benef_ens['PESO'].sum(),1)
    to_ton_dia_benef_ens = locale.format_string("%.2f",to_ton_dia_benef_ens,grouping=True)
##########################################################------------------------------------MENSAL--------------------------------------################################################################
    consulta_ultimo_mes_benef_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (44,38,221)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_mes_benef_ens = round(consulta_ultimo_mes_benef_ens['PESO'].sum(),1)
    to_ton_mes_benef_ens = locale.format_string("%.2f",to_ton_mes_benef_ens,grouping=True)

#################################################-------------------------------------------ANUAL-------------------------------------------########################################################
    consulta_ultimo_ano_benef_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (44,38,221)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_ano_benef_ens = round(consulta_ultimo_ano_benef_ens['PESO'].sum(),1)
    to_ton_ano_benef_ens = locale.format_string("%.2f",to_ton_ano_benef_ens,grouping=True) 
    
#############################################---------------------------------------CAL---CH--II-------------------------------------------------#########################################################


    consulta_dia_ch = pd.read_sql(f"""

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
            AND BPROEP = 3
            AND BPROFPRO = 34

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_ch_dia = round(consulta_dia_ch['PESO'].sum(),1)
    to_ton_ch_dia = locale.format_string("%.2f",to_ton_ch_dia,grouping=True)

##################################----------------MENSAL------------------------###################################################################
    
    consulta_mes_ch = pd.read_sql(f"""

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
    AND BPROEP = 3
    AND BPROFPRO = 34

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
     #KPI´S
    to_ton_ch_mes = round(consulta_mes_ch['PESO'].sum(),1)
    to_ton_ch_mes = locale.format_string("%.2f",to_ton_ch_mes,grouping=True)

#########################----------------ANUAL--------------------------------------#################################################################
    consulta_ano_ch = pd.read_sql(f"""

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
        AND BPROEP = 3
        AND BPROFPRO = 34
        

        ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

""",connection)
    
    #KPI´S
    to_ton_ano_ch = round(consulta_ano_ch['PESO'].sum(),1)
    to_ton_ano_ch = locale.format_string("%.2f",to_ton_ano_ch,grouping=True)

######################--------------------------------------------------------ENSACADOS----------------------------------------------#######################################################
    
    consulta_dia_ch_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (41,42,222)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_dia_ch_ens = round(consulta_dia_ch_ens['PESO'].sum(),1)
    to_ton_dia_ch_ens = locale.format_string("%.2f",to_ton_dia_ch_ens,grouping=True)
##########################################################------------------------------------MENSAL--------------------------------------################################################################
    consulta_mes_ch_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (41,42,222)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_mes_ch_ens = round(consulta_mes_ch_ens['PESO'].sum(),1)
    to_ton_mes_ch_ens = locale.format_string("%.2f",to_ton_mes_ch_ens,grouping=True)
#################################################-------------------------------------------ANUAL-------------------------------------------########################################################
    consulta_ano_ch_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (41,42,222)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_ano_ch_ens = round(consulta_ano_ch_ens['PESO'].sum(),1)
    to_ton_ano_ch_ens = locale.format_string("%.2f",to_ton_ano_ch_ens,grouping=True)

######################################----------------------------------------------------CAL------HIDRAULICA---------------------------------------##########################################################
    
    consulta_dia_hid = pd.read_sql(f"""

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
            AND BPROEP = 3
            AND BPROFPRO = 35

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_hid_dia = round(consulta_dia_hid['PESO'].sum(),1)
    to_ton_hid_dia = locale.format_string("%.2f",to_ton_hid_dia,grouping=True)
##################################----------------MENSAL------------------------###################################################################
    
    consulta_mes_hid = pd.read_sql(f"""

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
    AND BPROEP = 3
    AND BPROFPRO = 35

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
     #KPI´S
    to_ton_hid_mes = round(consulta_mes_hid['PESO'].sum(),1)
    to_ton_hid_mes = locale.format_string("%.2f",to_ton_hid_mes,grouping=True)
#########################----------------ANUAL--------------------------------------#################################################################
    consulta_ano_hid = pd.read_sql(f"""

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
        AND BPROEP = 3
        AND BPROFPRO = 35
        

        ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

""",connection)
    
    #KPI´S
    to_ton_ano_hid = round(consulta_ano_hid['PESO'].sum(),1)
    to_ton_ano_hid = locale.format_string("%.2f",to_ton_ano_hid,grouping=True)

######################--------------------------------------------------------ENSACADOS----------------------------------------------#######################################################
    
    consulta_dia_hid_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (38,40)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_dia_hid_ens = round(consulta_dia_hid_ens['PESO'].sum(),1)
    to_ton_dia_hid_ens = locale.format_string("%.2f",to_ton_dia_hid_ens,grouping=True)
##########################################################------------------------------------MENSAL--------------------------------------################################################################
    consulta_mes_hid_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (38,40)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_mes_hid_ens = round(consulta_mes_hid_ens['PESO'].sum(),1)
    to_ton_mes_hid_ens = locale.format_string("%.2f",to_ton_mes_hid_ens,grouping=True)
#################################################-------------------------------------------ANUAL-------------------------------------------########################################################
    consulta_ano_hid_ens = pd.read_sql(f"""

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
            AND BPROEP = 5
            AND BPROFPRO IN (41,42,222)

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD,BPROFPRO

            """,connection)
    
        #KPI´S
    to_ton_ano_hid_ens = round(consulta_ano_hid_ens['PESO'].sum(),1)   
    to_ton_ano_hid_ens = locale.format_string("%.2f",to_ton_ano_hid_ens,grouping=True)

####################################################-------------------------------------CARREGAMENTO GERAL-----------------------------------------##################################################
    
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
        AND GALMCOD = 1827
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
        AND GALMCOD = 1827
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
        AND GALMCOD = 1827
        AND GALMPRODVENDA = 'S'
        AND (SUBSTRING(NOPFLAGNF, 2, 1) = 'S' ) --Flag Circulação de Merc. 'S' 
        AND NFEMP = 1
        AND NFFIL = 0


        GROUP BY GALMCOD,GALMNOME, ESTQCOD, ESTQNOME,NFDATAORDEM
        ORDER BY GALMCOD,GALMNOME,NFDATAORDEM, ESTQCOD
""",connection)

    tot_ton_car_geral_ano = round(consulta_car_geral_ano['QUANTIDADETN'].sum(),1) 
    tot_ton_car_geral_ano = locale.format_string("%.2f",tot_ton_car_geral_ano,grouping=True)

    context = {
        'to_ton_azbe': to_ton_azbe,
        'to_ton_azbe_mes':to_ton_azbe_mes,
        'to_ton_ano_azbe':to_ton_ano_azbe,
        'to_ton_met':to_ton_met,
        'to_ton_met_mes':to_ton_met_mes,
        'to_ton_ano_met':to_ton_ano_met,
        'to_ton_fornos_dia':to_ton_fornos_dia,
        'to_ton_fornos_mes':to_ton_fornos_mes,
        'to_ton_fornos_ano':to_ton_fornos_ano,
        'to_ton_dia_benef':to_ton_dia_benef,
        'to_ton_mes_benef':to_ton_mes_benef,
        'to_ton_ano_benef':to_ton_ano_benef,
        'to_ton_dia_benef_ens':to_ton_dia_benef_ens,
        'to_ton_mes_benef_ens':to_ton_mes_benef_ens,
        'to_ton_ano_benef_ens':to_ton_ano_benef_ens,
        'to_ton_ano_ch_ens':to_ton_ano_ch_ens,
        'to_ton_mes_ch_ens':to_ton_mes_ch_ens,
        'to_ton_dia_ch_ens':to_ton_dia_ch_ens,
        'to_ton_ano_ch':to_ton_ano_ch,
        'to_ton_ch_mes':to_ton_ch_mes,
        'to_ton_ch_dia':to_ton_ch_dia,
        'to_ton_ano_hid_ens':to_ton_ano_hid_ens,
        'to_ton_mes_hid_ens':to_ton_mes_hid_ens,
        'to_ton_dia_hid_ens':to_ton_dia_hid_ens,
        'to_ton_ano_hid':to_ton_ano_hid,
        'to_ton_hid_mes':to_ton_hid_mes,
        'to_ton_hid_dia':to_ton_hid_dia,
        'tot_ton_car_geral_dia':tot_ton_car_geral_dia,
        'tot_ton_car_geral_mes':tot_ton_car_geral_mes,
        'tot_ton_car_geral_ano':tot_ton_car_geral_ano,

    }

    return render(request,'cal.html',context)
