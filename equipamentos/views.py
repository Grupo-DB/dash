from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime, date, timedelta
from .forms import form_data
import locale

def home_eqps(request):
    return render(request,'equipamentos.html')

def get_data(request):    
    if request.method == 'POST':
        form = form_data(request.POST)
        if form.is_valid():
            data_selecionada = form.cleaned_data['data_sel']
            
            #####################-----FCM01 - MG01 ######################################################
            data_prod =data_selecionada.strftime('%Y-%m-%d')
            consulta_fcm1_mg_01_data_prod =pd.read_sql(f"""
            SELECT
            BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,BPRODATA1,BPRODATA2,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST (BPRODATA as date) = '{data_prod}'

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 6
            AND BPROEQP = 110

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                """,connection)
            
            #KPI´S
            hora_prod_mg_01_fcm1 = round(consulta_fcm1_mg_01_data_prod['BPROHRPROD'].sum(),1)
            hora_parado_mg01_fcm1 = round(24 - hora_prod_mg_01_fcm1,1)
            tot_ton_mg_01_fcm1 = round(consulta_fcm1_mg_01_data_prod['PESO'].sum(),1)
            #tot_ton_mg_01_fcm1 = locale.format_string("%.2f",tot_ton_mg_01_fcm1,grouping=True)
           
           ##########################################----------------------FCMI MG-02-----------------------------------################################
           
            
            consulta_fcm1_mg_02_data_prod =pd.read_sql(f"""
            SELECT
            BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,BPRODATA1,BPRODATA2,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST (BPRODATA as date) = '{data_prod}'

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 6
            AND BPROEQP = 111

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                """,connection)
            


            #KPI´S
            
            hora_prod_mg_02_fcm1 = round(consulta_fcm1_mg_02_data_prod['BPROHRPROD'].sum(),1)
            hora_parado_mg02_fcm1 = round(24 - hora_prod_mg_02_fcm1,1)
            tot_ton_mg_02_fcm1 = round(consulta_fcm1_mg_02_data_prod['PESO'].sum(),1)
            tot_ton_fcm1 = round(tot_ton_mg_01_fcm1 + tot_ton_mg_02_fcm1,1)
            tot_produtividade = round(tot_ton_fcm1 / (hora_prod_mg_01_fcm1 + hora_prod_mg_02_fcm1),1)
            #tot_ton_mg_02_fcm1 = locale.format_string("%.2f",tot_ton_mg_02_fcm1,grouping=True)
            #tot_ton_fcm1 = locale.format_string("%.2f",tot_ton_fcm1,grouping=True)
            ########################### ---------------- FCM II -----------------------------------------------------------------------------

            consulta_fcm2_mg_01_data_prod=pd.read_sql(f"""
            SELECT
            BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,BPRODATA1,BPRODATA2,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST (BPRODATA as date) = '{data_prod}'

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 6
            AND BPROEQP = 169

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                """,connection)
            
            #KPI´S
            hora_prod_mg_01_fcm2 = round(consulta_fcm2_mg_01_data_prod['BPROHRPROD'].sum(),1)
            hora_parado_mg_01_fcm2 = round(24 - hora_prod_mg_01_fcm2,1)
            tot_ton_mg_01_fcm2 = round(consulta_fcm2_mg_01_data_prod['PESO'].sum(),1)
            tot_produtividade_fcm2 = round(tot_ton_mg_01_fcm2 / (hora_prod_mg_01_fcm2),1)
            #tot_ton_mg_01_fcm2 = locale.format_string("%.2f",tot_ton_mg_01_fcm2,grouping=True)
            

            ############################### FCM III #############################################################################################

            ######################################################------FCM3 MG01 #######################################################################

            consulta_fcm3_mg_01_data_prod =pd.read_sql(f"""
            SELECT
            BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,BPRODATA1,BPRODATA2,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST (BPRODATA as date) = '{data_prod}'

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 6
            AND BPROEQP = 18

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                """,connection)
            
            #KPI´S
            hora_prod_mg_01_fcm3 = round(consulta_fcm3_mg_01_data_prod['BPROHRPROD'].sum(),1)
            hora_parado_mg_01_fcm3 = round(24 - hora_prod_mg_01_fcm3,1)
            tot_ton_mg_01_fcm3 = round(consulta_fcm3_mg_01_data_prod['PESO'].sum(),1)
            #tot_ton_mg_01_fcm3 = locale.format_string("%.2f",tot_ton_mg_01_fcm3,grouping=True)
            ###################################################------FCM3-mg02---###############################################################

            consulta_fcm3_mg_02_data_prod =pd.read_sql(f"""
            SELECT
            BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,BPRODATA1,BPRODATA2,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST (BPRODATA as date) = '{data_prod}'

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 6
            AND BPROEQP = 19

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                """,connection)
            
            #KPI´S
            hora_prod_mg_02_fcm3 = round(consulta_fcm3_mg_02_data_prod['BPROHRPROD'].sum(),1)
            hora_parado_mg_02_fcm3 = round(24 - hora_prod_mg_02_fcm3,1)
            tot_ton_mg_02_fcm3 = round(consulta_fcm3_mg_02_data_prod['PESO'].sum(),1)
            #tot_ton_mg_02_fcm3 = locale.format_string("%.2f",tot_ton_mg_02_fcm3,grouping=True)

            ###########################################---FCM3_MG03--------#########################################################################

            consulta_fcm3_mg_03_data_prod =pd.read_sql(f"""
            SELECT
            BPROCOD, FORMAT(BPRODATA,'dd/MM/yyyy'), ESTQCOD, ESTQNOMECOMP,BPROEQP,BPROHRPROD,BPROHROPER,BPROFPROQUANT,BPROFPRO,BPRODATA1,BPRODATA2,
            IBPROQUANT, ((ESTQPESO*IBPROQUANT) /1000) PESO

            FROM BAIXAPRODUCAO
            JOIN ITEMBAIXAPRODUCAO ON BPROCOD = IBPROBPRO
            JOIN ESTOQUE ON ESTQCOD = IBPROREF
            LEFT OUTER JOIN EQUIPAMENTO ON EQPCOD = BPROEQP

            WHERE CAST (BPRODATA as date) = '{data_prod}'

            AND BPROEMP = 1
            AND BPROFIL = 0
            AND BPROSIT = 1
            AND IBPROTIPO = 'D'
            AND BPROEP = 6
            AND BPROEQP = 20

            ORDER BY BPRODATA, BPROCOD, ESTQNOMECOMP, ESTQCOD
                                """,connection)
            
           
            
            #KPI´S
            hora_prod_mg_03_fcm3 = round(consulta_fcm3_mg_03_data_prod['BPROHRPROD'].sum(),1)
            hora_parado_mg_03_fcm3 = round(24 - hora_prod_mg_03_fcm3,1)
            tot_ton_mg_03_fcm3 = round(consulta_fcm3_mg_03_data_prod['PESO'].sum(),1)
            #tot_ton_mg_03_fcm3 = locale.format_string("%.2f",tot_ton_mg_03_fcm3,grouping=True)
            #TOTAIS-FCM3
            tot_ton_fcm3 = round(tot_ton_mg_01_fcm3 + tot_ton_mg_02_fcm3 + tot_ton_mg_03_fcm3,1)
            tot_produtividade_fcm3 = round(tot_ton_fcm3 / (hora_prod_mg_01_fcm3 + hora_prod_mg_02_fcm3 + hora_prod_mg_03_fcm3) ,1)
            
            #TOTAIS-GERAL
            tot_ton_geral = round(tot_ton_fcm1 + tot_ton_mg_01_fcm2 + tot_ton_fcm3,1)
            tot_hora_prod = round((hora_prod_mg_01_fcm1 + hora_prod_mg_02_fcm1) + (hora_prod_mg_01_fcm2) + (hora_prod_mg_01_fcm3 + hora_prod_mg_02_fcm3 + hora_prod_mg_03_fcm3) ,1)
            tot_produtividade_geral = round(tot_ton_geral / tot_hora_prod,1)
            tot_ton_geral = locale.format_string("%.2f",tot_ton_geral,grouping=True)


            ###################################--------Carregamento-------------Geral__######################################################################

            consulta_carregamento_geral = pd.read_sql(f"""
            SELECT 
            NFDATAORDEM DATANF,NFNUM,NFPESOTOT,
            ESTQCOD, ESTQNOME,GALMCOD
            FROM NOTAFISCAL

            JOIN ITEMNOTAFISCAL ON INFNFCOD = NFCOD
            JOIN ESTOQUE ON ESTQCOD = INFESTQ
            JOIN ESPECIE ON ESPCOD = ESTQESP
            JOIN GRUPOALMOXARIFADO ON GALMCOD = 1587
            LEFT OUTER JOIN GRUPOPRODUTO ON GRPCOD = ESTQGRP
            JOIN NATUREZAOPERACAO ON NOPCOD = INFNOP

            WHERE NFSIT = 1
            AND CAST (NFDATA as date) = '{data_prod}'

            AND GALMPRODVENDA = 'S'
            AND (SUBSTRING(NOPFLAGNF, 2, 1) = 'S' ) --Flag Circulação de Merc. 'S' 
            AND NFEMP = 1
            AND NFFIL = 0


            GROUP BY NFDATAORDEM, ESTQCOD, ESTQNOME,GALMCOD,NFNUM,NFPESOTOT
            ORDER BY NFDATAORDEM, ESTQCOD
                                     """,connection)

            #KPI'S

            tot_carregamento = round(consulta_carregamento_geral['NFPESOTOT'].sum(),1)
            tot_carregamento = locale.format_string("%.2f",tot_carregamento,grouping=True)

            context = {
                'data_selecionada':data_selecionada,
                'tot_ton_mg_01_fcm1':tot_ton_mg_01_fcm1,
                'hora_prod_mg_01_fcm1':hora_prod_mg_01_fcm1,
                'hora_parado_mg01_fcm1':hora_parado_mg01_fcm1,
                'tot_ton_mg_02_fcm1':tot_ton_mg_02_fcm1,
                'hora_prod_mg_02_fcm1':hora_prod_mg_02_fcm1,
                'hora_parado_mg02_fcm1':hora_parado_mg02_fcm1,
                'tot_ton_fcm1':tot_ton_fcm1,
                'tot_produtividade':tot_produtividade,
                'hora_parado_mg_01_fcm2':hora_parado_mg_01_fcm2,
                'hora_prod_mg_01_fcm2': hora_prod_mg_01_fcm2,
                'tot_ton_mg_01_fcm2' :tot_ton_mg_01_fcm2,
                'tot_produtividade_fcm2':tot_produtividade_fcm2,
                'hora_prod_mg_01_fcm3': hora_prod_mg_01_fcm3,
                'hora_parado_mg_01_fcm3': hora_parado_mg_01_fcm3,
                'tot_ton_mg_01_fcm3':tot_ton_mg_01_fcm3,
                'hora_prod_mg_02_fcm3': hora_prod_mg_02_fcm3,
                'hora_parado_mg_02_fcm3':hora_parado_mg_02_fcm3,
                'tot_ton_mg_02_fcm3':tot_ton_mg_02_fcm3,
                'hora_prod_mg_03_fcm3':hora_prod_mg_03_fcm3,
                'hora_parado_mg_03_fcm3':hora_parado_mg_03_fcm3,
                'tot_ton_mg_03_fcm3':tot_ton_mg_03_fcm3,
                'tot_ton_fcm3':tot_ton_fcm3,
                'tot_produtividade_fcm3':tot_produtividade_fcm3,
                'produtividade_geral':tot_produtividade_geral,
                'tot_hora_prod':tot_hora_prod,
                'tot_ton_geral': tot_ton_geral,
                'tot_carregamento':tot_carregamento,
            }

            return render(request, 'equipamentos.html',context,) 
    return render(request, 'equipamentos.html', {'form': form})
            
    