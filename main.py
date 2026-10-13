from pyscript import document, display

def checkNum(e):
    num_bers = [3, 6, 8, 10, 88,]
   

    num1 = document.getElementById("number").value
    name = "MirGil"

    confirm_num = num1() in num_bers

    message = (f"Sorry {name}, your number cannot be found." , f"Yay {name}, your number was found!")

    document.getElementById("output1").innerHTML = message[confirm_num]