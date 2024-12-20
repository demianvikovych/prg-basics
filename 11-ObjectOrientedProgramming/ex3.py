class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1  

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        if new_channel_no > 0:  
            self.channel_no = new_channel_no
        else:
            print("Invalid channel number. Please enter a positive number.")

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")

tv = TV()

tv.show_status()      
tv.turn_on()           
tv.show_status()       
tv.set_channel(5)      
tv.show_status()       
tv.turn_off()          
tv.show_status()       
