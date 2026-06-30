class Paciente:
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf 
        self.telefone = telefone 
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario
        
        self.atendimentos = []

    def registrar_atendimento(self, tipo, custo):
        atendimento = {
            "tipo": tipo,
            "custo": custo 
        }

        self.atendimentos.append(atendimento)

        print(f"Paciente {self.nome} passou pelo atendimento do tipo '{tipo}' com o custo de R${custo:.2f}")
        
    def exibir_informacoes(self, detalhado):
        if detalhado == False: 
            print("=== INFORMAÇÕES BÁSICAS ===")
            print(f"Nome: {self.nome}")
            print(f"Prontuário: {self.numero_prontuario}")
            print(f"Tipo sanguineo: {self.tipo_sanguineo}")

        else: 
            print("=== INFORMAÇÕES BÁSICAS ===")
            print(f"Nome: {self.nome}")
            print(f"Data de nascimento: {self.data_nascimento}")
            print(f"CPF: {self.cpf}")
            print(f"Telefone: {self.telefone}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
            print(f"Prontuário: {self.numero_prontuario}")

            print("\n=== HISTÓRICO DE ATENDIMENTOS ===")

        if len(self.atendimentos) == 0:
            print("Nenhum atendimento registrado.")

        else: 
            for a in self.atendimentos:
                print(f"- {a['tipo']} | R${a['custo']:.2f}")
