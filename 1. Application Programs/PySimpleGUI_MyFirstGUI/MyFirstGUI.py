import PySimpleGUI as psg
# print(psg) - file location

# Step 1: Set theme (opinial)
#psg.theme("DarkAmber")
# Step 2: Create layout
layout = [
    [psg.Text("Eneter name")],
    [psg.InputText()],
    [psg.Button("Ok"), psg.Button("Cancel")]
]
# Step 3: Create window
window = psg.Window("Form", layout)
# Step 4: Event loop
while True:
    event, values = window.read()
    if event == "Cancel" or event == psg.WIN_CLOSED:
        break
    print("Hello " + str(values[0]) + "!")
# Step 5: Close window
window.close()