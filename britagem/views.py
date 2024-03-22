from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta
import locale


def home_britagem(request):
    rom_atual = int(-1)
    consulta_rom_dia = pd.read_sql(f"""
        SELECT C.PPDADOCHAR CLIMA, M.PPDADOCHAR MATERIAL, 

        SUM(CAL.P) CAL, SUM(CALCARIO.P) CALCARIO, SUM(DPRHRPROD) HR, 

        (ISNULL(SUM(CAL.P), 0) + ISNULL(SUM(CALCARIO.P), 0)) / CASE WHEN SUM(DPRHRPROD) = 0 THEN 1 ELSE SUM(DPRHRPROD) END TN_HR

        FROM DIARIAPROD DPR
        LEFT OUTER JOIN PESPARAMETRO C ON C.PPTPP = 4 AND C.PPREF = DPR.DPRCOD 
        LEFT OUTER JOIN PESPARAMETRO M ON M.PPTPP = 5 AND M.PPREF = DPR.DPRCOD 

        OUTER APPLY(
        SELECT SUM(ADTRPESOTOT) P 
        FROM ALIMDIARIATRANSP
        JOIN ITEMDIARIATRANSP ON IDTRCOD = ADTRIDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR
        JOIN LOCAL LD ON LD.LOCCOD = ADTRLOC
        JOIN PRODUCAOPRODUTO ON PPROCOD = LOCPPRO
        WHERE DTRSIT = 1
        AND IDTRTIPODEST = 1
        AND DTREMP = DPR.DPREMP
        AND DTRFIL = DPR.DPRFIL
        AND IDTRDPR = DPR.DPRCOD
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{rom_atual},GETDATE())AS DATE)
                                                    AND CAST (GETDATE() AS DATE)
        AND PPROCOD = 4) CAL

        OUTER APPLY(
        SELECT SUM(ADTRPESOTOT) P 
        FROM ALIMDIARIATRANSP
        JOIN ITEMDIARIATRANSP ON IDTRCOD = ADTRIDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR
        JOIN LOCAL LD ON LD.LOCCOD = ADTRLOC
        JOIN PRODUCAOPRODUTO ON PPROCOD = LOCPPRO
        WHERE DTRSIT = 1
        AND IDTRTIPODEST = 1
        AND DTREMP = DPR.DPREMP
        AND DTRFIL = DPR.DPRFIL
        AND IDTRDPR = DPR.DPRCOD
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{rom_atual},GETDATE())AS DATE)
                                                    AND CAST (GETDATE() AS DATE)
        AND PPROCOD = 5) CALCARIO

        WHERE DPRSIT = 1
        AND DPREMP = 1
        AND DPRFIL = 0
            AND CAST(DPRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{rom_atual},GETDATE())AS DATE)
                                                    AND CAST (GETDATE() AS DATE)
        AND DPREQP = 66

        GROUP BY C.PPDADOCHAR, M.PPDADOCHAR 
            """,connection)
    
        #KPI´S
    rom_calcario_dia = round(consulta_rom_dia['CALCARIO'].sum(),2)
    rom_calcario_dia = locale.format_string("%.2f",rom_calcario_dia,grouping=True)
    rom_cal_dia = round(consulta_rom_dia['CAL'].sum(),2)
    rom_cal_dia = locale.format_string("%.2f",rom_cal_dia,grouping=True)
    ########################################################################################-----MENSAL------------------------###############################################################################

    consulta_rom_mensal = pd.read_sql(f"""
        SELECT C.PPDADOCHAR CLIMA, M.PPDADOCHAR MATERIAL, 

        SUM(CAL.P) CAL, SUM(CALCARIO.P) CALCARIO, SUM(DPRHRPROD) HR, 

        (ISNULL(SUM(CAL.P), 0) + ISNULL(SUM(CALCARIO.P), 0)) / CASE WHEN SUM(DPRHRPROD) = 0 THEN 1 ELSE SUM(DPRHRPROD) END TN_HR

        FROM DIARIAPROD DPR
        LEFT OUTER JOIN PESPARAMETRO C ON C.PPTPP = 4 AND C.PPREF = DPR.DPRCOD 
        LEFT OUTER JOIN PESPARAMETRO M ON M.PPTPP = 5 AND M.PPREF = DPR.DPRCOD 

        OUTER APPLY(
        SELECT SUM(ADTRPESOTOT) P 
        FROM ALIMDIARIATRANSP
        JOIN ITEMDIARIATRANSP ON IDTRCOD = ADTRIDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR
        JOIN LOCAL LD ON LD.LOCCOD = ADTRLOC
        JOIN PRODUCAOPRODUTO ON PPROCOD = LOCPPRO
        WHERE DTRSIT = 1
        AND IDTRTIPODEST = 1
        AND DTREMP = DPR.DPREMP
        AND DTRFIL = DPR.DPRFIL
        AND IDTRDPR = DPR.DPRCOD
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DTRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))

        AND PPROCOD = 4) CAL

        OUTER APPLY(
        SELECT SUM(ADTRPESOTOT) P 
        FROM ALIMDIARIATRANSP
        JOIN ITEMDIARIATRANSP ON IDTRCOD = ADTRIDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR
        JOIN LOCAL LD ON LD.LOCCOD = ADTRLOC
        JOIN PRODUCAOPRODUTO ON PPROCOD = LOCPPRO
        WHERE DTRSIT = 1
        AND IDTRTIPODEST = 1
        AND DTREMP = DPR.DPREMP
        AND DTRFIL = DPR.DPRFIL
        AND IDTRDPR = DPR.DPRCOD
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DTRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))

        AND PPROCOD = 5) CALCARIO

        WHERE DPRSIT = 1
        AND DPREMP = 1
        AND DPRFIL = 0
            AND DPRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DPRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))

        AND DPREQP = 66

        GROUP BY C.PPDADOCHAR, M.PPDADOCHAR 
            """,connection)
    ##KPI´S
    rom_calcario_mes = round(consulta_rom_mensal['CALCARIO'].sum(),2)
    rom_cal_mes = round(consulta_rom_mensal['CAL'].sum(),2)
    vol_brit = rom_calcario_mes + rom_cal_mes
    rom_calcario_mes = locale.format_string("%.2f",rom_calcario_mes,grouping=True)
    rom_cal_mes = locale.format_string("%.2f",rom_cal_mes,grouping=True)
