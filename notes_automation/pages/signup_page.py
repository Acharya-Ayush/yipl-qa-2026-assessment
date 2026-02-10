from utils.config import BASE_URL, EMAIL, PASSWORD, NAME
import time

class SignupPage:
     def __init__(self, page):
          self.page = page

          # Locators
          self.signup_link = page.locator("//a[@data-testid='open-register-view']")
          self.name_input = page.locator("//input[@name='name']")
          self.email_input = page.locator("//input[@name='email']")
          self.password_input = page.locator("//input[@name='password']")
          self.password_input_confirmation = page.locator("//input[@name='confirmPassword']")
          self.submit_button = page.locator("//button[@data-testid='register-submit']")
          self.success_message = page.locator("//b[text()='User account created successfully']")
          self.alert_message = page.locator("//div[@data-testid='alert-message']")

     def navigate(self):
          self.page.goto(BASE_URL)

     def signup(self):
          """
          Perform signup action.
          If confirm_password is None, use password for confirmation.
          """
          self.signup_link.click()
          self.name_input.fill(NAME)
          self.email_input.fill(EMAIL)
          self.password_input.fill(PASSWORD)
          self.password_input_confirmation.fill(PASSWORD)
          self.submit_button.click()
          return self.check_signup_result() # Check result immediately after signup attempt
     
     
     def check_signup_result(self):
          self.page.wait_for_load_state("networkidle")

          # error message
          if self.alert_message.is_visible(timeout=5000):
               msg = self.alert_message.inner_text()
               print(f"Signup failed: {msg}")
               return False, msg

          # success message
          if self.success_message.is_visible(timeout=5000):
               msg = self.success_message.inner_text()
               print(f"Signup successful: {msg}")
               return True, msg

          raise Exception("Neither error nor success message appeared.")



          
            