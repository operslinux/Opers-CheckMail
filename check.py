#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from form.logo import LogoOne, LogoCero, LogoTwo
from selenium import webdriver
from colorama import Back, Fore, init
from tqdm import tqdm
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
#iniciamos colores
from time import sleep
init()


def Carga():
    loop = tqdm(total=50000, position=0, leave=False)
    for k in range(50000):
        loop.set_description(Fore.BLUE + "Loading .....".format(k) + Fore.RESET)
        loop.update(1)
    loop.close()


def MenuInicial():
    os.system('clear')
    LogoCero()
    sleep(0.7)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoOne()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(1.5)
    sleep(0.60)
    Carga()
    print(Fore.GREEN + "\t\tBienvenido a Check Mail BY OPERS LINUX\t\t")
    print("\t\t__________________________\t\t")


def verify():
    if os.path.isfile("/usr/bin/geckodriver") == True:

        print("{} [ {} + {} ] {} El archivo si existe {} <Ejecutando Script> {}".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.BLUE, Fore.GREEN, Fore.RESET))
        Carga()
    else:
        print("{} [ {} X {} ] {} el archivo no existe, {} comenzando DESCARGA.... {}".format(Fore.BLUE, Fore.RED, Fore.BLUE, Fore.RED, Fore.WHITE, Fore.RESET))
        Carga()
        os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz")
        os.system("sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver'")
        os.system("sudo chmod +x /usr/bin/geckodriver")
        os.system("rm geckodriver-v0.26.0-linux64.tar.gz")
        print("{} [ {} + {} ] {} DRIVER DESCARGADO ...... ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.WHITE))






def main():
    MenuInicial()
    verify()
    try:
        txt = open("list.txt", "r")
        for i, linea in enumerate(txt):
            #LogoTwo()
            #print("La Linea seleccionada es: ", linea)
            #print("La enumeracion es: ", i)
            print("{} [ {} + {} ] {} < Correo numero: > {}".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET) + str(i))
            driver = webdriver.Firefox()
            driver.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1588997537&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d850f8727-1591-ae21-b585-c72698a99647&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=FE61C9D2AF928E56&bk=1588997538&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=712c21a23c1143ab9fdc2cce33864bbf")
            alert = Alert(driver)
            alert.accept()
            #alert.dismiss()
            Carga()
            correo = linea.split("@")
            #print(correo[0])
            #print(correo[1])
            email = driver.find_element_by_xpath('//*[@id="MemberName"]')
            email.send_keys(correo[0])
            salida = correo[1]
            #print(salida)

            if "hotmail" in salida:
                victima = correo[0] + "@" + correo[1]
                print(victima)
                print("{} < EL correo es: > ".format(Fore.WHITE) + salida + "{}".format(Fore.RESET))
                clikeando = driver.find_element_by_xpath('//*[@id="LiveDomainBoxList"]')
                clikeando.send_keys(Keys.ARROW_DOWN)
                driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()
                Carga()
                try:
                    driver.find_element_by_xpath('//*[@id="PasswordInput"]').send_keys("jajajaj")
                    print("{} [ {} X {} ] {} < EL CORREO NO EXISTE > {}".format(Fore.BLUE, Fore.RED, Fore.BLUE, Fore.RED, Fore.RESET))
                    print("{} ________________________________________ {}".format(Fore.WHITE, Fore.RESET))
                    f = open('NO-EXISTE.txt', 'a')
                    f.write(str(victima))
                    f.close()
                except NoSuchElementException as exception:
                    print("{} [ {} + {} ] {} EL correo ya existe :( {}".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.GREEN, Fore.RESET))
                    print("{} ________________________________________ {} ".format(Fore.WHITE, Fore.RESET))
                    f = open('SI-EXISTE.txt', 'a')
                    f.write(str(victima))
                    f.close()

                Carga()

            elif "outlook" in salida:
                victima = correo[0] + "@" + correo[1]
                print(victima)
                print("{} < EL correo es: > ".format(Fore.WHITE) + salida + "{}".format(Fore.RESET))
                driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()
                Carga()
                try:
                    driver.find_element_by_xpath('//*[@id="PasswordInput"]').send_keys("jajajaj")
                    print(
                        "{} [ {} X {} ] {} < EL CORREO NO EXISTE > {}".format(Fore.BLUE, Fore.RED, Fore.BLUE, Fore.RED,
                                                                              Fore.RESET))
                    print("{} ________________________________________ {}".format(Fore.WHITE, Fore.RESET))
                    f = open('NO-EXISTE.txt', 'a')
                    f.write(victima)
                    f.close()
                except NoSuchElementException as exception:
                    print("{} [ {} + {} ] {} EL correo ya existe :( {}".format(Fore.BLUE, Fore.GREEN, Fore.BLUE,
                                                                               Fore.GREEN, Fore.RESET))
                    print("{} ________________________________________ {} ".format(Fore.WHITE, Fore.RESET))
                    f = open('SI-EXISTE.txt', 'a')
                    f.write(victima)
                    f.close()
                Carga()
            else:
                victima = correo[0] + "@" + correo[1]
                print(victima)
                print("{} < EL correo es: > ".format(Fore.WHITE) + salida + "{}".format(Fore.RESET))
                print("{} [ERROR]: {} CORREO ELECTRONICO NO SOPORTADO {} ".format(Fore.RED, Fore.WHITE, Fore.RESET) + salida)
                print("{} ________________________________________ {} ".format(Fore.WHITE, Fore.RESET))
                f = open('OTRO-DOMINIO.txt', 'a')
                f.write(victima)
                f.close()
            Carga()
            driver.close()
    except FileNotFoundError:
        LogoTwo()
        print("EL archivo no existe en este directorio, vuelva a iniciar")






if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
