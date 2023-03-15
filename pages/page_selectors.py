class AuthPage:
    LOGIN_FIELD = "#passp-field-login"
    PHONE_FIELD = "#passp-field-phone"
    SIGN_IN_BTN = "[id='passp:sign-in']"
    RESTORE_LINK = "[id='field:link-login'] [data-t='link:default']"
    LOGIN_TAB = "[data-type='login']"
    PHONE_TAB = "[data-type='phone']"
    LOGIN_ALERT = "[id='field:input-login:hint'][role='alert']"
    PHONE_ALERT = "[id='field:input-phone:hint'][role='alert']"
    TITLE = "[data-t='title']"


class WelcomePage:
    WELCOME_PAGE_ATTR = "[data-t='page:welcome']"
    INPUT_PASSWORD = "[data-t='field:input-passwd']"


class RegPage:
    REG_PAGE_ATTR = "[data-t='field:phoneCode']"


class DzenPage:
    PROFILE_ELEMENT = "[class='dzen-header-desktop__profileMenu-3q']"
    PROFILE_TEXT_CONTENT = "[class='header-profile-menu__menu'] [class='Menu-MenuItemTextContent']"