##############################################################################----------------ANUAL--------------#######################################################@##############################
    
    consulta_rom_anual = pd.read_sql(f"""
        SELECT C.PPDADOCHAR CLIMA, M.PPDADOCHAR MATERIAL, 

        SUM(CAL.P) CAL, SUM(CALCARIO.P) CALCARIO, SUM(DPRHRPROD) HR, 

        (ISNULL(SUM(CAL.P), 0) + ISNULL(SUM(CALCARIO.P), 0)) / CASE WHEN SUM(DPRHRPROD) = 0 THEN 1 ELSE SUM(DPRHRPROD) END TN_HR

        FROM DIARIAPROD DPR
        LEFT OUTER JOIN PESPARAMETRO C ON C.PPTPP = 4 AND C.PPREF = DPR.DPRCOD 
        LEFT OUTER JOIN PESPARAMETRO M ON M.PPTPP = 5 AND M.PPREF = DPR.DPRCOD 

        OUTER APPLY(
        SELECT SUM(ADTRPESOTOT) P 
        FROM ALIMDIARIATRANSP
        JOIN ITEMDIARIATRANSP ON IDTRCOD = ADTRIDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR
        JOIN LOCAL LD ON LD.LOCCOD = ADTRLOC
        JOIN PRODUCAOPRODUTO ON PPROCOD = LOCPPRO
        WHERE DTRSIT = 1
        AND IDTRTIPODEST = 1
        AND DTREMP = DPR.DPREMP
        AND DTRFIL = DPR.DPRFIL
        AND IDTRDPR = DPR.DPRCOD
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DTRDATA1 <= GETDATE()
        AND PPROCOD = 4) CAL

        OUTER APPLY(
        SELECT SUM(ADTRPESOTOT) P 
        FROM ALIMDIARIATRANSP
        JOIN ITEMDIARIATRANSP ON IDTRCOD = ADTRIDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR
        JOIN LOCAL LD ON LD.LOCCOD = ADTRLOC
        JOIN PRODUCAOPRODUTO ON PPROCOD = LOCPPRO
        WHERE DTRSIT = 1
        AND IDTRTIPODEST = 1
        AND DTREMP = DPR.DPREMP
        AND DTRFIL = DPR.DPRFIL
        AND IDTRDPR = DPR.DPRCOD
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DTRDATA1 <= GETDATE()
        AND PPROCOD = 5) CALCARIO

        WHERE DPRSIT = 1
        AND DPREMP = 1
        AND DPRFIL = 0
          AND  DPRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DPRDATA1 <= GETDATE()
        AND DPREQP = 66

        GROUP BY C.PPDADOCHAR, M.PPDADOCHAR 
            """,connection)
    ##KPI´S
    rom_calcario_ano = round(consulta_rom_anual['CALCARIO'].sum(),2)
    rom_calcario_ano = locale.format_string("%.2f",rom_calcario_ano,grouping=True)
    rom_cal_ano = round(consulta_rom_anual['CAL'].sum(),2)
    rom_cal_ano = locale.format_string("%.2f",rom_cal_ano,grouping=True)

