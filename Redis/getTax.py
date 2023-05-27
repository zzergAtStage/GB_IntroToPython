from selenium import webdriver

# Set up Selenium webdriver with headless option
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Navigate to the page with the dynamic content
url = 'https://mapr.tax.gov.me/ic/#/verify?iic=AA60EF1B8A50A0DC90D24DB6BD413FF5&tin=02984121&crtd=2023-05-03T11:47:46%2002:00&ord=305030222&bu=pl199ps858&cr=zz298he255&sw=tk106hm033&prc=3.37'
driver.get(url)

# Wait for the dynamic content to load
driver.implicitly_wait(120)

# Get the page source after the dynamic content has loaded
html = driver.page_source

# Write the page source to a file
with open('page.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Quit the webdriver
driver.quit()
