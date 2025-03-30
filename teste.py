from num2words import num2words as extenso

print('R$350.000,00')
valor_do_imóvel = 350000
print(extenso(valor_do_imóvel, lang='pt'), 'reais.')


# def exibir_contrato():
#     for paragrafo in doc.paragraphs:
#         print(paragrafo.text)
#     voltar_ao_menu()


# nome_proprietario = input('Digite o nome do Proprietário: ')

# for paragrafo in doc.paragraphs:
#     if "PROPRIETARIO" in paragrafo.text:
#         # Percorre cada 'run' para preservar a formatação existente
#         for run in paragrafo.runs:
#             if "PROPRIETARIO" in run.text:
#                 run.text = run.text.replace("PROPRIETARIO", nome_proprietario.upper())