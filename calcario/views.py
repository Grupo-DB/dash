from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta
import locale

def home_calcario(request):
    ##############################################---------------FCMI-----DIA------------------################################################
    dia = int(-1)
    consulta_fcm1 = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
    IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

    FROM BAIXAPRODUCAO
    JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
    JOIN ESTOQUE ON ESTQCOD = IBPROREF
    LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

    WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{dia},GETDATE())AS DATE)
                                AND CAST (GETDATE() AS DATE)

    AND BPROEMP = 1
    AND BPROFIL = 0
    AND BPROSIT = 1
    AND IBPROTIPO = 'D'
    AND BPROEP = 6
    AND BPROEQP IN (110, 111)

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm1_dia = round(consulta_fcm1['PESO'].sum(),1)
    tot_hs_dia = round(consulta_fcm1['BPROHRPROD'].sum(),1)
    if tot_hs_dia != 0 :
        tn_hora_dia_fcm1 = round(ton_fcm1_dia / tot_hs_dia,1)
    else:
        tn_hora_dia_fcm1 = 0
    ton_fcm1_dia = locale.format_string("%.2f",ton_fcm1_dia,grouping=True)
################################################-------------------------FCMI---MES-------------################################################
    consulta_fcm1_mes = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
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
    AND BPROEP = 6
    AND BPROEQP IN (110, 111)

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm1_mes = round(consulta_fcm1_mes['PESO'].sum(),1)
    tot_hs_mes = round(consulta_fcm1_mes['BPROHRPROD'].sum(),1)
    if tot_hs_mes != 0 :
        tn_hora_mes_fcm1 = round(ton_fcm1_mes / tot_hs_mes,1)
    else:
        tn_hora_mes_fcm1 = 0
    ton_fcm1_mes = locale.format_string("%.2f",ton_fcm1_mes,grouping=True)

################################################--------------------FCMI-------ANO---------------########################################
    consulta_fcm1_ano = pd.read_sql(f"""
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
    AND BPROEP = 6
    AND BPROEQP IN (110, 111)

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm1_ano = round(consulta_fcm1_ano['PESO'].sum(),1)
    tot_hs_ano = round(consulta_fcm1_ano['BPROHRPROD'].sum(),1)
    if tot_hs_ano != 0 :
        tn_hora_ano_fcm1 = round(ton_fcm1_ano / tot_hs_ano,1)
    else:
         tn_hora_ano_fcm1 = 0
    ton_fcm1_ano = locale.format_string("%.2f",ton_fcm1_ano,grouping=True)
#######################################################################--------------FCM2-----DIA--------##############################
         
    dia = int(-1)
    consulta_fcm2 = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
    IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

    FROM BAIXAPRODUCAO
    JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
    JOIN ESTOQUE ON ESTQCOD = IBPROREF
    LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

    WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{dia},GETDATE())AS DATE)
                                AND CAST (GETDATE() AS DATE)

    AND BPROEMP = 1
    AND BPROFIL = 0
    AND BPROSIT = 1
    AND IBPROTIPO = 'D'
    AND BPROEP = 6
    AND BPROEQP = 169

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm2_dia = round(consulta_fcm2['PESO'].sum(),1)
    tot_hs_dia = round(consulta_fcm2['BPROHRPROD'].sum(),1)
    if tot_hs_dia != 0 :
        tn_hora_dia_fcm2 = round(ton_fcm2_dia / tot_hs_dia,1)
    else:
        tn_hora_dia_fcm2 = 0     
    ton_fcm2_dia = locale.format_string("%.2f",ton_fcm2_dia,grouping=True)
###############################################################---------FCMII--------------------MENSAL----------------###########################
    consulta_fcm2_mes = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
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
    AND BPROEP = 6
    AND BPROEQP = 169

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm2_mes = round(consulta_fcm2_mes['PESO'].sum(),1)
    tot_hs_mes = round(consulta_fcm2_mes['BPROHRPROD'].sum(),1)
    if tot_hs_mes != 0 :
        tn_hora_mes_fcm2 = round(ton_fcm2_mes / tot_hs_mes,1)
    else:
        tn_hora_mes_fcm2 = 0    
    ton_fcm2_mes = locale.format_string("%.2f",ton_fcm2_mes,grouping=True)
##########################################################-----------------FCMII--------------------ANUAL-------------#########################
        
    consulta_fcm2_ano = pd.read_sql(f"""
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
    AND BPROEP = 6
    AND BPROEQP = 169

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm2_ano = round(consulta_fcm2_ano['PESO'].sum(),1)
    tot_hs_ano = round(consulta_fcm2_ano['BPROHRPROD'].sum(),1)
    if tot_hs_ano != 0 :
        tn_hora_ano_fcm2 = round(ton_fcm2_ano / tot_hs_ano,1)
    else:
         tn_hora_ano_fcm2 = 0    
    ton_fcm2_ano = locale.format_string("%.2f",ton_fcm2_ano,grouping=True)
#######################################################-------------------------FCMIII---------------DIARIO--------#######################
         
    dia = int(-1)
    consulta_fcm3 = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
    IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

    FROM BAIXAPRODUCAO
    JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
    JOIN ESTOQUE ON ESTQCOD = IBPROREF
    LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

    WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{dia},GETDATE())AS DATE)
                                AND CAST (GETDATE() AS DATE)

    AND BPROEMP = 1
    AND BPROFIL = 0
    AND BPROSIT = 1
    AND IBPROTIPO = 'D'
    AND BPROEP = 6
    AND BPROEQP IN (18,19,20)

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm3_dia = round(consulta_fcm3['PESO'].sum(),1)
    tot_hs_dia = round(consulta_fcm3['BPROHRPROD'].sum(),1)
    if tot_hs_dia != 0 :
        tn_hora_dia_fcm3 = round(ton_fcm3_dia / tot_hs_dia,1)
    else:
        tn_hora_dia_fcm3 = 0       
    ton_fcm3_dia = locale.format_string("%.2f",ton_fcm3_dia,grouping=True)
