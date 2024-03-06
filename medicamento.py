
# Clase Medicamento
class Medicamento():
    IVA = 0.18

    # Método constructor y sus parámteros con valores por defecto
    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_final = 0.0
        self.descuento = 0.0

    # Método estático que verifica si valor ingresado es mayor a cero
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    # Método getter que retorna el precio final del objeto
    @property
    def precio(self):
        return self.precio_final
    
    # Método setter que establece el precio final y el descuento en base al precio bruto
    @precio.setter
    def precio(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            self.precio_final = precio_bruto + precio_bruto * self.IVA

            # Establece valor de descuento en caso de que corresponda
            if self.precio_final >= 10000 and self.precio_final < 20000:
                self.descuento = 0.1
            elif self.precio_final >= 20000:
                self.descuento = 0.2
        
            # Si existe descuento se aplica
            if self.descuento:
                self.precio_final *= 1 - self.descuento

    # Método de igualdad que comprueba si dos medicamentos son iguales basándose en sus nombres
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()

    # Método para sumar el stock de dos medicamentos si son iguales
    def __iadd__(self, other):
        if self == other:
            self.stock += other.stock
        return self
    