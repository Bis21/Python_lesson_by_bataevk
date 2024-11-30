----------

# **Углублённая шпаргалка по KivyMD**


## **1. Основные концепции KivyMD**

### **Что такое KivyMD?**

KivyMD — это библиотека для создания мобильных приложений с поддержкой Material Design. Она включает готовые элементы интерфейса, такие как кнопки, текстовые поля, меню и т.д.

-   **Когда использовать KivyMD?**  
    Если вам нужен современный и удобный интерфейс с минимальными усилиями, KivyMD поможет сократить время разработки благодаря готовым решениям.
    
-   **Особенность структуры проекта:**
    
    -   `main.py`: хранит логику приложения.
    -   `.kv`-файл: содержит разметку интерфейса, отделяя её от кода. Это упрощает поддержку и масштабирование проекта.



## **2. Работа с экранами через ScreenManager**

### **Описание**

`ScreenManager` позволяет переключаться между экранами. Это удобно, когда ваше приложение содержит несколько логических блоков, например, главное меню, настройки или игровой процесс.

----------

### **Пример реализации (Python-код):**

```python
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

class MenuScreen(Screen):
    pass

class QuizScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(QuizScreen(name='quiz'))
        return sm

MyApp().run()

```

----------

### **Пример реализации (kv-файл):**

```yaml
ScreenManager:
    MenuScreen:
    QuizScreen:

<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: "Главное меню"
        halign: "center"

<QuizScreen>:
    name: 'quiz'
    MDLabel:
        text: "Экран викторины"
        halign: "center"

```

----------

### **Объяснение отличий:**

1.  **Python:**
    
    -   Более универсален, позволяет динамически добавлять или удалять экраны.
    -   Подходит, если количество экранов зависит от данных или пользовательских настроек.
2.  **kv-файл:**
    
    -   Удобен для статической структуры, где экраны заранее известны.
    -   Облегчает визуализацию интерфейса, так как вся разметка собрана в одном месте.
    - Проще объявлять ScreenManager:
    ```
    ScreenManager:
	    MenuScreen:
	    QuizScreen:
    ```

### **Спосбо смены экрана через событие кнопки**:
`app.root.current` = '[ИМЯ ЭКРАНА]'
```kv
on_release: app.root.current = "quiz"
```


## **3. Кнопки в KivyMD**

### **Описание**

Кнопки являются основным способом взаимодействия пользователя с приложением. В KivyMD есть несколько типов кнопок, например:

-   `MDRaisedButton`: с приподнятым эффектом.
-   `MDFlatButton`: плоская кнопка.
-   `MDRectangleFlatButton`: плоская кнопка с границей.

----------

### **Пример реализации (Python-код):**

```python
from kivymd.uix.button import MDRaisedButton

class MyApp(MDApp):
    def build(self):
        return MDRaisedButton(
            text="Нажми меня",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

```

----------

### **Пример реализации (kv-файл):**

```yaml
MDRaisedButton:
    text: "Нажми меня"
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

```


## **4. Текстовые метки (MDLabel)**

### **Описание**

Метки отображают текст. Выравнивание (`halign`) и стиль (`font_style`) позволяют настроить их под нужды приложения.

----------

### **Пример (kv-файл):**

```yaml
MDLabel:
    text: "Добро пожаловать!"
    font_style: "H4"
    halign: "center"

```

----------

### **Пример (Python-код):**

```python
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel(
            text="Добро пожаловать!",
            halign="center",
            font_style="H4"
        )

```



## **5. Обработка событий кнопок**

### **Описание**

Событие `on_release` позволяет кнопкам вызывать функции. Можно использовать как Python, так и `kv`.

----------

### **Пример (kv-файл):**

```yaml
MDRaisedButton:
    text: "Ответить"
    on_release: app.check_answer("Ответ")

```

----------

### **Пример (Python-код):**

```python
class MyApp(MDApp):
    def build(self):
        button = MDRaisedButton(
            text="Ответить",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=lambda x: self.check_answer("Ответ")
        )
        return button

    def check_answer(self, answer):
        print(f"Проверка ответа: {answer}")

```

----------


### **Объяснение :**

В обоих случаях, при нажатии кнопка использует написанный заранее метод  check_answer() . Так что даже перед тем как kv-разметке использовать вызов этого метода при нажатии кнопки, его надо написать в классе MyApp

## **6. Передача данных между экранами**

### **Описание**

Чтобы экраны могли обмениваться данными, можно использовать свойства самого приложения.

----------

### **Пример реализации:**

#### **Python-код:**

```python
class MyApp(MDApp):
    def build(self):
        self.score = 0  # Счётчик
        return ScreenManager()

```

#### **kv-файл:**

