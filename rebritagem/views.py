from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta
import locale
def home_rebritagem(request):
    #diaria
    dia = int(-1)
    consulta_rebri_diaria = pd.read_sql(f"""

        SELECT C.PPDADOCHAR CLIMA, M.PPDADOCHAR MATERIAL,
                               
        SUM(DPRHRPROD) HR, SUM(ADPRPESOTOT) TN

        FROM ALIMDIARIAPROD
        JOIN DIARIAPROD ON DPRCOD = ADPRDPR
        JOIN EQUIPAMENTO ON EQPCOD = DPREQP
        LEFT OUTER JOIN PESPARAMETRO C ON C.PPTPP = 4 AND C.PPREF = DPRCOD 
        LEFT OUTER JOIN PESPARAMETRO M ON M.PPTPP = 5 AND M.PPREF = DPRCOD 

        WHERE ADPREQP IN (91,92)
        AND CAST(DPRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{dia},GETDATE())AS DATE)
                                                            AND CAST (GETDATE() AS DATE)
        GROUP BY EQPCOD, EQPAUTOMTAG, C.PPDADOCHAR, M.PPDADOCHAR

        ORDER BY CLIMA, MATERIAL
                               """,connection)
    
        #KPI´S
    tot_tn_rebri_dia = round(consulta_rebri_diaria['TN'].sum(),1)
    tot_tn_rebri_dia = locale.format_string("%.2f",tot_tn_rebri_dia,grouping=True)

####################################-----------------------MES-----------------#################################
    consulta_rebri_mes = pd.read_sql(f"""

        SELECT C.PPDADOCHAR CLIMA, M.PPDADOCHAR MATERIAL,
                               
        SUM(DPRHRPROD) HR, SUM(ADPRPESOTOT) TN

        FROM ALIMDIARIAPROD
        JOIN DIARIAPROD ON DPRCOD = ADPRDPR
        JOIN EQUIPAMENTO ON EQPCOD = DPREQP
        LEFT OUTER JOIN PESPARAMETRO C ON C.PPTPP = 4 AND C.PPREF = DPRCOD 
        LEFT OUTER JOIN PESPARAMETRO M ON M.PPTPP = 5 AND M.PPREF = DPRCOD 

        WHERE ADPREQP IN (91,92)
        AND DPRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DPRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
        GROUP BY EQPCOD, EQPAUTOMTAG, C.PPDADOCHAR, M.PPDADOCHAR

        ORDER BY CLIMA, MATERIAL
                               """,connection)
    
        #KPI´S
    tot_tn_rebri_mes = round(consulta_rebri_mes['TN'].sum(),1)
    tot_tn_rebri_mes = locale.format_string("%.2f",tot_tn_rebri_mes,grouping=True)

###############################---------------------------ANUAL---------------------------##############################################################
    
    consulta_rebri_ano = pd.read_sql(f"""

        SELECT C.PPDADOCHAR CLIMA, M.PPDADOCHAR MATERIAL,
                               
        SUM(DPRHRPROD) HR, SUM(ADPRPESOTOT) TN

        FROM ALIMDIARIAPROD
        JOIN DIARIAPROD ON DPRCOD = ADPRDPR
        JOIN EQUIPAMENTO ON EQPCOD = DPREQP
        LEFT OUTER JOIN PESPARAMETRO C ON C.PPTPP = 4 AND C.PPREF = DPRCOD 
        LEFT OUTER JOIN PESPARAMETRO M ON M.PPTPP = 5 AND M.PPREF = DPRCOD 

        WHERE ADPREQP IN (91,92)
        AND DPRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DPRDATA1 <= GETDATE()
        GROUP BY EQPCOD, EQPAUTOMTAG, C.PPDADOCHAR, M.PPDADOCHAR

        ORDER BY CLIMA, MATERIAL
                               """,connection)
    
        #KPI´S
    tot_tn_rebri_ano = round(consulta_rebri_ano['TN'].sum(),1)
    tot_tn_rebri_ano = locale.format_string("%.2f",tot_tn_rebri_ano,grouping=True)

