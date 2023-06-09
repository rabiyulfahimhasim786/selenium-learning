#print("helloworld")
from PIL import Image
#from selenium import webdriver
from PIL import Image, ImageFilter
import time  
import base64
# import pytesseract 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\chromedriver\chromedriver.exe")
driver.get("https://www.allstatesusadirectory.com/submit.php")

# def get_captcha(driver, element, path):
#     # now that we have the preliminary stuff out of the way time to get that image :D
#     location = element.location
#     size = element.size
#     # saves screenshot of entire page
#     driver.save_screenshot(path)

#     # uses PIL library to open image in memory
#     image = Image.open(path)

#     left = location['x']
#     top = location['y'] + 140
#     right = location['x'] + size['width']
#     bottom = location['y'] + size['height'] + 140

#     image = image.crop((left, top, right, bottom))  # defines crop points
#     image.save(path, 'png')  # saves new cropped image
    

#     # captcha = pytesseract.image_to_string(image) 
#     # captcha = captcha.replace(" ", "").strip()
#     # print(captcha)
#     return path




# download image/captcha
ele_captcha  = driver.find_element("xpath","/html/body/div[4]/div[2]/form/table/tbody/tr[12]/td[2]/img")
# get_captcha(driver, img, "captcha.png")

img_captcha_base64 = driver.execute_async_script("""
    var ele = arguments[0], callback = arguments[1];
    ele.addEventListener('load', function fn(){
      ele.removeEventListener('load', fn, false);
      var cnv = document.createElement('canvas');
      cnv.width = this.width; cnv.height = this.height;
      cnv.getContext('2d').drawImage(this, 0, 0);
      callback(cnv.toDataURL('image/jpeg').substring(22));
    }, false);
    ele.dispatchEvent(new Event('load'));
    """, ele_captcha)

# save the captcha to a file
with open(r"captcha.jpg", 'wb') as f:
    f.write(base64.b64decode(img_captcha_base64))


from PIL import Image
import pytesseract

# Load the captcha image
image_path = 'captcha.jpg'  # Replace with the path to your captcha image
captcha_image = Image.open(image_path)

# Convert the image to grayscale
captcha_gray = captcha_image.convert('L')

# Use pytesseract to extract text from the captcha image
extracted_text = pytesseract.image_to_string(captcha_gray)

# Process the extracted text (optional)
processed_text = extracted_text.strip().lower()

print("Extracted Text:", extracted_text)
print("Processed Text:", processed_text)
time.sleep(10)
driver.close()