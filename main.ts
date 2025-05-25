basic.forever(function () {
    basic.showNumber(input.soundLevel())
    serial.writeNumbers([input.soundLevel(), 255])
})
