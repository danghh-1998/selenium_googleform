# Selenium Google Form

## Step 1: Install Google Chrome Webdriver

- Go to https://chromedriver.chromium.org/downloads and choose the download corresponding to your version number and operating system.

## Step 2: Install Selenium

```bash
pip install selenium
```

### Step 3: Configuring Selenium Webdriver

```python
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('-incognito')
option.headless = True
browser = webdriver.Chrome(executable_path='../resources/chromedriver', options=option)
```

## Step 4: Finding the elements in the Webpage

- Go to https://docs.google.com/forms/d/e/1FAIpQLSfMWIja0X-OQtNtwdX5rYBZyJQXN8AgyBWLnoE_TeWFBcPkTg/viewform
- Open Google Chrome dev tools and find the elements that you want to use

## Step 5: Interacting with the elements

- Use `find_elements_by_class_name()` or `find_element_by_id()` method to select elements
- To fill input form, use `send_keys()` method
- To select radio button or click button, use `click()` method
