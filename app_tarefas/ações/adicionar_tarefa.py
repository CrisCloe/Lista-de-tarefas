from singleton.lista_tarefas import ListaTarefas

class AdicionarTarefa:
    def executar(self):
        nome = input("Nome da tarefa: ")
        descricao = input("Descricao: ")
        status = "Disponivel"
        tarefa = {"nome": nome, "descricao": descricao, "status": status}
        ListaTarefas().tarefas.append(tarefa)