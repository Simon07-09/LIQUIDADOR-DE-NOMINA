class ErrorValorSalario(Exception): #entre
    """El salario base no puede ser negativo"""

class ErrorHorasExtras(Exception):
    pass

class ErrorTarifaHoraExtra(Exception):
    pass

class ErrorPorcentajeDeduccion(Exception):
    pass

class ErrorValorDeduccion(Exception):
    pass
    
def calcular_total_devengado(salario_base, horas_extras, tarifa_hora_extra):
    
    if salario_base <= 0:
        raise ErrorValorSalario("El valor del salario debe ser mayor que cero")
    if horas_extras < 0:
        raise ErrorHorasExtras("Las horas extras no pueden ser negativas")
    if tarifa_hora_extra < 0:
        raise ErrorTarifaHoraExtra("La tarifa de hora extra no puede ser negativa")
    
    return salario_base + (horas_extras * tarifa_hora_extra)
    
def calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones):
    
    if porcentaje_salud < 0 or porcentaje_pension < 0:
        raise ErrorPorcentajeDeduccion("Los porcentajes de deducción no pueden ser negativos")
    if otras_deducciones < 0:
        raise ErrorValorDeduccion("Las otras deducciones no pueden ser negativas")
    
    deduccion_salud = (porcentaje_salud / 100) * salario_base
    deduccion_pension = (porcentaje_pension / 100) * salario_base
    return deduccion_salud + deduccion_pension + otras_deducciones

def calcular_salario_neto(total_devengado, total_deducciones):
    """
    Calcula el salario neto después de aplicar deducciones.

    - Si el total devengado es 0, el salario neto será negativo debido a las deducciones.
    - Si el total devengado es mayor que 0, las deducciones no pueden ser mayores al devengado.
    """
    if total_devengado == 0:
        # Permitir que el salario neto sea negativo si hay deducciones sin devengado
        return -total_deducciones  
    
    if total_deducciones > total_devengado:
        raise ValueError("Las deducciones no pueden ser mayores que el total devengado")
    
    return total_devengado - total_deducciones





    