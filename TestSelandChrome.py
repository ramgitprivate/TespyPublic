from selenium import webdriver

# Set the path to the ChromeDriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=chromedriver_path)
 
# Navigate to a website (change the URL to your desired website)
url = 'https://www.example.com'
driver.get(url)

# Verify the page title
expected_title = 'Example Domain'
actual_title = driver.title

if expected_title in actual_title:
    print(f'Test Passed! Page title is: {actual_title}')
else:
    print(f'Test Failed! Expected title: {expected_title}, Actual title: {actual_title}')

# Close the browser
driver.quit()