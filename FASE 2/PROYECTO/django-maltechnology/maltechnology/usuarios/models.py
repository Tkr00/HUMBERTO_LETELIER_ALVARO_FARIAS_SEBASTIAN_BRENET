from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username} ({self.rut})"

class InfoHorno(models.Model):
    batch = models.CharField(max_length=22, primary_key=True)  # Definir BATCH como clave primaria
    fecha = models.DateField()
    variedad = models.CharField(max_length=40)
    
    temp_sobre_grano = models.FloatField()
    temp_bajo_tela = models.FloatField()
    temp_ambiente = models.FloatField()
    hr_sobre_tela = models.FloatField()
    
    p_apertura_damper = models.FloatField()
    presion_diferencial = models.FloatField()

    gas_total = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_1 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_2 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_3 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_4 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_5 = models.DecimalField(max_digits=10, decimal_places=2)
    gas_et_6 = models.DecimalField(max_digits=10, decimal_places=2)

    tiempo_total = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e1 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e2 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e3 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e4 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e5 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_barra_e6 = models.DecimalField(max_digits=10, decimal_places=2)

    sp_temp_1 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_2 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_3 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_4 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_5 = models.DecimalField(max_digits=10, decimal_places=2)
    sp_temp_6 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Batch: {self.batch} - Fecha: {self.fecha}"
    
    class Meta:
        db_table = 'INFO_HORNO'
        managed = False  # No permitir que Django administre esta tabla


class InfoProduccion(models.Model):
    batch = models.IntegerField(primary_key=True)  # Definir como clave primaria
    id_tipo_malta = models.IntegerField()
    id_tipo_horno = models.IntegerField()
    fecha_horneo = models.DateField()
    tipo_variedad = models.CharField(max_length=60)
    cebada_limpia = models.FloatField()
    cebada_sucia = models.FloatField()
    falla = models.IntegerField()
    impureza = models.IntegerField()
    polvo = models.IntegerField()
    malta_sucia = models.IntegerField()
    brote = models.IntegerField()
    pijilla_malta = models.IntegerField()
    malta_limpia = models.IntegerField()
    malta_verde = models.IntegerField()
    materiaseca = models.IntegerField()
    fecha_volteo = models.DateField()
    fecha_pulido = models.DateField()
    silo_destino_1 = models.CharField(max_length=60)
    kg_destino_1 = models.IntegerField()
    silo_destino_2 = models.CharField(max_length=60, blank=True, null=True)
    kg_destino_2 = models.IntegerField(blank=True, null=True)
    electricidad = models.IntegerField()
    agua = models.IntegerField()
    gas = models.IntegerField()
    cs_ci = models.FloatField()
    ci_mi = models.FloatField()
    # cs_ml = models.FloatField()
    # ms_ml = models.FloatField()
    # brote_ml = models.FloatField(
    #  db_column="brote/ml")
    factor_perdida_humedad = models.FloatField()
    factor_perdida_conversion = models.FloatField()
    kg_perdida_humedad = models.IntegerField()
    kg_perdida_conversion = models.IntegerField()
    factor_carbon = models.FloatField()
    factor_electricidad = models.FloatField()
    factor_agua = models.FloatField()
    # info_germinacion_cod_germinacion = models.IntegerField(
    # db_column='INFO_GERMINACION_COD_GERMINACION')
    info_horno_fecha = models.DateField()
    info_tina_cod_tina = models.IntegerField()

    class Meta:
        db_table = 'INFO_PRODUCCION'
        verbose_name = 'Información de Producción'
        verbose_name_plural = 'Información de Producción'
        managed = False  # No permitir que Django administre esta tabla


    def __str__(self):
        return f'Batch {self.batch} - Fecha: {self.fecha_horneo}'