################################################################################-------------------EVENTOS DE PARADA------------------------------###############################################################
    parada_atual = int(-2)
    consulta_evento_parada = pd.read_sql(f"""

    SELECT EVDCOD,  EVDNOME EVENTO, SUM(EDPRHRTOT * 3600) TEMPO,

(SUM(EDPRHRTOT * 3600) / (SELECT SUM(EDPRHRTOT * 3600) 
                          FROM DIARIAPROD
                          JOIN EVENTODIARIAPROD ON EDPRDPR = DPRCOD
                          WHERE DPRSIT = 1
                          AND DPREMP = 1
                          AND DPRFIL = 0
                          AND CAST(DPRDATA1 as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)
                          AND DPREQP = 66)) * 100 PERC

                        FROM DIARIAPROD
                        JOIN EVENTODIARIAPROD ON EDPRDPR = DPRCOD
                        JOIN EVENTODIARIA ON EVDCOD = EDPREVD

                        WHERE DPRSIT = 1
                        AND DPREMP = 1
                        AND DPRFIL = 0
                        AND CAST(DPRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{parada_atual},GETDATE())AS DATE)
                                                                    AND CAST (GETDATE() AS DATE)
                        AND DPREQP = 66

                        GROUP BY EVDCOD, EVDNOME

""",connection)
    
    ##KPI´S MAN MEC
    mec = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==15,['TEMPO','PERC']]
    x = mec['PERC'].values
    if x != 0 and x =='None':
        x_str = ', '.join(map(str, x))
        x_str = round(float(x_str),1)
    else:
        x_str = 0
    y = mec['TEMPO'].values
    if y != 0 and y =='None':
        y_str = ', '.join(map(str, y))
        y_str = round(float(y_str) / 3600,1)
    else:    
        y_str = 0

    #########PREPARANDO LOCAL
    loca = consulta_evento_parada.loc[consulta_evento_parada['EVDCOD']==9,['TEMPO','PERC']]
    a = loca['PERC'].values
    if a != 0 and a =='None':
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
    if c != 0 and c =='None':
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
    if e != 0 and e =='None':
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
    if g != 0 and g =='None':
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
    if i != 0 and i =='None':
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
    if l != 0 and l =='None':
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





    ######################################################-----------------------MOVIMENTAÇÕES DE CARGA----------------------------##################################################################
        

    mov_dia = int(-1)
    consulta_mov_cargas = pd.read_sql(f"""
        SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1 INICIO, DTRDATA2 FIM,

'MINA' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

FROM ITEMDIARIATRANSP IDTR
JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

WHERE DTRSIT = 1
AND DTREMP = 1
AND DTRFIL = 0
AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{mov_dia},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+100+%'
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+101+%'
AND IDTRTIPODEST = 1
AND IDTRDESTINO = 66

UNION ALL

SELECT 2 SEQ, DTRREF DIARIA, DTRDATA1 INICIO, DTRDATA2 FIM,

'MINA' ORIGEM, 'ESTOQUE' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

FROM ITEMDIARIATRANSP IDTR
JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

WHERE DTRSIT = 1
AND DTREMP = 1
AND DTRFIL = 0
AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{mov_dia},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+100+%'
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+101+%'
AND IDTRTIPODEST = 0
AND ((SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+12+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+13+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+100+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+101+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+21+%')

UNION ALL

SELECT 3 SEQ, DTRREF DIARIA, DTRDATA1 INICIO, DTRDATA2 FIM,

'ESTOQUE' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

FROM ITEMDIARIATRANSP IDTR
JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

WHERE DTRSIT = 1
AND DTREMP = 1
AND DTRFIL = 0
AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{mov_dia},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)
AND ((SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+12+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+13+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+100+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+101+%' OR
     (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
             ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
      FROM LOCAL L1
      LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
      LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
      WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+21+%')
AND IDTRTIPODEST = 1
AND IDTRDESTINO = 66

UNION ALL

SELECT 4 SEQ, DTRREF DIARIA, DTRDATA1 INICIO, DTRDATA2 FIM,

'MINA' ORIGEM, 'REJEITO' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

FROM ITEMDIARIATRANSP IDTR
JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

WHERE DTRSIT = 1
AND DTREMP = 1
AND DTRFIL = 0
AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{mov_dia},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
AND IDTRPPRO = 3
    """,connection)

    ###KPI´S
    mb = consulta_mov_cargas.loc[(consulta_mov_cargas['ORIGEM']=='MINA') & (consulta_mov_cargas['DESTINO']=='BRITADOR')]
    tot_tn_mn_brit = round(mb['PESO'].sum(),1)
    tot_tn_mn_brit = locale.format_string("%.2f",tot_tn_mn_brit,grouping=True)

    me = consulta_mov_cargas.loc[(consulta_mov_cargas['ORIGEM']=='MINA') & (consulta_mov_cargas['DESTINO']=='ESTOQUE')]
    tot_tn_me = round(me['PESO'].sum(),1)
    tot_tn_me = locale.format_string("%.2f",tot_tn_me,grouping=True)

    eb = consulta_mov_cargas.loc[(consulta_mov_cargas['ORIGEM']=='ESTOQUE') & (consulta_mov_cargas['DESTINO']=='BRITADOR')]
    tot_tn_eb = round(eb['PESO'].sum(),1)
    tot_tn_eb = locale.format_string("%.2f",tot_tn_eb,grouping=True)

    mr = consulta_mov_cargas.loc[(consulta_mov_cargas['ORIGEM']=='MINA') & (consulta_mov_cargas['DESTINO']=='REJEITO')]
    tot_tn_mr = round(mr['PESO'].sum(),1)
    tot_tn_mr = locale.format_string("%.2f",tot_tn_mr,grouping=True)

