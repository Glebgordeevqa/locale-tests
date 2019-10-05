import pytest
import time

def test_button(browser, request):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(10)
    lang = request.config.getoption("language")
    if lang == "fr":
        check = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket").text
        assert check == "Ajouter au panier", f"Button not found :("
    elif lang == "es":
        check = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket").text
        assert check == "Añadir al carrito", f"Button not found :("
    else:
        raise pytest.UsageError("--language should be fr or es "
                                "(Тест не обязательно должен поддерживать все языки по задаче)")

