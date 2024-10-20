from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from tkinter.filedialog import askopenfilename, askdirectory
from main import executar_automacao
from pathlib import Path
import threading


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Imagens")


def caminho_dos_recursos(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def selecionar_pasta():
    global pasta_rf
    pasta_rf = askdirectory(title="Selecione a pasta de RFs mais atual que você tem.")


def selecionar_planilha():
    global caminho_arq_excel
    caminho_arq_excel = askopenfilename(title="Selecione a planilha de E-mails dos gestores.", filetypes=[("Excel Files", "*.xls;*.xlsx;*.xlsm;*.xlsb"), ("CSV Files", "*.csv")])


def validar_input(P):
    return P == "" or P.isdigit()


def acionar_automacao():
    nf_inicial = entry_1.get()
    nf_final = entry_2.get()

    try:
        if not (pasta_rf and caminho_arq_excel and nf_inicial and nf_final):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return
    except:
            messagebox.showwarning("Aviso", "Selecione todos os arquivos.")
            return
    
    if int(nf_inicial) > int(nf_final):
        messagebox.showwarning("Aviso", "O número inicial deve ser menor ou igual ao número final.")
        return
    
    threading.Thread(target=executar_automacao, args=(nf_inicial, nf_final, pasta_rf, caminho_arq_excel)).start()


window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = str((screen_width - 900) // 2)
y = str((screen_height - 600) // 2)

window.geometry(f"939x315+{x}+{y}")
window.configure(bg = "#FFFFFF")
window.title("Automação Faturamento Vale")
window.iconbitmap(caminho_dos_recursos("robozinho.ico"))

vcmd = (window.register(validar_input), '%P')

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 315,
    width = 939,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=caminho_dos_recursos("Imagem de fundo.png"))
image_1 = canvas.create_image(
    469.0,
    157.0,
    image=image_image_1
)

entry_1 = Entry(
    bd=2,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    relief="groove",
    justify="center",
    highlightbackground="#000000",
    font=("Inter", 18 * -1),
    cursor="xterm",
    validate="key",
    validatecommand=vcmd
)
entry_1.place(
    x=222.0,
    y=75.0,
    width=180.0,
    height=30.0
)

entry_2 = Entry(
    bd=2,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    relief="groove",
    justify="center",
    highlightbackground="#000000",
    font=("Inter", 18 * -1),
    cursor="xterm",
    validate="key",
    validatecommand=vcmd
)
entry_2.place(
    x=461.0,
    y=75.0,
    width=180.0,
    height=30.0
)

canvas.create_text(
    268.0,
    50.0,
    anchor="nw",
    text="NFS Inicial",
    fill="#000000",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    509.0,
    50.0,
    anchor="nw",
    text="NFS Final",
    fill="#000000",
    font=("Inter", 18 * -1)
)

button_image_1 = PhotoImage(
    file=caminho_dos_recursos("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_pasta(),
    relief="flat",
    cursor="hand2"
)
button_1.place(
    x=193.0,
    y=200.0,
    width=230.0,
    height=44.0
)

button_image_2 = PhotoImage(
    file=caminho_dos_recursos("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_planilha(),
    relief="flat",
    cursor="hand2"
)
button_2.place(
    x=443.0,
    y=199.0,
    width=230.0,
    height=46.93616485595703
)

canvas.create_text(
    270.0,
    171.0,
    anchor="nw",
    text="Pasta RF",
    fill="#000000",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    484.0,
    171.0,
    anchor="nw",
    text="Planilha Gestores",
    fill="#000000",
    font=("Inter", 18 * -1)
)

button_image_3 = PhotoImage(
    file=caminho_dos_recursos("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: acionar_automacao(),
    relief="flat",
    cursor="hand2"
)
button_3.place(
    x=721.0,
    y=92.0,
    width=117.0,
    height=110.0
)
window.resizable(False, False)
window.mainloop()