#################################################--------------------------------MENSAL-------------''''''''''''''''''''''''''''''''''''''''''''''''''

    consulta_mov_cargas_me = pd.read_sql(f"""
        SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,

        'MINA' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DTRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+100+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+101+%'
        AND IDTRTIPODEST = 1
        AND IDTRDESTINO = 66

        UNION ALL

        SELECT 2 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,

        'MINA' ORIGEM, 'ESTOQUE' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DTRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+100+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+101+%'
        AND IDTRTIPODEST = 0
        AND ((SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+12+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+13+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+100+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+101+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+21+%')

        UNION ALL

        SELECT 3 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,

        'ESTOQUE' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DTRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
        AND ((SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+12+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+13+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+100+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+101+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+21+%')
        AND IDTRTIPODEST = 1
        AND IDTRDESTINO = 66

        UNION ALL

        SELECT 4 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,

        'MINA' ORIGEM, 'REJEITO' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND DTRDATA1 < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1))
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
        AND IDTRPPRO = 3
    """,connection)

    ###KPI´S
    mb_me = consulta_mov_cargas_me.loc[(consulta_mov_cargas_me['ORIGEM']=='MINA') & (consulta_mov_cargas_me['DESTINO']=='BRITADOR')]
    tot_tn_mn_brit_me = round(mb_me['PESO'].sum(),1)
    tot_tn_mn_brit_me = locale.format_string("%.2f",tot_tn_mn_brit_me,grouping=True)

    me_me = consulta_mov_cargas_me.loc[(consulta_mov_cargas_me['ORIGEM']=='MINA') & (consulta_mov_cargas_me['DESTINO']=='ESTOQUE')]
    tot_tn_me_me = round(me_me['PESO'].sum(),1)
    tot_tn_me_me = locale.format_string("%.2f",tot_tn_me_me,grouping=True)

    eb_me = consulta_mov_cargas_me.loc[(consulta_mov_cargas_me['ORIGEM']=='ESTOQUE') & (consulta_mov_cargas_me['DESTINO']=='BRITADOR')]
    tot_tn_eb_me = round(eb_me['PESO'].sum(),1)
    tot_tn_eb_me = locale.format_string("%.2f",tot_tn_eb_me,grouping=True)

    mr_me = consulta_mov_cargas_me.loc[(consulta_mov_cargas_me['ORIGEM']=='MINA') & (consulta_mov_cargas_me['DESTINO']=='REJEITO')]
    tot_tn_mr_me = round(mr_me['PESO'].sum(),1)
    tot_tn_mr_me = locale.format_string("%.2f",tot_tn_mr_me,grouping=True)


