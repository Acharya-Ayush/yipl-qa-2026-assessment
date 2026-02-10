import pytest
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from utils.config import BASE_URL

@pytest.mark.smoke
def test_valid_signup_and_login(page):
    signup_page = SignupPage(page)
    signup_page.navigate()
    signup_page.signup()
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login()  # uses credentials from .env