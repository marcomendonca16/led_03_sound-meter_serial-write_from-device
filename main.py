def on_forever():
    basic.show_number(input.sound_level())
    serial.write_numbers([input.sound_level(), 255])
basic.forever(on_forever)
