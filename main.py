from urllib.request import urlopen
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json
from tkinter.scrolledtext import ScrolledText
import shutil
from termcolor import colored
import threading
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from selenium.webdriver.support.ui import Select
from crawlers.utils.printlog import print_log as prt
import openpyxl