```yaml
<QuizScreen>:
    Button:
        text: "Увеличить счёт"
        on_release: app.score += 1

```

### **ИЛИ** *(через метод)*
#### **python:**
```python
class MyApp(MDApp):
    def build(self):
        self.score = 0  # Счётчик
        return ScreenManager()
    def update_score(self):
        self.score += 1
        print(f"Текущий счёт: {self.score}")
```
#### **kv-файл:**
```yaml
<QuizScreen>:
    Button:
        text: "Увеличить счёт"
        on_release: app.update_score()

```
----------
#### Метод для получения экрана в питоне
```python
# Получение экрана по его имени
self.root.get_screen("YOUR_SCREEN_NAME") 
# получение текущего экрана
self.root.current_screen 

```

---
# **Дополнительные материалы**

## **7. Навигация: AppBar и Drawer**

### **Описание**

Для удобной навигации между частями приложения можно использовать `MDToolbar` и `MDNavigationDrawer`.

-   **`MDToolbar`**: верхняя панель приложения, где можно разместить заголовок, кнопки и меню.
-   **`MDNavigationDrawer`**: боковая панель, содержащая пункты меню для перехода между экранами.

----------

### **Пример использования (Python-код):**

```python
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.app import MDApp


class HomeScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name='home'))

        # Настройка Toolbar и Drawer
        self.toolbar = MDToolbar(title="Главная")
        self.toolbar.left_action_items = [["menu", lambda x: self.toggle_drawer()]]

        self.drawer = MDNavigationDrawer()
        self.drawer.add_widget(ScreenManager())

        return self.toolbar

    def toggle_drawer(self):
        self.drawer.set_state("toggle")


MyApp().run()

```

----------

### **Пример использования (kv-файл):**

```yaml
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'home'
    MDToolbar:
        title: "Главная"
        left_action_items: [["menu", lambda x: app.toggle_drawer()]]
    MDNavigationDrawer:
        id: nav_drawer
        MDLabel:
            text: "Меню"
            halign: "center"

```

----------

### **Рекомендация**:

Используйте `MDNavigationDrawer` для создания интуитивно понятного интерфейса в приложениях с несколькими разделами. Если у приложения одно окно — достаточно `MDToolbar`.

----------

## **8. Работа с текстовыми полями (MDTextField)**

### **Описание**

`MDTextField` используется для ввода текста пользователем.

-   Можно задать подсказку (`hint_text`), ограничения (`max_text_length`) и проверку (`helper_text`).

----------

### **Пример реализации (Python-код):**

```python
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return MDTextField(
            hint_text="Введите имя",
            helper_text="Имя не может быть пустым",
            helper_text_mode="on_error",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint_x=0.8,
        )

MyApp().run()

```

----------

### **Пример реализации (kv-файл):**

```yaml
MDTextField:
    hint_text: "Введите имя"
    helper_text: "Имя не может быть пустым"
    helper_text_mode: "on_error"
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    size_hint_x: 0.8

```

----------

### **Советы**:

-   Используйте `helper_text_mode` для пользовательских подсказок и предупреждений.
-   Для числовых вводов используйте `input_filter: "int"`.

----------

## **9. Использование всплывающих окон (MDDialog)**

### **Описание**

`MDDialog` помогает выводить уведомления, предупреждения или собирать данные от пользователя.

----------

### **Пример использования (Python-код):**

```python
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return MDRaisedButton(
            text="Показать окно",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.show_dialog,
        )

    def show_dialog(self, *args):
        self.dialog = MDDialog(
            title="Приветствие",
            text="Добро пожаловать в приложение!",
            buttons=[
                MDRaisedButton(
                    text="Закрыть",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ],
        )
        self.dialog.open()

MyApp().run()

```

----------

### **Пример использования (kv-файл):**

```yaml
MDRaisedButton:
    text: "Показать окно"
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    on_release: app.show_dialog()

```

----------

### **Советы**:

-   Используйте `MDDialog` для отображения критически важной информации.
-   Для сбора данных добавьте в диалог текстовые поля (`MDTextField`).

----------

## **10. Таблицы данных (MDDataTable)**

### **Описание**

`MDDataTable` используется для отображения структурированных данных в виде таблицы.

----------

### **Пример использования (Python-код):**

```python
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            rows_num=5,
            column_data=[
                ("No.", dp(30)),
                ("Имя", dp(50)),
                ("Возраст", dp(30)),
            ],
            row_data=[
                ("1", "Иван", "25"),
                ("2", "Мария", "30"),
                ("3", "Алексей", "20"),
            ],
        )

MyApp().run()

```

----------

### **Советы**:

-   Настраивайте ширину столбцов через `dp`.
-   Используйте `row_data` для заполнения таблицы динамическими данными.

----------
