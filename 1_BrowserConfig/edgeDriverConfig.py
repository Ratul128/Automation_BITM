from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def edge_launch():
    edriver=webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))

edge_launch()