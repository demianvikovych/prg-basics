class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        if 1 <= new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no
        else:
            print("Invalid channel number. Please select a valid channel.")

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        if not self.channels:
            print("No channels available.")
        else:
            print("Channel list:")
            for i, channel in enumerate(self.channels, start=1):
                print(f"{i}. {channel}")

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                current_channel = self.channels[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({current_channel})")
            else:
                print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")

tv = TV()
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"])
tv.turn_on()
tv.set_channel(4)
tv.show_status()
tv.set_channel(7)
tv.show_status()
tv.set_channel(2)
tv.show_status()
tv.set_channel(10)
tv.show_status()
tv.turn_off()
tv.show_status()
