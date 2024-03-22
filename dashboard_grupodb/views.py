from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta
import plotly as pl
import plotly_express as px
import plotly.io as pio
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
######################################################################### ATUAL #######################################################################################################################
#home
def home(request):
      
      #CALCARIO
      atual = int(-1)
      consulta_calcario = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 6

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_calcario =(consulta_calcario['PESO'].sum())
      ton_calcario = locale.format_string("%.2f",ton_calcario,grouping=True) 
       
    
      #FERTILIZANTES
      atual = int(-1)         
      consulta_fertilizante = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 8

          ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                     
     """,connection)
      
      #KPI´S
      ton_fertilizante = consulta_fertilizante['PESO'].sum()
      ton_fertilizante = locale.format_string("%.2f",ton_fertilizante,grouping=True)

      #CAL     
      atual = int(-1)    
      consulta_cal = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 3

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_cal = consulta_cal['PESO'].sum()
      ton_cal = locale.format_string("%.2f",ton_cal,grouping=True)

      j = consulta_cal.groupby('ESTQAPELIDO',)['PESO'].sum() 

      fig_cal_ano = px.bar(
        j,
        y='PESO',
        height=250,
        width=380,
        color="PESO",
        color_continuous_scale=px.colors.sequential.Viridis_r
        )
      fig_cal_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_cal_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_cal = pio.to_html(fig_cal_ano, include_plotlyjs=False, full_html=False)

      #Argamassa     
      atual = int(-1)
      consulta_argamassa = pd.read_sql(f"""
      SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy')DATAW, ESTQCOD, ESTQAPELIDO,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 1

          ORDER BY BPRODATA, BPROCOD, ESTQCOD,ESTQAPELIDO
                                     
     """,connection)
       
      #KPI´S
      ton_argamassa = consulta_argamassa['PESO'].sum()
      ton_argamassa = locale.format_string("%.2f",ton_argamassa,grouping=True)

      h = consulta_argamassa.groupby('ESTQAPELIDO')['PESO'].sum()
      fig_arg_ano = px.scatter(
        h,
        y='PESO',
        size='PESO',
        height=250,
        width=380,
        color="PESO",
        color_continuous_scale=px.colors.sequential.Viridis_r
        )  
      fig_arg_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_arg_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_arg = pio.to_html(fig_arg_ano, include_plotlyjs=False, full_html=False)
       
      

          ################################################---------------------OS--------MANUTENÇÂO---########################################


      os_atual = int(-1)
      consulta_os_atual = pd.read_sql(f"""    
        SELECT MANCOD, MANSIT, MANDESC,FORMAT(MANDTABERT,'dd/MM/yyyy')
        FROM MANUTENCAO 
        WHERE CAST (MANDTABERT as date) BETWEEN CAST (DATEADD(DAY,{os_atual},GETDATE())AS DATE)
                                        AND CAST (GETDATE()AS DATE)  
        AND MANSIT IN (2,4)
                    """,connection)

        #KPI'S
      os_total = consulta_os_atual.groupby('MANSIT')['MANCOD'].sum()
      #grafico
      fig_os_dia = px.pie(
        consulta_os_atual,
        names='MANSIT',
        height=250,
        width=250,
        )
      
      plot_div = pio.to_html(fig_os_dia, include_plotlyjs=False, full_html=False)


      #######################################################===========TOTAL===BRITAGEM======================================================================================
      britagem_atual = int(-1) 
      consulta_britagem_atual = pd.read_sql(f"""
        SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1 INICIO, DTRDATA2 FIM,

        'MINA' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
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
AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
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
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
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
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
                                                    AND CAST (GETDATE() AS DATE)AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
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

      ton_britagem = consulta_britagem_atual['PESO'].sum()
      ton_britagem = locale.format_string("%.2f",ton_britagem,grouping=True)

      fig_brit_ano = px.pie(
      consulta_britagem_atual,
        values="PESO",
        names='DESTINO',
        height=250,
        width=380,
        color_discrete_sequence=px.colors.sequential.Agsunset        
        )
      fig_brit_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_brit_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_brit = pio.to_html(fig_brit_ano, include_plotlyjs=False, full_html=False)


      #britador

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
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
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
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                                    AND CAST (GETDATE() AS DATE)
        AND PPROCOD = 5) CALCARIO

        WHERE DPRSIT = 1
        AND DPREMP = 1
        AND DPRFIL = 0
            AND CAST(DPRDATA1 as date) BETWEEN CAST (DATEADD (DAY,-1,GETDATE())AS DATE)
                                                    AND CAST (GETDATE() AS DATE)
        AND DPREQP = 66

        GROUP BY C.PPDADOCHAR, M.PPDADOCHAR 
            """,connection)
    
        #KPI´S
      rom_calcario_dia = round(consulta_rom_dia['CALCARIO'].sum(),2)
      rom_cal_dia = round(consulta_rom_dia['CAL'].sum(),2)
      vol_brit = rom_cal_dia + rom_calcario_dia
      vol_brit = locale.format_string("%.2f",vol_brit,grouping=True)

      context = {
            'os_total': os_total,
            'fig_calc_dia':plot_div,
            'total_calcario': ton_calcario,
            'total_fertilizante': ton_fertilizante,
            'total_cal': ton_cal,
            'total_argamassa':ton_argamassa,
            'ton_britagem':ton_britagem,
            'vol_brit':vol_brit,
            'plot_brit':plot_brit,
            'plot_cal':plot_cal,
            'plot_arg':plot_arg,
      }

      return render(request, 'home.html',context)

############################################################################################ ###################################################################################################

############################################################################### ÚLTIMO MêS ####################################################################################################################

def mensal(request):
      #CALCARIO
      consulta_calcario = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,
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

          ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_calcario = round(consulta_calcario['PESO'].sum(),2)
      ton_calcario = locale.format_string("%.2f",ton_calcario,grouping=True)

      #FERTILIZANTES   
      consulta_fertilizante = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,
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
          AND BPROEP = 8

          ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                     
     """,connection)
      
      #KPI´S
      ton_fertilizante = round(consulta_fertilizante['PESO'].sum(),2)
      ton_fertilizante = locale.format_string("%.2f",ton_fertilizante,grouping=True)

      #CAL       
      consulta_cal = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
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

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_cal = round(consulta_cal['PESO'].sum(),2)
      ton_cal = locale.format_string("%.2f",ton_cal,grouping=True)

      j = consulta_cal.groupby('ESTQAPELIDO',)['PESO'].sum() 

      fig_cal_ano = px.bar(
        j,
        y='PESO',
        height=250,
        width=380,
        color="PESO",
        color_continuous_scale=px.colors.sequential.Viridis_r
        )
      fig_cal_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_cal_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_cal = pio.to_html(fig_cal_ano, include_plotlyjs=False, full_html=False)

      #Argamassa     
      consulta_argamassa = pd.read_sql(f"""
      SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
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

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_argamassa = round(consulta_argamassa['PESO'].sum(),2)
      ton_argamassa = locale.format_string("%.2f",ton_argamassa,grouping=True)

      h = consulta_argamassa.groupby('ESTQAPELIDO')['PESO'].sum()
      fig_arg_ano = px.scatter(
        h,
        y='PESO',
        size='PESO',
        height=250,
        width=380,
        color="PESO",
        color_continuous_scale=px.colors.sequential.Viridis_r
        )  
      fig_arg_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_arg_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_arg = pio.to_html(fig_arg_ano, include_plotlyjs=False, full_html=False)


      consulta_britagem_mes = pd.read_sql(f"""
        SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1,

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

                                                                        
        SELECT 3 SEQ, DTRREF DIARIA, DTRDATA1,

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

SELECT 4 SEQ, DTRREF DIARIA, DTRDATA1,

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

      ton_britagem = consulta_britagem_mes['PESO'].sum()
      ton_britagem = locale.format_string("%.2f",ton_britagem,grouping=True)

      fig_brit_ano = px.pie(
      consulta_britagem_mes,
        values="PESO",
        names='DESTINO',
        height=250,
        width=380,
        color_discrete_sequence=px.colors.sequential.Agsunset        
        )
      fig_brit_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_brit_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_brit = pio.to_html(fig_brit_ano, include_plotlyjs=False, full_html=False)

      consulta_os_mes = pd.read_sql(f"""    
        SELECT MANCOD, MANSIT, MANDESC,FORMAT(MANDTABERT,'dd/MM/yyyy')
        FROM MANUTENCAO 
        WHERE MANDTABERT >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            AND MANDTABERT < DATEADD(month, 1, DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)) 
        AND MANSIT IN (2,4)
                    """,connection)

        #KPI'S
      os_total = consulta_os_mes['MANCOD'].count()

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
      vol_brit = locale.format_string("%.2f",vol_brit,grouping=True)
      context = {
            'total_calcario': ton_calcario,
            'total_fertilizante': ton_fertilizante,
            'total_cal': ton_cal,
            'total_argamassa':ton_argamassa,
            'ton_britagem':ton_britagem,
            'os_total':os_total,
            'vol_brit':vol_brit,
            'plot_brit':plot_brit,
            'plot_cal':plot_cal,
            'plot_arg':plot_arg
      }

      return render(request, 'home.html',context)

###################################################################################### ULTIMO ANO ###########################################################################################################

def anual(request):
      #CALCARIO
      consulta_calcario = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,
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

          ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_calcario = round(consulta_calcario['PESO'].sum(),2)
      ton_calcario = locale.format_string("%.2f",ton_calcario,grouping=True)  

      #FERTILIZANTES         
      consulta_fertilizante = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,
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
          AND BPROEP = 8

          ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                     
     """,connection)
      
      #KPI´S
      ton_fertilizante = round(consulta_fertilizante['PESO'].sum(),2)
      ton_fertilizante = locale.format_string("%.2f",ton_fertilizante,grouping=True)

      #CAL      
      consulta_cal = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
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

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
      
      #KPI´S
      ton_cal = round(consulta_cal['PESO'].sum(),2)
      ton_cal = locale.format_string("%.2f",ton_cal,grouping=True) 

      j = consulta_cal.groupby('ESTQAPELIDO',)['PESO'].sum() 

      fig_cal_ano = px.bar(
        j,
        y='PESO',
        height=250,
        width=380,
        color="PESO",
        color_continuous_scale=px.colors.sequential.Viridis_r
        )
      fig_cal_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_cal_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_cal = pio.to_html(fig_cal_ano, include_plotlyjs=False, full_html=False)


      #Argamassa     
      consulta_argamassa_ano = pd.read_sql(f"""
      SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
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

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
       

      #KPI´S
      ton_argamassa = round(consulta_argamassa_ano['PESO'].sum(),2)
      ton_argamassa = locale.format_string("%.2f",ton_argamassa,grouping=True)  
      h = consulta_argamassa_ano.groupby('ESTQAPELIDO')['PESO'].sum()
      fig_arg_ano = px.scatter(
        h,
        y='PESO',
        size='PESO',
        height=250,
        width=380,
        color="PESO",
        color_continuous_scale=px.colors.sequential.Viridis_r
        )  
      fig_arg_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_arg_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_arg = pio.to_html(fig_arg_ano, include_plotlyjs=False, full_html=False)

      #os
      consulta_os_ano = pd.read_sql(f"""    
        SELECT MANCOD, MANSIT, MANDESC,FORMAT(MANDTABERT,'dd/MM/yyyy')
        FROM MANUTENCAO 
        WHERE MANDTABERT >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)
            AND MANDTABERT <= GETDATE() 
        AND MANSIT IN (2,4)
                    """,connection)

        #KPI'S
      os_total = consulta_os_ano['MANCOD'].count()  


      consulta_britagem_ano = pd.read_sql(f"""
        SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1,

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

        SELECT 3 SEQ, DTRREF DIARIA, DTRDATA1,

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

      ton_britagem = consulta_britagem_ano['PESO'].sum()
      ton_britagem = locale.format_string("%.2f",ton_britagem,grouping=True)
      
      fig_brit_ano = px.pie(
        consulta_britagem_ano,
        values="PESO",
        names='DESTINO',
        height=250,
        width=380,
        color_discrete_sequence=px.colors.sequential.Agsunset        
        )
      fig_brit_ano.update_layout(margin={"r":0,"t":10,"l":0,"b":2})  
      fig_brit_ano.update_layout(xaxis_visible=False, xaxis_showticklabels=False,yaxis_visible=False, yaxis_showticklabels=False)
      plot_brit = pio.to_html(fig_brit_ano, include_plotlyjs=False, full_html=False)

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
      rom_cal_ano = round(consulta_rom_anual['CAL'].sum(),2)  
      vol_brit = rom_calcario_ano + rom_cal_ano
      vol_brit = locale.format_string("%.2f",vol_brit,grouping=True)

      context = {
            'total_calcario': ton_calcario,
            'total_fertilizante': ton_fertilizante,
            'total_cal': ton_cal,
            'total_argamassa':ton_argamassa,
            'os_total':os_total,
            'ton_britagem':ton_britagem,
            'vol_brit':vol_brit,
            'plot_brit':plot_brit,
            'plot_arg':plot_arg,
            'plot_cal':plot_cal,
      }

      return render(request, 'home.html',context)

################################################################## FIM DA HOME #######################################################################################################################

################################################################ INICIO DA VIEW DA PRODUÇÃO ##########################################################################################################

def prod_ini(request):
    
    #CALCARIO
      atual = int(-2)
      consulta_calcario = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 6

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_calcario =(consulta_calcario['PESO'].sum())
      ton_calcario = locale.format_string("%.2f",ton_calcario,grouping=True) 
       
    
      #FERTILIZANTES
      atual = int(-2)         
      consulta_fertilizante = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 8

          ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                     
     """,connection)
      
      #KPI´S
      ton_fertilizante = consulta_fertilizante['PESO'].sum()
      ton_fertilizante = locale.format_string("%.2f",ton_fertilizante,grouping=True)

      #CAL     
      atual = int(-2)    
      consulta_cal = pd.read_sql(f"""
          SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQAPELIDO,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 3

          ORDER BY BPRODATA, BPROCOD, ESTQAPELIDO, ESTQCOD
                                     
     """,connection)
       
      #KPI´S
      ton_cal = consulta_cal['PESO'].sum()
      ton_cal = locale.format_string("%.2f",ton_cal,grouping=True)

      #Argamassa     
      atual = int(-2)
      consulta_argamassa = pd.read_sql(f"""
      SELECT
          BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy')DATAW, ESTQCOD, ESTQAPELIDO,
          IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

          FROM BAIXAPRODUCAO
          JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
          JOIN ESTOQUE ON ESTQCOD = IBPROREF
          LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

          WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{atual},GETDATE())AS DATE)
                                             AND CAST (GETDATE() AS DATE)

          AND BPROEMP = 1
          AND BPROFIL = 0
          AND BPROSIT = 1
          AND IBPROTIPO = 'D'
          AND BPROEP = 1

          ORDER BY BPRODATA, BPROCOD, ESTQCOD,ESTQAPELIDO
                                     
     """,connection)
       
      #KPI´S
      ton_argamassa = consulta_argamassa['PESO'].sum()
      ton_argamassa = locale.format_string("%.2f",ton_argamassa,grouping=True)

      britagem_atual = int(-2) 
      consulta_britagem_atual = pd.read_sql(f"""
        SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1 INICIO, DTRDATA2 FIM,

        'MINA' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

        FROM ITEMDIARIATRANSP IDTR
        JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

        WHERE DTRSIT = 1
        AND DTREMP = 1
        AND DTRFIL = 0
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
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
AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
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
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
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
        AND CAST(DTRDATA1 as date) BETWEEN CAST (DATEADD (DAY,{britagem_atual},GETDATE())AS DATE)
                                                    AND CAST (GETDATE() AS DATE)AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
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

      ton_britagem = consulta_britagem_atual['PESO'].sum()
      ton_britagem = locale.format_string("%.2f",ton_britagem,grouping=True)

      dia = int(-2)
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
      ton_rebritagem = round(consulta_rebri_diaria['TN'].sum(),1)
      ton_rebritagem = locale.format_string("%.2f",ton_rebritagem,grouping=True)
      context = {
           'ton_britagem':ton_britagem,
           'ton_argamassa':ton_argamassa,
           'ton_fertilizante':ton_fertilizante,
           'ton_calcario':ton_calcario,
           'ton_cal':ton_cal,
           'ton_rebritagem':ton_rebritagem,
      }

      return render(request, 'producao.html',context)

################################################################### DETALHA CALCARIO FCMI ###################################################################################################################

def det_calcario(request):
    #FCMI
    fcmi_anterior = int(-2)
    consulta_fcmi = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
    IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

    FROM BAIXAPRODUCAO
    JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
    JOIN ESTOQUE ON ESTQCOD = IBPROREF
    LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

    WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{fcmi_anterior},GETDATE())AS DATE)
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
    ton_fcmi = round(consulta_fcmi['PESO'].sum(),1)
    tot_hs_dia = round(consulta_fcmi['BPROHRPROD'].sum(),1)
    if tot_hs_dia != 0 :
        tn_hora = round(ton_fcmi / tot_hs_dia,1)
    else:
         tn_hora = 0




################################################################### DETALHA CALCARIO FCMII ###################################################################################################################


    #FCMII
    fcmi_mensal = int(-30)
    consulta_fcmi_mensal = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
    IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

    FROM BAIXAPRODUCAO
    JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
    JOIN ESTOQUE ON ESTQCOD = IBPROREF
    LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

    WHERE CAST(BPRODATA as date) BETWEEN CAST (DATEADD (DAY,{fcmi_mensal},GETDATE())AS DATE)
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
    ton2_fcmi = round(consulta_fcmi_mensal['PESO'].sum(),2)
    tot_hs_mes = round(consulta_fcmi_mensal['BPROHRPROD'].sum(),1)
    tn_hora_mes = round(ton2_fcmi / tot_hs_mes,1)
    


    consulta_fcmi_anual = pd.read_sql(f"""
    SELECT
    BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy HH:mm:ss'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,
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
    ton3_fcmi = round(consulta_fcmi_anual['PESO'].sum(),1)
    tot_hs_ano = round(consulta_fcmi_anual['BPROHRPROD'].sum(),1)
    tn_hora_ano = round(ton3_fcmi / tot_hs_ano,1)


    context = {
            'total_fcmi': ton_fcmi,
            'total_hs_dia':tot_hs_dia,
            'ton_hs_dia': tn_hora,
            'total2_fcmi': ton2_fcmi,
            'total_hs_mes': tot_hs_mes,
            'ton_hora_mes': tn_hora_mes,
            'total_hs_ano': tot_hs_ano,
            'ton_hora_ano': tn_hora_ano,
            'total3_fcmi': ton3_fcmi,
            
            
    }



    return render(request, 'detalha_calcario.html',context)