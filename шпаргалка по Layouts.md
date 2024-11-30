### Основные Layouts в Kivy

1. **BoxLayout**
   - Располагает виджеты в одном направлении: горизонтально или вертикально.
   - Параметры:
     - `orientation`: 'vertical' или 'horizontal'.
     - `spacing`: расстояние между виджетами.
     - `padding`: отступы внутри layout.
   - Пример:
     ```python
     BoxLayout:
         orientation: 'vertical'
         spacing: 10
         padding: 10
         Button:
             text: 'Button 1'
         Button:
             text: 'Button 2'
     ```

2. **GridLayout**
   - Располагает виджеты в виде сетки (таблицы).
   - Параметры:
     - `cols`: количество столбцов.
     - `rows`: количество строк.
     - `spacing`: расстояние между виджетами.
     - `padding`: отступы внутри layout.
   - Пример:
     ```python
     GridLayout:
         cols: 2
         rows: 2
         spacing: 10
         padding: 10
         Button:
             text: 'Button 1'
         Button:
             text: 'Button 2'
         Button:
             text: 'Button 3'
         Button:
             text: 'Button 4'
     ```

3. **StackLayout**
   - Располагает виджеты в одном направлении, но с возможностью переноса на новую строку или столбец.
   - Параметры:
     - `orientation`: 'lr-tb' (слева направо, сверху вниз), 'tb-lr', 'rl-tb', 'bt-lr'.
     - `spacing`: расстояние между виджетами.
     - `padding`: отступы внутри layout.
   - Пример:
     ```python
     StackLayout:
         orientation: 'lr-tb'
         spacing: 10
         padding: 10
         Button:
             text: 'Button 1'
             size_hint: (None, None)
             size: (100, 100)
         Button:
             text: 'Button 2'
             size_hint: (None, None)
             size: (100, 100)
     ```

4. **AnchorLayout**
   - Располагает виджеты относительно углов или центра layout.
   - Параметры:
     - `anchor_x`: 'left', 'center', 'right'.
     - `anchor_y`: 'top', 'center', 'bottom'.
   - Пример:
     ```python
     AnchorLayout:
         anchor_x: 'center'
         anchor_y: 'center'
         Button:
             text: 'Button'
             size_hint: (None, None)
             size: (100, 100)
     ```

5. **RelativeLayout**
   - Располагает виджеты относительно координат layout.
   - Параметры:
     - `pos_hint`: словарь с ключами 'x', 'y', 'center_x', 'center_y', 'right', 'top'.
   - Пример:
     ```python
     RelativeLayout:
         Button:
             text: 'Button'
             size_hint: (None, None)
             size: (100, 100)
             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
     ```

6. **ScrollView**
   - Позволяет прокручивать содержимое, если оно не помещается в видимую область.
   - Параметры:
     - `effect_cls`: класс эффекта прокрутки (например, 'ScrollEffect').
     - `scroll_type`: тип прокрутки ('bars', 'content').
   - Пример:
     ```python
     ScrollView:
         effect_cls: 'ScrollEffect'
         BoxLayout:
             orientation: 'vertical'
             size_hint_y: None
             height: self.minimum_height
             Button:
                 text: 'Button 1'
                 size_hint_y: None
                 height: 100
             Button:
                 text: 'Button 2'
                 size_hint_y: None
                 height: 100
             # Добавьте больше кнопок для прокрутки
     ```

### Основные Layouts в KivyMD

1. **MDGridLayout**
   - Аналогичен GridLayout в Kivy, но с дополнительными стилями и функциями KivyMD.
   - Пример:
     ```python
     MDGridLayout:
         cols: 2
         rows: 2
         spacing: 10
         padding: 10
         MDRaisedButton:
             text: 'Button 1'
         MDRaisedButton:
             text: 'Button 2'
         MDRaisedButton:
             text: 'Button 3'
         MDRaisedButton:
             text: 'Button 4'
     ```

2. **MDStackLayout**
   - Аналогичен StackLayout в Kivy, но с дополнительными стилями и функциями KivyMD.
   - Пример:
     ```python
     MDStackLayout:
         orientation: 'lr-tb'
         spacing: 10
         padding: 10
         MDRaisedButton:
             text: 'Button 1'
             size_hint: (None, None)
             size: (100, 100)
         MDRaisedButton:
             text: 'Button 2'
             size_hint: (None, None)
             size: (100, 100)
     ```

3. **MDAnchorLayout**
   - Аналогичен AnchorLayout в Kivy, но с дополнительными стилями и функциями KivyMD.
   - Пример:
     ```python
     MDAnchorLayout:
         anchor_x: 'center'
         anchor_y: 'center'
         MDRaisedButton:
             text: 'Button'
             size_hint: (None, None)
             size: (100, 100)
     ```

4. **MDRelativeLayout**
   - Аналогичен RelativeLayout в Kivy, но с дополнительными стилями и функциями KivyMD.
   - Пример:
     ```python
     MDRelativeLayout:
         MDRaisedButton:
             text: 'Button'
             size_hint: (None, None)
             size: (100, 100)
             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
     ```

5. **MDScrollView**
   - Аналогичен ScrollView в Kivy, но с дополнительными стилями и функциями KivyMD.
   - Пример:
     ```python
     MDScrollView:
         MDList:
             OneLineListItem:
                 text: 'Item 1'
             OneLineListItem:
                 text: 'Item 2'
             # Добавьте больше элементов для прокрутки
     ```

