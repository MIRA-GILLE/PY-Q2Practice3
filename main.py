from pyscript import document

def checkNum(e):
    num_bers = ["3", "6", "8", "10", "88"]
   

    num1 = document.getElementById("number").value
    name = "MirGil"

    if not num1:
        document.getElementById("output1").textContent = "Please enter a number."
        return

    confirm_num = num1 in num_bers

    if confirm_num:
        message = f"Yay {name}, your number {num1} was found!"
    else:
        message = f"Sorry {name}, your number {num1} cannot be found."

    document.getElementById("output1").textContent = message
