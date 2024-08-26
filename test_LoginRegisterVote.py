from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

class ObjectRegisterPage():
    pageUrl = "https://buggy.justtestit.org"
    registerButton = (By.LINK_TEXT, "Register")
    username = (By.ID, "username")
    firstName = (By.ID, "firstName")
    lastName = (By.ID, "lastName")
    password = (By.ID, "password")
    confirmPassword = (By.ID, "confirmPassword")
    registerFormButton = (By.CLASS_NAME, "btn-default")
    loginForm = (By.NAME, "login")
    passwordForm = (By.NAME, "password")
    successButton = (By.CLASS_NAME, "btn-success")
    logo = (By.CLASS_NAME, "navbar-brand")


class Data():
    user = "David032"
    fName = "David"
    lName = "Ledesma"
    pWord = "HolaHo12*"
    confPassword = "HolaHo12*"
    commentArea = "Que hermoso auto"

class VotePage():
    popularMake = (By. CSS_SELECTOR, "a[href='/make/ckl2phsabijs71623vk0']")
    popularModel = (By.CSS_SELECTOR, "a[href='/model/ckl2phsabijs71623vk0|ckl2phsabijs71623vqg']")
    overallRating = (By.CSS_SELECTOR, "a[href='/overall']")
    commentArea = (By.CLASS_NAME, "form-control")





######Pruebas para la creación de usuario######
def test_CreateUser():
    driver.get(ObjectRegisterPage.pageUrl)
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ObjectRegisterPage.registerButton)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.username)).send_keys(Data.user)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ObjectRegisterPage.firstName)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ObjectRegisterPage.firstName)).send_keys(Data.fName)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.lastName)).send_keys(Data.lName)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.password)).send_keys(Data.pWord)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.confirmPassword)).send_keys(Data.confPassword)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.registerFormButton)).click()
    time.sleep(5)
    assert(driver.find_element(By.CSS_SELECTOR, ".result")).text == "Registration is successful"




####Pruebas para iniciar seision con el ususario recien creado####
def test_Login():
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.logo)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.loginForm)).send_keys(Data.user)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.passwordForm)).send_keys(Data.pWord)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.successButton)).click()
    time.sleep(10)
    assert(driver.find_element(By.CSS_SELECTOR, ".disabled")).is_displayed()

###Pruebas para votar por el auto más popular###
def test_PopularModelCar():
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(VotePage.popularModel)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(VotePage.commentArea)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(VotePage.commentArea)).send_keys(Data.commentArea)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ObjectRegisterPage.successButton)).click()
    time.sleep(10)
    assert(driver.find_element(By.CLASS_NAME, "card-text")).text == "Thank you for your vote!"


