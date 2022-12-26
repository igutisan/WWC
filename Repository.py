cdias_registrados = [
  'luis3@w&r+',
  'maocb@w?r+',
  'pedro@w=r+',
  'ana34@we&+',
  'maria@w=e+',
  'pipe?@wer+',
  'tato3@wer+',
  'andre@w=e+',
  'julio@w+r&'
]

def getTotalCDIASRegistrados():
  return len(cdias_registrados);

def buscar_cdia(cdia):
  try:
    cdias_registrados.index(cdia)
    return True
  except:
    return False