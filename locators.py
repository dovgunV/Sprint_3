class Locator:
    btn_personal_account = "//a[@href='/account']"  # Кнопка "Личный кабинет".
    btn_registration_for_authorization = "//a[contains(text(), 'Зарегистрироваться')]"  # Кнопка "Зарегистрироваться" на странице авторизации.
    input_name = "//label[contains(text(), 'Имя')]/following-sibling::input"  # Поле ввода имени.
    input_email = "//label[contains(text(), 'Email')]/following-sibling::input"  # Поле ввода электронной почты.
    input_password = (
        "//input[@name='Пароль']"  # Поле ввода "Пароль" в форме регистрации
    )
    btn_register = "//button[contains(text(), 'Зарегистрироваться')]"  # Кнопка "Зарегистироваться" на странице регистрации.
    header_authorization = (
        "//h2[contains(text(), 'Вход')]"  # Заголовок на странице входа.
    )
    message_incorrect_password = "//p[contains(text(), 'Некорректный пароль')]"  # Сообщение об ошибке "Некорректный пароль".
    header_registration = "//h2[contains(text(), 'Регистрация')]"  # Заголовок на странице регистрации.
    logo = "//div[@class='AppHeader_header__logo__2D0X2']"  # Логотип.
    btn_login_main = "//button[contains(text(), 'Войти в аккаунт')]"  # Кнопка "Войти" на основной странице.
    btn_login = "//button[contains(text(), 'Войти')]"  # Кнопка "Войти" на странице авторизации.
    btn_checkout = "//button[contains(text(), 'Оформить заказ')]"  # Кнопка "Оформить заказ" на основной странице.
    btn_login_register = "//a[contains(text(), 'Войти')]"  # Кнопка "Войти" на странице регистрации.
    btn_restore_password = "//a[contains(text(), 'Восстановить пароль')]"  # Кнопка "Восстановить пароль" на странице авторизации.
    btn_login_restore_password = "//a[contains(text(), 'Войти')]"  # Кнопка "Войти" на странице восстановления пароля.
    btn_exit = "//button[contains(text(), 'Выход')]"  # Кнопка "Выход" в личном кабинете.
    btn_constructor = "//p[contains(text(), 'Конструктор')]"  # Кнопка "Конструктор" в личном кабинете.
    header_main = "//h1[contains(text(), 'Соберите бургер')]"  # Заголовок "Соберите бургер" на основной странице.
    btn_rolls = "//span[contains(text(), 'Булки')]"  # Кнопка "Булки" на основной странице.
    header_rolls = "//h2[contains(text(), 'Булки')]"  # Заголовок "Булки" на основной странице.
    btn_sauces = "//span[contains(text(), 'Соусы')]"  # Кнопка "Соусы" на основной странице.
    header_sauces = "//h2[contains(text(), 'Соусы')]"  # Заголовок "Соусы" на основной странице.
    btn_fillings = "//span[contains(text(), 'Начинки')]"  # Кнопка "Начинки" на основной странице.
    header_fillings = "//h2[contains(text(), 'Начинки')]"  # Заголовок "Начинки" на основной странице.
