from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time


def select_dropdown(driver, id, text):
    name = Select(driver.find_element(By.ID, id))
    name.select_by_visible_text(text)
    time.sleep(0.5)

def enter_text(driver, id, text):
    name = driver.find_element(By.ID, id)
    name.send_keys(text)
    time.sleep(0.5)

def test_case_1():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:5000/")
    # time.sleep(3)

    # Navigation bar
    nav_bar = driver.find_element(By.XPATH, "/html/body/nav")
    nav_bar_items = nav_bar.find_elements(By.TAG_NAME, 'li')

    # Make prediction
    make_pred = driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[3]/a").click()
    # time.sleep(3)

    select_dropdown(driver, 'gender', 'Male')
    enter_text(driver, 'age', '52')
    select_dropdown(driver, 'hypert', 'Yes')
    select_dropdown(driver, 'heart_d', 'Yes')
    select_dropdown(driver, 'marital', 'Married')
    select_dropdown(driver, 'w_class', 'Private')
    select_dropdown(driver, 'resident', 'Rural')
    enter_text(driver, 'avg_gl', '125')
    enter_text(driver, 'c_loss', '52')
    select_dropdown(driver, 'smoking', 'Smokes')

    # Submit form input
    driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[11]/button").click()

    # Check result
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/p").text
    assert result == "Congratulations! Based on your inputs you are not likely to get a stroke."
    time.sleep(1)
    driver.close()

def test_case_2():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:5000/")
    # time.sleep(3)

    # Navigation bar
    nav_bar = driver.find_element(By.XPATH, "/html/body/nav")
    nav_bar_items = nav_bar.find_elements(By.TAG_NAME, 'li')

    # Make prediction
    make_pred = driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[3]/a").click()
    time.sleep(3)
    
    select_dropdown(driver, 'gender', 'Female')
    enter_text(driver, 'age', '85')
    select_dropdown(driver, 'hypert', 'No')
    select_dropdown(driver, 'heart_d', 'Yes')
    select_dropdown(driver, 'marital', 'Married')
    select_dropdown(driver, 'w_class', 'Private')
    select_dropdown(driver, 'resident', 'Urban')
    enter_text(driver, 'avg_gl', '125')
    enter_text(driver, 'c_loss', '52')
    select_dropdown(driver, 'smoking', 'Smokes')

    # Submit form input
    driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[11]/button").click()
    
    # Check result
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/p").text
    assert result == "Congratulations! Based on your inputs you are not likely to get a stroke."
    time.sleep(1)
    driver.close()

def test_case_3():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:5000/")
    # time.sleep(3)

    # Navigation bar
    nav_bar = driver.find_element(By.XPATH, "/html/body/nav")
    nav_bar_items = nav_bar.find_elements(By.TAG_NAME, 'li')

    # Make prediction
    make_pred = driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[3]/a").click()
    # time.sleep(3)

    select_dropdown(driver, 'gender', 'Female')
    enter_text(driver, 'age', '25')
    select_dropdown(driver, 'hypert', 'No')
    select_dropdown(driver, 'heart_d', 'No')
    select_dropdown(driver, 'marital', 'Single or Divorced')
    select_dropdown(driver, 'w_class', 'Government Job')
    select_dropdown(driver, 'resident', 'Urban')
    enter_text(driver, 'avg_gl', '125')
    enter_text(driver, 'c_loss', '36')
    select_dropdown(driver, 'smoking', 'Never Smoked')

    # Submit form input
    driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[11]/button").click()

    # Check result
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/p").text
    assert result == "Congratulations! Based on your inputs you are not likely to get a stroke."
    time.sleep(1)
    driver.close()
