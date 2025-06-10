def situacao_aluno(media):
  if media >= 7:
    return "Aprovado"
  elif media >= 5:
    return "Recuperação"
  else:
    return "Reprovado"