################################################--------------EVENTOS de PARADA------------------------################################################
    parada_atual = int(-1)
    consulta_evento_parada = pd.read_sql(f"""

        SELECT EVDCOD, EVDNOME EVENTO, SUM(EDPRHRTOT * 3600) TEMPO,

        (SUM(EDPRHRTOT * 3600) / (SELECT SUM(EDPRHRTOT * 3600) 
                                FROM DIARIAPROD
                                JOIN EVENTODIARIAPROD ON EDPRDPR = DPRCOD
                                WHERE DPRSIT = 1
                                AND DPREMP = 1
                                AND DPRFIL = 0
                                AND CAST(DPRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{parada_atual},GETDATE())AS DATE)
                                                            AND CAST (GETDATE() AS DATE)
                                AND DPREQP IN (91,92))) * 100 PERC

        FROM DIARIAPROD
        JOIN EVENTODIARIAPROD ON EDPRDPR = DPRCOD
        JOIN EVENTODIARIA ON EVDCOD = EDPREVD

        WHERE DPRSIT = 1
        AND DPREMP = 1
        AND DPRFIL = 0
        AND CAST(DPRDATA1 as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                                            AND CAST (GETDATE() AS DATE)
                                AND DPREQP IN (91,92)
        GROUP BY EVDCOD, EVDNOME

        ORDER BY EVDCOD, EVDNOME

""",connection)
    
    ##KPI´S MAN MEC
    mec = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==15,['TEMPO','PERC']]
    x = mec['PERC'].values
    if x != 0:
        x_str = ', '.join(map(str, x))
        x_str = round(float(x_str),1)
    else:
        x_str = 0
    y = mec['TEMPO'].values
    if y != 0:
        y_str = ', '.join(map(str, y))
        y_str = round(float(y_str) / 3600,1)
    else:    
        y_str = 0

    #########PREPARANDO LOCAL
    loca = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==9,['TEMPO','PERC']]
    a = loca['PERC'].values
    if a != 0:
        a_str = ', '.join(map(str, a))
        a_str = round(float(a_str),1)
    else:
        a_str = 0
    b = loca['TEMPO'].values
    if b != 0:
        b_str = ', '.join(map(str, b))
        b_str = round(float(b_str) / 3600,1)
    else:    
        b_str = 0

    ###########--EMBUCHAMENTO-DESARME######################
    des = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==26,['TEMPO','PERC']]
    c = des['PERC'].values
    if c != 0:
        c_str = ', '.join(map(str, c))
        c_str = round(float(c_str),1)
    else:
        c_str = 0
    d = des['TEMPO'].values
    if d != 0:
        d_str = ', '.join(map(str, d))
        d_str = round(float(d_str) / 3600,1)
    else:    
        d_str = 0

    ################--ALMOÇO/JANTA----------########################
    alm = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==6,['TEMPO','PERC']]
    e = alm['PERC'].values
    if e != 0:
        e_str = ', '.join(map(str, e))
        e_str = round(float(e_str),1)
    else:
        e_str = 0
    f = alm['TEMPO'].values
    if f != 0:
        f_str = ', '.join(map(str, f))
        f_str = round(float(f_str) / 3600,1)
    else:    
        f_str = 0

    ############--------SETUP------------###############################
    tro = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==27,['TEMPO','PERC']]
    g = tro['PERC'].values
    if g != 0:
        g_str = ', '.join(map(str, g))
        g_str = round(float(g_str),1)
    else:
        g_str = 0
    h = tro['TEMPO'].values
    if h != 0:
        h_str = ', '.join(map(str, h))
        h_str = round(float(h_str) / 3600,1)
    else:    
        h_str = 0

    ############--------Alimentador ------------###############################
    ades = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==53,['TEMPO','PERC']]
    i = ades['PERC'].values
    if i != 0:
        i_str = ', '.join(map(str, i))
        i_str = round(float(i_str),1)
    else:
        i_str = 0
    j = ades['TEMPO'].values
    if j != 0:
        j_str = ', '.join(map(str, j))
        j_str = round(float(j_str) / 3600,1)
    else:    
        j_str = 0  

    ############--------Materia Prima ------------###############################
    mpr = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==14,['TEMPO','PERC']]
    l = mpr['PERC'].values
    if l != 0:
        l_str = ', '.join(map(str, l))
        l_str = round(float(l_str),1)
    else:
        l_str = 0
    m = mpr['TEMPO'].values
    if m != 0:
        m_str = ', '.join(map(str, m))
        m_str = round(float(m_str) / 3600,1)
    else:    
        m_str = 0

    context = {
            'tot_tn_rebri_dia':tot_tn_rebri_dia,
            'tot_tn_rebri_mes':tot_tn_rebri_mes,
            'tot_tn_rebri_ano':tot_tn_rebri_ano,
            'x':x_str,
            'y':y_str,
            'a':a_str,
            'b':b_str,
            'c':c_str,
            'd':d_str,
            'e':e_str,
            'f':f_str,
            'g':g_str,
            'h':h_str,
            'i':i_str,
            'j':j_str,
            'l':l_str,
            'm':m_str,
        }

    return render(request,'rebritagem.html',context)
