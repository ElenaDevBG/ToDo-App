import FreeSimpleGUI as sg


def convert_feet_to_meters(feet, inches):
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters

sg.theme("Black")

label1 = sg.Text("Enter feet")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output", text_color="white")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    try:
        converted_meters = convert_feet_to_meters(values["feet"], values["inches"])
        window["output"].update(value=f"{converted_meters} m")
    except ValueError:
        sg.popup("Please provide two numbers")

window.close()
