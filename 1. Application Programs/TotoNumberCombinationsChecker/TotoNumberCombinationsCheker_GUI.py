import PySimpleGUI as psg
layout = [
    [psg.Text("Въведи 6 числа от 1 до 49:"), psg.InputText(do_not_clear=False, size=(2, 2)),
     psg.InputText(do_not_clear=False, size=(2, 2)),
     psg.InputText(do_not_clear=False, size=(2, 2)), psg.InputText(do_not_clear=False, size=(2, 2)),
     psg.InputText(do_not_clear=False, size=(2, 2)), psg.InputText(do_not_clear=False, size=(2, 2))],
    [psg.Button("Провери числата"), psg.Button("Изчисти чисата")]
]
window = psg.Window("Тото 6/49", layout)
while True:
    event, values = window.read()
    if event == "Провери числата":
        for i in range(0, 6):
            print(values[i], end=" ")
        print()
    elif event == "Изчисти чисата":
        pass
    elif event == psg.WIN_CLOSED:
        break
window.close()