# prueba

# caracteristicas base de objetos
class objeto:
  def __init__(self,nombre,exp,nivel,duracion,ataque,tipo):
    self.nombre = nombre
    self.exp = exp
    self.nivel = nivel
    self.duracion = duracion
    self.ataque = ataque
    sefl.tipo = tipo

  def aumento(self):
    pass
  def degradacion(self):
    pass

# campo para elemetos a prueba
class campo:
  def __init__(self,nombre):
    self.nombre = nombre
    self.elementos = []
    self.estatus = 0
    self.ataque = 0

  def agregar(self):
    pass
  def status(self):
    pass
  def ataque(self):
    pass
  def estadoGeneral(self):
    pass
  def combate(self):
    pass

# principal
def main():
  pass

if __name__ == "__main__":
  main()
