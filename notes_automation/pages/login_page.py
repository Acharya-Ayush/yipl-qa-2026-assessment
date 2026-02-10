from utils.config import EMAIL, PASSWORD
import time

class LoginPage:
     def __init__(self, page):
          self.page = page

          # Locators
          self.login_click = page.locator("//a[text()='Login']")
          self.email_input = page.locator("//input[@name='email']")
          self.password_input = page.locator("//input[@name='password']")
          self.logIn_button = page.locator("//button[@data-testid='login-submit']")
          self.profile_icon = page.locator("text=Logout")
          self.alert_message = page.locator("//div[@data-testid='alert-message']")
          
     def navigate(self, url):
          self.page.goto(url)

     def login(self):
          self.login_click.click()
          self.email_input.fill(EMAIL)
          self.password_input.fill(PASSWORD)
          self.logIn_button.click()
          
          # Check login result
          status, message = self.is_login_successful()
          assert status, f"Login failed → {message}"
          
     def is_login_successful(self):
          """
          Check if login succeeded or failed based on messages or profile icon.
          Returns tuple: (status: bool, message: str)
          """

          # Wait for the page to settle
          self.page.wait_for_load_state("networkidle")

          # Case 1 → alert message appears (login failed)
          if self.alert_message.is_visible(timeout=5000):
               msg = self.alert_message.inner_text()
               print(f"Login failed: {msg}")
               return False, msg

          # Case 2 → profile icon appears (login succeeded)
          if self.profile_icon.is_visible(timeout=5000):
               print("Login successful.")
               return True, "Login successful"

          # Case 3 → neither appeared → unknown state
          raise Exception("Login result not detected: No alert or profile icon found.")
