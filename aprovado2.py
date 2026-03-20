def aprovado(media, total, faltas):
    # Cálculo correto da porcentagem de presença (0 a 100)
    porcentagem_presenca = ((total - faltas) / total) * 100
    
    # 1º Passo: Verificar faltas (Critério Eliminatório)
    if porcentagem_presenca < 75:
        return "Reprovado por faltas"
    
    # 2º Passo: Se ele não reprovou por faltas, verificamos a nota
    if media >= 6:
        return "Aprovado"
    else:
        return "Precisa fazer a prova final"