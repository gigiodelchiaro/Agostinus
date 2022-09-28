from tkinter import *
import pyperclip
root = Tk()

root.title("Agostinus")
root.geometry("500x600")
#root.iconbitmap("sources/icon.ico")

clefs = [
    "c1",
    "c2",
    "c3",
    "c4",
    "c5",
    
]
clicked_clefs = StringVar(root)
clicked_clefs.set(clefs[0])


notes = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    
]

clicked_notes = StringVar(root)
clicked_notes.set(notes[0])



qclef = Label(root, text="Qual vai ser a clave?")
qclef.pack()

aclef = OptionMenu(root, clicked_clefs, *clefs)
aclef.pack()

qnote = Label(root, text="Qual vai ser a nota principal?")
qnote.pack()

anote = aclef = OptionMenu(root, clicked_notes, *notes)
anote.pack()

qtext = Label(root, text="Qual vai ser o texto?")
qtext.pack()

atext = Text(root, width=50, height=15)
atext.pack()
global clicked_line_break
global clicked_respiration
clicked_line_break = StringVar(root)
clicked_respiration = StringVar(root)

qline_break = Checkbutton(text="Adicionar quebra de linha depois de todos os pontos finais", variable=clicked_line_break, onvalue="n", offvalue="y")
qline_break.select()
qline_break.pack()
qrespiration = Checkbutton(text="Adicionar respiração depois das vírgulas", variable=clicked_respiration, onvalue="n", offvalue="y")
qrespiration.select()
qrespiration.pack()

global text_final
text_final = ""
text = atext.get("1.0",'end-1c')
def generate():
    note = clicked_notes.get()

    if note == "a":
        note_down = "a"

    elif note == "b":
        note_down = "a"

    elif note == "c":
        note_down = "b"

    elif note == "d":
        note_down = "c"

    elif note == "e":
        note_down = "d"

    elif note == "f":
        note_down = "e"

    elif note == "g":
        note_down = "f"

    elif note == "h":
        note_down = "g"

    elif note == "i":
        note_down = "h"

    elif note == "j":
        note_down = "i"

    elif note == "k":
        note_down = "j"

    elif note == "l":
        note_down = "k"

    elif note == "m":
        note_down = "l"


    text_clef = "("+ clicked_clefs.get() + ")" + atext.get("1.0",'end-1c')

    fix1 = text_clef.replace(". ",".")


    text_space = fix1.replace(" ",f"({note}) ")
    text_hyphen = text_space.replace("-",f"-({note})")

    line_break = clicked_line_break.get()
    respiration = clicked_respiration.get()


    if line_break == "n":
        text_dot = text_hyphen.replace(".",f".({note}.) (::Z) ")
    else:
        text_dot = text_hyphen.replace(".",f".({note}.) (::) ")


    if respiration == "n":
        text_comma = text_dot.replace(",",f",({note}.) (,) ")
    else:
        text_comma = text_dot.replace(",",f",({note})")



    fix2 = text_comma.replace("<",f"({note_down})")
    text_manual_respiration = fix2.replace(">",f"({note_down}.) (,) ")
    text_manual_double = text_manual_respiration.replace("@",f"({note}{note_down}.)")

    fix3 = text_manual_double.replace(f"({note}.) (,) ({note_down}.) (,)",f"({note_down}.) (,)")
    fix4 = fix3.replace(f"({note})({note_down}.)",f"({note_down}.)")

    fix5 = fix4.replace(f"({note})({note_down})",f"({note_down})")
    fix6 = fix5.replace(f"({note_down})({note})",f"({note_down})")

    fix7 = fix6.replace(f"({note_down}),({note_down}.)",f",({note_down}.)")
    fix8 = fix7.replace(f"({note}),({note}.)",f",({note}.)")

    fix9 = fix8.replace(f"(,) ({note})",f"(,)")
    fix10 = fix9.replace(f"(,) ({note_down})",f"(,)")

    fix11 = fix10.replace(f"({note_down}),({note}.)",f",({note_down}.)")
    fix12 = fix11.replace(f"({note_down}).({note}.)",f".({note_down}.)")
    fix13 = fix12.replace(f"({note})({note}{note_down}.)",f"({note}{note_down}.)")

    fix14 = fix13.replace(f"({note})({note})", f"({note})")

    text_final = fix14
    text_copy.configure(state=NORMAL)
    text_copy.delete('1.0', END)
    text_copy.insert(INSERT, text_final)
    text_copy.configure(state=DISABLED)



atext_copy = Label(root, text="Resultado:")
atext_copy.pack()
global text_copy
text_copy = Text(root, width=50 ,height=5)
text_copy.insert(INSERT, text_final)
text_copy.configure(state=DISABLED)
text_copy.pack()


def copy_select():
    pyperclip.copy(text_copy.get("1.0",'end-1c'))

button_generate = Button(root, text="Gerar", command=generate)
button_generate.pack()

button_copy = Button(root,text="Copiar",command=copy_select)
button_copy.pack()

#Final 1
#Por(g) Cris-(h)to,(h) nos-(h)so(h) Se-(h)nhor(hg.). F
#Ó* Deus, ao parti-ci-par-mos da a-le-gri-a da sal-va-ção que en-cheu de jú-*bi-lo São Ma-teus*, re-*ce-ben-do o Sal-va-dor em su-a ca-sa, con-*ce-dei se-ja-mos sem-pre re-fei-tos à me-sa da-que-le que vei-o cha-mar à sal-va-ção não os jus-tos*, mas* os pe-*ca-*do-res.
#Mateus*, re*cebendo

#Ó Deus, que mos-trais vos-so po-der so-bre-tu-do no per-dão e na mi-se-ri-cór-dia, der-ra-mai sem-pre em nós a vos-sa gra-ça, pa-ra que, ca-mi-nhan-do ao en-con-tro das vos-sas pro-mes-sas, al-can-ce-mos os bens que re-ser-vais. Por nos-so Sen-hor Je-sus Cris-to, vos-so Fi-lho, na u-ni-da-de do Es-pí-ri-to San-to.
#Ó< Deus, que mos-trais vos-so po-der so-bre-tu-do no per-dão e na mi-se-ri-cór-dia, der-ra-mai sem-pre em nós a vos-sa gra-ça>, pa-<ra que, ca-mi-nhan-do ao en-con-tro das vos-sas pro-mes-sas, al-can-ce-mos os bens que re-<ser-<vais. Por< nos-so Sen-hor Je-sus Cris-to, vos-so Fi-lho>, na< u-ni-da-de do Es-pí-ri-<to San-@to.
#Ó< Deus, que, pa-ra o so-cor-ro dos po-bres e for-ma-ção do cle-ro,> en-<ri-que-ces-tes o pres-bí-te-ro São Vi-cen-te de Pau-lo com as vir-tu-des a-pos-tó-li-<cas,> fa-<zei-nos, a-ni-ma-dos pe-lo mes-mo es-pí-ri-to, a-mar o que e-le a-mou e pra-ti-car o que en-<si-<nou. Por< nos-so Se-nhor Je-sus Cri-sto, vos-so Fi-lho, na u-ni-da-de do Es-pí-ri-<to San-@to.
root.mainloop()