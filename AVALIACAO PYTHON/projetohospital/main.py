from paciente import Paciente
from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio


# =========================
# Paciente Particular
# =========================

paciente1 = PacienteParticular(
    "Evageline Barreto",
    "15/08/1998",
    "123.456.789-09",
    "(11) 99999-9999",
    "O+",
    "PR001",
    "Cartão de Crédito",
    0.10
)


paciente1.registrar_atendimento("Consulta Clínica", 200)

valor = paciente1.calcular_valor_final(200)

print(f"\nValor Final da consulta: R${valor:.2f}\n")

paciente1.exibir_informacoes(True)

print("\n" + "=" * 50 + "\n")

# ============================
# Paciente Convênio 
# ============================

paciente2 = PacienteConvenio(
    "Adriano Souza",
    "20/03/2005",
    "957.569.321-00",
    "(11)98888-9999",
    "A+",
    "PR002",
    "Unimed",
    "987654321",
)


paciente2.registrar_atendimento("Consulta Neurológica", 300)

paciente2.registrar_autorizacao("Consulta Neurológica", 0)

print()

paciente2.exibir_informacoes(True)