###############################################################================FCMIII-----------MENSAL====================########################

    consulta_fcm3_mes = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
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
    AND BPROEP = 6
    AND BPROEQP IN (18,19,20)

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm3_mes = round(consulta_fcm3_mes['PESO'].sum(),1)
    tot_hs_mes = round(consulta_fcm3_mes['BPROHRPROD'].sum(),1)
    if tot_hs_mes != 0 :
        tn_hora_mes_fcm3 = round(ton_fcm3_mes / tot_hs_mes,1)
    else:
        tn_hora_mes_fcm3 = 0    
    ton_fcm3_mes = locale.format_string("%.2f",ton_fcm3_mes,grouping=True)
########################################################-----------------FCMIII----------ANUAL------##################################
        
    consulta_fcm3_ano = pd.read_sql(f"""
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
    AND BPROEP = 6
    AND BPROEQP = 169

    ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD               
            """,connection)
    
     
      #KPI´S
    ton_fcm3_ano = round(consulta_fcm3_ano['PESO'].sum(),1)
    tot_hs_ano = round(consulta_fcm3_ano['BPROHRPROD'].sum(),1)
    if tot_hs_ano != 0 :
        tn_hora_ano_fcm3 = round(ton_fcm3_ano / tot_hs_ano,1)
    else:
         tn_hora_ano_fcm3 = 0    
    ton_fcm3_ano = locale.format_string("%.2f",ton_fcm3_ano,grouping=True)

    context = {
        'tn_hora_dia_fcm1':tn_hora_dia_fcm1,
        'ton_fcm1_dia':ton_fcm1_dia,
        'tn_hora_dia_fcm2':tn_hora_dia_fcm2,
        'ton_fcm2_dia':ton_fcm2_dia,
        'tn_hora_dia_fcm3':tn_hora_dia_fcm3,
        'ton_fcm3_dia':ton_fcm3_dia,
        'tn_hora_mes_fcm1':tn_hora_mes_fcm1,
        'ton_fcm1_mes':ton_fcm1_mes,
        'tn_hora_mes_fcm2':tn_hora_mes_fcm2,
        'ton_fcm2_mes':ton_fcm2_mes,
        'tn_hora_mes_fcm3':tn_hora_mes_fcm3,
        'ton_fcm3_mes':ton_fcm3_mes,
        'tn_hora_ano_fcm1':tn_hora_ano_fcm1,
        'ton_fcm1_ano':ton_fcm1_ano,
        'tn_hora_ano_fcm2':tn_hora_ano_fcm2,
        'ton_fcm2_ano':ton_fcm2_ano,
        'tn_hora_ano_fcm3':tn_hora_ano_fcm3,
        'ton_fcm3_ano':ton_fcm3_ano,
        
        

    }

    return render(request,'calcario.html',context)