import tkinter as tk
from tkinter import filedialog
from pathlib import Path

class InterfaceGrafica:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RDA & HANDLE")
        self.root.geometry("500x300")
        self.root.iconbitmap("C:/PRJ/ESTAGIARIOS/Bianca/algoritmoComparativo/algoritmoComparativo/src/img/icon.ico") 
        #self.root.iconbitmap("src/icon.ico")

        self.imagem_fundo = tk.PhotoImage(file="C:/PRJ/ESTAGIARIOS/Bianca/algoritmoComparativo/algoritmoComparativo/src/img/background.png")
        self.label_imagem_fundo = tk.Label(self.root, image=self.imagem_fundo)
        self.label_imagem_fundo.place(relx=0.5, rely=0.5, anchor="center") 
        #self.imagem_fundo = tk.PhotoImage(file="src/background.png")

        self.label_pasta1 = tk.Label(self.root, text="Selecione a pasta RDA, o caminho aparecerá aqui:")
        self.label_pasta1.place(relx=0.5, rely=0.3, anchor="center")

        self.btn_selecionar_pasta1 = tk.Button(self.root, text="Selecionar RDA", command=self.selecionar_pasta_1)
        self.btn_selecionar_pasta1.place(relx=0.5, rely=0.4, anchor="center")

        self.label_pasta2 = tk.Label(self.root, text="Selecione a pasta HANDLE, o caminho aparecerá aqui:")
        self.label_pasta2.place(relx=0.5, rely=0.5, anchor="center")

        self.btn_selecionar_pasta2 = tk.Button(self.root, text="Selecionar HANDLE", command=self.selecionar_pasta_2)
        self.btn_selecionar_pasta2.place(relx=0.5, rely=0.6, anchor="center")

        self.btn_enter = tk.Button(self.root, text="Enter", command=self.executar_comparacao)
        self.btn_enter.place(relx=0.5, rely=0.7, anchor="center")


    def selecionar_pasta_1(self):
        pasta = filedialog.askdirectory()
        self.pasta_rda = Path(pasta)
        self.label_pasta1.config(text=f"Pasta RDA selecionada: {self.pasta_rda}")

    def selecionar_pasta_2(self):
        pasta = filedialog.askdirectory()
        self.pasta_handle = Path(pasta)
        self.label_pasta2.config(text=f"Pasta HANDLE selecionada: {self.pasta_handle}")

    def executar_comparacao(self):
        from scriptPrincipal import main
        
        # Verifica se ambas as pastas foram selecionadas
        if hasattr(self, 'pasta_rda') and hasattr(self, 'pasta_handle'):
            # Chama a função principal passando as pastas como argumentos
            main(self.pasta_rda, self.pasta_handle)
        else:
            print("Selecione ambas as pastas para continuar.")

    def iniciar(self):
        self.root.mainloop()

    def fechar(self):
        self.root.destroy()

# Função main para iniciar a interface gráfica
def main():
    interface = InterfaceGrafica()
    interface.iniciar()

if __name__ == "__main__":
    main()
