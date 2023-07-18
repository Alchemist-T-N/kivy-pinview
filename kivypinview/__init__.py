from kivy.graphics import RoundedRectangle, Color
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

kv = """
<PinView>
    id:pinview
    box_count:4
    size_hint:.99,None
    height:(self.width-((self.box_count-1)*self.box_spacing))//self.box_count
    text_color:[1,0,0,1]
    font_name:''
    font_size:70
    box_size_hint:1,1
    box_spacing:30
    box_radius:[30]
    box_bg_color:[1,1,0,1]
    default_text:'-'
    box_bg_image:None
    markup:True
    pos_hint:{'center_x':.5, 'center_y':.5}
    TextInput:
        id:otp
        pos:self.parent.pos
        background_color:[1,1,1,0]
        foreground_color:[0,0,0,0]
        cursor_color:[1,1,1,0]
        input_type:'number'
        on_text:
            root._what_on_otp(self.text)
    BoxLayout:
        id:box_holder
        spacing:pinview.box_spacing
        pos:self.parent.pos
"""

Builder.load_string(kv)


class Box(Label):
    def __init__(self, box_radius=10, box_bg_color=None, box_bg_image=None, **kwargs):
        super().__init__(**kwargs)
        if box_bg_color is None:
            box_bg_color = [0, 0, 1, 1]
        self.radius = box_radius
        self.source = box_bg_image
        self.box_bg_color = box_bg_color

    def on_size(self, *args):
        with self.canvas.before:
            self.canvas.before.clear()
            Color(rgba=self.box_bg_color) if len(self.box_bg_color) > 3 else Color(rgb=self.box_bg_color)
            RoundedRectangle(size=self.size, pos=self.pos, radius=self.radius, source=self.source)


class PinView(FloatLayout):
    otp = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = None

    def on_kv_post(self, base_widget):
        self.count = self.box_count
        for i in range(self.count):
            try:
                self.ids.box_holder.add_widget(Box(
                    font_name=self.font_name if self.font_name != '' else self.font_name,
                    color=self.text_color,
                    text=self.default_text,
                    font_size=self.font_size,
                    size_hint=self.box_size_hint,
                    markup=self.markup,
                    box_radius=self.box_radius,
                    box_bg_color=self.box_bg_color,
                    box_bg_image=self.box_bg_image
                ))
            except IOError:
                self.ids.box_holder.add_widget(Box(
                    color=self.text_color,
                    text=self.default_text,
                    font_size=self.font_size,
                    markup=self.markup,
                    size_hint=self.box_size_hint,
                    box_radius=self.box_radius,
                    box_bg_color=self.box_bg_color,
                    box_bg_image=self.box_bg_image
                ))

    def on_otp(self, who, otp):
        pass

    def _what_on_otp(self, text):
        # maintain text length according to the box count
        if len(text) > self.count:
            self.ids.otp.text = text[0:self.count]
        # set the text to their respective boxes
        for i, box in enumerate(reversed(self.ids.box_holder.children)):
            try:
                box.text = text[i]
            except IndexError:
                box.text = self.default_text
        # if full otp is entered, invoke the on_otp
        if len(text) == self.box_count:
            self.otp = text

