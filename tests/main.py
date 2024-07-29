from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://inteli-exec-m3.streamlit.app/Treinar_modelo")
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[2]/div/section/button').send_keys("/Users/otaviovasconceloss/code/codeinteli/dockerproject/Inteli-Exec/data/processed/InteliBank_Inadimplencia_de_credito__Avaliacao.xlsx")
time.sleep(5)
