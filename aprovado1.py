        def aprovado(media, total, faltas):
    presencas = total - faltas
    # O limite de faltas permitido é 25% do total. 
    # Logo, a presença deve ser maior ou igual a 75%.
    if presencas >= 0.75 * total:
        if media >= 6:
            return "Aprovado"
        else:
            return "Precisa fazer a prova final"
    else:
        return "Reprovado por faltas"