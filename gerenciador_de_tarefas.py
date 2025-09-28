import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

tarefas = []
proximo_id = 1

def atualizar_lista_tarefas():
    listbox_tarefas.delete(0, tk.END)
    
    for tarefa in tarefas:
        status = tarefa['status']
        descricao = tarefa['descricao']
        id_tarefa = tarefa['id']
        
        texto_tarefa = f"{id_tarefa}: {descricao} [{status}]"
        listbox_tarefas.insert(tk.END, texto_tarefa)
        
        if status == 'concluída':
            listbox_tarefas.itemconfig(tk.END, {'fg': 'gray'})
        else:
            listbox_tarefas.itemconfig(tk.END, {'fg': 'black'})

def adicionar_tarefa():
    global proximo_id
    descricao = entry_tarefa.get()
    
    if not descricao:
        messagebox.showwarning("Aviso", "A descrição da tarefa não pode estar vazia.")
        return
        
    nova_tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "status": "pendente"
    }
    tarefas.append(nova_tarefa)
    proximo_id += 1
    
    entry_tarefa.delete(0, tk.END)
    atualizar_lista_tarefas()

def get_id_selecionado():
    selecionado = listbox_tarefas.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa na lista.")
        return None
    
    texto_selecionado = listbox_tarefas.get(selecionado[0])
    id_tarefa = int(texto_selecionado.split(':')[0])
    return id_tarefa

def marcar_tarefa_concluida():
    id_selecionado = get_id_selecionado()
    if id_selecionado is None:
        return

    for tarefa in tarefas:
        if tarefa['id'] == id_selecionado:
            tarefa['status'] = 'concluída'
            break
    
    atualizar_lista_tarefas()

def remover_tarefa():
    id_selecionado = get_id_selecionado()
    if id_selecionado is None:
        return
        
    confirmar = messagebox.askyesno("Confirmar Remoção", f"Tem certeza que deseja remover a tarefa ID {id_selecionado}?")
    
    if confirmar:
        tarefa_para_remover = None
        for tarefa in tarefas:
            if tarefa['id'] == id_selecionado:
                tarefa_para_remover = tarefa
                break
        
        if tarefa_para_remover:
            tarefas.remove(tarefa_para_remover)
        
        atualizar_lista_tarefas()

root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("600x450")
root.configure(bg="#f0f0f0")

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

frame_entrada = ttk.Frame(main_frame)
frame_entrada.pack(fill=tk.X, pady=5)

label_tarefa = ttk.Label(frame_entrada, text="Nova Tarefa:")
label_tarefa.pack(side=tk.LEFT, padx=(0, 5))

entry_tarefa = ttk.Entry(frame_entrada, width=40)
entry_tarefa.pack(side=tk.LEFT, fill=tk.X, expand=True)

btn_adicionar = ttk.Button(frame_entrada, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(side=tk.LEFT, padx=(5, 0))

listbox_tarefas = tk.Listbox(main_frame, height=15, selectbackground="#00396C")
listbox_tarefas.pack(fill=tk.BOTH, expand=True, pady=10)

frame_botoes = ttk.Frame(main_frame)
frame_botoes.pack(fill=tk.X)

btn_concluir = ttk.Button(frame_botoes, text="Marcar como Concluída", command=marcar_tarefa_concluida)
btn_concluir.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

btn_remover = ttk.Button(frame_botoes, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

btn_sair = ttk.Button(frame_botoes, text="Sair", command=root.quit)
btn_sair.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

atualizar_lista_tarefas()
root.mainloop()