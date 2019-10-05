import pytest
import time

def test_button(browser, request):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    lang = request.config.getoption("language")
    if lang == "fr":
        browser.implicitly_wait(10)
        check = browser.find_element_by_css_selector("button.btn-lg.btn-primary[value='Ajouter au panier']")
        assert check != "Ajouter au panier", f"Button not found :("
    elif lang == "es":
        browser.implicitly_wait(10)
        check = browser.find_element_by_css_selector("button.btn-lg.btn-primary[value='Añadir al carrito']")
        assert check != "Añadir al carrito", f"Button not found :("
    else:
        raise pytest.UsageError("--language should be fr or es "
                                "(Тест не обязательно должен поддерживать все языки по задаче)")