################################################---------------anual-------------------####################################

    consulta_mov_cargas_ano = pd.read_sql(f"""
        SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,
        'MINA' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DTRDATA1 <= GETDATE()
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+100+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+101+%'
        AND IDTRTIPODEST = 1
        AND IDTRDESTINO = 66

        UNION ALL

        SELECT 2 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,

        'MINA' ORIGEM, 'ESTOQUE' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DTRDATA1 <= GETDATE()
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+100+%'
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+101+%'
        AND IDTRTIPODEST = 0
        AND ((SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+12+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+13+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+100+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+101+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRDESTINO) LIKE '%+21+%')

        UNION ALL

        SELECT 3 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,

        'ESTOQUE' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DTRDATA1 <= GETDATE()
        AND ((SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+12+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+13+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+100+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+101+%' OR
            (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+21+%')
        AND IDTRTIPODEST = 1
        AND IDTRDESTINO = 66

        UNION ALL

        SELECT 4 SEQ, DTRREF DIARIA, DTRDATA1 INICIO,

        'MINA' ORIGEM, 'REJEITO' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND DTRDATA1 >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND DTRDATA1 <= GETDATE()
        AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
                    ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
            FROM LOCAL L1
            LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
            LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
            WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
        AND IDTRPPRO = 3
    """,connection)

    ###KPI´S
    mb_ano = consulta_mov_cargas_ano.loc[(consulta_mov_cargas_ano['ORIGEM']=='MINA') & (consulta_mov_cargas_ano['DESTINO']=='BRITADOR')]
    tot_tn_mn_brit_ano = round(mb_ano['PESO'].sum(),1)
    tot_tn_mn_brit_ano = locale.format_string("%.2f",tot_tn_mn_brit_ano,grouping=True)

    me_ano = consulta_mov_cargas_ano.loc[(consulta_mov_cargas_ano['ORIGEM']=='MINA') & (consulta_mov_cargas_ano['DESTINO']=='ESTOQUE')]
    tot_tn_me_ano = round(me_ano['PESO'].sum(),1)
    tot_tn_me_ano = locale.format_string("%.2f",tot_tn_me_ano,grouping=True)

    eb_ano = consulta_mov_cargas_ano.loc[(consulta_mov_cargas_ano['ORIGEM']=='ESTOQUE') & (consulta_mov_cargas_ano['DESTINO']=='BRITADOR')]
    tot_tn_eb_ano = round(eb_ano['PESO'].sum(),1)
    tot_tn_eb_ano = locale.format_string("%.2f",tot_tn_eb_ano,grouping=True)

    mr_ano = consulta_mov_cargas_ano.loc[(consulta_mov_cargas_ano['ORIGEM']=='MINA') & (consulta_mov_cargas_ano['DESTINO']=='REJEITO')]
    tot_tn_mr_ano = round(mr_ano['PESO'].sum(),1)
    tot_tn_mr_ano = locale.format_string("%.2f",tot_tn_mr_ano,grouping=True)


    context =  {
            'rom_calcario_dia':rom_calcario_dia,
            'rom_cal_dia': rom_cal_dia,
            'rom_calcario_mes': rom_calcario_mes,
            'rom_cal_mes': rom_cal_mes,
            'rom_calcario_ano': rom_calcario_ano,
            'rom_cal_ano': rom_cal_ano,
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
            'tot_tn_mn_brit':tot_tn_mn_brit,
            'tot_tn_me':tot_tn_me,
            'tot_tn_eb':tot_tn_eb,
            'tot_tn_mr':tot_tn_mr,
            'tot_tn_mn_brit_me':tot_tn_mn_brit_me,
            'tot_tn_me_me':tot_tn_me_me,
            'tot_tn_eb_me':tot_tn_eb_me,
            'tot_tn_mr_me':tot_tn_mr_me,
            'tot_tn_mn_brit_ano':tot_tn_mn_brit_ano,
            'tot_tn_me_ano':tot_tn_me_ano,
            'tot_tn_eb_ano':tot_tn_eb_ano,
            'tot_tn_mr_ano':tot_tn_mr_ano,
            'vol_brit':vol_brit,


        }
    return render(request, 'britagem.html',context)