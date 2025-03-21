from tkinter import *

#imports do selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from tkinter import messagebox



# Top level window 
frame = Tk() 
frame.title("brincadeira do mortal") 
frame.geometry('200x200') 
# Function for getting Input 
# from textbox and printing it 
# at label widget 

dollar = "?"
def dollarValue():
	options = Options()
	options.add_argument("--headless")
	options.add_argument("--disable-gpu")
	options.add_argument("--window-size=1920x1080")
	options.add_argument("--no-sandbox")
	options.add_argument("--disable-dev-shm-usage")
	options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


	driver = webdriver.Chrome(options=options)
	driver.get("https://br.investing.com/currencies/usd-brl")
	wait = WebDriverWait(driver, 5)
	dollar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-test="instrument-price-last"]')))
	lbl.config(text = "O valor do dollar atualmente: " + dollar.text)
	print(dollar.text)
	driver.quit()

def printInput(): 
	inp = inputtxt.get(1.0, "end-1c") 
	lbl.config(text = "Provided Input: "+inp)

# TextBox Creation 
inputtxt = Text(frame, 
				height = 5, 
				width = 20) 

inputtxt.pack() 

# Button Creation 
printButton = Button(frame, 
						text = "Print", 
						command = printInput) 
printButton.pack() 


closeButton = Button(frame, text = "Verificar dollar", command = dollarValue)
closeButton.pack()

dollarText = Label(frame, text=dollar)
dollarText.pack()


# Label Creation 
lbl = Label(frame, text = "") 
lbl.pack() 
frame.mainloop() 
