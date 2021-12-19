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
    enter_text(driver, 'age', '25')
    select_dropdown(driver, 'hypert', 'No')
    select_dropdown(driver, 'heart_d', 'No')
    select_dropdown(driver, 'marital', 'Single or Divorced')
    select_dropdown(driver, 'w_class', 'Never Worked')
    select_dropdown(driver, 'resident', 'Rural')
    enter_text(driver, 'avg_gl', '175')
    enter_text(driver, 'c_loss', '18')
    select_dropdown(driver, 'smoking', 'Never Smoked')

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
    enter_text(driver, 'age', '30')
    select_dropdown(driver, 'hypert', 'No')
    select_dropdown(driver, 'heart_d', 'No')
    select_dropdown(driver, 'marital', 'Single or Divorced')
    select_dropdown(driver, 'w_class', 'Never Worked')
    select_dropdown(driver, 'resident', 'Rural')
    enter_text(driver, 'avg_gl', '120')
    enter_text(driver, 'c_loss', '25')
    select_dropdown(driver, 'smoking', 'Never Smoked')

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

    select_dropdown(driver, 'gender', 'Male')
    enter_text(driver, 'age', '35')
    select_dropdown(driver, 'hypert', 'No')
    select_dropdown(driver, 'heart_d', 'Yes')
    select_dropdown(driver, 'marital', 'Married')
    select_dropdown(driver, 'w_class', 'Private')
    select_dropdown(driver, 'resident', 'Urban')
    enter_text(driver, 'avg_gl', '200')
    enter_text(driver, 'c_loss', '30')
    select_dropdown(driver, 'smoking', 'Smokes')

    # Submit form input
    driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[11]/button").click()

    # Check result
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/p").text
    assert result == "Please consult a doctor. Based on your inputs you are likely to get stroke."
    time.sleep(1)
    driver.close()

def test_case_4():

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
    enter_text(driver, 'age', '40')
    select_dropdown(driver, 'hypert', 'No')
    select_dropdown(driver, 'heart_d', 'Yes')
    select_dropdown(driver, 'marital', 'Married')
    select_dropdown(driver, 'w_class', 'Children')
    select_dropdown(driver, 'resident', 'Rural')
    enter_text(driver, 'avg_gl', '190')
    enter_text(driver, 'c_loss', '10')
    select_dropdown(driver, 'smoking', 'Formerly Smoked')

    # Submit form input
    driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[11]/button").click()

    # Check result
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/p").text
    assert result == "Please consult a doctor. Based on your inputs you are likely to get stroke."
    time.sleep(1)
    driver.close()

def test_case_5():

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
    enter_text(driver, 'age', '45')
    select_dropdown(driver, 'hypert', 'Yes')
    select_dropdown(driver, 'heart_d', 'Yes')
    select_dropdown(driver, 'marital', 'Married')
    select_dropdown(driver, 'w_class', 'Self Employed')
    select_dropdown(driver, 'resident', 'Urban')
    enter_text(driver, 'avg_gl', '210')
    enter_text(driver, 'c_loss', '37')
    select_dropdown(driver, 'smoking', 'Smokes')

    # Submit form input
    driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[11]/button").click()

    # Check result
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/p").text
    assert result == "Congratulations! Based on your inputs you are not likely to get a stroke."
    time.sleep(1)
    driver.close()
