### Пошаговое руководство по созданию мобильного приложения с Kivy и KivyMD

Это руководство поможет тебе понять, как использовать Python и библиотеки Kivy и KivyMD для создания простого мобильного приложения. Не волнуйся, если что-то не сразу будет понятно — каждый шаг подробно объяснен, и ты научишься делать свое приложение!

### Что нам нужно:
1. Установить Python (если еще не установлен).
2. Установить библиотеки Kivy и KivyMD.

#### Установка библиотек
Открой командную строку или терминал и установи Kivy и KivyMD с помощью команд:
```bash
pip install kivy kivymd
```

Теперь, когда у нас есть все необходимое, начнем создавать наше первое приложение.

### Шаг 1: Создаем основной файл приложения
Создаем файл `main.py`. Этот файл будет содержать основную логику приложения.

1. В `main.py` мы определим экран нашего приложения и несколько простых экранов для переходов. Это как будто ты строишь комнаты в доме — каждая комната отвечает за свою задачу.
2. Начнем с базовой структуры, используя классы `App` и `ScreenManager` из KivyMD.

```python
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

MyApp().run()
```

**Объяснение кода:**
- `MainScreen` и `SecondScreen` — это наши экраны.
- `ScreenManager` управляет переключением между экранами.
- `MyApp` запускает приложение.

### Шаг 2: Создаем файл интерфейса `myapp.kv`
Теперь добавим файл `myapp.kv`, который определит, как будет выглядеть интерфейс нашего приложения. Этот файл отделит дизайн от кода, что сделает его более аккуратным и понятным.

```kv
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Главный экран'
            halign: 'center'
        MDRaisedButton:
            text: 'Перейти на второй экран'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'second'

<SecondScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Второй экран'
            halign: 'center'
        MDRaisedButton:
            text: 'Назад'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'main'
```

**Объяснение кода:**
- **`BoxLayout`**: используется для расположения элементов один за другим вертикально (сверху вниз).
- **`MDLabel`**: надпись на экране.
- **`MDRaisedButton`**: кнопка, которая выполняет переход на другой экран. Функция `on_release` переключает экран, когда кнопка нажата.

### Шаг 3: Запускаем приложение
Запусти `main.py`, чтобы проверить, как работает приложение. Ты увидишь главный экран с кнопкой, которая при нажатии переключит тебя на второй экран. 

### Шаг 4: Добавляем больше экранов
Теперь добавим еще экраны, чтобы приложение стало интереснее. В `main.py` добавим еще пару классов для дополнительных экранов.

```python
class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

# Добавим эти экраны в ScreenManager
class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        return sm
```

В файле `myapp.kv` добавим разметку для новых экранов:

```kv
<ThirdScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Третий экран'
            halign: 'center'
        MDRaisedButton:
            text: 'Назад'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'main'

<FourthScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Четвертый экран'
            halign: 'center'
        MDRaisedButton:
            text: 'Назад'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'main'
```

В этом шаге мы добавим кнопки на главный экран, которые будут переключать нас на третий и четвертый экраны. Эти кнопки позволят пользователю легко перемещаться по приложению.

### Шаг 5: Добавляем кнопки для переходов на третий и четвертый экраны

Внесем изменения в файл `myapp.kv`, чтобы добавить кнопки для переходов на третий и четвертый экраны в интерфейс `MainScreen`.

Обновленный код в `myapp.kv` для главного экрана будет выглядеть так:

```kv
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Главный экран'
            halign: 'center'
        
        MDRaisedButton:
            text: 'Перейти на второй экран'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'second'
        
        MDRaisedButton:
            text: 'Перейти на третий экран'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'third'
        
        MDRaisedButton:
            text: 'Перейти на четвертый экран'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'fourth'
```

### Объяснение
Теперь на главном экране у нас есть три кнопки:
- **Первая кнопка** отправляет нас на второй экран.
- **Вторая кнопка** отправляет нас на третий экран.
- **Третья кнопка** отправляет нас на четвертый экран.

### Итог
Запусти `main.py`, и теперь у тебя будет полноценный главный экран с кнопками, которые позволяют перемещаться между всеми экранами приложения.


### Шаг 6: Добавляем интерактивность
Добавим текстовое поле, куда пользователь сможет ввести текст. Этот текст отобразится на экране при нажатии на кнопку.

В `SecondScreen` в файле `myapp.kv` изменим код так:

```kv
<SecondScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDTextField:
            id: text_field
            hint_text: 'Введите текст'
            helper_text: 'Напишите что-то'
            helper_text_mode: 'on_focus'
        MDRaisedButton:
            text: 'Показать текст'
            pos_hint: {'center_x': 0.5}
            on_release: label.text = text_field.text
        MDLabel:
            id: label
            text: ''
            halign: 'center'
        MDRaisedButton:
            text: 'Назад'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'main'
```

Теперь добавим функцию в `MyApp` в `main.py`, чтобы показывать текст из `MDTextField` в `MDLabel`:

```python
class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        return sm

    def show_text(self, text):
        self.root.get_screen('second').ids.label.text = text
```

Чтобы добавить текст с прокруткой на четвертый экран, мы используем виджет `ScrollView`, который позволяет прокручивать содержимое. Текст будет размещен внутри `Label`, и при необходимости можно будет прокручивать его вертикально.

### Шаг 5: Добавляем текст с прокруткой на четвертый экран

Внесем изменения в разметку четвертого экрана в файле `myapp.kv`, добавив `ScrollView` и `Label` с длинным текстом.

```kv
<FourthScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDLabel:
            text: 'Четвертый экран с прокручиваемым текстом'
            halign: 'center'
        
        ScrollView:
            MDLabel:
                id: scroll_label
                text: 'Это текст с прокруткой' * 20  # Повторение текста для примера
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                halign: 'left'
                valign: 'top'

        MDRaisedButton:
            text: 'Назад'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'main'
```

### Объяснение:
- **`ScrollView`**: позволяет прокручивать содержимое, если оно не помещается на экране.
- **`MDLabel` внутри `ScrollView`**: используется для текста. Мы установили `size_hint_y: None` и задали высоту с помощью `height: self.texture_size[1]`, чтобы текст прокручивался вертикально.
- **`text: ' '.join(['Это текст с прокруткой. '] * 20)`**: генерирует длинный текст для прокрутки (20 повторений фразы "Это текст с прокруткой.").

### Результат
Теперь, запустив `main.py`, ты сможешь увидеть четвертый экран с длинным текстом, который можно прокручивать.


### Подведем итоги
- Мы создали несколько экранов, использовали кнопки для перехода между ними и добавили поле для ввода текста.
- Использовали файл `.kv` для определения интерфейса, чтобы разделить логику и дизайн, что сделало код понятнее.

**Поздравляем!** Ты создал свое первое приложение с использованием Kivy и KivyMD. Продолжай эксперименты, добавляя больше функций и изучая новые виджеты!
