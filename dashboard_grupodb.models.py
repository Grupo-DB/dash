# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abatcontareceber(models.Model):
    abcrcod = models.IntegerField(db_column='ABCRCOD', primary_key=True)  # Field name made lowercase.
    abcrcr = models.ForeignKey('Contareceber', models.DO_NOTHING, db_column='ABCRCR')  # Field name made lowercase.
    abcrnfemp = models.ForeignKey('Notafiscal', models.DO_NOTHING, db_column='ABCRNFEMP', to_field='NFSNF', blank=True, null=True)  # Field name made lowercase.
    abcrnffil = models.ForeignKey('Notafiscal', models.DO_NOTHING, db_column='ABCRNFFIL', to_field='NFSNF', related_name='abatcontareceber_abcrnffil_set', blank=True, null=True)  # Field name made lowercase.
    abcrnfsnf = models.ForeignKey('Notafiscal', models.DO_NOTHING, db_column='ABCRNFSNF', to_field='NFSNF', related_name='abatcontareceber_abcrnfsnf_set', blank=True, null=True)  # Field name made lowercase.
    abcrnfnum = models.ForeignKey('Notafiscal', models.DO_NOTHING, db_column='ABCRNFNUM', to_field='NFSNF', related_name='abatcontareceber_abcrnfnum_set', blank=True, null=True)  # Field name made lowercase.
    abcrvalor = models.FloatField(db_column='ABCRVALOR', blank=True, null=True)  # Field name made lowercase.
    abcrabatnfemp = models.IntegerField(db_column='ABCRABATNFEMP', blank=True, null=True)  # Field name made lowercase.
    abcrabatnffil = models.IntegerField(db_column='ABCRABATNFFIL', blank=True, null=True)  # Field name made lowercase.
    abcrabatnfsnf = models.IntegerField(db_column='ABCRABATNFSNF', blank=True, null=True)  # Field name made lowercase.
    abcrabatnfnum = models.IntegerField(db_column='ABCRABATNFNUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ABATCONTARECEBER'


class Acessobase(models.Model):
    acbcod = models.IntegerField(db_column='ACBCOD', primary_key=True)  # Field name made lowercase.
    acbnome = models.CharField(db_column='ACBNOME', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acbequip = models.CharField(db_column='ACBEQUIP', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acbhost = models.CharField(db_column='ACBHOST', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acbporta = models.IntegerField(db_column='ACBPORTA', blank=True, null=True)  # Field name made lowercase.
    acbnumero = models.IntegerField(db_column='ACBNUMERO', blank=True, null=True)  # Field name made lowercase.
    acbbloq = models.CharField(db_column='ACBBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acbinventsai = models.CharField(db_column='ACBINVENTSAI', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACESSOBASE'


class Acessoevento(models.Model):
    acevcod = models.IntegerField(db_column='ACEVCOD', primary_key=True)  # Field name made lowercase.
    acevdata = models.DateTimeField(db_column='ACEVDATA', blank=True, null=True)  # Field name made lowercase.
    acevtipo = models.CharField(db_column='ACEVTIPO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acevacevref = models.ForeignKey('self', models.DO_NOTHING, db_column='ACEVACEVREF', blank=True, null=True)  # Field name made lowercase.
    acevacl = models.ForeignKey('Acessoliberacao', models.DO_NOTHING, db_column='ACEVACL', blank=True, null=True)  # Field name made lowercase.
    acevcodigo = models.CharField(db_column='ACEVCODIGO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACESSOEVENTO'


class Acessoliberacao(models.Model):
    aclcod = models.IntegerField(db_column='ACLCOD', primary_key=True)  # Field name made lowercase.
    aclacb = models.ForeignKey(Acessobase, models.DO_NOTHING, db_column='ACLACB')  # Field name made lowercase.
    aclfun = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ACLFUN', blank=True, null=True)  # Field name made lowercase.
    aclmot = models.ForeignKey('Motorista', models.DO_NOTHING, db_column='ACLMOT', blank=True, null=True)  # Field name made lowercase.
    aclcli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='ACLCLI', blank=True, null=True)  # Field name made lowercase.
    aclfor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='ACLFOR', blank=True, null=True)  # Field name made lowercase.
    aclrep = models.ForeignKey('Representante', models.DO_NOTHING, db_column='ACLREP', blank=True, null=True)  # Field name made lowercase.
    aclnf = models.IntegerField(db_column='ACLNF', blank=True, null=True)  # Field name made lowercase.
    aclcodigo = models.CharField(db_column='ACLCODIGO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acldata = models.DateTimeField(db_column='ACLDATA', blank=True, null=True)  # Field name made lowercase.
    acldata1 = models.DateTimeField(db_column='ACLDATA1', blank=True, null=True)  # Field name made lowercase.
    acldata2 = models.DateTimeField(db_column='ACLDATA2', blank=True, null=True)  # Field name made lowercase.
    aclquantlib = models.IntegerField(db_column='ACLQUANTLIB', blank=True, null=True)  # Field name made lowercase.
    aclcop = models.ForeignKey('Contratopessoal', models.DO_NOTHING, db_column='ACLCOP', blank=True, null=True)  # Field name made lowercase.
    acldescricao = models.CharField(db_column='ACLDESCRICAO', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acldataproc = models.DateTimeField(db_column='ACLDATAPROC', blank=True, null=True)  # Field name made lowercase.
    acldatabaixa = models.DateTimeField(db_column='ACLDATABAIXA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACESSOLIBERACAO'


class Acessoprogpedido(models.Model):
    appedcod = models.IntegerField(db_column='APPEDCOD', primary_key=True)  # Field name made lowercase.
    appeddesc = models.CharField(db_column='APPEDDESC', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACESSOPROGPEDIDO'


class Acessorio(models.Model):
    acecod = models.IntegerField(db_column='ACECOD', primary_key=True)  # Field name made lowercase.
    aceestq = models.ForeignKey('Estoque', models.DO_NOTHING, db_column='ACEESTQ', blank=True, null=True)  # Field name made lowercase.
    acetipo = models.IntegerField(db_column='ACETIPO', blank=True, null=True)  # Field name made lowercase.
    aceemp = models.IntegerField(db_column='ACEEMP', blank=True, null=True)  # Field name made lowercase.
    acefil = models.IntegerField(db_column='ACEFIL', blank=True, null=True)  # Field name made lowercase.
    acesit = models.IntegerField(db_column='ACESIT', blank=True, null=True)  # Field name made lowercase.
    acevidautil = models.IntegerField(db_column='ACEVIDAUTIL', blank=True, null=True)  # Field name made lowercase.
    acevidautilcanc = models.IntegerField(db_column='ACEVIDAUTILCANC', blank=True, null=True)  # Field name made lowercase.
    acebest = models.ForeignKey('Baixaestoque', models.DO_NOTHING, db_column='ACEBEST', blank=True, null=True)  # Field name made lowercase.
    acemace = models.ForeignKey('Motivoacessorio', models.DO_NOTHING, db_column='ACEMACE', blank=True, null=True)  # Field name made lowercase.
    acedatamot = models.DateTimeField(db_column='ACEDATAMOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACESSORIO'


class Acompcobranca(models.Model):
    acobcod = models.IntegerField(db_column='ACOBCOD', primary_key=True)  # Field name made lowercase.
    acobfun = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ACOBFUN')  # Field name made lowercase.
    acobdatainicio = models.DateTimeField(db_column='ACOBDATAINICIO', blank=True, null=True)  # Field name made lowercase.
    acobdatafinal = models.DateTimeField(db_column='ACOBDATAFINAL', blank=True, null=True)  # Field name made lowercase.
    acobproxagenda = models.DateTimeField(db_column='ACOBPROXAGENDA', blank=True, null=True)  # Field name made lowercase.
    acobcli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='ACOBCLI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACOMPCOBRANCA'


class Acopdiariatransp(models.Model):
    acdtrcod = models.IntegerField(db_column='ACDTRCOD', primary_key=True)  # Field name made lowercase.
    acdtrdtr = models.ForeignKey('Diariatransp', models.DO_NOTHING, db_column='ACDTRDTR')  # Field name made lowercase.
    acdtreqp = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='ACDTREQP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACOPDIARIATRANSP'


class Acopdispositivomovel(models.Model):
    admcod = models.IntegerField(db_column='ADMCOD', primary_key=True)  # Field name made lowercase.
    admdm = models.ForeignKey('Dispositivomovel', models.DO_NOTHING, db_column='ADMDM', blank=True, null=True)  # Field name made lowercase.
    admeqp = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='ADMEQP', blank=True, null=True)  # Field name made lowercase.
    admdata = models.DateTimeField(db_column='ADMDATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACOPDISPOSITIVOMOVEL'


class Acopequipamento(models.Model):
    aeqpcod = models.IntegerField(db_column='AEQPCOD', primary_key=True)  # Field name made lowercase.
    aeqpeqp = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='AEQPEQP')  # Field name made lowercase.
    aeqpeqpacop = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='AEQPEQPACOP', related_name='acopequipamento_aeqpeqpacop_set', blank=True, null=True)  # Field name made lowercase.
    aeqpdata = models.DateTimeField(db_column='AEQPDATA', blank=True, null=True)  # Field name made lowercase.
    aeqpchv = models.IntegerField(db_column='AEQPCHV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACOPEQUIPAMENTO'


class Adiantamentocliente(models.Model):
    adccod = models.IntegerField(db_column='ADCCOD', primary_key=True)  # Field name made lowercase.
    adcreg = models.ForeignKey('Registro', models.DO_NOTHING, db_column='ADCREG')  # Field name made lowercase.
    adcdata = models.DateTimeField(db_column='ADCDATA')  # Field name made lowercase.
    adccli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='ADCCLI')  # Field name made lowercase.
    adctotal = models.FloatField(db_column='ADCTOTAL', blank=True, null=True)  # Field name made lowercase.
    adctotalliq = models.FloatField(db_column='ADCTOTALLIQ', blank=True, null=True)  # Field name made lowercase.
    adctotalcanc = models.FloatField(db_column='ADCTOTALCANC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADIANTAMENTOCLIENTE'


class Adiantamentofornecedor(models.Model):
    adfcod = models.IntegerField(db_column='ADFCOD', primary_key=True)  # Field name made lowercase.
    adfreg = models.ForeignKey('Registro', models.DO_NOTHING, db_column='ADFREG')  # Field name made lowercase.
    adfdata = models.DateTimeField(db_column='ADFDATA')  # Field name made lowercase.
    adffor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='ADFFOR')  # Field name made lowercase.
    adftotal = models.FloatField(db_column='ADFTOTAL', blank=True, null=True)  # Field name made lowercase.
    adftotalliq = models.FloatField(db_column='ADFTOTALLIQ', blank=True, null=True)  # Field name made lowercase.
    adftotalcanc = models.FloatField(db_column='ADFTOTALCANC', blank=True, null=True)  # Field name made lowercase.
    adfdatacanc = models.DateTimeField(db_column='ADFDATACANC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADIANTAMENTOFORNECEDOR'


class Agendacliente(models.Model):
    aclicod = models.IntegerField(db_column='ACLICOD', primary_key=True)  # Field name made lowercase.
    aclidata = models.DateTimeField(db_column='ACLIDATA', blank=True, null=True)  # Field name made lowercase.
    aclifun = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ACLIFUN')  # Field name made lowercase.
    aclicot = models.IntegerField(db_column='ACLICOT', blank=True, null=True)  # Field name made lowercase.
    acliassunto = models.CharField(db_column='ACLIASSUNTO', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acliobs = models.BinaryField(db_column='ACLIOBS', blank=True, null=True)  # Field name made lowercase.
    aclistatus = models.IntegerField(db_column='ACLISTATUS', blank=True, null=True)  # Field name made lowercase.
    aclidataref = models.DateTimeField(db_column='ACLIDATAREF', blank=True, null=True)  # Field name made lowercase.
    acliscot = models.IntegerField(db_column='ACLISCOT', blank=True, null=True)  # Field name made lowercase.
    aclitipo = models.IntegerField(db_column='ACLITIPO', blank=True, null=True)  # Field name made lowercase.
    acliemp = models.IntegerField(db_column='ACLIEMP', blank=True, null=True)  # Field name made lowercase.
    aclifil = models.IntegerField(db_column='ACLIFIL', blank=True, null=True)  # Field name made lowercase.
    aclicli = models.IntegerField(db_column='ACLICLI', blank=True, null=True)  # Field name made lowercase.
    aclirep = models.IntegerField(db_column='ACLIREP')  # Field name made lowercase.
    aclicoc = models.IntegerField(db_column='ACLICOC', blank=True, null=True)  # Field name made lowercase.
    aclidatabase = models.DateTimeField(db_column='ACLIDATABASE', blank=True, null=True)  # Field name made lowercase.
    acliscotconc = models.IntegerField(db_column='ACLISCOTCONC', blank=True, null=True)  # Field name made lowercase.
    acliped = models.IntegerField(db_column='ACLIPED', blank=True, null=True)  # Field name made lowercase.
    acliecli = models.ForeignKey('Enderecocliente', models.DO_NOTHING, db_column='ACLIECLI', blank=True, null=True)  # Field name made lowercase.
    aclidataprevprox = models.DateTimeField(db_column='ACLIDATAPREVPROX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGENDACLIENTE'


class Agendatiporel(models.Model):
    atrtr = models.IntegerField(db_column='ATRTR', primary_key=True)  # Field name made lowercase.
    atrperiod = models.IntegerField(db_column='ATRPERIOD', blank=True, null=True)  # Field name made lowercase.
    atrdiaenvio = models.IntegerField(db_column='ATRDIAENVIO', blank=True, null=True)  # Field name made lowercase.
    atrhoraenvio = models.DateTimeField(db_column='ATRHORAENVIO', blank=True, null=True)  # Field name made lowercase.
    atrdepperativo = models.CharField(db_column='ATRDEPPERATIVO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atremp = models.IntegerField(db_column='ATREMP', blank=True, null=True)  # Field name made lowercase.
    atrfil = models.IntegerField(db_column='ATRFIL', blank=True, null=True)  # Field name made lowercase.
    atrultenvio = models.DateTimeField(db_column='ATRULTENVIO', blank=True, null=True)  # Field name made lowercase.
    atrfunorig = models.IntegerField(db_column='ATRFUNORIG', blank=True, null=True)  # Field name made lowercase.
    atremaildest = models.CharField(db_column='ATREMAILDEST', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atrconsulta = models.BinaryField(db_column='ATRCONSULTA', blank=True, null=True)  # Field name made lowercase.
    atremailpdf = models.CharField(db_column='ATREMAILPDF', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atrlocalarquivo = models.CharField(db_column='ATRLOCALARQUIVO', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atrarquivounico = models.CharField(db_column='ATRARQUIVOUNICO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atremailcsv = models.CharField(db_column='ATREMAILCSV', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGENDATIPOREL'


class Agendatiporelhor(models.Model):
    atrhtr = models.IntegerField(db_column='ATRHTR', blank=True, null=True)  # Field name made lowercase.
    atrhhora = models.DateTimeField(db_column='ATRHHORA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGENDATIPORELHOR'


class Ajustefretepgnf(models.Model):
    afnfnf = models.IntegerField(db_column='AFNFNF', primary_key=True)  # Field name made lowercase.
    afnfdata = models.DateTimeField(db_column='AFNFDATA', blank=True, null=True)  # Field name made lowercase.
    afnffun = models.IntegerField(db_column='AFNFFUN', blank=True, null=True)  # Field name made lowercase.
    afnfnfcanc = models.IntegerField(db_column='AFNFNFCANC', blank=True, null=True)  # Field name made lowercase.
    afnfvalororig = models.FloatField(db_column='AFNFVALORORIG', blank=True, null=True)  # Field name made lowercase.
    afnfmotivo = models.CharField(db_column='AFNFMOTIVO', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AJUSTEFRETEPGNF'


class Ajustetabelafrete(models.Model):
    atfcod = models.IntegerField(db_column='ATFCOD', primary_key=True)  # Field name made lowercase.
    atftfcod = models.ForeignKey('Tabelafrete', models.DO_NOTHING, db_column='ATFTFCOD')  # Field name made lowercase.
    atftveiccod = models.IntegerField(db_column='ATFTVEICCOD')  # Field name made lowercase.
    atfdata = models.DateTimeField(db_column='ATFDATA')  # Field name made lowercase.
    atfpercent = models.FloatField(db_column='ATFPERCENT', blank=True, null=True)  # Field name made lowercase.
    atfobs = models.BinaryField(db_column='ATFOBS', blank=True, null=True)  # Field name made lowercase.
    atffreunit = models.FloatField(db_column='ATFFREUNIT', blank=True, null=True)  # Field name made lowercase.
    atffreunitmin = models.FloatField(db_column='ATFFREUNITMIN', blank=True, null=True)  # Field name made lowercase.
    atffreunitmax = models.FloatField(db_column='ATFFREUNITMAX', blank=True, null=True)  # Field name made lowercase.
    atfrepbase = models.FloatField(db_column='ATFREPBASE', blank=True, null=True)  # Field name made lowercase.
    atfrepmax = models.FloatField(db_column='ATFREPMAX', blank=True, null=True)  # Field name made lowercase.
    atfvalpedman = models.FloatField(db_column='ATFVALPEDMAN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AJUSTETABELAFRETE'


class Alertafuncionario(models.Model):
    alfdataalerta = models.DateTimeField(db_column='ALFDATAALERTA', blank=True, null=True)  # Field name made lowercase.
    alfdataenvio = models.DateTimeField(db_column='ALFDATAENVIO', blank=True, null=True)  # Field name made lowercase.
    alftipo = models.IntegerField(db_column='ALFTIPO', blank=True, null=True)  # Field name made lowercase.
    alffunrem = models.IntegerField(db_column='ALFFUNREM', blank=True, null=True)  # Field name made lowercase.
    alffun = models.IntegerField(db_column='ALFFUN', blank=True, null=True)  # Field name made lowercase.
    alffunlista = models.CharField(db_column='ALFFUNLISTA', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alfassunto = models.CharField(db_column='ALFASSUNTO', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alfmensagem = models.TextField(db_column='ALFMENSAGEM', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    alfultenvio = models.DateTimeField(db_column='ALFULTENVIO', blank=True, null=True)  # Field name made lowercase.
    alfultenvioevt = models.CharField(db_column='ALFULTENVIOEVT', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALERTAFUNCIONARIO'


class Alimdiariaprod(models.Model):
    adprcod = models.IntegerField(db_column='ADPRCOD', primary_key=True)  # Field name made lowercase.
    adprdpr = models.ForeignKey('Diariaprod', models.DO_NOTHING, db_column='ADPRDPR')  # Field name made lowercase.
    adprloc = models.IntegerField(db_column='ADPRLOC')  # Field name made lowercase.
    adpreqp = models.IntegerField(db_column='ADPREQP')  # Field name made lowercase.
    adprceq = models.IntegerField(db_column='ADPRCEQ')  # Field name made lowercase.
    adprpesotot = models.FloatField(db_column='ADPRPESOTOT', blank=True, null=True)  # Field name made lowercase.
    adprdprdest = models.IntegerField(db_column='ADPRDPRDEST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALIMDIARIAPROD'


class Alimdiariatransp(models.Model):
    adtrcod = models.IntegerField(db_column='ADTRCOD', primary_key=True)  # Field name made lowercase.
    adtridtr = models.ForeignKey('Itemdiariatransp', models.DO_NOTHING, db_column='ADTRIDTR')  # Field name made lowercase.
    adtrloc = models.IntegerField(db_column='ADTRLOC')  # Field name made lowercase.
    adtreqp = models.IntegerField(db_column='ADTREQP')  # Field name made lowercase.
    adtrceq = models.IntegerField(db_column='ADTRCEQ')  # Field name made lowercase.
    adtrpesotot = models.FloatField(db_column='ADTRPESOTOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALIMDIARIATRANSP'


class Alunotreinamento(models.Model):
    atrncod = models.IntegerField(db_column='ATRNCOD', primary_key=True)  # Field name made lowercase.
    atrntrn = models.ForeignKey('Treinamento', models.DO_NOTHING, db_column='ATRNTRN')  # Field name made lowercase.
    atrnfor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='ATRNFOR')  # Field name made lowercase.
    atrnnota = models.FloatField(db_column='ATRNNOTA', blank=True, null=True)  # Field name made lowercase.
    atrnaprov = models.CharField(db_column='ATRNAPROV', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atrnobs = models.BinaryField(db_column='ATRNOBS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALUNOTREINAMENTO'


class Amortizacaocusto(models.Model):
    accod = models.IntegerField(db_column='ACCOD', primary_key=True)  # Field name made lowercase.
    actipo = models.IntegerField(db_column='ACTIPO')  # Field name made lowercase.
    acref = models.IntegerField(db_column='ACREF')  # Field name made lowercase.
    acdata = models.DateTimeField(db_column='ACDATA')  # Field name made lowercase.
    accc = models.ForeignKey('Centrocusto', models.DO_NOTHING, db_column='ACCC')  # Field name made lowercase.
    acpeqp = models.IntegerField(db_column='ACPEQP', blank=True, null=True)  # Field name made lowercase.
    acparnum = models.IntegerField(db_column='ACPARNUM', blank=True, null=True)  # Field name made lowercase.
    acpartot = models.IntegerField(db_column='ACPARTOT', blank=True, null=True)  # Field name made lowercase.
    acvalor = models.FloatField(db_column='ACVALOR', blank=True, null=True)  # Field name made lowercase.
    aceqp = models.IntegerField(db_column='ACEQP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMORTIZACAOCUSTO'


class Amostraparanalise(models.Model):
    aprancod = models.IntegerField(db_column='APRANCOD', primary_key=True)  # Field name made lowercase.
    apranpran = models.IntegerField(db_column='APRANPRAN')  # Field name made lowercase.
    apranam = models.IntegerField(db_column='APRANAM', blank=True, null=True)  # Field name made lowercase.
    apranvalor = models.FloatField(db_column='APRANVALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMOSTRAPARANALISE'


class Analise(models.Model):
    ancod = models.IntegerField(db_column='ANCOD', primary_key=True)  # Field name made lowercase.
    anpan = models.IntegerField(db_column='ANPAN', blank=True, null=True)  # Field name made lowercase.
    andatacol = models.DateTimeField(db_column='ANDATACOL', blank=True, null=True)  # Field name made lowercase.
    andataan = models.DateTimeField(db_column='ANDATAAN', blank=True, null=True)  # Field name made lowercase.
    annat = models.IntegerField(db_column='ANNAT', blank=True, null=True)  # Field name made lowercase.
    anorig = models.IntegerField(db_column='ANORIG', blank=True, null=True)  # Field name made lowercase.
    anlpro = models.IntegerField(db_column='ANLPRO', blank=True, null=True)  # Field name made lowercase.
    anlcol = models.IntegerField(db_column='ANLCOL', blank=True, null=True)  # Field name made lowercase.
    anlot = models.IntegerField(db_column='ANLOT', blank=True, null=True)  # Field name made lowercase.
    anilot = models.IntegerField(db_column='ANILOT', blank=True, null=True)  # Field name made lowercase.
    anfunrespcol = models.IntegerField(db_column='ANFUNRESPCOL', blank=True, null=True)  # Field name made lowercase.
    anfunrespan = models.IntegerField(db_column='ANFUNRESPAN', blank=True, null=True)  # Field name made lowercase.
    annumam = models.IntegerField(db_column='ANNUMAM', blank=True, null=True)  # Field name made lowercase.
    anident = models.CharField(db_column='ANIDENT', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ananorig = models.IntegerField(db_column='ANANORIG', blank=True, null=True)  # Field name made lowercase.
    anres = models.CharField(db_column='ANRES', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ansit = models.IntegerField(db_column='ANSIT', blank=True, null=True)  # Field name made lowercase.
    anobs = models.BinaryField(db_column='ANOBS', blank=True, null=True)  # Field name made lowercase.
    aninfe = models.IntegerField(db_column='ANINFE', blank=True, null=True)  # Field name made lowercase.
    andpr = models.IntegerField(db_column='ANDPR', blank=True, null=True)  # Field name made lowercase.
    anemp = models.IntegerField(db_column='ANEMP', blank=True, null=True)  # Field name made lowercase.
    anfil = models.IntegerField(db_column='ANFIL', blank=True, null=True)  # Field name made lowercase.
    anbpro = models.IntegerField(db_column='ANBPRO', blank=True, null=True)  # Field name made lowercase.
    anident2 = models.CharField(db_column='ANIDENT2', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    anativada = models.CharField(db_column='ANATIVADA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aneel = models.IntegerField(db_column='ANEEL', blank=True, null=True)  # Field name made lowercase.
    anestq = models.IntegerField(db_column='ANESTQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANALISE'


class Analisepedido(models.Model):
    apedtipo = models.IntegerField(db_column='APEDTIPO', primary_key=True)  # Field name made lowercase. The composite primary key (APEDTIPO, APEDNUM, APEDREF) found, that is not supported. The first column is selected.
    apednum = models.IntegerField(db_column='APEDNUM')  # Field name made lowercase.
    apedref = models.CharField(db_column='APEDREF', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    apedresp = models.CharField(db_column='APEDRESP', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apedobs = models.BinaryField(db_column='APEDOBS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANALISEPEDIDO'
        unique_together = (('apedtipo', 'apednum', 'apedref'),)


class Apiario(models.Model):
    apicod = models.IntegerField(db_column='APICOD', primary_key=True)  # Field name made lowercase.
    apifor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='APIFOR')  # Field name made lowercase.
    apinome = models.CharField(db_column='APINOME', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apicid = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='APICID')  # Field name made lowercase.
    apiquantcolm = models.IntegerField(db_column='APIQUANTCOLM', blank=True, null=True)  # Field name made lowercase.
    apidatacad = models.DateTimeField(db_column='APIDATACAD', blank=True, null=True)  # Field name made lowercase.
    apidatabaixa = models.DateTimeField(db_column='APIDATABAIXA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APIARIO'


class Apliccandidato(models.Model):
    acancod = models.IntegerField(db_column='ACANCOD', primary_key=True)  # Field name made lowercase.
    acancan = models.IntegerField(db_column='ACANCAN')  # Field name made lowercase.
    acansetor = models.IntegerField(db_column='ACANSETOR', blank=True, null=True)  # Field name made lowercase.
    acancargo = models.IntegerField(db_column='ACANCARGO', blank=True, null=True)  # Field name made lowercase.
    acanfuncao = models.IntegerField(db_column='ACANFUNCAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APLICCANDIDATO'


class Aplicdispositivomovel(models.Model):
    apdmcod = models.IntegerField(db_column='APDMCOD', primary_key=True)  # Field name made lowercase.
    apdmteqp = models.ForeignKey('Tipoequipamento', models.DO_NOTHING, db_column='APDMTEQP', blank=True, null=True)  # Field name made lowercase.
    apdmeqp = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='APDMEQP', blank=True, null=True)  # Field name made lowercase.
    apdmdidm = models.ForeignKey('Definfodispositivomovel', models.DO_NOTHING, db_column='APDMDIDM', blank=True, null=True)  # Field name made lowercase.
    apdmevd = models.ForeignKey('Eventodiaria', models.DO_NOTHING, db_column='APDMEVD', blank=True, null=True)  # Field name made lowercase.
    apdmevdbase = models.ForeignKey('Eventodiaria', models.DO_NOTHING, db_column='APDMEVDBASE', related_name='aplicdispositivomovel_apdmevdbase_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APLICDISPOSITIVOMOVEL'


class Aprovacao(models.Model):
    apcod = models.IntegerField(db_column='APCOD', primary_key=True)  # Field name made lowercase.
    aprap = models.ForeignKey('Regraaprovacao', models.DO_NOTHING, db_column='APRAP')  # Field name made lowercase.
    appcom = models.ForeignKey('Pendenciacompra', models.DO_NOTHING, db_column='APPCOM', blank=True, null=True)  # Field name made lowercase.
    appco = models.ForeignKey('Processocompra', models.DO_NOTHING, db_column='APPCO', blank=True, null=True)  # Field name made lowercase.
    apdatapend = models.DateTimeField(db_column='APDATAPEND', blank=True, null=True)  # Field name made lowercase.
    apvalor = models.FloatField(db_column='APVALOR', blank=True, null=True)  # Field name made lowercase.
    apaprov = models.CharField(db_column='APAPROV', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptipolimite = models.CharField(db_column='APTIPOLIMITE', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apreg = models.ForeignKey('Registro', models.DO_NOTHING, db_column='APREG', blank=True, null=True)  # Field name made lowercase.
    aprpa = models.ForeignKey('Rpa', models.DO_NOTHING, db_column='APRPA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APROVACAO'


class Aprovador(models.Model):
    aprcod = models.IntegerField(db_column='APRCOD', primary_key=True)  # Field name made lowercase.
    aprap = models.ForeignKey(Aprovacao, models.DO_NOTHING, db_column='APRAP')  # Field name made lowercase.
    aprfun = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='APRFUN')  # Field name made lowercase.
    aprdataaprov = models.DateTimeField(db_column='APRDATAAPROV', blank=True, null=True)  # Field name made lowercase.
    apraprov = models.CharField(db_column='APRAPROV', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aprobs = models.CharField(db_column='APROBS', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APROVADOR'


class Aprovpedido(models.Model):
    appcod = models.IntegerField(db_column='APPCOD', primary_key=True)  # Field name made lowercase.
    appped = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='APPPED')  # Field name made lowercase.
    appfun = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='APPFUN')  # Field name made lowercase.
    appgrupo = models.CharField(db_column='APPGRUPO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    appdata = models.DateTimeField(db_column='APPDATA', blank=True, null=True)  # Field name made lowercase.
    appaprov = models.CharField(db_column='APPAPROV', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APROVPEDIDO'


class Apuracaoajuste(models.Model):
    aacod = models.IntegerField(db_column='AACOD', primary_key=True)  # Field name made lowercase.
    aaai = models.ForeignKey('Apuracaoimposto', models.DO_NOTHING, db_column='AAAI')  # Field name made lowercase.
    aacodigo = models.CharField(db_column='AACODIGO', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aaindorigem = models.IntegerField(db_column='AAINDORIGEM', blank=True, null=True)  # Field name made lowercase.
    aadesc = models.CharField(db_column='AADESC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aadesccomp = models.CharField(db_column='AADESCCOMP', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aavalor = models.FloatField(db_column='AAVALOR', blank=True, null=True)  # Field name made lowercase.
    aanumdoc = models.CharField(db_column='AANUMDOC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aaauto = models.CharField(db_column='AAAUTO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aacredcont = models.CharField(db_column='AACREDCONT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aaccdatabase = models.DateTimeField(db_column='AACCDATABASE', blank=True, null=True)  # Field name made lowercase.
    aaccdatalimite = models.DateTimeField(db_column='AACCDATALIMITE', blank=True, null=True)  # Field name made lowercase.
    aacctipocred = models.IntegerField(db_column='AACCTIPOCRED', blank=True, null=True)  # Field name made lowercase.
    aaccperccred = models.FloatField(db_column='AACCPERCCRED', blank=True, null=True)  # Field name made lowercase.
    aaccsaldoant = models.FloatField(db_column='AACCSALDOANT', blank=True, null=True)  # Field name made lowercase.
    aacccredaprop = models.FloatField(db_column='AACCCREDAPROP', blank=True, null=True)  # Field name made lowercase.
    aacccredtransf = models.FloatField(db_column='AACCCREDTRANSF', blank=True, null=True)  # Field name made lowercase.
    aaccsaldo = models.FloatField(db_column='AACCSALDO', blank=True, null=True)  # Field name made lowercase.
    aacccodutilcred = models.CharField(db_column='AACCCODUTILCRED', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aaccnumdoc = models.CharField(db_column='AACCNUMDOC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aacccodigoaprop = models.CharField(db_column='AACCCODIGOAPROP', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOAJUSTE'


class Apuracaoajustepiscofins(models.Model):
    aapccod = models.IntegerField(db_column='AAPCCOD', primary_key=True)  # Field name made lowercase.
    aapcai = models.ForeignKey('Apuracaoimposto', models.DO_NOTHING, db_column='AAPCAI')  # Field name made lowercase.
    aapctipo = models.CharField(db_column='AAPCTIPO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aapcref = models.IntegerField(db_column='AAPCREF', blank=True, null=True)  # Field name made lowercase.
    aapcindaj = models.IntegerField(db_column='AAPCINDAJ', blank=True, null=True)  # Field name made lowercase.
    aapccodigo = models.IntegerField(db_column='AAPCCODIGO', blank=True, null=True)  # Field name made lowercase.
    aapcvalor = models.FloatField(db_column='AAPCVALOR', blank=True, null=True)  # Field name made lowercase.
    aapcnumdoc = models.CharField(db_column='AAPCNUMDOC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aapcdescricao = models.CharField(db_column='AAPCDESCRICAO', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aapcdataref = models.DateTimeField(db_column='AAPCDATAREF', blank=True, null=True)  # Field name made lowercase.
    aapcreqcomp = models.CharField(db_column='AAPCREQCOMP', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aapccst = models.IntegerField(db_column='AAPCCST', blank=True, null=True)  # Field name made lowercase.
    aapcbase = models.FloatField(db_column='AAPCBASE', blank=True, null=True)  # Field name made lowercase.
    aapcaliq = models.FloatField(db_column='AAPCALIQ', blank=True, null=True)  # Field name made lowercase.
    aapcdataoper = models.DateTimeField(db_column='AAPCDATAOPER', blank=True, null=True)  # Field name made lowercase.
    aapcconta = models.CharField(db_column='AAPCCONTA', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aapcauto = models.CharField(db_column='AAPCAUTO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aapcaplic = models.IntegerField(db_column='AAPCAPLIC', blank=True, null=True)  # Field name made lowercase.
    aapcfil = models.IntegerField(db_column='AAPCFIL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOAJUSTEPISCOFINS'


class Apuracaobasecreditopiscofins(models.Model):
    abcpccod = models.IntegerField(db_column='ABCPCCOD', primary_key=True)  # Field name made lowercase.
    abcpcacpc = models.ForeignKey('Apuracaocreditopiscofins', models.DO_NOTHING, db_column='ABCPCACPC')  # Field name made lowercase.
    abcpcnatbc = models.IntegerField(db_column='ABCPCNATBC', blank=True, null=True)  # Field name made lowercase.
    abcpccst = models.IntegerField(db_column='ABCPCCST', blank=True, null=True)  # Field name made lowercase.
    abcpcbasecum = models.FloatField(db_column='ABCPCBASECUM', blank=True, null=True)  # Field name made lowercase.
    abcpcbasenc = models.FloatField(db_column='ABCPCBASENC', blank=True, null=True)  # Field name made lowercase.
    abcpcbase = models.FloatField(db_column='ABCPCBASE', blank=True, null=True)  # Field name made lowercase.
    abcpcbasequanttot = models.FloatField(db_column='ABCPCBASEQUANTTOT', blank=True, null=True)  # Field name made lowercase.
    abcpcbasequant = models.FloatField(db_column='ABCPCBASEQUANT', blank=True, null=True)  # Field name made lowercase.
    abcpcdesc = models.CharField(db_column='ABCPCDESC', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOBASECREDITOPISCOFINS'


class Apuracaocreditopiscofins(models.Model):
    acpccod = models.IntegerField(db_column='ACPCCOD', primary_key=True)  # Field name made lowercase.
    acpcai = models.ForeignKey('Apuracaoimposto', models.DO_NOTHING, db_column='ACPCAI')  # Field name made lowercase.
    acpctipocred = models.IntegerField(db_column='ACPCTIPOCRED', blank=True, null=True)  # Field name made lowercase.
    acpcorigem = models.IntegerField(db_column='ACPCORIGEM', blank=True, null=True)  # Field name made lowercase.
    acpcbase = models.FloatField(db_column='ACPCBASE', blank=True, null=True)  # Field name made lowercase.
    acpcaliq = models.FloatField(db_column='ACPCALIQ', blank=True, null=True)  # Field name made lowercase.
    acpcbasequant = models.FloatField(db_column='ACPCBASEQUANT', blank=True, null=True)  # Field name made lowercase.
    acpcaliqquant = models.FloatField(db_column='ACPCALIQQUANT', blank=True, null=True)  # Field name made lowercase.
    acpcvalor = models.FloatField(db_column='ACPCVALOR', blank=True, null=True)  # Field name made lowercase.
    acpcvalorajac = models.FloatField(db_column='ACPCVALORAJAC', blank=True, null=True)  # Field name made lowercase.
    acpcvalorajred = models.FloatField(db_column='ACPCVALORAJRED', blank=True, null=True)  # Field name made lowercase.
    acpcvalordif = models.FloatField(db_column='ACPCVALORDIF', blank=True, null=True)  # Field name made lowercase.
    acpcvalordisp = models.FloatField(db_column='ACPCVALORDISP', blank=True, null=True)  # Field name made lowercase.
    acpcutilizacao = models.IntegerField(db_column='ACPCUTILIZACAO', blank=True, null=True)  # Field name made lowercase.
    acpcvalordesc = models.FloatField(db_column='ACPCVALORDESC', blank=True, null=True)  # Field name made lowercase.
    acpcsaldofut = models.FloatField(db_column='ACPCSALDOFUT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOCREDITOPISCOFINS'


class Apuracaodebitopiscofins(models.Model):
    adpccod = models.IntegerField(db_column='ADPCCOD', primary_key=True)  # Field name made lowercase.
    adpcai = models.ForeignKey('Apuracaoimposto', models.DO_NOTHING, db_column='ADPCAI')  # Field name made lowercase.
    adpccodcont = models.IntegerField(db_column='ADPCCODCONT', blank=True, null=True)  # Field name made lowercase.
    adpcrecbruta = models.FloatField(db_column='ADPCRECBRUTA', blank=True, null=True)  # Field name made lowercase.
    adpcbase = models.FloatField(db_column='ADPCBASE', blank=True, null=True)  # Field name made lowercase.
    adpcaliq = models.FloatField(db_column='ADPCALIQ', blank=True, null=True)  # Field name made lowercase.
    adpcbasequant = models.FloatField(db_column='ADPCBASEQUANT', blank=True, null=True)  # Field name made lowercase.
    adpcaliqquant = models.FloatField(db_column='ADPCALIQQUANT', blank=True, null=True)  # Field name made lowercase.
    adpcvalor = models.FloatField(db_column='ADPCVALOR', blank=True, null=True)  # Field name made lowercase.
    adpcvalorajac = models.FloatField(db_column='ADPCVALORAJAC', blank=True, null=True)  # Field name made lowercase.
    adpcvalorajred = models.FloatField(db_column='ADPCVALORAJRED', blank=True, null=True)  # Field name made lowercase.
    adpcvalordif = models.FloatField(db_column='ADPCVALORDIF', blank=True, null=True)  # Field name made lowercase.
    adpcvalordifant = models.FloatField(db_column='ADPCVALORDIFANT', blank=True, null=True)  # Field name made lowercase.
    adpcvalortot = models.FloatField(db_column='ADPCVALORTOT', blank=True, null=True)  # Field name made lowercase.
    adpcbaseajac = models.FloatField(db_column='ADPCBASEAJAC', blank=True, null=True)  # Field name made lowercase.
    adpcbaseajred = models.FloatField(db_column='ADPCBASEAJRED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAODEBITOPISCOFINS'


class Apuracaodocajuste(models.Model):
    adacod = models.IntegerField(db_column='ADACOD', primary_key=True)  # Field name made lowercase.
    adaaa = models.ForeignKey(Apuracaoajuste, models.DO_NOTHING, db_column='ADAAA')  # Field name made lowercase.
    adacli = models.IntegerField(db_column='ADACLI', blank=True, null=True)  # Field name made lowercase.
    adafor = models.IntegerField(db_column='ADAFOR', blank=True, null=True)  # Field name made lowercase.
    adamodelo = models.IntegerField(db_column='ADAMODELO', blank=True, null=True)  # Field name made lowercase.
    adaser = models.CharField(db_column='ADASER', max_length=4, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adasub = models.CharField(db_column='ADASUB', max_length=3, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adanumdoc = models.IntegerField(db_column='ADANUMDOC', blank=True, null=True)  # Field name made lowercase.
    adadatadoc = models.DateTimeField(db_column='ADADATADOC', blank=True, null=True)  # Field name made lowercase.
    adaestq = models.IntegerField(db_column='ADAESTQ', blank=True, null=True)  # Field name made lowercase.
    adaserv = models.IntegerField(db_column='ADASERV', blank=True, null=True)  # Field name made lowercase.
    adavalor = models.FloatField(db_column='ADAVALOR', blank=True, null=True)  # Field name made lowercase.
    adachavedoc = models.CharField(db_column='ADACHAVEDOC', max_length=44, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAODOCAJUSTE'


class Apuracaoicms(models.Model):
    apimesano = models.IntegerField(db_column='APIMESANO', primary_key=True)  # Field name made lowercase. The composite primary key (APIMESANO, APIEMP, APIFIL, APICHAVE) found, that is not supported. The first column is selected.
    apichave = models.IntegerField(db_column='APICHAVE')  # Field name made lowercase.
    apidef = models.CharField(db_column='APIDEF', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apiref = models.IntegerField(db_column='APIREF', blank=True, null=True)  # Field name made lowercase.
    apidesc = models.CharField(db_column='APIDESC', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apidata = models.DateTimeField(db_column='APIDATA', blank=True, null=True)  # Field name made lowercase.
    apivalor = models.FloatField(db_column='APIVALOR', blank=True, null=True)  # Field name made lowercase.
    apibase = models.FloatField(db_column='APIBASE', blank=True, null=True)  # Field name made lowercase.
    apiimposto = models.FloatField(db_column='APIIMPOSTO', blank=True, null=True)  # Field name made lowercase.
    apiisntrib = models.FloatField(db_column='APIISNTRIB', blank=True, null=True)  # Field name made lowercase.
    apioutras = models.FloatField(db_column='APIOUTRAS', blank=True, null=True)  # Field name made lowercase.
    apiemp = models.IntegerField(db_column='APIEMP')  # Field name made lowercase.
    apifil = models.IntegerField(db_column='APIFIL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOICMS'
        unique_together = (('apimesano', 'apiemp', 'apifil', 'apichave'),)


class Apuracaoimposto(models.Model):
    aicod = models.IntegerField(db_column='AICOD', primary_key=True)  # Field name made lowercase.
    aiemp = models.IntegerField(db_column='AIEMP')  # Field name made lowercase.
    aifil = models.IntegerField(db_column='AIFIL')  # Field name made lowercase.
    aiest = models.IntegerField(db_column='AIEST')  # Field name made lowercase.
    aidata1 = models.DateTimeField(db_column='AIDATA1', blank=True, null=True)  # Field name made lowercase.
    aidata2 = models.DateTimeField(db_column='AIDATA2', blank=True, null=True)  # Field name made lowercase.
    aiimposto = models.CharField(db_column='AIIMPOSTO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aidataproc = models.DateTimeField(db_column='AIDATAPROC', blank=True, null=True)  # Field name made lowercase.
    aifunproc = models.IntegerField(db_column='AIFUNPROC', blank=True, null=True)  # Field name made lowercase.
    aipendente = models.CharField(db_column='AIPENDENTE', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aiicmsestcred = models.FloatField(db_column='AIICMSESTCRED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOIMPOSTO'


class Apuracaoinfoad(models.Model):
    aadcod = models.IntegerField(db_column='AADCOD', primary_key=True)  # Field name made lowercase.
    aadai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='AADAI')  # Field name made lowercase.
    aadcodigo = models.CharField(db_column='AADCODIGO', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aaddesc = models.CharField(db_column='AADDESC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aaddesccomp = models.CharField(db_column='AADDESCCOMP', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aadvalor = models.FloatField(db_column='AADVALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOINFOAD'


class Apuracaoinfoajuste(models.Model):
    aiacod = models.IntegerField(db_column='AIACOD', primary_key=True)  # Field name made lowercase.
    aiaaa = models.ForeignKey(Apuracaoajuste, models.DO_NOTHING, db_column='AIAAA')  # Field name made lowercase.
    aianumda = models.CharField(db_column='AIANUMDA', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aianumproc = models.CharField(db_column='AIANUMPROC', max_length=15, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aiaindproc = models.IntegerField(db_column='AIAINDPROC', blank=True, null=True)  # Field name made lowercase.
    aiaproc = models.CharField(db_column='AIAPROC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aiatxtcompl = models.CharField(db_column='AIATXTCOMPL', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOINFOAJUSTE'


class Apuracaoipi(models.Model):
    aipimesano = models.IntegerField(db_column='AIPIMESANO', primary_key=True)  # Field name made lowercase. The composite primary key (AIPIMESANO, AIPIEMP, AIPIFIL, AIPICHAVE) found, that is not supported. The first column is selected.
    aipichave = models.IntegerField(db_column='AIPICHAVE')  # Field name made lowercase.
    aipidef = models.CharField(db_column='AIPIDEF', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aipiref = models.IntegerField(db_column='AIPIREF', blank=True, null=True)  # Field name made lowercase.
    aipidesc = models.CharField(db_column='AIPIDESC', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aipidata = models.DateTimeField(db_column='AIPIDATA', blank=True, null=True)  # Field name made lowercase.
    aipivalor = models.FloatField(db_column='AIPIVALOR', blank=True, null=True)  # Field name made lowercase.
    aipibase = models.FloatField(db_column='AIPIBASE', blank=True, null=True)  # Field name made lowercase.
    aipiimposto = models.FloatField(db_column='AIPIIMPOSTO', blank=True, null=True)  # Field name made lowercase.
    aipiisntrib = models.FloatField(db_column='AIPIISNTRIB', blank=True, null=True)  # Field name made lowercase.
    aipioutras = models.FloatField(db_column='AIPIOUTRAS', blank=True, null=True)  # Field name made lowercase.
    aipiemp = models.IntegerField(db_column='AIPIEMP')  # Field name made lowercase.
    aipifil = models.IntegerField(db_column='AIPIFIL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOIPI'
        unique_together = (('aipimesano', 'aipiemp', 'aipifil', 'aipichave'),)


class Apuracaoobrig(models.Model):
    aocod = models.IntegerField(db_column='AOCOD', primary_key=True)  # Field name made lowercase.
    aoai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='AOAI')  # Field name made lowercase.
    aocodor = models.CharField(db_column='AOCODOR', max_length=3, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aodesc = models.CharField(db_column='AODESC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aovalor = models.FloatField(db_column='AOVALOR', blank=True, null=True)  # Field name made lowercase.
    aovenc = models.DateTimeField(db_column='AOVENC', blank=True, null=True)  # Field name made lowercase.
    aocodrec = models.CharField(db_column='AOCODREC', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aonumproc = models.CharField(db_column='AONUMPROC', max_length=15, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aoindproc = models.IntegerField(db_column='AOINDPROC', blank=True, null=True)  # Field name made lowercase.
    aoproc = models.CharField(db_column='AOPROC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aotxtcompl = models.CharField(db_column='AOTXTCOMPL', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aodataref = models.DateTimeField(db_column='AODATAREF', blank=True, null=True)  # Field name made lowercase.
    aoauto = models.CharField(db_column='AOAUTO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOOBRIG'


class Apuracaoobrigpiscofins(models.Model):
    aopccod = models.IntegerField(db_column='AOPCCOD', primary_key=True)  # Field name made lowercase.
    aopcai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='AOPCAI')  # Field name made lowercase.
    aopctipo = models.IntegerField(db_column='AOPCTIPO', blank=True, null=True)  # Field name made lowercase.
    aopccodrec = models.CharField(db_column='AOPCCODREC', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aopcvalor = models.FloatField(db_column='AOPCVALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOOBRIGPISCOFINS'


class Apuracaooperext(models.Model):
    aoecod = models.IntegerField(db_column='AOECOD', primary_key=True)  # Field name made lowercase.
    aoeai = models.IntegerField(db_column='AOEAI')  # Field name made lowercase.
    aoepai = models.ForeignKey('Pais', models.DO_NOTHING, db_column='AOEPAI')  # Field name made lowercase.
    aoetipo = models.CharField(db_column='AOETIPO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aoeforma = models.IntegerField(db_column='AOEFORMA', blank=True, null=True)  # Field name made lowercase.
    aoenatoper = models.IntegerField(db_column='AOENATOPER', blank=True, null=True)  # Field name made lowercase.
    aoevalor = models.FloatField(db_column='AOEVALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOOPEREXT'


class Apuracaopartce(models.Model):
    apcecod = models.IntegerField(db_column='APCECOD', primary_key=True)  # Field name made lowercase.
    apceai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='APCEAI')  # Field name made lowercase.
    apcecnpj = models.CharField(db_column='APCECNPJ', max_length=18, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcecnpjlider = models.CharField(db_column='APCECNPJLIDER', max_length=18, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcecond = models.IntegerField(db_column='APCECOND', blank=True, null=True)  # Field name made lowercase.
    apcerecper = models.FloatField(db_column='APCERECPER', blank=True, null=True)  # Field name made lowercase.
    apcerectot = models.FloatField(db_column='APCERECTOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOPARTCE'


class Apuracaopartmep(models.Model):
    apmcod = models.IntegerField(db_column='APMCOD', primary_key=True)  # Field name made lowercase.
    apmai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='APMAI')  # Field name made lowercase.
    apmsoc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='APMSOC')  # Field name made lowercase.
    apmdtevento = models.DateTimeField(db_column='APMDTEVENTO', blank=True, null=True)  # Field name made lowercase.
    apmindrelac = models.IntegerField(db_column='APMINDRELAC', blank=True, null=True)  # Field name made lowercase.
    apmvalor = models.FloatField(db_column='APMVALOR', blank=True, null=True)  # Field name made lowercase.
    apmvalormoe = models.FloatField(db_column='APMVALORMOE', blank=True, null=True)  # Field name made lowercase.
    apmreseqpat = models.FloatField(db_column='APMRESEQPAT', blank=True, null=True)  # Field name made lowercase.
    apmdataaquis = models.DateTimeField(db_column='APMDATAAQUIS', blank=True, null=True)  # Field name made lowercase.
    apmindproccar = models.CharField(db_column='APMINDPROCCAR', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apmnumproccar = models.CharField(db_column='APMNUMPROCCAR', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apmforcart = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='APMFORCART', blank=True, null=True)  # Field name made lowercase.
    apmindprocrfb = models.CharField(db_column='APMINDPROCRFB', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apmnumprocrfb = models.CharField(db_column='APMNUMPROCRFB', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOPARTMEP'


class Apuracaopiscofins(models.Model):
    apccod = models.IntegerField(db_column='APCCOD', primary_key=True)  # Field name made lowercase.
    apcemp = models.IntegerField(db_column='APCEMP')  # Field name made lowercase.
    apcfil = models.IntegerField(db_column='APCFIL')  # Field name made lowercase.
    apcppc = models.ForeignKey('Padraopiscofins', models.DO_NOTHING, db_column='APCPPC')  # Field name made lowercase.
    apclanc = models.ForeignKey('Lancamento', models.DO_NOTHING, db_column='APCLANC')  # Field name made lowercase.
    apcdata = models.DateTimeField(db_column='APCDATA', blank=True, null=True)  # Field name made lowercase.
    apcindoper = models.IntegerField(db_column='APCINDOPER', blank=True, null=True)  # Field name made lowercase.
    apccli = models.IntegerField(db_column='APCCLI', blank=True, null=True)  # Field name made lowercase.
    apcfor = models.IntegerField(db_column='APCFOR', blank=True, null=True)  # Field name made lowercase.
    apcvalor = models.FloatField(db_column='APCVALOR', blank=True, null=True)  # Field name made lowercase.
    apcpiscst = models.IntegerField(db_column='APCPISCST', blank=True, null=True)  # Field name made lowercase.
    apcpisbase = models.FloatField(db_column='APCPISBASE', blank=True, null=True)  # Field name made lowercase.
    apcpisaliq = models.FloatField(db_column='APCPISALIQ', blank=True, null=True)  # Field name made lowercase.
    apcpisvalor = models.FloatField(db_column='APCPISVALOR', blank=True, null=True)  # Field name made lowercase.
    apccofinscst = models.IntegerField(db_column='APCCOFINSCST', blank=True, null=True)  # Field name made lowercase.
    apccofinsbase = models.FloatField(db_column='APCCOFINSBASE', blank=True, null=True)  # Field name made lowercase.
    apccofinsaliq = models.FloatField(db_column='APCCOFINSALIQ', blank=True, null=True)  # Field name made lowercase.
    apccofinsvalor = models.FloatField(db_column='APCCOFINSVALOR', blank=True, null=True)  # Field name made lowercase.
    apcnatbccred = models.IntegerField(db_column='APCNATBCCRED', blank=True, null=True)  # Field name made lowercase.
    apcindorigcred = models.IntegerField(db_column='APCINDORIGCRED', blank=True, null=True)  # Field name made lowercase.
    apcdesc = models.CharField(db_column='APCDESC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcnatrec = models.IntegerField(db_column='APCNATREC', blank=True, null=True)  # Field name made lowercase.
    apcconta = models.CharField(db_column='APCCONTA', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOPISCOFINS'


class Apuracaoreceitacnae(models.Model):
    arccod = models.IntegerField(db_column='ARCCOD', primary_key=True)  # Field name made lowercase.
    arcai = models.IntegerField(db_column='ARCAI')  # Field name made lowercase.
    arccnpj = models.CharField(db_column='ARCCNPJ', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    arccnae = models.IntegerField(db_column='ARCCNAE', blank=True, null=True)  # Field name made lowercase.
    arcvalor = models.FloatField(db_column='ARCVALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAORECEITACNAE'


class Apuracaoremdir(models.Model):
    ardcod = models.IntegerField(db_column='ARDCOD', primary_key=True)  # Field name made lowercase.
    ardai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='ARDAI')  # Field name made lowercase.
    ardsoc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='ARDSOC')  # Field name made lowercase.
    ardremtrab = models.FloatField(db_column='ARDREMTRAB', blank=True, null=True)  # Field name made lowercase.
    ardlucdiv = models.FloatField(db_column='ARDLUCDIV', blank=True, null=True)  # Field name made lowercase.
    ardjurcap = models.FloatField(db_column='ARDJURCAP', blank=True, null=True)  # Field name made lowercase.
    arddemrend = models.FloatField(db_column='ARDDEMREND', blank=True, null=True)  # Field name made lowercase.
    ardirret = models.FloatField(db_column='ARDIRRET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOREMDIR'


class Apuracaosaldoirpjcssl(models.Model):
    asiccod = models.IntegerField(db_column='ASICCOD', primary_key=True)  # Field name made lowercase.
    asicai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='ASICAI')  # Field name made lowercase.
    asicconta = models.CharField(db_column='ASICCONTA', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    asicdesc = models.CharField(db_column='ASICDESC', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    asicdata = models.DateTimeField(db_column='ASICDATA', blank=True, null=True)  # Field name made lowercase.
    asicdatainic = models.DateTimeField(db_column='ASICDATAINIC', blank=True, null=True)  # Field name made lowercase.
    asicdatalim = models.DateTimeField(db_column='ASICDATALIM', blank=True, null=True)  # Field name made lowercase.
    asiccontaorig = models.CharField(db_column='ASICCONTAORIG', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    asiccontadest = models.CharField(db_column='ASICCONTADEST', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    asictributo = models.CharField(db_column='ASICTRIBUTO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    asictiporev = models.IntegerField(db_column='ASICTIPOREV', blank=True, null=True)  # Field name made lowercase.
    asicpercrev = models.FloatField(db_column='ASICPERCREV', blank=True, null=True)  # Field name made lowercase.
    asicvalororig = models.FloatField(db_column='ASICVALORORIG', blank=True, null=True)  # Field name made lowercase.
    asicsaldoinic = models.FloatField(db_column='ASICSALDOINIC', blank=True, null=True)  # Field name made lowercase.
    asicvalorrev = models.FloatField(db_column='ASICVALORREV', blank=True, null=True)  # Field name made lowercase.
    asiccnpjsitesp = models.CharField(db_column='ASICCNPJSITESP', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    asicindicador = models.IntegerField(db_column='ASICINDICADOR', blank=True, null=True)  # Field name made lowercase.
    asicvaloradic = models.FloatField(db_column='ASICVALORADIC', blank=True, null=True)  # Field name made lowercase.
    asicpadraoparteb = models.CharField(db_column='ASICPADRAOPARTEB', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOSALDOIRPJCSSL'


class Apuracaosaldopiscofins(models.Model):
    aspccod = models.IntegerField(db_column='ASPCCOD', primary_key=True)  # Field name made lowercase.
    aspcai = models.ForeignKey(Apuracaoimposto, models.DO_NOTHING, db_column='ASPCAI')  # Field name made lowercase.
    aspcdataref = models.DateTimeField(db_column='ASPCDATAREF', blank=True, null=True)  # Field name made lowercase.
    aspcorigem = models.IntegerField(db_column='ASPCORIGEM', blank=True, null=True)  # Field name made lowercase.
    aspccnpjorigem = models.CharField(db_column='ASPCCNPJORIGEM', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aspctipocred = models.IntegerField(db_column='ASPCTIPOCRED', blank=True, null=True)  # Field name made lowercase.
    aspccredtot = models.FloatField(db_column='ASPCCREDTOT', blank=True, null=True)  # Field name made lowercase.
    aspccredext = models.FloatField(db_column='ASPCCREDEXT', blank=True, null=True)  # Field name made lowercase.
    aspccredapu = models.FloatField(db_column='ASPCCREDAPU', blank=True, null=True)  # Field name made lowercase.
    aspcdescant = models.FloatField(db_column='ASPCDESCANT', blank=True, null=True)  # Field name made lowercase.
    aspcressant = models.FloatField(db_column='ASPCRESSANT', blank=True, null=True)  # Field name made lowercase.
    aspccompant = models.FloatField(db_column='ASPCCOMPANT', blank=True, null=True)  # Field name made lowercase.
    aspcsaldo = models.FloatField(db_column='ASPCSALDO', blank=True, null=True)  # Field name made lowercase.
    aspcdesc = models.FloatField(db_column='ASPCDESC', blank=True, null=True)  # Field name made lowercase.
    aspcress = models.FloatField(db_column='ASPCRESS', blank=True, null=True)  # Field name made lowercase.
    aspccomp = models.FloatField(db_column='ASPCCOMP', blank=True, null=True)  # Field name made lowercase.
    aspctrans = models.FloatField(db_column='ASPCTRANS', blank=True, null=True)  # Field name made lowercase.
    aspcoutras = models.FloatField(db_column='ASPCOUTRAS', blank=True, null=True)  # Field name made lowercase.
    aspcsaldofut = models.FloatField(db_column='ASPCSALDOFUT', blank=True, null=True)  # Field name made lowercase.
    aspctipo = models.IntegerField(db_column='ASPCTIPO', blank=True, null=True)  # Field name made lowercase.
    aspcauto = models.CharField(db_column='ASPCAUTO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOSALDOPISCOFINS'


class Apuracaotiporegistro(models.Model):
    aptrcod = models.IntegerField(db_column='APTRCOD', primary_key=True)  # Field name made lowercase.
    aptremp = models.IntegerField(db_column='APTREMP', blank=True, null=True)  # Field name made lowercase.
    aptrfil = models.IntegerField(db_column='APTRFIL', blank=True, null=True)  # Field name made lowercase.
    aptrimposto = models.CharField(db_column='APTRIMPOSTO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptropcao = models.CharField(db_column='APTROPCAO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptrcampo = models.CharField(db_column='APTRCAMPO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptrtreg = models.IntegerField(db_column='APTRTREG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOTIPOREGISTRO'


class Apuracaototal(models.Model):
    atai = models.OneToOneField(Apuracaoimposto, models.DO_NOTHING, db_column='ATAI', primary_key=True)  # Field name made lowercase. The composite primary key (ATAI, ATCAMPO) found, that is not supported. The first column is selected.
    atcampo = models.CharField(db_column='ATCAMPO', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    atseq = models.IntegerField(db_column='ATSEQ', blank=True, null=True)  # Field name made lowercase.
    atvalor = models.FloatField(db_column='ATVALOR', blank=True, null=True)  # Field name made lowercase.
    attipo = models.IntegerField(db_column='ATTIPO', blank=True, null=True)  # Field name made lowercase.
    atdesc = models.CharField(db_column='ATDESC', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APURACAOTOTAL'
        unique_together = (('atai', 'atcampo'),)


class Argnotafiscal(models.Model):
    anfnfcod = models.IntegerField(db_column='ANFNFCOD', primary_key=True)  # Field name made lowercase.
    anfeqp = models.IntegerField(db_column='ANFEQP', blank=True, null=True)  # Field name made lowercase.
    anflacre = models.IntegerField(db_column='ANFLACRE', blank=True, null=True)  # Field name made lowercase.
    anfrecarga = models.CharField(db_column='ANFRECARGA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    anflacre2 = models.IntegerField(db_column='ANFLACRE2', blank=True, null=True)  # Field name made lowercase.
    anflacre3 = models.IntegerField(db_column='ANFLACRE3', blank=True, null=True)  # Field name made lowercase.
    anflacre4 = models.IntegerField(db_column='ANFLACRE4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARGNOTAFISCAL'


class Arquivorpa(models.Model):
    arpacod = models.IntegerField(db_column='ARPACOD', primary_key=True)  # Field name made lowercase.
    arpafor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='ARPAFOR')  # Field name made lowercase.
    arpaforref = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='ARPAFORREF', related_name='arquivorpa_arpaforref_set')  # Field name made lowercase.
    arpadata = models.DateTimeField(db_column='ARPADATA', blank=True, null=True)  # Field name made lowercase.
    arpainssbase = models.FloatField(db_column='ARPAINSSBASE', blank=True, null=True)  # Field name made lowercase.
    arpainssvalor = models.FloatField(db_column='ARPAINSSVALOR', blank=True, null=True)  # Field name made lowercase.
    arpacodcat = models.IntegerField(db_column='ARPACODCAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARQUIVORPA'


class Atributooperacao(models.Model):
    atrocod = models.IntegerField(db_column='ATROCOD', primary_key=True)  # Field name made lowercase.
    atrota = models.ForeignKey('Tipoatributo', models.DO_NOTHING, db_column='ATROTA')  # Field name made lowercase.
    atroop = models.ForeignKey('Operacaorec', models.DO_NOTHING, db_column='ATROOP')  # Field name made lowercase.
    atrodado = models.IntegerField(db_column='ATRODADO', blank=True, null=True)  # Field name made lowercase.
    atrodadoval = models.FloatField(db_column='ATRODADOVAL', blank=True, null=True)  # Field name made lowercase.
    atrodadodata = models.DateTimeField(db_column='ATRODADODATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATRIBUTOOPERACAO'


class Atributooperacaotexto(models.Model):
    atrocod = models.OneToOneField(Atributooperacao, models.DO_NOTHING, db_column='ATROCOD', primary_key=True)  # Field name made lowercase.
    atrodadotexto = models.CharField(db_column='ATRODADOTEXTO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATRIBUTOOPERACAOTEXTO'


class Aulatreinamento(models.Model):
    autrncod = models.IntegerField(db_column='AUTRNCOD', primary_key=True)  # Field name made lowercase.
    autrntrn = models.ForeignKey('Treinamento', models.DO_NOTHING, db_column='AUTRNTRN')  # Field name made lowercase.
    autrnforinstrutor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='AUTRNFORINSTRUTOR')  # Field name made lowercase.
    autrndatainicial = models.DateTimeField(db_column='AUTRNDATAINICIAL', blank=True, null=True)  # Field name made lowercase.
    autrndatafinal = models.DateTimeField(db_column='AUTRNDATAFINAL', blank=True, null=True)  # Field name made lowercase.
    autrnlocal = models.CharField(db_column='AUTRNLOCAL', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autrnobs = models.BinaryField(db_column='AUTRNOBS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AULATREINAMENTO'


class Autcontareceber(models.Model):
    acrcr = models.OneToOneField('Contareceber', models.DO_NOTHING, db_column='ACRCR', primary_key=True)  # Field name made lowercase.
    acrfun = models.IntegerField(db_column='ACRFUN')  # Field name made lowercase.
    acrdata = models.DateTimeField(db_column='ACRDATA', blank=True, null=True)  # Field name made lowercase.
    acrjuros = models.FloatField(db_column='ACRJUROS', blank=True, null=True)  # Field name made lowercase.
    acrmulta = models.FloatField(db_column='ACRMULTA', blank=True, null=True)  # Field name made lowercase.
    acrdesc = models.FloatField(db_column='ACRDESC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTCONTARECEBER'


class Autenticacaointegracao(models.Model):
    auticod = models.IntegerField(db_column='AUTICOD', primary_key=True)  # Field name made lowercase.
    autiident = models.CharField(db_column='AUTIIDENT', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autiref = models.CharField(db_column='AUTIREF', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autitipotoken = models.CharField(db_column='AUTITIPOTOKEN', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autidataaut = models.DateTimeField(db_column='AUTIDATAAUT', blank=True, null=True)  # Field name made lowercase.
    autitempoexpiracao = models.DateTimeField(db_column='AUTITEMPOEXPIRACAO', blank=True, null=True)  # Field name made lowercase.
    autitoken = models.BinaryField(db_column='AUTITOKEN', blank=True, null=True)  # Field name made lowercase.
    autitokenat = models.BinaryField(db_column='AUTITOKENAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTENTICACAOINTEGRACAO'


class Auttransportador(models.Model):
    atrancod = models.IntegerField(db_column='ATRANCOD', primary_key=True)  # Field name made lowercase.
    atranemp = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='ATRANEMP', blank=True, null=True)  # Field name made lowercase.
    atranfil = models.ForeignKey('Filial', models.DO_NOTHING, db_column='ATRANFIL', blank=True, null=True)  # Field name made lowercase.
    atrantranref = models.ForeignKey('Transportador', models.DO_NOTHING, db_column='ATRANTRANREF', blank=True, null=True)  # Field name made lowercase.
    atrancli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='ATRANCLI', blank=True, null=True)  # Field name made lowercase.
    atranecli = models.ForeignKey('Enderecocliente', models.DO_NOTHING, db_column='ATRANECLI', blank=True, null=True)  # Field name made lowercase.
    atranped = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='ATRANPED', blank=True, null=True)  # Field name made lowercase.
    atrantran = models.ForeignKey('Transportador', models.DO_NOTHING, db_column='ATRANTRAN', related_name='auttransportador_atrantran_set', blank=True, null=True)  # Field name made lowercase.
    atranplaca = models.CharField(db_column='ATRANPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atranmot = models.ForeignKey('Motorista', models.DO_NOTHING, db_column='ATRANMOT', blank=True, null=True)  # Field name made lowercase.
    atrandata1 = models.DateTimeField(db_column='ATRANDATA1', blank=True, null=True)  # Field name made lowercase.
    atrandata2 = models.DateTimeField(db_column='ATRANDATA2', blank=True, null=True)  # Field name made lowercase.
    atrantranlocal = models.CharField(db_column='ATRANTRANLOCAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atrantipo = models.IntegerField(db_column='ATRANTIPO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTTRANSPORTADOR'


class Backupdado(models.Model):
    bkdcod = models.IntegerField(db_column='BKDCOD', blank=True, null=True)  # Field name made lowercase.
    bkddata = models.DateTimeField(db_column='BKDDATA', blank=True, null=True)  # Field name made lowercase.
    bkdfun = models.IntegerField(db_column='BKDFUN', blank=True, null=True)  # Field name made lowercase.
    bkdtabela = models.CharField(db_column='BKDTABELA', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bkdcondicao = models.CharField(db_column='BKDCONDICAO', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bkdcampo = models.CharField(db_column='BKDCAMPO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bkddadointeger = models.IntegerField(db_column='BKDDADOINTEGER', blank=True, null=True)  # Field name made lowercase.
    bkddadosmallint = models.IntegerField(db_column='BKDDADOSMALLINT', blank=True, null=True)  # Field name made lowercase.
    bkddadovarchar = models.CharField(db_column='BKDDADOVARCHAR', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bkddadodouble = models.FloatField(db_column='BKDDADODOUBLE', blank=True, null=True)  # Field name made lowercase.
    bkddadotimestamp = models.DateTimeField(db_column='BKDDADOTIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    bkddadoblob = models.BinaryField(db_column='BKDDADOBLOB', blank=True, null=True)  # Field name made lowercase.
    bkdius = models.IntegerField(db_column='BKDIUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BACKUPDADO'


class Baixaestoque(models.Model):
    bestcod = models.IntegerField(db_column='BESTCOD', primary_key=True)  # Field name made lowercase.
    bestestq = models.ForeignKey('Estoque', models.DO_NOTHING, db_column='BESTESTQ')  # Field name made lowercase.
    bestfunreq = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='BESTFUNREQ')  # Field name made lowercase.
    bestcc = models.ForeignKey('Centrocusto', models.DO_NOTHING, db_column='BESTCC')  # Field name made lowercase.
    bestgrp = models.IntegerField(db_column='BESTGRP')  # Field name made lowercase.
    bestdata = models.DateTimeField(db_column='BESTDATA', blank=True, null=True)  # Field name made lowercase.
    bestestm = models.IntegerField(db_column='BESTESTM', blank=True, null=True)  # Field name made lowercase.
    bestquantreq = models.FloatField(db_column='BESTQUANTREQ', blank=True, null=True)  # Field name made lowercase.
    bestquantdev = models.FloatField(db_column='BESTQUANTDEV', blank=True, null=True)  # Field name made lowercase.
    bestquant = models.FloatField(db_column='BESTQUANT', blank=True, null=True)  # Field name made lowercase.
    bestquantbase = models.FloatField(db_column='BESTQUANTBASE', blank=True, null=True)  # Field name made lowercase.
    bestcustounit = models.FloatField(db_column='BESTCUSTOUNIT', blank=True, null=True)  # Field name made lowercase.
    bestcustounitbase = models.FloatField(db_column='BESTCUSTOUNITBASE', blank=True, null=True)  # Field name made lowercase.
    bestcusto = models.FloatField(db_column='BESTCUSTO', blank=True, null=True)  # Field name made lowercase.
    bestcustobase = models.FloatField(db_column='BESTCUSTOBASE', blank=True, null=True)  # Field name made lowercase.
    bestfunautor = models.IntegerField(db_column='BESTFUNAUTOR', blank=True, null=True)  # Field name made lowercase.
    bestfunalmox = models.IntegerField(db_column='BESTFUNALMOX', blank=True, null=True)  # Field name made lowercase.
    bestman = models.IntegerField(db_column='BESTMAN', blank=True, null=True)  # Field name made lowercase.
    bestpeqp = models.IntegerField(db_column='BESTPEQP', blank=True, null=True)  # Field name made lowercase.
    bestmotc = models.ForeignKey('Motivocusto', models.DO_NOTHING, db_column='BESTMOTC', blank=True, null=True)  # Field name made lowercase.
    besthorim = models.IntegerField(db_column='BESTHORIM', blank=True, null=True)  # Field name made lowercase.
    bestveloc = models.IntegerField(db_column='BESTVELOC', blank=True, null=True)  # Field name made lowercase.
    bestsit = models.IntegerField(db_column='BESTSIT', blank=True, null=True)  # Field name made lowercase.
    bestdataapl = models.DateTimeField(db_column='BESTDATAAPL', blank=True, null=True)  # Field name made lowercase.
    besthrtot = models.FloatField(db_column='BESTHRTOT', blank=True, null=True)  # Field name made lowercase.
    bestkmtot = models.FloatField(db_column='BESTKMTOT', blank=True, null=True)  # Field name made lowercase.
    bestgrpdestino = models.IntegerField(db_column='BESTGRPDESTINO', blank=True, null=True)  # Field name made lowercase.
    bestmesesam = models.IntegerField(db_column='BESTMESESAM', blank=True, null=True)  # Field name made lowercase.
    bestdet = models.IntegerField(db_column='BESTDET', blank=True, null=True)  # Field name made lowercase.
    besteqp = models.IntegerField(db_column='BESTEQP', blank=True, null=True)  # Field name made lowercase.
    bestbestdev = models.IntegerField(db_column='BESTBESTDEV', blank=True, null=True)  # Field name made lowercase.
    bestchv = models.IntegerField(db_column='BESTCHV', blank=True, null=True)  # Field name made lowercase.
    bestbloqlpe = models.CharField(db_column='BESTBLOQLPE', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bestemp = models.IntegerField(db_column='BESTEMP')  # Field name made lowercase.
    bestfil = models.IntegerField(db_column='BESTFIL')  # Field name made lowercase.
    bestbpro = models.IntegerField(db_column='BESTBPRO', blank=True, null=True)  # Field name made lowercase.
    bestplaca = models.CharField(db_column='BESTPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bestrepasseunit = models.FloatField(db_column='BESTREPASSEUNIT', blank=True, null=True)  # Field name made lowercase.
    bestrepasse = models.FloatField(db_column='BESTREPASSE', blank=True, null=True)  # Field name made lowercase.
    bestfor = models.IntegerField(db_column='BESTFOR', blank=True, null=True)  # Field name made lowercase.
    bestpgrepasse = models.IntegerField(db_column='BESTPGREPASSE', blank=True, null=True)  # Field name made lowercase.
    bestprecounit = models.FloatField(db_column='BESTPRECOUNIT', blank=True, null=True)  # Field name made lowercase.
    bestprecounitbase = models.FloatField(db_column='BESTPRECOUNITBASE', blank=True, null=True)  # Field name made lowercase.
    bestpreco = models.FloatField(db_column='BESTPRECO', blank=True, null=True)  # Field name made lowercase.
    bestprecobase = models.FloatField(db_column='BESTPRECOBASE', blank=True, null=True)  # Field name made lowercase.
    bestcfv = models.IntegerField(db_column='BESTCFV', blank=True, null=True)  # Field name made lowercase.
    besttipo = models.IntegerField(db_column='BESTTIPO', blank=True, null=True)  # Field name made lowercase.
    bestref = models.IntegerField(db_column='BESTREF', blank=True, null=True)  # Field name made lowercase.
    bestfunentr = models.IntegerField(db_column='BESTFUNENTR')  # Field name made lowercase.
    bestinfe = models.IntegerField(db_column='BESTINFE', blank=True, null=True)  # Field name made lowercase.
    bestvia = models.IntegerField(db_column='BESTVIA', blank=True, null=True)  # Field name made lowercase.
    bestscf = models.IntegerField(db_column='BESTSCF', blank=True, null=True)  # Field name made lowercase.
    bestcf = models.IntegerField(db_column='BESTCF', blank=True, null=True)  # Field name made lowercase.
    bestnumform = models.IntegerField(db_column='BESTNUMFORM', blank=True, null=True)  # Field name made lowercase.
    bestcop = models.IntegerField(db_column='BESTCOP', blank=True, null=True)  # Field name made lowercase.
    bestepimotivo = models.IntegerField(db_column='BESTEPIMOTIVO', blank=True, null=True)  # Field name made lowercase.
    bestepisemficha = models.CharField(db_column='BESTEPISEMFICHA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bestico1 = models.IntegerField(db_column='BESTICO1', blank=True, null=True)  # Field name made lowercase.
    bestico2 = models.IntegerField(db_column='BESTICO2', blank=True, null=True)  # Field name made lowercase.
    bestico3 = models.IntegerField(db_column='BESTICO3', blank=True, null=True)  # Field name made lowercase.
    bestrecop = models.IntegerField(db_column='BESTRECOP', blank=True, null=True)  # Field name made lowercase.
    bestcustoesticms = models.FloatField(db_column='BESTCUSTOESTICMS', blank=True, null=True)  # Field name made lowercase.
    bestalm = models.IntegerField(db_column='BESTALM', blank=True, null=True)  # Field name made lowercase.
    bestiem = models.ForeignKey('Itemestoquemanutencao', models.DO_NOTHING, db_column='BESTIEM', blank=True, null=True)  # Field name made lowercase.
    bestnumformos = models.IntegerField(db_column='BESTNUMFORMOS', blank=True, null=True)  # Field name made lowercase.
    bestcustounitbruto = models.FloatField(db_column='BESTCUSTOUNITBRUTO', blank=True, null=True)  # Field name made lowercase.
    bestcustobruto = models.FloatField(db_column='BESTCUSTOBRUTO', blank=True, null=True)  # Field name made lowercase.
    bestinf = models.IntegerField(db_column='BESTINF', blank=True, null=True)  # Field name made lowercase.
    bestencer_old = models.IntegerField(db_column='BESTENCER_OLD', blank=True, null=True)  # Field name made lowercase.
    bestencer = models.FloatField(db_column='BESTENCER', blank=True, null=True)  # Field name made lowercase.
    besttran = models.IntegerField(db_column='BESTTRAN', blank=True, null=True)  # Field name made lowercase.
    bestcai = models.IntegerField(db_column='BESTCAI', blank=True, null=True)  # Field name made lowercase.
    bestbai = models.IntegerField(db_column='BESTBAI', blank=True, null=True)  # Field name made lowercase.
    best_impl = models.CharField(db_column='BEST_IMPL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bestmotexcedeutol = models.CharField(db_column='BESTMOTEXCEDEUTOL', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bestbproab = models.IntegerField(db_column='BESTBPROAB', blank=True, null=True)  # Field name made lowercase.
    bestiab_old = models.IntegerField(db_column='BESTIAB_OLD', blank=True, null=True)  # Field name made lowercase.
    bestiab = models.CharField(db_column='BESTIAB', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bestel = models.IntegerField(db_column='BESTEL', blank=True, null=True)  # Field name made lowercase.
    bestultalt = models.DateTimeField(db_column='BESTULTALT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BAIXAESTOQUE'


class Baixaestoqueindiv(models.Model):
    beiei = models.OneToOneField('Estoqueindiv', models.DO_NOTHING, db_column='BEIEI', primary_key=True)  # Field name made lowercase. The composite primary key (BEIEI, BEIBEST) found, that is not supported. The first column is selected.
    beibest = models.ForeignKey(Baixaestoque, models.DO_NOTHING, db_column='BEIBEST')  # Field name made lowercase.
    beiquant = models.FloatField(db_column='BEIQUANT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BAIXAESTOQUEINDIV'
        unique_together = (('beiei', 'beibest'),)


class Baixaitembemativoimob(models.Model):
    bibaicod = models.IntegerField(db_column='BIBAICOD', primary_key=True)  # Field name made lowercase.
    bibaiibai = models.ForeignKey('Itembemativoimob', models.DO_NOTHING, db_column='BIBAIIBAI')  # Field name made lowercase.
    bibaidata = models.DateTimeField(db_column='BIBAIDATA', blank=True, null=True)  # Field name made lowercase.
    bibaidestnome = models.CharField(db_column='BIBAIDESTNOME', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bibaidestcnpjcpf = models.CharField(db_column='BIBAIDESTCNPJCPF', max_length=18, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bibainfdesc = models.CharField(db_column='BIBAINFDESC', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bibainfnum = models.CharField(db_column='BIBAINFNUM', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bibaivalor = models.FloatField(db_column='BIBAIVALOR', blank=True, null=True)  # Field name made lowercase.
    bibaivalordepac = models.FloatField(db_column='BIBAIVALORDEPAC', blank=True, null=True)  # Field name made lowercase.
    bibaiicmsap = models.FloatField(db_column='BIBAIICMSAP', blank=True, null=True)  # Field name made lowercase.
    bibaiicmsda = models.FloatField(db_column='BIBAIICMSDA', blank=True, null=True)  # Field name made lowercase.
    bibaisit = models.IntegerField(db_column='BIBAISIT', blank=True, null=True)  # Field name made lowercase.
    bibaivalufir = models.FloatField(db_column='BIBAIVALUFIR', blank=True, null=True)  # Field name made lowercase.
    bibaiqtdufir = models.FloatField(db_column='BIBAIQTDUFIR', blank=True, null=True)  # Field name made lowercase.
    bibaiufirdepac = models.FloatField(db_column='BIBAIUFIRDEPAC', blank=True, null=True)  # Field name made lowercase.
    bibaiicmsapst = models.FloatField(db_column='BIBAIICMSAPST', blank=True, null=True)  # Field name made lowercase.
    bibaiicmsapfrete = models.FloatField(db_column='BIBAIICMSAPFRETE', blank=True, null=True)  # Field name made lowercase.
    bibaieconvalordepac = models.FloatField(db_column='BIBAIECONVALORDEPAC', blank=True, null=True)  # Field name made lowercase.
    bibaieconufirdepac = models.FloatField(db_column='BIBAIECONUFIRDEPAC', blank=True, null=True)  # Field name made lowercase.
    bibaitransf = models.CharField(db_column='BIBAITRANSF', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bibaiicmstransf = models.FloatField(db_column='BIBAIICMSTRANSF', blank=True, null=True)  # Field name made lowercase.
    bibaicredpisbase = models.FloatField(db_column='BIBAICREDPISBASE', blank=True, null=True)  # Field name made lowercase.
    bibaicredpisaliq = models.FloatField(db_column='BIBAICREDPISALIQ', blank=True, null=True)  # Field name made lowercase.
    bibaicredpisvalor = models.FloatField(db_column='BIBAICREDPISVALOR', blank=True, null=True)  # Field name made lowercase.
    bibaicredcofinsbase = models.FloatField(db_column='BIBAICREDCOFINSBASE', blank=True, null=True)  # Field name made lowercase.
    bibaicredcofinsaliq = models.FloatField(db_column='BIBAICREDCOFINSALIQ', blank=True, null=True)  # Field name made lowercase.
    bibaicredcofinsvalor = models.FloatField(db_column='BIBAICREDCOFINSVALOR', blank=True, null=True)  # Field name made lowercase.
    bibaiicms = models.FloatField(db_column='BIBAIICMS', blank=True, null=True)  # Field name made lowercase.
    bibaiipi = models.FloatField(db_column='BIBAIIPI', blank=True, null=True)  # Field name made lowercase.
    bibaiicmsdadestacado = models.FloatField(db_column='BIBAIICMSDADESTACADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BAIXAITEMBEMATIVOIMOB'


class Baixaproducao(models.Model):
    bprocod = models.IntegerField(db_column='BPROCOD', primary_key=True)  # Field name made lowercase.
    bproemp = models.IntegerField(db_column='BPROEMP')  # Field name made lowercase.
    bprofil = models.IntegerField(db_column='BPROFIL')  # Field name made lowercase.
    bprodata = models.DateTimeField(db_column='BPRODATA', blank=True, null=True)  # Field name made lowercase.
    bprosublote = models.IntegerField(db_column='BPROSUBLOTE', blank=True, null=True)  # Field name made lowercase.
    bprodesc = models.CharField(db_column='BPRODESC', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bprotipo = models.CharField(db_column='BPROTIPO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bprofunresp = models.IntegerField(db_column='BPROFUNRESP', blank=True, null=True)  # Field name made lowercase.
    bprofundig = models.IntegerField(db_column='BPROFUNDIG', blank=True, null=True)  # Field name made lowercase.
    bprosit = models.IntegerField(db_column='BPROSIT', blank=True, null=True)  # Field name made lowercase.
    bproep = models.IntegerField(db_column='BPROEP', blank=True, null=True)  # Field name made lowercase.
    bproeqp = models.IntegerField(db_column='BPROEQP', blank=True, null=True)  # Field name made lowercase.
    bprofor = models.IntegerField(db_column='BPROFOR', blank=True, null=True)  # Field name made lowercase.
    bpronfe = models.IntegerField(db_column='BPRONFE', blank=True, null=True)  # Field name made lowercase.
    bprofpro = models.IntegerField(db_column='BPROFPRO', blank=True, null=True)  # Field name made lowercase.
    bprofproquant = models.FloatField(db_column='BPROFPROQUANT', blank=True, null=True)  # Field name made lowercase.
    bprofproversao = models.IntegerField(db_column='BPROFPROVERSAO', blank=True, null=True)  # Field name made lowercase.
    bprofproopcao = models.CharField(db_column='BPROFPROOPCAO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bproqetipo = models.IntegerField(db_column='BPROQETIPO', blank=True, null=True)  # Field name made lowercase.
    bproqeref = models.IntegerField(db_column='BPROQEREF', blank=True, null=True)  # Field name made lowercase.
    bprofproserie = models.IntegerField(db_column='BPROFPROSERIE', blank=True, null=True)  # Field name made lowercase.
    bproqetipoorig = models.IntegerField(db_column='BPROQETIPOORIG', blank=True, null=True)  # Field name made lowercase.
    bproqereforig = models.IntegerField(db_column='BPROQEREFORIG', blank=True, null=True)  # Field name made lowercase.
    bprodataref = models.DateTimeField(db_column='BPRODATAREF', blank=True, null=True)  # Field name made lowercase.
    bproultalt = models.DateTimeField(db_column='BPROULTALT', blank=True, null=True)  # Field name made lowercase.
    bprocli = models.IntegerField(db_column='BPROCLI', blank=True, null=True)  # Field name made lowercase.
    bprodata1 = models.DateTimeField(db_column='BPRODATA1', blank=True, null=True)  # Field name made lowercase.
    bprodata2 = models.DateTimeField(db_column='BPRODATA2', blank=True, null=True)  # Field name made lowercase.
    bprofproopcao2 = models.CharField(db_column='BPROFPROOPCAO2', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bprofproopcao3 = models.CharField(db_column='BPROFPROOPCAO3', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bproobs = models.BinaryField(db_column='BPROOBS', blank=True, null=True)  # Field name made lowercase.
    bprodataemissao = models.DateTimeField(db_column='BPRODATAEMISSAO', blank=True, null=True)  # Field name made lowercase.
    bproobspub = models.BinaryField(db_column='BPROOBSPUB', blank=True, null=True)  # Field name made lowercase.
    bprodataprimreg = models.DateTimeField(db_column='BPRODATAPRIMREG', blank=True, null=True)  # Field name made lowercase.
    bpronatureza = models.IntegerField(db_column='BPRONATUREZA', blank=True, null=True)  # Field name made lowercase.
    bprocura = models.IntegerField(db_column='BPROCURA', blank=True, null=True)  # Field name made lowercase.
    bprocuradata = models.DateTimeField(db_column='BPROCURADATA', blank=True, null=True)  # Field name made lowercase.
    bprocurareg = models.CharField(db_column='BPROCURAREG', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bproqetipodest = models.IntegerField(db_column='BPROQETIPODEST', blank=True, null=True)  # Field name made lowercase.
    bproqerefdest = models.IntegerField(db_column='BPROQEREFDEST', blank=True, null=True)  # Field name made lowercase.
    bproped = models.IntegerField(db_column='BPROPED', blank=True, null=True)  # Field name made lowercase.
    bprochv1 = models.IntegerField(db_column='BPROCHV1', blank=True, null=True)  # Field name made lowercase.
    bprochv2 = models.IntegerField(db_column='BPROCHV2', blank=True, null=True)  # Field name made lowercase.
    bprohr1 = models.IntegerField(db_column='BPROHR1', blank=True, null=True)  # Field name made lowercase.
    bprohr2 = models.IntegerField(db_column='BPROHR2', blank=True, null=True)  # Field name made lowercase.
    bprohrsn = models.CharField(db_column='BPROHRSN', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bprohrtot = models.FloatField(db_column='BPROHRTOT', blank=True, null=True)  # Field name made lowercase.
    bprohroper = models.FloatField(db_column='BPROHROPER', blank=True, null=True)  # Field name made lowercase.
    bprohrprod = models.FloatField(db_column='BPROHRPROD', blank=True, null=True)  # Field name made lowercase.
    bprosobra = models.FloatField(db_column='BPROSOBRA', blank=True, null=True)  # Field name made lowercase.
    bproencer_old = models.IntegerField(db_column='BPROENCER_OLD', blank=True, null=True)  # Field name made lowercase.
    bproencer = models.FloatField(db_column='BPROENCER', blank=True, null=True)  # Field name made lowercase.
    bproqtdporhr = models.FloatField(db_column='BPROQTDPORHR', blank=True, null=True)  # Field name made lowercase.
    bproacumbal = models.FloatField(db_column='BPROACUMBAL', blank=True, null=True)  # Field name made lowercase.
    bproquantmanual = models.CharField(db_column='BPROQUANTMANUAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bproromaneio = models.IntegerField(db_column='BPROROMANEIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BAIXAPRODUCAO'


class Balanca(models.Model):
    balcod = models.IntegerField(db_column='BALCOD', primary_key=True)  # Field name made lowercase.
    baltipo = models.IntegerField(db_column='BALTIPO')  # Field name made lowercase.
    balnum = models.IntegerField(db_column='BALNUM')  # Field name made lowercase.
    balfun = models.IntegerField(db_column='BALFUN')  # Field name made lowercase.
    baldata = models.DateTimeField(db_column='BALDATA', blank=True, null=True)  # Field name made lowercase.
    balplaca = models.CharField(db_column='BALPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    balpeso = models.FloatField(db_column='BALPESO', blank=True, null=True)  # Field name made lowercase.
    balsaldo = models.FloatField(db_column='BALSALDO', blank=True, null=True)  # Field name made lowercase.
    balobs = models.CharField(db_column='BALOBS', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    balbalint = models.IntegerField(db_column='BALBALINT', blank=True, null=True)  # Field name made lowercase.
    balpesototal = models.FloatField(db_column='BALPESOTOTAL', blank=True, null=True)  # Field name made lowercase.
    balcodorig = models.IntegerField(db_column='BALCODORIG', blank=True, null=True)  # Field name made lowercase.
    balcanclib = models.CharField(db_column='BALCANCLIB', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    balcancdata = models.DateTimeField(db_column='BALCANCDATA', blank=True, null=True)  # Field name made lowercase.
    balsensorfuga1 = models.CharField(db_column='BALSENSORFUGA1', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    balsensorfuga2 = models.CharField(db_column='BALSENSORFUGA2', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BALANCA'


class Balancaatual(models.Model):
    balanum = models.IntegerField(db_column='BALANUM', primary_key=True)  # Field name made lowercase.
    balabal = models.IntegerField(db_column='BALABAL', blank=True, null=True)  # Field name made lowercase.
    balanovo = models.CharField(db_column='BALANOVO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baladispplaca = models.CharField(db_column='BALADISPPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baladisptara = models.FloatField(db_column='BALADISPTARA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BALANCAATUAL'


class Balancaguardian(models.Model):
    bgcod = models.IntegerField(db_column='BGCOD', primary_key=True)  # Field name made lowercase.
    bgbalsga = models.IntegerField(db_column='BGBALSGA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BALANCAGUARDIAN'


class Balancaint(models.Model):
    balicod = models.IntegerField(db_column='BALICOD', primary_key=True)  # Field name made lowercase.
    balibal = models.IntegerField(db_column='BALIBAL')  # Field name made lowercase.
    baliseq = models.IntegerField(db_column='BALISEQ', blank=True, null=True)  # Field name made lowercase.
    balipeso = models.FloatField(db_column='BALIPESO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BALANCAINT'


class Balanco(models.Model):
    blcod = models.IntegerField(db_column='BLCOD', primary_key=True)  # Field name made lowercase.
    blemp = models.IntegerField(db_column='BLEMP', blank=True, null=True)  # Field name made lowercase.
    bldata = models.DateTimeField(db_column='BLDATA', blank=True, null=True)  # Field name made lowercase.
    blnome = models.CharField(db_column='BLNOME', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    blniveis = models.IntegerField(db_column='BLNIVEIS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BALANCO'


class Balancocontas(models.Model):
    blccod = models.IntegerField(db_column='BLCCOD', primary_key=True)  # Field name made lowercase.
    blcbl = models.ForeignKey(Balanco, models.DO_NOTHING, db_column='BLCBL', blank=True, null=True)  # Field name made lowercase.
    blcvalor = models.FloatField(db_column='BLCVALOR', blank=True, null=True)  # Field name made lowercase.
    blcnome_old = models.CharField(db_column='BLCNOME_OLD', max_length=30, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    blcnome = models.CharField(db_column='BLCNOME', max_length=150, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    blcconta_antigo = models.CharField(db_column='BLCCONTA_ANTIGO', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    blcconta = models.CharField(db_column='BLCCONTA', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BALANCOCONTAS'


class Banco(models.Model):
    bancod = models.IntegerField(db_column='BANCOD', primary_key=True)  # Field name made lowercase.
    bannome = models.CharField(db_column='BANNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    bansigla = models.CharField(db_column='BANSIGLA', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banendereco = models.CharField(db_column='BANENDERECO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banbairro = models.CharField(db_column='BANBAIRRO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancep = models.CharField(db_column='BANCEP', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancidade = models.IntegerField(db_column='BANCIDADE', blank=True, null=True)  # Field name made lowercase.
    bancontato = models.CharField(db_column='BANCONTATO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bantelefone = models.CharField(db_column='BANTELEFONE', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banfax = models.CharField(db_column='BANFAX', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banemail = models.CharField(db_column='BANEMAIL', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banweb = models.CharField(db_column='BANWEB', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banagencia = models.CharField(db_column='BANAGENCIA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banconta = models.CharField(db_column='BANCONTA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancheque = models.IntegerField(db_column='BANCHEQUE', blank=True, null=True)  # Field name made lowercase.
    bannumremessa = models.IntegerField(db_column='BANNUMREMESSA', blank=True, null=True)  # Field name made lowercase.
    bannumretorno = models.IntegerField(db_column='BANNUMRETORNO', blank=True, null=True)  # Field name made lowercase.
    banbolnum = models.FloatField(db_column='BANBOLNUM', blank=True, null=True)  # Field name made lowercase.
    bancodcont = models.CharField(db_column='BANCODCONT', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banobs = models.BinaryField(db_column='BANOBS', blank=True, null=True)  # Field name made lowercase.
    bantipobancob = models.IntegerField(db_column='BANTIPOBANCOB', blank=True, null=True)  # Field name made lowercase.
    bancobstr1 = models.CharField(db_column='BANCOBSTR1', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobstr2 = models.CharField(db_column='BANCOBSTR2', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobstr3 = models.CharField(db_column='BANCOBSTR3', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobstr4 = models.CharField(db_column='BANCOBSTR4', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobdiascomp = models.IntegerField(db_column='BANCOBDIASCOMP', blank=True, null=True)  # Field name made lowercase.
    bancodcontdesc = models.CharField(db_column='BANCODCONTDESC', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobjurosdia = models.FloatField(db_column='BANCOBJUROSDIA', blank=True, null=True)  # Field name made lowercase.
    bancobstr5 = models.CharField(db_column='BANCOBSTR5', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banhppgto = models.IntegerField(db_column='BANHPPGTO', blank=True, null=True)  # Field name made lowercase.
    banccctipoban = models.IntegerField(db_column='BANCCCTIPOBAN', blank=True, null=True)  # Field name made lowercase.
    bancccnumremessa = models.IntegerField(db_column='BANCCCNUMREMESSA', blank=True, null=True)  # Field name made lowercase.
    bancccnumretorno = models.IntegerField(db_column='BANCCCNUMRETORNO', blank=True, null=True)  # Field name made lowercase.
    bancccarqrem = models.CharField(db_column='BANCCCARQREM', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccarqretorig = models.CharField(db_column='BANCCCARQRETORIG', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccarqretfin = models.CharField(db_column='BANCCCARQRETFIN', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccstr1 = models.CharField(db_column='BANCCCSTR1', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccstr2 = models.CharField(db_column='BANCCCSTR2', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccstr3 = models.CharField(db_column='BANCCCSTR3', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccstr4 = models.CharField(db_column='BANCCCSTR4', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccstr5 = models.CharField(db_column='BANCCCSTR5', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontche = models.CharField(db_column='BANCODCONTCHE', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontantcam = models.CharField(db_column='BANCODCONTANTCAM', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobdespesa = models.FloatField(db_column='BANCOBDESPESA', blank=True, null=True)  # Field name made lowercase.
    banemp = models.IntegerField(db_column='BANEMP', blank=True, null=True)  # Field name made lowercase.
    repfunresp = models.IntegerField(db_column='REPFUNRESP', blank=True, null=True)  # Field name made lowercase.
    bancban = models.IntegerField(db_column='BANCBAN', blank=True, null=True)  # Field name made lowercase.
    ban_numero = models.IntegerField(db_column='BAN_NUMERO', blank=True, null=True)  # Field name made lowercase.
    banpgetipoban = models.CharField(db_column='BANPGETIPOBAN', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgenumremessa = models.IntegerField(db_column='BANPGENUMREMESSA', blank=True, null=True)  # Field name made lowercase.
    banpgenumretorno = models.IntegerField(db_column='BANPGENUMRETORNO', blank=True, null=True)  # Field name made lowercase.
    banpgestr1 = models.CharField(db_column='BANPGESTR1', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgestr2 = models.CharField(db_column='BANPGESTR2', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgestr3 = models.CharField(db_column='BANPGESTR3', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgestr4 = models.CharField(db_column='BANPGESTR4', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgestr5 = models.CharField(db_column='BANPGESTR5', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgefinalidade = models.CharField(db_column='BANPGEFINALIDADE', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobmens = models.CharField(db_column='BANCOBMENS', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobmensprot = models.CharField(db_column='BANCOBMENSPROT', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobmenssprot = models.CharField(db_column='BANCOBMENSSPROT', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banimpbolprefixo = models.CharField(db_column='BANIMPBOLPREFIXO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banimpbolproximo = models.IntegerField(db_column='BANIMPBOLPROXIMO', blank=True, null=True)  # Field name made lowercase.
    bancobcart_old = models.IntegerField(db_column='BANCOBCART_OLD', blank=True, null=True)  # Field name made lowercase.
    bancobcarteira = models.CharField(db_column='BANCOBCARTEIRA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banimpbolcarteira = models.CharField(db_column='BANIMPBOLCARTEIRA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banchequeexp = models.IntegerField(db_column='BANCHEQUEEXP', blank=True, null=True)  # Field name made lowercase.
    bancobeventoprot = models.IntegerField(db_column='BANCOBEVENTOPROT', blank=True, null=True)  # Field name made lowercase.
    bancodcontport = models.CharField(db_column='BANCODCONTPORT', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobmulta = models.FloatField(db_column='BANCOBMULTA', blank=True, null=True)  # Field name made lowercase.
    banhprec = models.IntegerField(db_column='BANHPREC', blank=True, null=True)  # Field name made lowercase.
    bancodcedente = models.CharField(db_column='BANCODCEDENTE', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobconvref = models.CharField(db_column='BANCOBCONVREF', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobconvemp = models.IntegerField(db_column='BANCOBCONVEMP', blank=True, null=True)  # Field name made lowercase.
    bancobconvfil = models.IntegerField(db_column='BANCOBCONVFIL', blank=True, null=True)  # Field name made lowercase.
    banrpcheque = models.IntegerField(db_column='BANRPCHEQUE', blank=True, null=True)  # Field name made lowercase.
    bancobarqrem_old = models.CharField(db_column='BANCOBARQREM_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobarqrem = models.CharField(db_column='BANCOBARQREM', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobarqretorig_old = models.CharField(db_column='BANCOBARQRETORIG_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobarqretorig = models.CharField(db_column='BANCOBARQRETORIG', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobarqretfin_old = models.CharField(db_column='BANCOBARQRETFIN_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobarqretfin = models.CharField(db_column='BANCOBARQRETFIN', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqrem_old = models.CharField(db_column='BANPGEARQREM_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqrem = models.CharField(db_column='BANPGEARQREM', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretorig_old = models.CharField(db_column='BANPGEARQRETORIG_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretorig = models.CharField(db_column='BANPGEARQRETORIG', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretfin_old = models.CharField(db_column='BANPGEARQRETFIN_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretfin = models.CharField(db_column='BANPGEARQRETFIN', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqrem2_old = models.CharField(db_column='BANPGEARQREM2_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqrem2 = models.CharField(db_column='BANPGEARQREM2', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretorig2_old = models.CharField(db_column='BANPGEARQRETORIG2_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretorig2 = models.CharField(db_column='BANPGEARQRETORIG2', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretfin2_old = models.CharField(db_column='BANPGEARQRETFIN2_OLD', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banpgearqretfin2 = models.CharField(db_column='BANPGEARQRETFIN2', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontaplic1 = models.CharField(db_column='BANCODCONTAPLIC1', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontaplic2 = models.CharField(db_column='BANCODCONTAPLIC2', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontaplic3 = models.CharField(db_column='BANCODCONTAPLIC3', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancartaotreg = models.ForeignKey('Tiporegistro', models.DO_NOTHING, db_column='BANCARTAOTREG', blank=True, null=True)  # Field name made lowercase.
    bancartaotregopcao = models.CharField(db_column='BANCARTAOTREGOPCAO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancartaocorte = models.IntegerField(db_column='BANCARTAOCORTE', blank=True, null=True)  # Field name made lowercase.
    bancartaomeses = models.IntegerField(db_column='BANCARTAOMESES', blank=True, null=True)  # Field name made lowercase.
    bancartaodia = models.IntegerField(db_column='BANCARTAODIA', blank=True, null=True)  # Field name made lowercase.
    bancartaoprazo = models.IntegerField(db_column='BANCARTAOPRAZO', blank=True, null=True)  # Field name made lowercase.
    bancartaocli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='BANCARTAOCLI', blank=True, null=True)  # Field name made lowercase.
    bancobdiaslibcred = models.IntegerField(db_column='BANCOBDIASLIBCRED', blank=True, null=True)  # Field name made lowercase.
    bancobinstprot = models.CharField(db_column='BANCOBINSTPROT', max_length=5, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancorrespban = models.IntegerField(db_column='BANCORRESPBAN', blank=True, null=True)  # Field name made lowercase.
    bancorrespcarteira = models.CharField(db_column='BANCORRESPCARTEIRA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banfortit = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='BANFORTIT', blank=True, null=True)  # Field name made lowercase.
    bantregliq = models.ForeignKey('Tiporegistro', models.DO_NOTHING, db_column='BANTREGLIQ', related_name='banco_bantregliq_set', blank=True, null=True)  # Field name made lowercase.
    bancartaotar = models.FloatField(db_column='BANCARTAOTAR', blank=True, null=True)  # Field name made lowercase.
    bancartaotarparc = models.FloatField(db_column='BANCARTAOTARPARC', blank=True, null=True)  # Field name made lowercase.
    bancartaomaxparc = models.IntegerField(db_column='BANCARTAOMAXPARC', blank=True, null=True)  # Field name made lowercase.
    banwstipobancob = models.CharField(db_column='BANWSTIPOBANCOB', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banwsurl = models.CharField(db_column='BANWSURL', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banwsstr1 = models.CharField(db_column='BANWSSTR1', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banccccodinstmov = models.CharField(db_column='BANCCCCODINSTMOV', max_length=2, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancccnumcadastro = models.IntegerField(db_column='BANCCCNUMCADASTRO', blank=True, null=True)  # Field name made lowercase.
    banwsstr2 = models.CharField(db_column='BANWSSTR2', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banimpbollocpag = models.CharField(db_column='BANIMPBOLLOCPAG', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banholtipoban = models.IntegerField(db_column='BANHOLTIPOBAN', blank=True, null=True)  # Field name made lowercase.
    bancadcontatipoban = models.IntegerField(db_column='BANCADCONTATIPOBAN', blank=True, null=True)  # Field name made lowercase.
    banholnumremessa = models.IntegerField(db_column='BANHOLNUMREMESSA', blank=True, null=True)  # Field name made lowercase.
    banholarqrem = models.CharField(db_column='BANHOLARQREM', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banwsstr3 = models.CharField(db_column='BANWSSTR3', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banwsstr4 = models.CharField(db_column='BANWSSTR4', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banholstr1 = models.CharField(db_column='BANHOLSTR1', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banholstr2 = models.CharField(db_column='BANHOLSTR2', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banholstr3 = models.CharField(db_column='BANHOLSTR3', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banholstr4 = models.CharField(db_column='BANHOLSTR4', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banholstr5 = models.CharField(db_column='BANHOLSTR5', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontbloq = models.CharField(db_column='BANCODCONTBLOQ', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banhprecbloq = models.IntegerField(db_column='BANHPRECBLOQ', blank=True, null=True)  # Field name made lowercase.
    bantregliqcp = models.ForeignKey('Tiporegistro', models.DO_NOTHING, db_column='BANTREGLIQCP', related_name='banco_bantregliqcp_set', blank=True, null=True)  # Field name made lowercase.
    bancartaoautom = models.CharField(db_column='BANCARTAOAUTOM', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobemp = models.IntegerField(db_column='BANCOBEMP', blank=True, null=True)  # Field name made lowercase.
    bancobfil = models.IntegerField(db_column='BANCOBFIL', blank=True, null=True)  # Field name made lowercase.
    bancompencont = models.IntegerField(db_column='BANCOMPENCONT', blank=True, null=True)  # Field name made lowercase.
    bancartaocnpjcred = models.CharField(db_column='BANCARTAOCNPJCRED', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banmasctit = models.CharField(db_column='BANMASCTIT', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banvinc = models.IntegerField(db_column='BANVINC', blank=True, null=True)  # Field name made lowercase.
    banvincseq = models.CharField(db_column='BANVINCSEQ', max_length=5, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancobdiascomptar = models.IntegerField(db_column='BANCOBDIASCOMPTAR', blank=True, null=True)  # Field name made lowercase.
    banforinst = models.IntegerField(db_column='BANFORINST', blank=True, null=True)  # Field name made lowercase.
    banbolmsgcorpoemail = models.BinaryField(db_column='BANBOLMSGCORPOEMAIL', blank=True, null=True)  # Field name made lowercase.
    bancodcontatransitoria = models.CharField(db_column='BANCODCONTATRANSITORIA', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banwscobjurosmes = models.FloatField(db_column='BANWSCOBJUROSMES', blank=True, null=True)  # Field name made lowercase.
    banwsdtenvioatual = models.CharField(db_column='BANWSDTENVIOATUAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banflag_old = models.CharField(db_column='BANFLAG_OLD', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banflag = models.CharField(db_column='BANFLAG', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontjurosrec = models.CharField(db_column='BANCODCONTJUROSREC', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bansecrisco = models.FloatField(db_column='BANSECRISCO', blank=True, null=True)  # Field name made lowercase.
    bancodcontdircred = models.CharField(db_column='BANCODCONTDIRCRED', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancodcontantrec = models.CharField(db_column='BANCODCONTANTREC', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bancc = models.IntegerField(db_column='BANCC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BANCO'


class Bandeira(models.Model):
    bandcod = models.IntegerField(db_column='BANDCOD', primary_key=True)  # Field name made lowercase.
    bandnome = models.CharField(db_column='BANDNOME', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bandcodsefaz = models.IntegerField(db_column='BANDCODSEFAZ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BANDEIRA'


class Bandeiracartao(models.Model):
    bcarban = models.IntegerField(db_column='BCARBAN', primary_key=True)  # Field name made lowercase. The composite primary key (BCARBAN, BCARBAND) found, that is not supported. The first column is selected.
    bcarband = models.IntegerField(db_column='BCARBAND')  # Field name made lowercase.
    bcarcartaotar = models.FloatField(db_column='BCARCARTAOTAR', blank=True, null=True)  # Field name made lowercase.
    bcarcartaotarparc = models.FloatField(db_column='BCARCARTAOTARPARC', blank=True, null=True)  # Field name made lowercase.
    bcarcartaomaxparc = models.IntegerField(db_column='BCARCARTAOMAXPARC', blank=True, null=True)  # Field name made lowercase.
    bcarcartaoprazo = models.IntegerField(db_column='BCARCARTAOPRAZO', blank=True, null=True)  # Field name made lowercase.
    bcarcartaocorte = models.IntegerField(db_column='BCARCARTAOCORTE', blank=True, null=True)  # Field name made lowercase.
    bcarcartaomeses = models.IntegerField(db_column='BCARCARTAOMESES', blank=True, null=True)  # Field name made lowercase.
    bcarcartaodia = models.IntegerField(db_column='BCARCARTAODIA', blank=True, null=True)  # Field name made lowercase.
    bcarcartaoprazoavista = models.IntegerField(db_column='BCARCARTAOPRAZOAVISTA', blank=True, null=True)  # Field name made lowercase.
    bcarcartaominparc = models.IntegerField(db_column='BCARCARTAOMINPARC', blank=True, null=True)  # Field name made lowercase.
    bcarprzcomissao = models.IntegerField(db_column='BCARPRZCOMISSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BANDEIRACARTAO'
        unique_together = (('bcarban', 'bcarband'),)


class Basecompra(models.Model):
    bcomcod = models.IntegerField(db_column='BCOMCOD', primary_key=True)  # Field name made lowercase.
    bcomnome = models.CharField(db_column='BCOMNOME', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bcombloq = models.CharField(db_column='BCOMBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BASECOMPRA'


class Basetreinamento(models.Model):
    btrncod = models.IntegerField(db_column='BTRNCOD', primary_key=True)  # Field name made lowercase.
    btrnnome = models.CharField(db_column='BTRNNOME', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    btrncargahr = models.IntegerField(db_column='BTRNCARGAHR', blank=True, null=True)  # Field name made lowercase.
    btrnnumaulas = models.IntegerField(db_column='BTRNNUMAULAS', blank=True, null=True)  # Field name made lowercase.
    btrntipoaval = models.CharField(db_column='BTRNTIPOAVAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    btrnfreqmin = models.FloatField(db_column='BTRNFREQMIN', blank=True, null=True)  # Field name made lowercase.
    btrnnotamin = models.FloatField(db_column='BTRNNOTAMIN', blank=True, null=True)  # Field name made lowercase.
    btrnfor = models.IntegerField(db_column='BTRNFOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BASETREINAMENTO'


class Bemativoimob(models.Model):
    baicod = models.IntegerField(db_column='BAICOD', primary_key=True)  # Field name made lowercase.
    baicai = models.ForeignKey('Contaativoimob', models.DO_NOTHING, db_column='BAICAI')  # Field name made lowercase.
    baicc = models.IntegerField(db_column='BAICC', blank=True, null=True)  # Field name made lowercase.
    baiemp = models.IntegerField(db_column='BAIEMP')  # Field name made lowercase.
    baifil = models.IntegerField(db_column='BAIFIL')  # Field name made lowercase.
    baiimobandopcao = models.CharField(db_column='BAIIMOBANDOPCAO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baiimobandinicio = models.DateTimeField(db_column='BAIIMOBANDINICIO', blank=True, null=True)  # Field name made lowercase.
    baiimobandfinal = models.DateTimeField(db_column='BAIIMOBANDFINAL', blank=True, null=True)  # Field name made lowercase.
    baibloq = models.CharField(db_column='BAIBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baieqp = models.IntegerField(db_column='BAIEQP', blank=True, null=True)  # Field name made lowercase.
    baiccinv = models.IntegerField(db_column='BAICCINV', blank=True, null=True)  # Field name made lowercase.
    baieqpsn = models.CharField(db_column='BAIEQPSN', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bainome_old = models.CharField(db_column='BAINOME_OLD', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baidescricao_old = models.CharField(db_column='BAIDESCRICAO_OLD', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bainome = models.CharField(db_column='BAINOME', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baidescricao = models.CharField(db_column='BAIDESCRICAO', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bai_imp = models.IntegerField(db_column='BAI_IMP', blank=True, null=True)  # Field name made lowercase.
    baictativoimoband = models.CharField(db_column='BAICTATIVOIMOBAND', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BEMATIVOIMOB'


class Bloqueioestoque(models.Model):
    becod = models.IntegerField(db_column='BECOD', primary_key=True)  # Field name made lowercase.
    beemp = models.IntegerField(db_column='BEEMP', blank=True, null=True)  # Field name made lowercase.
    befil = models.IntegerField(db_column='BEFIL', blank=True, null=True)  # Field name made lowercase.
    beestq = models.ForeignKey('Estoque', models.DO_NOTHING, db_column='BEESTQ')  # Field name made lowercase.
    beico1 = models.IntegerField(db_column='BEICO1', blank=True, null=True)  # Field name made lowercase.
    beico2 = models.IntegerField(db_column='BEICO2', blank=True, null=True)  # Field name made lowercase.
    beico3 = models.IntegerField(db_column='BEICO3', blank=True, null=True)  # Field name made lowercase.
    beqetipo = models.IntegerField(db_column='BEQETIPO', blank=True, null=True)  # Field name made lowercase.
    beqeref = models.IntegerField(db_column='BEQEREF', blank=True, null=True)  # Field name made lowercase.
    beinfe = models.ForeignKey('Itemnotafiscalentrada', models.DO_NOTHING, db_column='BEINFE')  # Field name made lowercase.
    befun = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='BEFUN')  # Field name made lowercase.
    bedata = models.DateTimeField(db_column='BEDATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BLOQUEIOESTOQUE'


class Bmxdocumento(models.Model):
    bmxddocumentoid = models.CharField(db_column='BMXDDOCUMENTOID', max_length=20, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    bmxdentregaid = models.CharField(db_column='BMXDENTREGAID', max_length=20, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    bmxdnfrem = models.IntegerField(db_column='BMXDNFREM', blank=True, null=True)  # Field name made lowercase.
    bmxdnfserv = models.IntegerField(db_column='BMXDNFSERV', blank=True, null=True)  # Field name made lowercase.
    bmxdseq = models.IntegerField(db_column='BMXDSEQ', blank=True, null=True)  # Field name made lowercase.
    bmxdfracao = models.FloatField(db_column='BMXDFRACAO', blank=True, null=True)  # Field name made lowercase.
    bmxddocumentonum_old = models.CharField(db_column='BMXDDOCUMENTONUM_OLD', max_length=30, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxddocumentonum = models.CharField(db_column='BMXDDOCUMENTONUM', max_length=30, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxdtipointegracao = models.CharField(db_column='BMXDTIPOINTEGRACAO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BMXDOCUMENTO'


class Bmxentrega(models.Model):
    bmxeentregaid = models.CharField(db_column='BMXEENTREGAID', primary_key=True, max_length=20, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    bmxeemp = models.IntegerField(db_column='BMXEEMP')  # Field name made lowercase.
    bmxefil = models.IntegerField(db_column='BMXEFIL')  # Field name made lowercase.
    bmxecli = models.IntegerField(db_column='BMXECLI')  # Field name made lowercase.
    bmxeestq = models.IntegerField(db_column='BMXEESTQ')  # Field name made lowercase.
    bmxequant = models.FloatField(db_column='BMXEQUANT', blank=True, null=True)  # Field name made lowercase.
    bmxevltotal = models.FloatField(db_column='BMXEVLTOTAL', blank=True, null=True)  # Field name made lowercase.
    bmxeobraid = models.CharField(db_column='BMXEOBRAID', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxeenderecoobra = models.CharField(db_column='BMXEENDERECOOBRA', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxecidobra = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='BMXECIDOBRA', blank=True, null=True)  # Field name made lowercase.
    bmxefck = models.FloatField(db_column='BMXEFCK', blank=True, null=True)  # Field name made lowercase.
    bmxeagua = models.FloatField(db_column='BMXEAGUA', blank=True, null=True)  # Field name made lowercase.
    bmxelacre = models.IntegerField(db_column='BMXELACRE', blank=True, null=True)  # Field name made lowercase.
    bmxepesotara = models.FloatField(db_column='BMXEPESOTARA', blank=True, null=True)  # Field name made lowercase.
    bmxepesoliq = models.FloatField(db_column='BMXEPESOLIQ', blank=True, null=True)  # Field name made lowercase.
    bmxebpro = models.ForeignKey(Baixaproducao, models.DO_NOTHING, db_column='BMXEBPRO', blank=True, null=True)  # Field name made lowercase.
    bmxefracao = models.FloatField(db_column='BMXEFRACAO', blank=True, null=True)  # Field name made lowercase.
    bmxetipointegracao = models.CharField(db_column='BMXETIPOINTEGRACAO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxeslump1_temp = models.IntegerField(db_column='BMXESLUMP1_TEMP', blank=True, null=True)  # Field name made lowercase.
    bmxeslump1 = models.FloatField(db_column='BMXESLUMP1', blank=True, null=True)  # Field name made lowercase.
    bmxeslump2_temp = models.IntegerField(db_column='BMXESLUMP2_TEMP', blank=True, null=True)  # Field name made lowercase.
    bmxeslump2 = models.FloatField(db_column='BMXESLUMP2', blank=True, null=True)  # Field name made lowercase.
    bmxeplacabomba = models.CharField(db_column='BMXEPLACABOMBA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxeprodid = models.CharField(db_column='BMXEPRODID', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxeprodnome = models.CharField(db_column='BMXEPRODNOME', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BMXENTREGA'


class Bmxpedido(models.Model):
    bmxppedidoid = models.CharField(db_column='BMXPPEDIDOID', primary_key=True, max_length=20, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    bmxpemp = models.IntegerField(db_column='BMXPEMP')  # Field name made lowercase.
    bmxpfil = models.IntegerField(db_column='BMXPFIL')  # Field name made lowercase.
    bmxpcli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='BMXPCLI')  # Field name made lowercase.
    bmxprep = models.IntegerField(db_column='BMXPREP', blank=True, null=True)  # Field name made lowercase.
    bmxpobraid = models.CharField(db_column='BMXPOBRAID', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxpenderecoobra = models.CharField(db_column='BMXPENDERECOOBRA', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxpcidobra = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='BMXPCIDOBRA', blank=True, null=True)  # Field name made lowercase.
    bmxpcobtipo = models.IntegerField(db_column='BMXPCOBTIPO', blank=True, null=True)  # Field name made lowercase.
    bmxppgtonparc = models.IntegerField(db_column='BMXPPGTONPARC', blank=True, null=True)  # Field name made lowercase.
    bmxppgtoprazost = models.CharField(db_column='BMXPPGTOPRAZOST', max_length=120, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxppgtotipo = models.IntegerField(db_column='BMXPPGTOTIPO', blank=True, null=True)  # Field name made lowercase.
    bmxptipointegracao = models.CharField(db_column='BMXPTIPOINTEGRACAO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxpcno = models.CharField(db_column='BMXPCNO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxpart = models.CharField(db_column='BMXPART', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BMXPEDIDO'


class Bmxproxdocumento(models.Model):
    bmxpdemp = models.IntegerField(db_column='BMXPDEMP', blank=True, null=True)  # Field name made lowercase.
    bmxpdfil = models.IntegerField(db_column='BMXPDFIL', blank=True, null=True)  # Field name made lowercase.
    bmxpdproxdoc = models.CharField(db_column='BMXPDPROXDOC', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxpdlimitedoc = models.CharField(db_column='BMXPDLIMITEDOC', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BMXPROXDOCUMENTO'


class Bmxservico(models.Model):
    bmxsdocumentoid = models.CharField(db_column='BMXSDOCUMENTOID', primary_key=True, max_length=20, db_collation='Latin1_General_CI_AS')  # Field name made lowercase. The composite primary key (BMXSDOCUMENTOID, BMXSSEQ, BMXSNFSERV) found, that is not supported. The first column is selected.
    bmxsseq = models.IntegerField(db_column='BMXSSEQ')  # Field name made lowercase.
    bmxsemp = models.IntegerField(db_column='BMXSEMP')  # Field name made lowercase.
    bmxsfil = models.IntegerField(db_column='BMXSFIL')  # Field name made lowercase.
    bmxscli = models.IntegerField(db_column='BMXSCLI')  # Field name made lowercase.
    bmxspedidoid = models.CharField(db_column='BMXSPEDIDOID', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxsdescricao = models.CharField(db_column='BMXSDESCRICAO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxsestq = models.ForeignKey('Estoque', models.DO_NOTHING, db_column='BMXSESTQ', blank=True, null=True)  # Field name made lowercase.
    bmxsquant = models.FloatField(db_column='BMXSQUANT', blank=True, null=True)  # Field name made lowercase.
    bmxsvlunit = models.FloatField(db_column='BMXSVLUNIT', blank=True, null=True)  # Field name made lowercase.
    bmxstotal = models.FloatField(db_column='BMXSTOTAL', blank=True, null=True)  # Field name made lowercase.
    bmxsquantorig = models.FloatField(db_column='BMXSQUANTORIG', blank=True, null=True)  # Field name made lowercase.
    bmxsvlunitorig = models.FloatField(db_column='BMXSVLUNITORIG', blank=True, null=True)  # Field name made lowercase.
    bmxstotalorig = models.FloatField(db_column='BMXSTOTALORIG', blank=True, null=True)  # Field name made lowercase.
    bmxsnfserv = models.IntegerField(db_column='BMXSNFSERV')  # Field name made lowercase.
    bmxstipointegracao = models.CharField(db_column='BMXSTIPOINTEGRACAO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxsdocumentonum_old = models.CharField(db_column='BMXSDOCUMENTONUM_OLD', max_length=30, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxsdocumentonum = models.CharField(db_column='BMXSDOCUMENTONUM', max_length=30, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bmxsempfat = models.IntegerField(db_column='BMXSEMPFAT', blank=True, null=True)  # Field name made lowercase.
    bmxsfilfat = models.IntegerField(db_column='BMXSFILFAT', blank=True, null=True)  # Field name made lowercase.
    bmxsnfservadic = models.IntegerField(db_column='BMXSNFSERVADIC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BMXSERVICO'
        unique_together = (('bmxsdocumentoid', 'bmxsseq', 'bmxsnfserv'),)


class Boleto(models.Model):
    bolcod = models.IntegerField(db_column='BOLCOD', primary_key=True)  # Field name made lowercase.
    bolemp = models.IntegerField(db_column='BOLEMP', blank=True, null=True)  # Field name made lowercase.
    bolfil = models.IntegerField(db_column='BOLFIL', blank=True, null=True)  # Field name made lowercase.
    boltiporef = models.IntegerField(db_column='BOLTIPOREF', blank=True, null=True)  # Field name made lowercase.
    bolref = models.IntegerField(db_column='BOLREF', blank=True, null=True)  # Field name made lowercase.
    bolsds = models.IntegerField(db_column='BOLSDS', blank=True, null=True)  # Field name made lowercase.
    bolparnum = models.IntegerField(db_column='BOLPARNUM', blank=True, null=True)  # Field name made lowercase.
    bolpartot = models.IntegerField(db_column='BOLPARTOT', blank=True, null=True)  # Field name made lowercase.
    bolsit = models.IntegerField(db_column='BOLSIT', blank=True, null=True)  # Field name made lowercase.
    boldatainc = models.DateTimeField(db_column='BOLDATAINC', blank=True, null=True)  # Field name made lowercase.
    boldatareg = models.DateTimeField(db_column='BOLDATAREG', blank=True, null=True)  # Field name made lowercase.
    boldataliq = models.DateTimeField(db_column='BOLDATALIQ', blank=True, null=True)  # Field name made lowercase.
    boldatabaixa = models.DateTimeField(db_column='BOLDATABAIXA', blank=True, null=True)  # Field name made lowercase.
    bolmsg = models.CharField(db_column='BOLMSG', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bolcr = models.IntegerField(db_column='BOLCR', blank=True, null=True)  # Field name made lowercase.
    bolcli = models.IntegerField(db_column='BOLCLI', blank=True, null=True)  # Field name made lowercase.
    bolban = models.IntegerField(db_column='BOLBAN', blank=True, null=True)  # Field name made lowercase.
    boldatacr = models.DateTimeField(db_column='BOLDATACR', blank=True, null=True)  # Field name made lowercase.
    boldatavenc = models.DateTimeField(db_column='BOLDATAVENC', blank=True, null=True)  # Field name made lowercase.
    bolvalor = models.FloatField(db_column='BOLVALOR', blank=True, null=True)  # Field name made lowercase.
    bolcobnumbanco = models.CharField(db_column='BOLCOBNUMBANCO', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bolidenttit = models.CharField(db_column='BOLIDENTTIT', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bolreftit = models.CharField(db_column='BOLREFTIT', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bolnumremessa = models.IntegerField(db_column='BOLNUMREMESSA', blank=True, null=True)  # Field name made lowercase.
    bolseqenvio = models.IntegerField(db_column='BOLSEQENVIO', blank=True, null=True)  # Field name made lowercase.
    bolcarteira_old = models.CharField(db_column='BOLCARTEIRA_OLD', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bolcarteira = models.CharField(db_column='BOLCARTEIRA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETO'


class Budget(models.Model):
    budcod = models.IntegerField(db_column='BUDCOD', primary_key=True)  # Field name made lowercase.
    budmes = models.DateTimeField(db_column='BUDMES')  # Field name made lowercase.
    budcli = models.IntegerField(db_column='BUDCLI')  # Field name made lowercase.
    budpro = models.IntegerField(db_column='BUDPRO')  # Field name made lowercase.
    buddata = models.DateTimeField(db_column='BUDDATA', blank=True, null=True)  # Field name made lowercase.
    budsit = models.IntegerField(db_column='BUDSIT', blank=True, null=True)  # Field name made lowercase.
    budquant = models.FloatField(db_column='BUDQUANT', blank=True, null=True)  # Field name made lowercase.
    budunit = models.FloatField(db_column='BUDUNIT', blank=True, null=True)  # Field name made lowercase.
    budtotalparc = models.FloatField(db_column='BUDTOTALPARC', blank=True, null=True)  # Field name made lowercase.
    budfrete = models.FloatField(db_column='BUDFRETE', blank=True, null=True)  # Field name made lowercase.
    budfretecusto = models.FloatField(db_column='BUDFRETECUSTO', blank=True, null=True)  # Field name made lowercase.
    budtotal = models.FloatField(db_column='BUDTOTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BUDGET'


class Cadastronis(models.Model):
    cncod = models.IntegerField(db_column='CNCOD', primary_key=True)  # Field name made lowercase.
    cncop = models.ForeignKey('Contratopessoal', models.DO_NOTHING, db_column='CNCOP')  # Field name made lowercase.
    cnfunarq = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='CNFUNARQ', blank=True, null=True)  # Field name made lowercase.
    cndataarq = models.DateTimeField(db_column='CNDATAARQ', blank=True, null=True)  # Field name made lowercase.
    cnnomearq = models.CharField(db_column='CNNOMEARQ', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnarq = models.BinaryField(db_column='CNARQ', blank=True, null=True)  # Field name made lowercase.
    cnsit = models.IntegerField(db_column='CNSIT', blank=True, null=True)  # Field name made lowercase.
    cndataret = models.DateTimeField(db_column='CNDATARET', blank=True, null=True)  # Field name made lowercase.
    cnnisativo = models.CharField(db_column='CNNISATIVO', max_length=11, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnarqret = models.BinaryField(db_column='CNARQRET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CADASTRONIS'


class Cadbanco(models.Model):
    cbancod = models.IntegerField(db_column='CBANCOD', primary_key=True)  # Field name made lowercase.
    cbannome = models.CharField(db_column='CBANNOME', max_length=60, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    cbanapelido = models.CharField(db_column='CBANAPELIDO', max_length=60, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cbanweb = models.CharField(db_column='CBANWEB', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CADBANCO'


class Caddelete(models.Model):
    cdelcadupdate = models.IntegerField(db_column='CDELCADUPDATE', primary_key=True)  # Field name made lowercase.
    cdeltabela = models.CharField(db_column='CDELTABELA', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cdelcod = models.IntegerField(db_column='CDELCOD', blank=True, null=True)  # Field name made lowercase.
    cdeldata = models.DateTimeField(db_column='CDELDATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CADDELETE'


class Calculo(models.Model):
    calcod = models.IntegerField(db_column='CALCOD', primary_key=True)  # Field name made lowercase.
    caltpc = models.ForeignKey('Tipocalculo', models.DO_NOTHING, db_column='CALTPC')  # Field name made lowercase.
    caldatabase = models.DateTimeField(db_column='CALDATABASE', blank=True, null=True)  # Field name made lowercase.
    calsit = models.CharField(db_column='CALSIT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    calusarreplic = models.CharField(db_column='CALUSARREPLIC', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    calemp = models.IntegerField(db_column='CALEMP', blank=True, null=True)  # Field name made lowercase.
    calfil = models.IntegerField(db_column='CALFIL', blank=True, null=True)  # Field name made lowercase.
    caldata1 = models.DateTimeField(db_column='CALDATA1', blank=True, null=True)  # Field name made lowercase.
    caldata2 = models.DateTimeField(db_column='CALDATA2', blank=True, null=True)  # Field name made lowercase.
    caldatapgto = models.DateTimeField(db_column='CALDATAPGTO', blank=True, null=True)  # Field name made lowercase.
    calesidedm = models.CharField(db_column='CALESIDEDM', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALCULO'


class Calculofrete(models.Model):
    cfrecod = models.IntegerField(db_column='CFRECOD', primary_key=True)  # Field name made lowercase.
    cfrenfcod = models.IntegerField(db_column='CFRENFCOD', blank=True, null=True)  # Field name made lowercase.
    cfrecfcod = models.IntegerField(db_column='CFRECFCOD', blank=True, null=True)  # Field name made lowercase.
    cfretipocarga = models.IntegerField(db_column='CFRETIPOCARGA', blank=True, null=True)  # Field name made lowercase.
    cfrenumeixos = models.IntegerField(db_column='CFRENUMEIXOS', blank=True, null=True)  # Field name made lowercase.
    cfredistancia = models.FloatField(db_column='CFREDISTANCIA', blank=True, null=True)  # Field name made lowercase.
    cfreperclotacao = models.FloatField(db_column='CFREPERCLOTACAO', blank=True, null=True)  # Field name made lowercase.
    cfreindice = models.FloatField(db_column='CFREINDICE', blank=True, null=True)  # Field name made lowercase.
    cfrefrete = models.FloatField(db_column='CFREFRETE', blank=True, null=True)  # Field name made lowercase.
    cfrecargadesc = models.FloatField(db_column='CFRECARGADESC', blank=True, null=True)  # Field name made lowercase.
    cfrepedagio = models.FloatField(db_column='CFREPEDAGIO', blank=True, null=True)  # Field name made lowercase.
    cfretotal = models.FloatField(db_column='CFRETOTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALCULOFRETE'


class Cambio(models.Model):
    camcod = models.IntegerField(db_column='CAMCOD', primary_key=True)  # Field name made lowercase.
    cammoe = models.ForeignKey('Moeda', models.DO_NOTHING, db_column='CAMMOE')  # Field name made lowercase.
    camnumero = models.CharField(db_column='CAMNUMERO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    camdatacambio = models.DateTimeField(db_column='CAMDATACAMBIO', blank=True, null=True)  # Field name made lowercase.
    camdatacred = models.DateTimeField(db_column='CAMDATACRED', blank=True, null=True)  # Field name made lowercase.
    camdataconc = models.DateTimeField(db_column='CAMDATACONC', blank=True, null=True)  # Field name made lowercase.
    camantec = models.CharField(db_column='CAMANTEC', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    camobs = models.CharField(db_column='CAMOBS', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cammoevalor = models.FloatField(db_column='CAMMOEVALOR', blank=True, null=True)  # Field name made lowercase.
    cammoecot = models.FloatField(db_column='CAMMOECOT', blank=True, null=True)  # Field name made lowercase.
    cammoecotdespcont = models.FloatField(db_column='CAMMOECOTDESPCONT', blank=True, null=True)  # Field name made lowercase.
    camvalor = models.FloatField(db_column='CAMVALOR', blank=True, null=True)  # Field name made lowercase.
    camdespcontmoe = models.FloatField(db_column='CAMDESPCONTMOE', blank=True, null=True)  # Field name made lowercase.
    camdespcont = models.FloatField(db_column='CAMDESPCONT', blank=True, null=True)  # Field name made lowercase.
    camdespbanqmoe = models.FloatField(db_column='CAMDESPBANQMOE', blank=True, null=True)  # Field name made lowercase.
    camdespbanq = models.FloatField(db_column='CAMDESPBANQ', blank=True, null=True)  # Field name made lowercase.
    camdespiraliq = models.FloatField(db_column='CAMDESPIRALIQ', blank=True, null=True)  # Field name made lowercase.
    camdespirmoe = models.FloatField(db_column='CAMDESPIRMOE', blank=True, null=True)  # Field name made lowercase.
    camdespir = models.FloatField(db_column='CAMDESPIR', blank=True, null=True)  # Field name made lowercase.
    camsit = models.CharField(db_column='CAMSIT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    camban = models.IntegerField(db_column='CAMBAN', blank=True, null=True)  # Field name made lowercase.
    camemp = models.IntegerField(db_column='CAMEMP')  # Field name made lowercase.
    camfil = models.IntegerField(db_column='CAMFIL')  # Field name made lowercase.
    camiofaliq = models.FloatField(db_column='CAMIOFALIQ', blank=True, null=True)  # Field name made lowercase.
    camiofvalor = models.FloatField(db_column='CAMIOFVALOR', blank=True, null=True)  # Field name made lowercase.
    cammoecompvalor = models.FloatField(db_column='CAMMOECOMPVALOR', blank=True, null=True)  # Field name made lowercase.
    cammoecompcot = models.FloatField(db_column='CAMMOECOMPCOT', blank=True, null=True)  # Field name made lowercase.
    camcompvalor = models.FloatField(db_column='CAMCOMPVALOR', blank=True, null=True)  # Field name made lowercase.
    camcli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='CAMCLI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAMBIO'


class Cancnotafiscal(models.Model):
    cnfnfcod = models.IntegerField(db_column='CNFNFCOD', primary_key=True)  # Field name made lowercase.
    cnfjustcanc = models.CharField(db_column='CNFJUSTCANC', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CANCNOTAFISCAL'


class Candidato(models.Model):
    cancod = models.IntegerField(db_column='CANCOD', primary_key=True)  # Field name made lowercase.
    canfor = models.IntegerField(db_column='CANFOR')  # Field name made lowercase.
    candata = models.DateTimeField(db_column='CANDATA', blank=True, null=True)  # Field name made lowercase.
    cansit = models.CharField(db_column='CANSIT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    canproxcont = models.DateTimeField(db_column='CANPROXCONT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CANDIDATO'


class Candidatovaga(models.Model):
    cvagcod = models.IntegerField(db_column='CVAGCOD', primary_key=True)  # Field name made lowercase.
    cvagvag = models.ForeignKey('Vaga', models.DO_NOTHING, db_column='CVAGVAG')  # Field name made lowercase.
    cvagcan = models.ForeignKey(Candidato, models.DO_NOTHING, db_column='CVAGCAN')  # Field name made lowercase.
    cvagobs = models.BinaryField(db_column='CVAGOBS', blank=True, null=True)  # Field name made lowercase.
    cvagsit = models.CharField(db_column='CVAGSIT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CANDIDATOVAGA'


class Carga(models.Model):
    carcod = models.IntegerField(db_column='CARCOD', primary_key=True)  # Field name made lowercase.
    carcli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='CARCLI')  # Field name made lowercase.
    cardata = models.DateTimeField(db_column='CARDATA')  # Field name made lowercase.
    carsnf = models.IntegerField(db_column='CARSNF', blank=True, null=True)  # Field name made lowercase.
    carnf = models.IntegerField(db_column='CARNF', blank=True, null=True)  # Field name made lowercase.
    carquant = models.FloatField(db_column='CARQUANT', blank=True, null=True)  # Field name made lowercase.
    cardatalib = models.DateTimeField(db_column='CARDATALIB', blank=True, null=True)  # Field name made lowercase.
    cartran = models.IntegerField(db_column='CARTRAN', blank=True, null=True)  # Field name made lowercase.
    carplaca = models.CharField(db_column='CARPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carufplaca = models.IntegerField(db_column='CARUFPLACA', blank=True, null=True)  # Field name made lowercase.
    carmotor = models.CharField(db_column='CARMOTOR', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carsit = models.IntegerField(db_column='CARSIT', blank=True, null=True)  # Field name made lowercase.
    carobs = models.BinaryField(db_column='CAROBS', blank=True, null=True)  # Field name made lowercase.
    carcontainer = models.CharField(db_column='CARCONTAINER', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    caremp = models.IntegerField(db_column='CAREMP')  # Field name made lowercase.
    carfil = models.IntegerField(db_column='CARFIL')  # Field name made lowercase.
    carcarbase = models.IntegerField(db_column='CARCARBASE', blank=True, null=True)  # Field name made lowercase.
    caramostra = models.CharField(db_column='CARAMOSTRA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carretorno = models.CharField(db_column='CARRETORNO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carobslib = models.BinaryField(db_column='CAROBSLIB', blank=True, null=True)  # Field name made lowercase.
    carredist = models.CharField(db_column='CARREDIST', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carnfcod = models.IntegerField(db_column='CARNFCOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARGA'


class Cargacomposta(models.Model):
    carccod = models.IntegerField(db_column='CARCCOD', primary_key=True)  # Field name made lowercase.
    carcciddest = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CARCCIDDEST')  # Field name made lowercase.
    carcdesc = models.CharField(db_column='CARCDESC', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carctran = models.IntegerField(db_column='CARCTRAN', blank=True, null=True)  # Field name made lowercase.
    carcplaca = models.CharField(db_column='CARCPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carcplaca1 = models.CharField(db_column='CARCPLACA1', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carcplaca2 = models.CharField(db_column='CARCPLACA2', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carcufplaca = models.IntegerField(db_column='CARCUFPLACA', blank=True, null=True)  # Field name made lowercase.
    carcmot = models.IntegerField(db_column='CARCMOT', blank=True, null=True)  # Field name made lowercase.
    carcplaca3 = models.CharField(db_column='CARCPLACA3', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARGACOMPOSTA'


class Cargafrac(models.Model):
    carfcod = models.IntegerField(db_column='CARFCOD', primary_key=True)  # Field name made lowercase.
    carfemp = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='CARFEMP')  # Field name made lowercase.
    carffil = models.IntegerField(db_column='CARFFIL')  # Field name made lowercase.
    carfciddest = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CARFCIDDEST')  # Field name made lowercase.
    carfdesc = models.CharField(db_column='CARFDESC', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carftran = models.IntegerField(db_column='CARFTRAN', blank=True, null=True)  # Field name made lowercase.
    carfplaca = models.CharField(db_column='CARFPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carfplaca1 = models.CharField(db_column='CARFPLACA1', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carfplaca2 = models.CharField(db_column='CARFPLACA2', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carfplaca3 = models.CharField(db_column='CARFPLACA3', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carfmot = models.IntegerField(db_column='CARFMOT', blank=True, null=True)  # Field name made lowercase.
    carfdata = models.DateTimeField(db_column='CARFDATA', blank=True, null=True)  # Field name made lowercase.
    carfsit = models.IntegerField(db_column='CARFSIT', blank=True, null=True)  # Field name made lowercase.
    carftveic = models.IntegerField(db_column='CARFTVEIC', blank=True, null=True)  # Field name made lowercase.
    carfbaltara = models.IntegerField(db_column='CARFBALTARA', blank=True, null=True)  # Field name made lowercase.
    carftara = models.FloatField(db_column='CARFTARA', blank=True, null=True)  # Field name made lowercase.
    carfbalbruto = models.IntegerField(db_column='CARFBALBRUTO', blank=True, null=True)  # Field name made lowercase.
    carfbruto = models.FloatField(db_column='CARFBRUTO', blank=True, null=True)  # Field name made lowercase.
    carftpcarf = models.ForeignKey('Tipocargafrac', models.DO_NOTHING, db_column='CARFTPCARF', blank=True, null=True)  # Field name made lowercase.
    carfbalfunautesp = models.IntegerField(db_column='CARFBALFUNAUTESP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARGAFRAC'


class Centcodigo(models.Model):
    ccodemp = models.IntegerField(db_column='CCODEMP', blank=True, null=True)  # Field name made lowercase.
    ccodfil = models.IntegerField(db_column='CCODFIL', blank=True, null=True)  # Field name made lowercase.
    ccodtabela = models.CharField(db_column='CCODTABELA', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccodchave = models.CharField(db_column='CCODCHAVE', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccodcod = models.IntegerField(db_column='CCODCOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTCODIGO'


class Centpedido(models.Model):
    centpped = models.OneToOneField('Pedido', models.DO_NOTHING, db_column='CENTPPED', primary_key=True)  # Field name made lowercase. The composite primary key (CENTPPED, CENTPEMP, CENTPFIL) found, that is not supported. The first column is selected.
    centpemp = models.IntegerField(db_column='CENTPEMP')  # Field name made lowercase.
    centpfil = models.IntegerField(db_column='CENTPFIL')  # Field name made lowercase.
    centpident = models.CharField(db_column='CENTPIDENT', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    centpinfo = models.BinaryField(db_column='CENTPINFO', blank=True, null=True)  # Field name made lowercase.
    centpbloq = models.CharField(db_column='CENTPBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTPEDIDO'
        unique_together = (('centpped', 'centpemp', 'centpfil'),)


class Centralhv(models.Model):
    chvcod = models.IntegerField(db_column='CHVCOD', primary_key=True)  # Field name made lowercase.
    chveqp = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='CHVEQP')  # Field name made lowercase.
    chvfunresp = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='CHVFUNRESP')  # Field name made lowercase.
    chvdata = models.DateTimeField(db_column='CHVDATA', blank=True, null=True)  # Field name made lowercase.
    chvflhorim = models.CharField(db_column='CHVFLHORIM', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chvflveloc = models.CharField(db_column='CHVFLVELOC', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chvhorim = models.IntegerField(db_column='CHVHORIM', blank=True, null=True)  # Field name made lowercase.
    chvveloc = models.IntegerField(db_column='CHVVELOC', blank=True, null=True)  # Field name made lowercase.
    chvhrper = models.FloatField(db_column='CHVHRPER', blank=True, null=True)  # Field name made lowercase.
    chvkmper = models.FloatField(db_column='CHVKMPER', blank=True, null=True)  # Field name made lowercase.
    chvhrtot = models.FloatField(db_column='CHVHRTOT', blank=True, null=True)  # Field name made lowercase.
    chvkmtot = models.FloatField(db_column='CHVKMTOT', blank=True, null=True)  # Field name made lowercase.
    chvchvacoplado = models.ForeignKey('self', models.DO_NOTHING, db_column='CHVCHVACOPLADO', blank=True, null=True)  # Field name made lowercase.
    chvrefinteg = models.CharField(db_column='CHVREFINTEG', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTRALHV'


class Centralizacao(models.Model):
    centemp = models.IntegerField(db_column='CENTEMP', blank=True, null=True)  # Field name made lowercase.
    centfil = models.IntegerField(db_column='CENTFIL', blank=True, null=True)  # Field name made lowercase.
    centestrutura = models.IntegerField(db_column='CENTESTRUTURA', blank=True, null=True)  # Field name made lowercase.
    centtran = models.IntegerField(db_column='CENTTRAN', blank=True, null=True)  # Field name made lowercase.
    centcli = models.IntegerField(db_column='CENTCLI', blank=True, null=True)  # Field name made lowercase.
    centped = models.IntegerField(db_column='CENTPED', blank=True, null=True)  # Field name made lowercase.
    centultchave = models.IntegerField(db_column='CENTULTCHAVE', blank=True, null=True)  # Field name made lowercase.
    centtped = models.IntegerField(db_column='CENTTPED', blank=True, null=True)  # Field name made lowercase.
    centecli = models.IntegerField(db_column='CENTECLI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTRALIZACAO'


class Centralizacaocontareceber(models.Model):
    ccremp = models.IntegerField(db_column='CCREMP')  # Field name made lowercase.
    ccrfil = models.IntegerField(db_column='CCRFIL')  # Field name made lowercase.
    ccrcr = models.IntegerField(db_column='CCRCR')  # Field name made lowercase.
    ccrnfcod = models.IntegerField(db_column='CCRNFCOD')  # Field name made lowercase.
    ccrparnum = models.IntegerField(db_column='CCRPARNUM')  # Field name made lowercase.
    ccrvalor = models.FloatField(db_column='CCRVALOR', blank=True, null=True)  # Field name made lowercase.
    ccrvenc = models.DateTimeField(db_column='CCRVENC', blank=True, null=True)  # Field name made lowercase.
    ccrliq = models.DateTimeField(db_column='CCRLIQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTRALIZACAOCONTARECEBER'


class Centrocusto(models.Model):
    cccod = models.IntegerField(db_column='CCCOD', primary_key=True)  # Field name made lowercase.
    ccccpai = models.IntegerField(db_column='CCCCPAI')  # Field name made lowercase.
    cctemfilho = models.CharField(db_column='CCTEMFILHO', max_length=1, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    ccresumoparc = models.CharField(db_column='CCRESUMOPARC', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccctcusto = models.CharField(db_column='CCCTCUSTO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccctservpf = models.CharField(db_column='CCCTSERVPF', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccctservpj = models.CharField(db_column='CCCTSERVPJ', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cchpbaixa = models.IntegerField(db_column='CCHPBAIXA', blank=True, null=True)  # Field name made lowercase.
    ccsigla = models.CharField(db_column='CCSIGLA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccimobsn = models.CharField(db_column='CCIMOBSN', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cccai = models.IntegerField(db_column='CCCAI', blank=True, null=True)  # Field name made lowercase.
    ccbai = models.IntegerField(db_column='CCBAI', blank=True, null=True)  # Field name made lowercase.
    ccindivcp = models.CharField(db_column='CCINDIVCP', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccstordem = models.CharField(db_column='CCSTORDEM', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccdistribsn = models.CharField(db_column='CCDISTRIBSN', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccbloq = models.CharField(db_column='CCBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cceqpchv = models.IntegerField(db_column='CCEQPCHV', blank=True, null=True)  # Field name made lowercase.
    cccustopublico = models.CharField(db_column='CCCUSTOPUBLICO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccexigirplaca = models.CharField(db_column='CCEXIGIRPLACA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccrepasse = models.CharField(db_column='CCREPASSE', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccnivel = models.IntegerField(db_column='CCNIVEL', blank=True, null=True)  # Field name made lowercase.
    ccstcod = models.CharField(db_column='CCSTCOD', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccexigircf = models.CharField(db_column='CCEXIGIRCF', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccccefd = models.IntegerField(db_column='CCCCEFD', blank=True, null=True)  # Field name made lowercase.
    cccomp = models.CharField(db_column='CCCOMP', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccccref = models.IntegerField(db_column='CCCCREF', blank=True, null=True)  # Field name made lowercase.
    ccrefersn = models.CharField(db_column='CCREFERSN', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccemp_old = models.IntegerField(db_column='CCEMP_OLD', blank=True, null=True)  # Field name made lowercase.
    ccfil_old = models.IntegerField(db_column='CCFIL_OLD', blank=True, null=True)  # Field name made lowercase.
    ccobs = models.BinaryField(db_column='CCOBS', blank=True, null=True)  # Field name made lowercase.
    ccbcom = models.ForeignKey(Basecompra, models.DO_NOTHING, db_column='CCBCOM', blank=True, null=True)  # Field name made lowercase.
    ccidexterno = models.CharField(db_column='CCIDEXTERNO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccinformacoes = models.BinaryField(db_column='CCINFORMACOES', blank=True, null=True)  # Field name made lowercase.
    ccnome_old = models.CharField(db_column='CCNOME_OLD', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccnome = models.CharField(db_column='CCNOME', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccnomeing = models.CharField(db_column='CCNOMEING', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccseq = models.IntegerField(db_column='CCSEQ', blank=True, null=True)  # Field name made lowercase.
    cccomp3 = models.CharField(db_column='CCCOMP3', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccresponsavel = models.IntegerField(db_column='CCRESPONSAVEL', blank=True, null=True)  # Field name made lowercase.
    ccautinvestimento = models.CharField(db_column='CCAUTINVESTIMENTO', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccabertura = models.DateTimeField(db_column='CCABERTURA', blank=True, null=True)  # Field name made lowercase.
    ccencerramento = models.DateTimeField(db_column='CCENCERRAMENTO', blank=True, null=True)  # Field name made lowercase.
    ccnaopermapliccusto = models.CharField(db_column='CCNAOPERMAPLICCUSTO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccnaopermaloceqp = models.CharField(db_column='CCNAOPERMALOCEQP', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cccompcod = models.IntegerField(db_column='CCCOMPCOD', blank=True, null=True)  # Field name made lowercase.
    ccidexternocod = models.IntegerField(db_column='CCIDEXTERNOCOD', blank=True, null=True)  # Field name made lowercase.
    cccompcod3 = models.IntegerField(db_column='CCCOMPCOD3', blank=True, null=True)  # Field name made lowercase.
    ccexigirbpro = models.CharField(db_column='CCEXIGIRBPRO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccnaoexigirospcom = models.CharField(db_column='CCNAOEXIGIROSPCOM', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cccompcod4 = models.IntegerField(db_column='CCCOMPCOD4', blank=True, null=True)  # Field name made lowercase.
    cccompcod5 = models.IntegerField(db_column='CCCOMPCOD5', blank=True, null=True)  # Field name made lowercase.
    cccompcod6 = models.IntegerField(db_column='CCCOMPCOD6', blank=True, null=True)  # Field name made lowercase.
    ccnomecomp = models.CharField(db_column='CCNOMECOMP', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTROCUSTO'


class Centrocustoempfil(models.Model):
    ccefcc = models.OneToOneField(Centrocusto, models.DO_NOTHING, db_column='CCEFCC', primary_key=True)  # Field name made lowercase. The composite primary key (CCEFCC, CCEFEMP, CCEFFIL) found, that is not supported. The first column is selected.
    ccefemp = models.IntegerField(db_column='CCEFEMP')  # Field name made lowercase.
    cceffil = models.IntegerField(db_column='CCEFFIL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTROCUSTOEMPFIL'
        unique_together = (('ccefcc', 'ccefemp', 'cceffil'),)


class Centrocustoempfildados(models.Model):
    ccefdcc = models.OneToOneField(Centrocusto, models.DO_NOTHING, db_column='CCEFDCC', primary_key=True)  # Field name made lowercase. The composite primary key (CCEFDCC, CCEFDEMP, CCEFDFIL) found, that is not supported. The first column is selected.
    ccefdemp = models.IntegerField(db_column='CCEFDEMP')  # Field name made lowercase.
    ccefdfil = models.IntegerField(db_column='CCEFDFIL')  # Field name made lowercase.
    ccefdregfpemp = models.IntegerField(db_column='CCEFDREGFPEMP')  # Field name made lowercase.
    ccefdregfpfil = models.IntegerField(db_column='CCEFDREGFPFIL')  # Field name made lowercase.
    ccefdloc = models.IntegerField(db_column='CCEFDLOC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTROCUSTOEMPFILDADOS'
        unique_together = (('ccefdcc', 'ccefdemp', 'ccefdfil'),)


class Centrocustoequipamento(models.Model):
    ccecod = models.IntegerField(db_column='CCECOD', primary_key=True)  # Field name made lowercase.
    cceeqp = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='CCEEQP')  # Field name made lowercase.
    ccedata = models.DateTimeField(db_column='CCEDATA', blank=True, null=True)  # Field name made lowercase.
    ccecc = models.IntegerField(db_column='CCECC', blank=True, null=True)  # Field name made lowercase.
    ccehorim = models.IntegerField(db_column='CCEHORIM', blank=True, null=True)  # Field name made lowercase.
    cceveloc = models.IntegerField(db_column='CCEVELOC', blank=True, null=True)  # Field name made lowercase.
    cceobs = models.CharField(db_column='CCEOBS', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccechv = models.IntegerField(db_column='CCECHV', blank=True, null=True)  # Field name made lowercase.
    cceemp = models.IntegerField(db_column='CCEEMP', blank=True, null=True)  # Field name made lowercase.
    ccefil = models.IntegerField(db_column='CCEFIL', blank=True, null=True)  # Field name made lowercase.
    cceinf = models.ForeignKey('Itemnotafiscal', models.DO_NOTHING, db_column='CCEINF', blank=True, null=True)  # Field name made lowercase.
    cceinfe = models.ForeignKey('Itemnotafiscalentrada', models.DO_NOTHING, db_column='CCEINFE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTROCUSTOEQUIPAMENTO'


class Centrocustofun(models.Model):
    ccfcc = models.IntegerField(db_column='CCFCC', blank=True, null=True)  # Field name made lowercase.
    ccffun = models.IntegerField(db_column='CCFFUN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTROCUSTOFUN'


class Centrocustogerencial(models.Model):
    ccgcod = models.IntegerField(db_column='CCGCOD', primary_key=True)  # Field name made lowercase.
    ccggccg = models.ForeignKey('Grupocentrocustogerencial', models.DO_NOTHING, db_column='CCGGCCG')  # Field name made lowercase.
    ccgccgpai = models.IntegerField(db_column='CCGCCGPAI')  # Field name made lowercase.
    ccgtemfilho = models.CharField(db_column='CCGTEMFILHO', max_length=1, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    ccgstordem = models.CharField(db_column='CCGSTORDEM', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcustoom = models.IntegerField(db_column='CCGCUSTOOM', blank=True, null=True)  # Field name made lowercase.
    ccgcustooa = models.IntegerField(db_column='CCGCUSTOOA', blank=True, null=True)  # Field name made lowercase.
    ccgcustor = models.IntegerField(db_column='CCGCUSTOR', blank=True, null=True)  # Field name made lowercase.
    ccgcustoominfo = models.BinaryField(db_column='CCGCUSTOOMINFO', blank=True, null=True)  # Field name made lowercase.
    ccgcustooainfo = models.BinaryField(db_column='CCGCUSTOOAINFO', blank=True, null=True)  # Field name made lowercase.
    ccgcustorinfo = models.BinaryField(db_column='CCGCUSTORINFO', blank=True, null=True)  # Field name made lowercase.
    ccgprodom = models.IntegerField(db_column='CCGPRODOM', blank=True, null=True)  # Field name made lowercase.
    ccgprodoa = models.IntegerField(db_column='CCGPRODOA', blank=True, null=True)  # Field name made lowercase.
    ccgprodr = models.IntegerField(db_column='CCGPRODR', blank=True, null=True)  # Field name made lowercase.
    ccgprodominfo = models.BinaryField(db_column='CCGPRODOMINFO', blank=True, null=True)  # Field name made lowercase.
    ccgprodoainfo = models.BinaryField(db_column='CCGPRODOAINFO', blank=True, null=True)  # Field name made lowercase.
    ccgprodrinfo = models.BinaryField(db_column='CCGPRODRINFO', blank=True, null=True)  # Field name made lowercase.
    ccgprodesp = models.IntegerField(db_column='CCGPRODESP', blank=True, null=True)  # Field name made lowercase.
    ccghrom = models.IntegerField(db_column='CCGHROM', blank=True, null=True)  # Field name made lowercase.
    ccghroa = models.IntegerField(db_column='CCGHROA', blank=True, null=True)  # Field name made lowercase.
    ccghrr = models.IntegerField(db_column='CCGHRR', blank=True, null=True)  # Field name made lowercase.
    ccghrominfo = models.BinaryField(db_column='CCGHROMINFO', blank=True, null=True)  # Field name made lowercase.
    ccghroainfo = models.BinaryField(db_column='CCGHROAINFO', blank=True, null=True)  # Field name made lowercase.
    ccghrrinfo = models.BinaryField(db_column='CCGHRRINFO', blank=True, null=True)  # Field name made lowercase.
    ccgkmom = models.IntegerField(db_column='CCGKMOM', blank=True, null=True)  # Field name made lowercase.
    ccgkmoa = models.IntegerField(db_column='CCGKMOA', blank=True, null=True)  # Field name made lowercase.
    ccgkmr = models.IntegerField(db_column='CCGKMR', blank=True, null=True)  # Field name made lowercase.
    ccgkmominfo = models.BinaryField(db_column='CCGKMOMINFO', blank=True, null=True)  # Field name made lowercase.
    ccgkmoainfo = models.BinaryField(db_column='CCGKMOAINFO', blank=True, null=True)  # Field name made lowercase.
    ccgkmrinfo = models.BinaryField(db_column='CCGKMRINFO', blank=True, null=True)  # Field name made lowercase.
    ccgnegrito = models.CharField(db_column='CCGNEGRITO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgvendaom = models.IntegerField(db_column='CCGVENDAOM', blank=True, null=True)  # Field name made lowercase.
    ccgvendaoa = models.IntegerField(db_column='CCGVENDAOA', blank=True, null=True)  # Field name made lowercase.
    ccgvendar = models.IntegerField(db_column='CCGVENDAR', blank=True, null=True)  # Field name made lowercase.
    ccgvendaominfo = models.BinaryField(db_column='CCGVENDAOMINFO', blank=True, null=True)  # Field name made lowercase.
    ccgvendaoainfo = models.BinaryField(db_column='CCGVENDAOAINFO', blank=True, null=True)  # Field name made lowercase.
    ccgvendarinfo = models.BinaryField(db_column='CCGVENDARINFO', blank=True, null=True)  # Field name made lowercase.
    ccgreceitaom = models.IntegerField(db_column='CCGRECEITAOM', blank=True, null=True)  # Field name made lowercase.
    ccgreceitaoa = models.IntegerField(db_column='CCGRECEITAOA', blank=True, null=True)  # Field name made lowercase.
    ccgreceitar = models.IntegerField(db_column='CCGRECEITAR', blank=True, null=True)  # Field name made lowercase.
    ccgreceitaominfo = models.BinaryField(db_column='CCGRECEITAOMINFO', blank=True, null=True)  # Field name made lowercase.
    ccgreceitaoainfo = models.BinaryField(db_column='CCGRECEITAOAINFO', blank=True, null=True)  # Field name made lowercase.
    ccgreceitarinfo = models.BinaryField(db_column='CCGRECEITARINFO', blank=True, null=True)  # Field name made lowercase.
    ccgoperacao = models.CharField(db_column='CCGOPERACAO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgemp = models.IntegerField(db_column='CCGEMP', blank=True, null=True)  # Field name made lowercase.
    ccgfil = models.IntegerField(db_column='CCGFIL', blank=True, null=True)  # Field name made lowercase.
    ccgprefixo = models.CharField(db_column='CCGPREFIXO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgsufixo = models.CharField(db_column='CCGSUFIXO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgprioridade = models.IntegerField(db_column='CCGPRIORIDADE', blank=True, null=True)  # Field name made lowercase.
    ccgccmatriz = models.IntegerField(db_column='CCGCCMATRIZ', blank=True, null=True)  # Field name made lowercase.
    ccgnomematriz = models.CharField(db_column='CCGNOMEMATRIZ', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgccref = models.IntegerField(db_column='CCGCCREF', blank=True, null=True)  # Field name made lowercase.
    ccgccgref = models.IntegerField(db_column='CCGCCGREF', blank=True, null=True)  # Field name made lowercase.
    ccgsinal = models.CharField(db_column='CCGSINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgvendaoriginal = models.CharField(db_column='CCGVENDAORIGINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgreceitaoriginal = models.CharField(db_column='CCGRECEITAORIGINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcustooriginal = models.CharField(db_column='CCGCUSTOORIGINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgprodoriginal = models.CharField(db_column='CCGPRODORIGINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccghroriginal = models.CharField(db_column='CCGHRORIGINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgkmoriginal = models.CharField(db_column='CCGKMORIGINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcentralizado = models.CharField(db_column='CCGCENTRALIZADO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgarred = models.IntegerField(db_column='CCGARRED', blank=True, null=True)  # Field name made lowercase.
    ccgabrang = models.IntegerField(db_column='CCGABRANG', blank=True, null=True)  # Field name made lowercase.
    ccgtodasemp_old = models.CharField(db_column='CCGTODASEMP_OLD', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgquandoemp_old = models.CharField(db_column='CCGQUANDOEMP_OLD', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgsempreemp_old = models.CharField(db_column='CCGSEMPREEMP_OLD', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgsaltarpag = models.CharField(db_column='CCGSALTARPAG', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgsaltarlin = models.CharField(db_column='CCGSALTARLIN', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgbasecent = models.CharField(db_column='CCGBASECENT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcodcopia = models.IntegerField(db_column='CCGCODCOPIA', blank=True, null=True)  # Field name made lowercase.
    ccgnaoatmatriz = models.CharField(db_column='CCGNAOATMATRIZ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgnomealt = models.CharField(db_column='CCGNOMEALT', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgom = models.IntegerField(db_column='CCGOM', blank=True, null=True)  # Field name made lowercase.
    ccgoa = models.IntegerField(db_column='CCGOA', blank=True, null=True)  # Field name made lowercase.
    ccgr = models.IntegerField(db_column='CCGR', blank=True, null=True)  # Field name made lowercase.
    ccgominfo = models.BinaryField(db_column='CCGOMINFO', blank=True, null=True)  # Field name made lowercase.
    ccgoainfo = models.BinaryField(db_column='CCGOAINFO', blank=True, null=True)  # Field name made lowercase.
    ccgrinfo = models.BinaryField(db_column='CCGRINFO', blank=True, null=True)  # Field name made lowercase.
    ccgoriginal = models.CharField(db_column='CCGORIGINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgnome_old = models.CharField(db_column='CCGNOME_OLD', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgnome = models.CharField(db_column='CCGNOME', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcontnatpadrao = models.CharField(db_column='CCGCONTNATPADRAO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcontnatfisc = models.CharField(db_column='CCGCONTNATFISC', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcontnatecon = models.CharField(db_column='CCGCONTNATECON', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgbloq = models.CharField(db_column='CCGBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcalcprimdia = models.CharField(db_column='CCGCALCPRIMDIA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgnaocritdup = models.CharField(db_column='CCGNAOCRITDUP', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgnaocalcprimdia = models.CharField(db_column='CCGNAOCALCPRIMDIA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgnaotot = models.CharField(db_column='CCGNAOTOT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcalcultdia = models.CharField(db_column='CCGCALCULTDIA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgnaocalcultdia = models.CharField(db_column='CCGNAOCALCULTDIA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgdesc = models.BinaryField(db_column='CCGDESC', blank=True, null=True)  # Field name made lowercase.
    ccginvopcao = models.IntegerField(db_column='CCGINVOPCAO', blank=True, null=True)  # Field name made lowercase.
    ccginvtipo = models.IntegerField(db_column='CCGINVTIPO', blank=True, null=True)  # Field name made lowercase.
    ccginvref = models.IntegerField(db_column='CCGINVREF', blank=True, null=True)  # Field name made lowercase.
    ccginvestq = models.ForeignKey('Estoque', models.DO_NOTHING, db_column='CCGINVESTQ', blank=True, null=True)  # Field name made lowercase.
    ccgrecalctot = models.CharField(db_column='CCGRECALCTOT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgintegrar = models.CharField(db_column='CCGINTEGRAR', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcompl_ant = models.CharField(db_column='CCGCOMPL_ANT', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcompl = models.CharField(db_column='CCGCOMPL', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcompl2_ant = models.CharField(db_column='CCGCOMPL2_ANT', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcompl2 = models.CharField(db_column='CCGCOMPL2', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcompl3_ant = models.CharField(db_column='CCGCOMPL3_ANT', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcompl3 = models.CharField(db_column='CCGCOMPL3', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccgcontnatorca = models.CharField(db_column='CCGCONTNATORCA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTROCUSTOGERENCIAL'


class Centservidor(models.Model):
    cscod = models.IntegerField(db_column='CSCOD', primary_key=True)  # Field name made lowercase.
    csbase = models.IntegerField(db_column='CSBASE', blank=True, null=True)  # Field name made lowercase.
    csdata = models.DateTimeField(db_column='CSDATA', blank=True, null=True)  # Field name made lowercase.
    csnometabela = models.CharField(db_column='CSNOMETABELA', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csnomechave = models.CharField(db_column='CSNOMECHAVE', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csnomechave2 = models.CharField(db_column='CSNOMECHAVE2', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csnomechave3 = models.CharField(db_column='CSNOMECHAVE3', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csnomechave4 = models.CharField(db_column='CSNOMECHAVE4', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cschave = models.IntegerField(db_column='CSCHAVE', blank=True, null=True)  # Field name made lowercase.
    cschave2 = models.IntegerField(db_column='CSCHAVE2', blank=True, null=True)  # Field name made lowercase.
    cschave3 = models.IntegerField(db_column='CSCHAVE3', blank=True, null=True)  # Field name made lowercase.
    cschave4 = models.IntegerField(db_column='CSCHAVE4', blank=True, null=True)  # Field name made lowercase.
    cschavest = models.CharField(db_column='CSCHAVEST', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csxml = models.BinaryField(db_column='CSXML', blank=True, null=True)  # Field name made lowercase.
    cssit = models.IntegerField(db_column='CSSIT', blank=True, null=True)  # Field name made lowercase.
    csmsg = models.CharField(db_column='CSMSG', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csemp = models.IntegerField(db_column='CSEMP', blank=True, null=True)  # Field name made lowercase.
    csfil = models.IntegerField(db_column='CSFIL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTSERVIDOR'


class Centservidorbases(models.Model):
    csbbase = models.IntegerField(db_column='CSBBASE', blank=True, null=True)  # Field name made lowercase.
    csbsga = models.CharField(db_column='CSBSGA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CENTSERVIDORBASES'


class Certificado(models.Model):
    certcod = models.IntegerField(db_column='CERTCOD', primary_key=True)  # Field name made lowercase.
    certnome = models.CharField(db_column='CERTNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    certatdata = models.DateTimeField(db_column='CERTATDATA', blank=True, null=True)  # Field name made lowercase.
    certtexto = models.BinaryField(db_column='CERTTEXTO', blank=True, null=True)  # Field name made lowercase.
    certcli = models.IntegerField(db_column='CERTCLI', blank=True, null=True)  # Field name made lowercase.
    certmultpro = models.CharField(db_column='CERTMULTPRO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    certestq = models.IntegerField(db_column='CERTESTQ', blank=True, null=True)  # Field name made lowercase.
    certpro_old = models.IntegerField(db_column='CERTPRO_OLD', blank=True, null=True)  # Field name made lowercase.
    certcertref = models.IntegerField(db_column='CERTCERTREF', blank=True, null=True)  # Field name made lowercase.
    certbloq = models.CharField(db_column='CERTBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CERTIFICADO'


class Cfdocumento(models.Model):
    cfdcfcod = models.IntegerField(db_column='CFDCFCOD')  # Field name made lowercase.
    cfdmodelo = models.IntegerField(db_column='CFDMODELO', blank=True, null=True)  # Field name made lowercase.
    cfdchavenfe = models.CharField(db_column='CFDCHAVENFE', max_length=44, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfdsds = models.IntegerField(db_column='CFDSDS', blank=True, null=True)  # Field name made lowercase.
    cfdserie = models.CharField(db_column='CFDSERIE', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfdnumero = models.IntegerField(db_column='CFDNUMERO', blank=True, null=True)  # Field name made lowercase.
    cfdemissao = models.DateTimeField(db_column='CFDEMISSAO', blank=True, null=True)  # Field name made lowercase.
    cfdicmsbase = models.FloatField(db_column='CFDICMSBASE', blank=True, null=True)  # Field name made lowercase.
    cfdicmsvalor = models.FloatField(db_column='CFDICMSVALOR', blank=True, null=True)  # Field name made lowercase.
    cfdicmsstbase = models.FloatField(db_column='CFDICMSSTBASE', blank=True, null=True)  # Field name made lowercase.
    cfdicmsstvalor = models.FloatField(db_column='CFDICMSSTVALOR', blank=True, null=True)  # Field name made lowercase.
    cfdtotalpro = models.FloatField(db_column='CFDTOTALPRO', blank=True, null=True)  # Field name made lowercase.
    cfdtotalnf = models.FloatField(db_column='CFDTOTALNF', blank=True, null=True)  # Field name made lowercase.
    cfdcfop = models.IntegerField(db_column='CFDCFOP', blank=True, null=True)  # Field name made lowercase.
    cfdpeso = models.FloatField(db_column='CFDPESO', blank=True, null=True)  # Field name made lowercase.
    cfdromaneio = models.CharField(db_column='CFDROMANEIO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfdpedido = models.CharField(db_column='CFDPEDIDO', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfdaplic = models.IntegerField(db_column='CFDAPLIC', blank=True, null=True)  # Field name made lowercase.
    cfdncm = models.CharField(db_column='CFDNCM', max_length=12, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFDOCUMENTO'


class Cffracionado(models.Model):
    cffcfcod = models.IntegerField(db_column='CFFCFCOD', primary_key=True)  # Field name made lowercase.
    cffquant = models.FloatField(db_column='CFFQUANT', blank=True, null=True)  # Field name made lowercase.
    cffpeso = models.FloatField(db_column='CFFPESO', blank=True, null=True)  # Field name made lowercase.
    cffcomp = models.FloatField(db_column='CFFCOMP', blank=True, null=True)  # Field name made lowercase.
    cffadvalorem = models.FloatField(db_column='CFFADVALOREM', blank=True, null=True)  # Field name made lowercase.
    cffadvaloremorig = models.FloatField(db_column='CFFADVALOREMORIG', blank=True, null=True)  # Field name made lowercase.
    cfffretepeso = models.FloatField(db_column='CFFFRETEPESO', blank=True, null=True)  # Field name made lowercase.
    cfffretepesoorig = models.FloatField(db_column='CFFFRETEPESOORIG', blank=True, null=True)  # Field name made lowercase.
    cfftaxa1 = models.FloatField(db_column='CFFTAXA1', blank=True, null=True)  # Field name made lowercase.
    cfftaxa1orig = models.FloatField(db_column='CFFTAXA1ORIG', blank=True, null=True)  # Field name made lowercase.
    cfftaxa2 = models.FloatField(db_column='CFFTAXA2', blank=True, null=True)  # Field name made lowercase.
    cfftaxa2orig = models.FloatField(db_column='CFFTAXA2ORIG', blank=True, null=True)  # Field name made lowercase.
    cffcoleta = models.FloatField(db_column='CFFCOLETA', blank=True, null=True)  # Field name made lowercase.
    cffcoletaorig = models.FloatField(db_column='CFFCOLETAORIG', blank=True, null=True)  # Field name made lowercase.
    cffentrega = models.FloatField(db_column='CFFENTREGA', blank=True, null=True)  # Field name made lowercase.
    cffentregaorig = models.FloatField(db_column='CFFENTREGAORIG', blank=True, null=True)  # Field name made lowercase.
    cffcoletar = models.CharField(db_column='CFFCOLETAR', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cffentregar = models.CharField(db_column='CFFENTREGAR', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFFRACIONADO'


class Cfgequipamento(models.Model):
    ceqcod = models.IntegerField(db_column='CEQCOD', primary_key=True)  # Field name made lowercase.
    ceqnome = models.CharField(db_column='CEQNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    ceqeqp = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='CEQEQP')  # Field name made lowercase.
    ceqbloqsn = models.CharField(db_column='CEQBLOQSN', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ceqmetaprod = models.FloatField(db_column='CEQMETAPROD', blank=True, null=True)  # Field name made lowercase.
    ceqtipoalt = models.IntegerField(db_column='CEQTIPOALT', blank=True, null=True)  # Field name made lowercase.
    ceqpercalt = models.FloatField(db_column='CEQPERCALT', blank=True, null=True)  # Field name made lowercase.
    ceqorigem = models.IntegerField(db_column='CEQORIGEM', blank=True, null=True)  # Field name made lowercase.
    ceqquanthr = models.FloatField(db_column='CEQQUANTHR', blank=True, null=True)  # Field name made lowercase.
    ceqquantperda = models.CharField(db_column='CEQQUANTPERDA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ceqopcao = models.IntegerField(db_column='CEQOPCAO', blank=True, null=True)  # Field name made lowercase.
    ceqnaoretdprdest = models.CharField(db_column='CEQNAORETDPRDEST', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFGEQUIPAMENTO'


class Cfgitemcfgequipamento(models.Model):
    ciceqcod = models.IntegerField(db_column='CICEQCOD', primary_key=True)  # Field name made lowercase.
    ciceqiceq = models.ForeignKey('Itemcfgequipamento', models.DO_NOTHING, db_column='CICEQICEQ')  # Field name made lowercase.
    ciceqceq = models.IntegerField(db_column='CICEQCEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFGITEMCFGEQUIPAMENTO'


class Cfviagem(models.Model):
    cfvcod = models.IntegerField(db_column='CFVCOD', primary_key=True)  # Field name made lowercase.
    cfvplaca = models.CharField(db_column='CFVPLACA', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfvmot = models.ForeignKey('Motorista', models.DO_NOTHING, db_column='CFVMOT', blank=True, null=True)  # Field name made lowercase.
    cfveqp = models.IntegerField(db_column='CFVEQP', blank=True, null=True)  # Field name made lowercase.
    cfvdatainic = models.DateTimeField(db_column='CFVDATAINIC', blank=True, null=True)  # Field name made lowercase.
    cfvdatafim = models.DateTimeField(db_column='CFVDATAFIM', blank=True, null=True)  # Field name made lowercase.
    cfvsit = models.IntegerField(db_column='CFVSIT', blank=True, null=True)  # Field name made lowercase.
    cfvadiant = models.FloatField(db_column='CFVADIANT', blank=True, null=True)  # Field name made lowercase.
    cfvreceb = models.FloatField(db_column='CFVRECEB', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa = models.FloatField(db_column='CFVDESPESA', blank=True, null=True)  # Field name made lowercase.
    cfvdesplanc = models.FloatField(db_column='CFVDESPLANC', blank=True, null=True)  # Field name made lowercase.
    cfvdiaria = models.FloatField(db_column='CFVDIARIA', blank=True, null=True)  # Field name made lowercase.
    cfvpedagio = models.FloatField(db_column='CFVPEDAGIO', blank=True, null=True)  # Field name made lowercase.
    cfvapagar = models.FloatField(db_column='CFVAPAGAR', blank=True, null=True)  # Field name made lowercase.
    cfvquantdiaria = models.FloatField(db_column='CFVQUANTDIARIA', blank=True, null=True)  # Field name made lowercase.
    cfvdiferencaant = models.FloatField(db_column='CFVDIFERENCAANT', blank=True, null=True)  # Field name made lowercase.
    cfvdiferencaprox = models.FloatField(db_column='CFVDIFERENCAPROX', blank=True, null=True)  # Field name made lowercase.
    cfvbascula = models.CharField(db_column='CFVBASCULA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfvdescarga = models.FloatField(db_column='CFVDESCARGA', blank=True, null=True)  # Field name made lowercase.
    cfvchv1 = models.IntegerField(db_column='CFVCHV1', blank=True, null=True)  # Field name made lowercase.
    cfvchv2 = models.IntegerField(db_column='CFVCHV2', blank=True, null=True)  # Field name made lowercase.
    cfvkmtot = models.FloatField(db_column='CFVKMTOT', blank=True, null=True)  # Field name made lowercase.
    cfvrecfaturado = models.FloatField(db_column='CFVRECFATURADO', blank=True, null=True)  # Field name made lowercase.
    cfvreckmvalor = models.FloatField(db_column='CFVRECKMVALOR', blank=True, null=True)  # Field name made lowercase.
    cfvreckm = models.FloatField(db_column='CFVRECKM', blank=True, null=True)  # Field name made lowercase.
    cfvreckmtotal = models.FloatField(db_column='CFVRECKMTOTAL', blank=True, null=True)  # Field name made lowercase.
    cfvrectotal = models.FloatField(db_column='CFVRECTOTAL', blank=True, null=True)  # Field name made lowercase.
    cfvrecdiarias = models.FloatField(db_column='CFVRECDIARIAS', blank=True, null=True)  # Field name made lowercase.
    cfvrecdescarga = models.FloatField(db_column='CFVRECDESCARGA', blank=True, null=True)  # Field name made lowercase.
    cfvrecpedagio = models.FloatField(db_column='CFVRECPEDAGIO', blank=True, null=True)  # Field name made lowercase.
    cfvrecoutros = models.FloatField(db_column='CFVRECOUTROS', blank=True, null=True)  # Field name made lowercase.
    cfvemp = models.IntegerField(db_column='CFVEMP', blank=True, null=True)  # Field name made lowercase.
    cfvfil = models.IntegerField(db_column='CFVFIL', blank=True, null=True)  # Field name made lowercase.
    cfvadiant2 = models.FloatField(db_column='CFVADIANT2', blank=True, null=True)  # Field name made lowercase.
    cfvadiant3 = models.FloatField(db_column='CFVADIANT3', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa1 = models.FloatField(db_column='CFVDESPESA1', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa2 = models.FloatField(db_column='CFVDESPESA2', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa3 = models.FloatField(db_column='CFVDESPESA3', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa4 = models.FloatField(db_column='CFVDESPESA4', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa5 = models.FloatField(db_column='CFVDESPESA5', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa6 = models.FloatField(db_column='CFVDESPESA6', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa7 = models.FloatField(db_column='CFVDESPESA7', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa8 = models.FloatField(db_column='CFVDESPESA8', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa9 = models.FloatField(db_column='CFVDESPESA9', blank=True, null=True)  # Field name made lowercase.
    cfvdespesa10 = models.FloatField(db_column='CFVDESPESA10', blank=True, null=True)  # Field name made lowercase.
    cfvrecebprev = models.FloatField(db_column='CFVRECEBPREV', blank=True, null=True)  # Field name made lowercase.
    cfvdesplancprev = models.FloatField(db_column='CFVDESPLANCPREV', blank=True, null=True)  # Field name made lowercase.
    cfvsit_old = models.IntegerField(db_column='CFVSIT_OLD', blank=True, null=True)  # Field name made lowercase.
    cfvdatavalid = models.DateTimeField(db_column='CFVDATAVALID', blank=True, null=True)  # Field name made lowercase.
    cfvcc = models.IntegerField(db_column='CFVCC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFVIAGEM'


class Chequerec(models.Model):
    chrdata = models.DateTimeField(db_column='CHRDATA', blank=True, null=True)  # Field name made lowercase.
    chrnumban = models.IntegerField(db_column='CHRNUMBAN', blank=True, null=True)  # Field name made lowercase.
    chrnumag = models.CharField(db_column='CHRNUMAG', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chrnumconta = models.CharField(db_column='CHRNUMCONTA', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chrnumch = models.IntegerField(db_column='CHRNUMCH', blank=True, null=True)  # Field name made lowercase.
    chrsacado = models.CharField(db_column='CHRSACADO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chrvalor = models.FloatField(db_column='CHRVALOR', blank=True, null=True)  # Field name made lowercase.
    chrdataadesc = models.DateTimeField(db_column='CHRDATAADESC', blank=True, null=True)  # Field name made lowercase.
    chrdatadesc = models.DateTimeField(db_column='CHRDATADESC', blank=True, null=True)  # Field name made lowercase.
    chrconsulta = models.CharField(db_column='CHRCONSULTA', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chrrec = models.IntegerField(db_column='CHRREC')  # Field name made lowercase.
    chrcod = models.IntegerField(db_column='CHRCOD', primary_key=True)  # Field name made lowercase.
    chrregdep = models.IntegerField(db_column='CHRREGDEP', blank=True, null=True)  # Field name made lowercase.
    chrdatadesc1 = models.DateTimeField(db_column='CHRDATADESC1', blank=True, null=True)  # Field name made lowercase.
    chrregdep1 = models.IntegerField(db_column='CHRREGDEP1', blank=True, null=True)  # Field name made lowercase.
    chrdatadesc2 = models.DateTimeField(db_column='CHRDATADESC2', blank=True, null=True)  # Field name made lowercase.
    chrregdep2 = models.IntegerField(db_column='CHRREGDEP2', blank=True, null=True)  # Field name made lowercase.
    chrobs = models.CharField(db_column='CHROBS', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chrportfor = models.IntegerField(db_column='CHRPORTFOR', blank=True, null=True)  # Field name made lowercase.
    chrportpg = models.IntegerField(db_column='CHRPORTPG', blank=True, null=True)  # Field name made lowercase.
    chrtroco = models.FloatField(db_column='CHRTROCO', blank=True, null=True)  # Field name made lowercase.
    chrjuros = models.FloatField(db_column='CHRJUROS', blank=True, null=True)  # Field name made lowercase.
    chrdesc = models.FloatField(db_column='CHRDESC', blank=True, null=True)  # Field name made lowercase.
    chrdinheiro = models.FloatField(db_column='CHRDINHEIRO', blank=True, null=True)  # Field name made lowercase.
    chrprop = models.CharField(db_column='CHRPROP', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chrselecao = models.IntegerField(db_column='CHRSELECAO', blank=True, null=True)  # Field name made lowercase.
    chrrecorig = models.IntegerField(db_column='CHRRECORIG', blank=True, null=True)  # Field name made lowercase.
    chrbandep = models.IntegerField(db_column='CHRBANDEP', blank=True, null=True)  # Field name made lowercase.
    chrbandep1 = models.IntegerField(db_column='CHRBANDEP1', blank=True, null=True)  # Field name made lowercase.
    chrbandep2 = models.IntegerField(db_column='CHRBANDEP2', blank=True, null=True)  # Field name made lowercase.
    chrdatadev1 = models.DateTimeField(db_column='CHRDATADEV1', blank=True, null=True)  # Field name made lowercase.
    chrdatadev2 = models.DateTimeField(db_column='CHRDATADEV2', blank=True, null=True)  # Field name made lowercase.
    chrdatasubs = models.DateTimeField(db_column='CHRDATASUBS', blank=True, null=True)  # Field name made lowercase.
    chrsit_old = models.CharField(db_column='CHRSIT_OLD', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chrsit = models.IntegerField(db_column='CHRSIT', blank=True, null=True)  # Field name made lowercase.
    chrdatasustado = models.DateTimeField(db_column='CHRDATASUSTADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHEQUEREC'


class Cid10(models.Model):
    c10cod = models.IntegerField(db_column='C10COD', primary_key=True)  # Field name made lowercase.
    c10cid = models.CharField(db_column='C10CID', max_length=10, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    c10desc = models.CharField(db_column='C10DESC', max_length=250, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    c10ativo = models.CharField(db_column='C10ATIVO', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CID10'


class Cidade(models.Model):
    cidcod = models.IntegerField(db_column='CIDCOD', primary_key=True)  # Field name made lowercase.
    cidnome = models.CharField(db_column='CIDNOME', max_length=60, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    cidest = models.IntegerField(db_column='CIDEST', blank=True, null=True)  # Field name made lowercase.
    cidflag = models.CharField(db_column='CIDFLAG', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cidcep = models.CharField(db_column='CIDCEP', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cidtipo = models.IntegerField(db_column='CIDTIPO', blank=True, null=True)  # Field name made lowercase.
    cidsit = models.IntegerField(db_column='CIDSIT', blank=True, null=True)  # Field name made lowercase.
    cidsubor = models.IntegerField(db_column='CIDSUBOR', blank=True, null=True)  # Field name made lowercase.
    ciddistkm = models.FloatField(db_column='CIDDISTKM', blank=True, null=True)  # Field name made lowercase.
    cidrg = models.IntegerField(db_column='CIDRG', blank=True, null=True)  # Field name made lowercase.
    cidpai = models.IntegerField(db_column='CIDPAI', blank=True, null=True)  # Field name made lowercase.
    cidcodibge = models.IntegerField(db_column='CIDCODIBGE', blank=True, null=True)  # Field name made lowercase.
    cidcentchave = models.IntegerField(db_column='CIDCENTCHAVE', blank=True, null=True)  # Field name made lowercase.
    cidcadupdate = models.IntegerField(db_column='CIDCADUPDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIDADE'


class Cidadebanco(models.Model):
    cbanban = models.IntegerField(db_column='CBANBAN', primary_key=True)  # Field name made lowercase. The composite primary key (CBANBAN, CBANCID) found, that is not supported. The first column is selected.
    cbancid = models.IntegerField(db_column='CBANCID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIDADEBANCO'
        unique_together = (('cbanban', 'cbancid'),)


class Cidaderota(models.Model):
    crotcidorig = models.OneToOneField(Cidade, models.DO_NOTHING, db_column='CROTCIDORIG', primary_key=True)  # Field name made lowercase. The composite primary key (CROTCIDORIG, CROTCIDDEST, CROTCLICOB) found, that is not supported. The first column is selected.
    crotciddest = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='CROTCIDDEST', related_name='cidaderota_crotciddest_set')  # Field name made lowercase.
    crotclicob = models.IntegerField(db_column='CROTCLICOB')  # Field name made lowercase.
    crotdistan = models.FloatField(db_column='CROTDISTAN', blank=True, null=True)  # Field name made lowercase.
    crottempo = models.DateTimeField(db_column='CROTTEMPO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIDADEROTA'
        unique_together = (('crotcidorig', 'crotciddest', 'crotclicob'),)


class Cidrotapracapedagio(models.Model):
    crotciddest = models.OneToOneField(Cidade, models.DO_NOTHING, db_column='CROTCIDDEST', primary_key=True)  # Field name made lowercase. The composite primary key (CROTCIDDEST, CROTCIDORIG, CROTCLICOB, PPEDCOD) found, that is not supported. The first column is selected.
    crotcidorig = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='CROTCIDORIG', related_name='cidrotapracapedagio_crotcidorig_set')  # Field name made lowercase.
    crotclicob = models.IntegerField(db_column='CROTCLICOB')  # Field name made lowercase.
    ppedcod = models.ForeignKey('Pracapedagio', models.DO_NOTHING, db_column='PPEDCOD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIDROTAPRACAPEDAGIO'
        unique_together = (('crotciddest', 'crotcidorig', 'crotclicob', 'ppedcod'),)


class Ciot(models.Model):
    ciotcod = models.IntegerField(db_column='CIOTCOD', primary_key=True)  # Field name made lowercase.
    ciotemp = models.IntegerField(db_column='CIOTEMP')  # Field name made lowercase.
    ciotfil = models.IntegerField(db_column='CIOTFIL')  # Field name made lowercase.
    ciottipo = models.IntegerField(db_column='CIOTTIPO', blank=True, null=True)  # Field name made lowercase.
    ciotref = models.IntegerField(db_column='CIOTREF', blank=True, null=True)  # Field name made lowercase.
    ciotsit = models.IntegerField(db_column='CIOTSIT', blank=True, null=True)  # Field name made lowercase.
    ciotdata = models.DateTimeField(db_column='CIOTDATA', blank=True, null=True)  # Field name made lowercase.
    ciotdataemissao = models.DateTimeField(db_column='CIOTDATAEMISSAO', blank=True, null=True)  # Field name made lowercase.
    ciotdatacanc = models.DateTimeField(db_column='CIOTDATACANC', blank=True, null=True)  # Field name made lowercase.
    ciotprotcanc = models.CharField(db_column='CIOTPROTCANC', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ciotnumero = models.CharField(db_column='CIOTNUMERO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cioterro = models.CharField(db_column='CIOTERRO', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ciotpdf = models.BinaryField(db_column='CIOTPDF', blank=True, null=True)  # Field name made lowercase.
    ciotprotenc = models.CharField(db_column='CIOTPROTENC', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIOT'


class Classealmoxarifado(models.Model):
    calmcod = models.IntegerField(db_column='CALMCOD', primary_key=True)  # Field name made lowercase.
    calmnome = models.CharField(db_column='CALMNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    calmtipo = models.IntegerField(db_column='CALMTIPO', blank=True, null=True)  # Field name made lowercase.
    calmbloq = models.CharField(db_column='CALMBLOQ', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSEALMOXARIFADO'


class Classecliente(models.Model):
    clccod = models.IntegerField(db_column='CLCCOD', primary_key=True)  # Field name made lowercase.
    clcnome = models.CharField(db_column='CLCNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    clctipodoc = models.IntegerField(db_column='CLCTIPODOC', blank=True, null=True)  # Field name made lowercase.
    clcflag = models.CharField(db_column='CLCFLAG', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clcnop = models.IntegerField(db_column='CLCNOP', blank=True, null=True)  # Field name made lowercase.
    clccentchave = models.IntegerField(db_column='CLCCENTCHAVE', blank=True, null=True)  # Field name made lowercase.
    clccodcent = models.IntegerField(db_column='CLCCODCENT', blank=True, null=True)  # Field name made lowercase.
    clcnopsub = models.IntegerField(db_column='CLCNOPSUB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSECLIENTE'


class Classeclienteaplic(models.Model):
    clcacod = models.IntegerField(db_column='CLCACOD', primary_key=True)  # Field name made lowercase.
    clcanome = models.CharField(db_column='CLCANOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    clcanop = models.IntegerField(db_column='CLCANOP', blank=True, null=True)  # Field name made lowercase.
    clcacentchave = models.IntegerField(db_column='CLCACENTCHAVE', blank=True, null=True)  # Field name made lowercase.
    clcacalcimptot = models.CharField(db_column='CLCACALCIMPTOT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clcainet = models.CharField(db_column='CLCAINET', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clcaconsfinal = models.CharField(db_column='CLCACONSFINAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clcacodcent = models.IntegerField(db_column='CLCACODCENT', blank=True, null=True)  # Field name made lowercase.
    clcanopsub = models.IntegerField(db_column='CLCANOPSUB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSECLIENTEAPLIC'


class Classecompra(models.Model):
    ccomcod = models.IntegerField(db_column='CCOMCOD', primary_key=True)  # Field name made lowercase.
    ccomnome = models.CharField(db_column='CCOMNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSECOMPRA'


class Classefornecedor(models.Model):
    cforcod = models.IntegerField(db_column='CFORCOD', primary_key=True)  # Field name made lowercase.
    cfornome = models.CharField(db_column='CFORNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    cfortipodoc = models.IntegerField(db_column='CFORTIPODOC', blank=True, null=True)  # Field name made lowercase.
    cforcadincomp = models.CharField(db_column='CFORCADINCOMP', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfororgaopub = models.CharField(db_column='CFORORGAOPUB', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cforsimplesnac = models.CharField(db_column='CFORSIMPLESNAC', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cforcalm = models.IntegerField(db_column='CFORCALM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSEFORNECEDOR'


class Classemanutencao(models.Model):
    cmancod = models.IntegerField(db_column='CMANCOD', primary_key=True)  # Field name made lowercase.
    cmannome = models.CharField(db_column='CMANNOME', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    cmantexto = models.BinaryField(db_column='CMANTEXTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSEMANUTENCAO'


class Classificacaofiscal(models.Model):
    clfcod = models.IntegerField(db_column='CLFCOD', primary_key=True)  # Field name made lowercase.
    clfnumero = models.IntegerField(db_column='CLFNUMERO', blank=True, null=True)  # Field name made lowercase.
    clfdesc = models.CharField(db_column='CLFDESC', max_length=40, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    clfcstdapi = models.IntegerField(db_column='CLFCSTDAPI', blank=True, null=True)  # Field name made lowercase.
    clfcstarqmov = models.IntegerField(db_column='CLFCSTARQMOV', blank=True, null=True)  # Field name made lowercase.
    clfflag = models.CharField(db_column='CLFFLAG', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clfcentchave = models.IntegerField(db_column='CLFCENTCHAVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSIFICACAOFISCAL'


class Cliente(models.Model):
    clicod = models.IntegerField(db_column='CLICOD', primary_key=True)  # Field name made lowercase.
    clicep = models.CharField(db_column='CLICEP', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clicidade = models.IntegerField(db_column='CLICIDADE', blank=True, null=True)  # Field name made lowercase.
    clicobcep = models.CharField(db_column='CLICOBCEP', max_length=8, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clicobcidade = models.IntegerField(db_column='CLICOBCIDADE', blank=True, null=True)  # Field name made lowercase.
    clicnpjcpf = models.CharField(db_column='CLICNPJCPF', max_length=18, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliiepr = models.CharField(db_column='CLIIEPR', max_length=18, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clitelefone = models.CharField(db_column='CLITELEFONE', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clifax = models.CharField(db_column='CLIFAX', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliweb = models.CharField(db_column='CLIWEB', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clipgtotipo = models.IntegerField(db_column='CLIPGTOTIPO', blank=True, null=True)  # Field name made lowercase.
    clibloqvenda = models.CharField(db_column='CLIBLOQVENDA', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clibloqtotal = models.CharField(db_column='CLIBLOQTOTAL', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clipgtonparc = models.IntegerField(db_column='CLIPGTONPARC', blank=True, null=True)  # Field name made lowercase.
    clicobbanco = models.IntegerField(db_column='CLICOBBANCO', blank=True, null=True)  # Field name made lowercase.
    cliclc = models.IntegerField(db_column='CLICLC', blank=True, null=True)  # Field name made lowercase.
    clicobtipo = models.IntegerField(db_column='CLICOBTIPO', blank=True, null=True)  # Field name made lowercase.
    clilimcred = models.FloatField(db_column='CLILIMCRED', blank=True, null=True)  # Field name made lowercase.
    clicobinst = models.IntegerField(db_column='CLICOBINST', blank=True, null=True)  # Field name made lowercase.
    cliultcons = models.DateTimeField(db_column='CLIULTCONS', blank=True, null=True)  # Field name made lowercase.
    clicobprazoinst = models.IntegerField(db_column='CLICOBPRAZOINST', blank=True, null=True)  # Field name made lowercase.
    clivalcred = models.DateTimeField(db_column='CLIVALCRED', blank=True, null=True)  # Field name made lowercase.
    clisaldo = models.FloatField(db_column='CLISALDO', blank=True, null=True)  # Field name made lowercase.
    clicodcont = models.IntegerField(db_column='CLICODCONT', blank=True, null=True)  # Field name made lowercase.
    clicodcontfor = models.IntegerField(db_column='CLICODCONTFOR', blank=True, null=True)  # Field name made lowercase.
    cliinfocotacao = models.CharField(db_column='CLIINFOCOTACAO', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clipercon1 = models.DateTimeField(db_column='CLIPERCON1', blank=True, null=True)  # Field name made lowercase.
    clipercon2 = models.DateTimeField(db_column='CLIPERCON2', blank=True, null=True)  # Field name made lowercase.
    clidatacad = models.DateTimeField(db_column='CLIDATACAD', blank=True, null=True)  # Field name made lowercase.
    clidataultnota = models.DateTimeField(db_column='CLIDATAULTNOTA', blank=True, null=True)  # Field name made lowercase.
    cliultnota = models.IntegerField(db_column='CLIULTNOTA', blank=True, null=True)  # Field name made lowercase.
    climalaendcob = models.CharField(db_column='CLIMALAENDCOB', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliobs = models.BinaryField(db_column='CLIOBS', blank=True, null=True)  # Field name made lowercase.
    clidatavenc = models.DateTimeField(db_column='CLIDATAVENC', blank=True, null=True)  # Field name made lowercase.
    cliloc = models.BinaryField(db_column='CLILOC', blank=True, null=True)  # Field name made lowercase.
    clicaract = models.BinaryField(db_column='CLICARACT', blank=True, null=True)  # Field name made lowercase.
    clirep = models.IntegerField(db_column='CLIREP', blank=True, null=True)  # Field name made lowercase.
    clisegc = models.IntegerField(db_column='CLISEGC', blank=True, null=True)  # Field name made lowercase.
    cliclicont = models.IntegerField(db_column='CLICLICONT', blank=True, null=True)  # Field name made lowercase.
    cliultconsobs = models.CharField(db_column='CLIULTCONSOBS', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliultconsfunresp = models.IntegerField(db_column='CLIULTCONSFUNRESP', blank=True, null=True)  # Field name made lowercase.
    cliultconsvalid = models.IntegerField(db_column='CLIULTCONSVALID', blank=True, null=True)  # Field name made lowercase.
    cliultconsreprov = models.CharField(db_column='CLIULTCONSREPROV', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliclca = models.IntegerField(db_column='CLICLCA', blank=True, null=True)  # Field name made lowercase.
    clicomissaoperc = models.FloatField(db_column='CLICOMISSAOPERC', blank=True, null=True)  # Field name made lowercase.
    clipgtofobcif = models.IntegerField(db_column='CLIPGTOFOBCIF', blank=True, null=True)  # Field name made lowercase.
    cliportoorig = models.IntegerField(db_column='CLIPORTOORIG', blank=True, null=True)  # Field name made lowercase.
    cliportodest = models.IntegerField(db_column='CLIPORTODEST', blank=True, null=True)  # Field name made lowercase.
    cliendereconum = models.IntegerField(db_column='CLIENDERECONUM', blank=True, null=True)  # Field name made lowercase.
    clienderecocomp = models.CharField(db_column='CLIENDERECOCOMP', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clicobendereconum = models.IntegerField(db_column='CLICOBENDERECONUM', blank=True, null=True)  # Field name made lowercase.
    clicobenderecocomp = models.CharField(db_column='CLICOBENDERECOCOMP', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clipgtodiasvenc = models.CharField(db_column='CLIPGTODIASVENC', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliadvert = models.CharField(db_column='CLIADVERT', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clifunresp = models.IntegerField(db_column='CLIFUNRESP', blank=True, null=True)  # Field name made lowercase.
    clicentchave = models.IntegerField(db_column='CLICENTCHAVE', blank=True, null=True)  # Field name made lowercase.
    clicentstatus = models.IntegerField(db_column='CLICENTSTATUS', blank=True, null=True)  # Field name made lowercase.
    clinome = models.CharField(db_column='CLINOME', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clinomefant = models.CharField(db_column='CLINOMEFANT', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliendereco = models.CharField(db_column='CLIENDERECO', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clibairro = models.CharField(db_column='CLIBAIRRO', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clibloqinet = models.CharField(db_column='CLIBLOQINET', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clifecfaturamento = models.IntegerField(db_column='CLIFECFATURAMENTO', blank=True, null=True)  # Field name made lowercase.
    clipgtodiasvencsem = models.CharField(db_column='CLIPGTODIASVENCSEM', max_length=7, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clicomissaoflag = models.CharField(db_column='CLICOMISSAOFLAG', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliquantmedia = models.FloatField(db_column='CLIQUANTMEDIA', blank=True, null=True)  # Field name made lowercase.
    clibloqquantmedia = models.DateTimeField(db_column='CLIBLOQQUANTMEDIA', blank=True, null=True)  # Field name made lowercase.
    clifrcobtipo = models.IntegerField(db_column='CLIFRCOBTIPO', blank=True, null=True)  # Field name made lowercase.
    clifrcobbanco = models.IntegerField(db_column='CLIFRCOBBANCO', blank=True, null=True)  # Field name made lowercase.
    clifrpgtonparc = models.IntegerField(db_column='CLIFRPGTONPARC', blank=True, null=True)  # Field name made lowercase.
    clifrpgtotipo = models.IntegerField(db_column='CLIFRPGTOTIPO', blank=True, null=True)  # Field name made lowercase.
    clioutcobtipo = models.IntegerField(db_column='CLIOUTCOBTIPO', blank=True, null=True)  # Field name made lowercase.
    clioutcobbanco = models.IntegerField(db_column='CLIOUTCOBBANCO', blank=True, null=True)  # Field name made lowercase.
    clioutpgtonparc = models.IntegerField(db_column='CLIOUTPGTONPARC', blank=True, null=True)  # Field name made lowercase.
    clioutpgtotipo = models.IntegerField(db_column='CLIOUTPGTOTIPO', blank=True, null=True)  # Field name made lowercase.
    clicobimpprop = models.CharField(db_column='CLICOBIMPPROP', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clititulo = models.CharField(db_column='CLITITULO', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliius = models.IntegerField(db_column='CLIIUS', blank=True, null=True)  # Field name made lowercase.
    cliemailnfetipo = models.IntegerField(db_column='CLIEMAILNFETIPO', blank=True, null=True)  # Field name made lowercase.
    cliemail = models.CharField(db_column='CLIEMAIL', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clirntrc = models.CharField(db_column='CLIRNTRC', max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cliinscmun = models.CharField(db_column='CLIINSCMUN', max_length=18, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clitoldeb = models.IntegerField(db_column='CLITOLDEB', blank=True, null=True)  # Field name made lowercase.
    clidescantec = models.FloatField(db_column='CLIDESCANTEC', blank=True, null=True)  # Field name made lowercase.
    clidescantecdias = models.IntegerField(db_column='CLIDESCANTECDIAS', blank=True, null=True)  # Field name made lowercase.
    clifecfatdias = models.CharField(db_column='CLIFECFATDIAS', max_length=40, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clifecfatpeso = models.FloatField(db_column='CLIFECFATPESO', blank=True, null=True)  # Field name made lowercase.
    cliflag = models.CharField(db_column='CLIFLAG', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
