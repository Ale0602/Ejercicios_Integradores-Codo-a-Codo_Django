def creador_dict(cadena):

  list_1= cadena.split()
  dict_1={}
  for i in list_1:
    if i in dict_1:
      dict_1[i] +=1
    else:
      dict_1[i]= 1
  return dict_1

entrada=input('Ingrese su cadena de caracteres: ')
print(creador_dict(entrada))