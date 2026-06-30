from paciente import Paciente


class PacienteParticular(Paciente):
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo,
                 numero_prontuario, forma_pagamento, desconto_fidelidade):

        super().__init__(
            nome,
            data_nascimento,
            cpf,
            telefone,
            tipo_sanguineo,
            numero_prontuario
        )

        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade

    def calcular_valor_final(self, valor_consulta):
        valor_final = valor_consulta - (valor_consulta * self.desconto_fidelidade)

        print(f"Valor original: R${valor_consulta:.2f}")
        print(f"Desconto: {self.desconto_fidelidade * 100: .0f}%")
        print(f"Valor final: R${valor_final:.2f}")

        return valor_final

    def exibir_informacoes(self, detalhado):
        super().exibir_informacoes(detalhado)

        print(f"Forma de pagamento: {self.forma_pagamento}")
        print(f"Desconto: {self.desconto_fidelidade * 100:.0f}%")