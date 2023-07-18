# kivy-pinview
This is an android pinview implementation for kivy 
You can use [this platform](https://github.com/Alchemist-T-N/kivy-pinview/issues) to write your content.

#      installation:
        pip install kivypinview

#       uninstall:
        pip uninstall kivypinview

#       kivy-pinview
        This module is built using some ready to use kivy widgets like Label, TextInput, BoxLayout, FloatLayout etc.
        Structure:
                FloatLayout:
                  -> TextInput:
                  -> BoxLayout:
                      -> Labels:
        Working:
                On touching the view, TextInput takes focus and text entered in that is rendered to the Labels and on fully entering data into labels, on_otp(self, caller_obj, otp) is fired which can be overridden.
        Use:
                can be used to take otp(one time password) inputs...
                
#       Example:

        from kivy.lang import Builder
        from kivy.app import App
        from kivypinview import PinView

        kv = """
        #:import PinView pinview.PinView

        PinView:
                size_hint_x:.8
                pos_hint:{'center_x':.5,'center_y':.5}
            #Box Related:
                box_spacing:10
                box_radius:[5, 5]
                box_count:5

            #Text Related:
                text_color:[0,.4,1,1]
                default_text:'-'
                #font_name:'your_font_name.ttf'
                font_size:50
                markup:True
                on_otp:print(self.otp)

             #Box Canvas related:
                box_bg_color:[1,.4,1,1]
                #box_bg_image:'your_bg_image.jpg'
        """

        class MyApp(App):
            def build(self):
                return Builder.load_string(kv)
