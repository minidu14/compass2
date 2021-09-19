input.onPinPressed(TouchPin.P0, function () {
    basic.showArrow(ArrowNames.South)
})
input.onButtonPressed(Button.A, function () {
    basic.showArrow(ArrowNames.West)
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showArrow(ArrowNames.SouthEast)
})
input.onButtonPressed(Button.B, function () {
    basic.showArrow(ArrowNames.North)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showArrow(ArrowNames.NorthEast)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showArrow(ArrowNames.East)
})
basic.forever(function () {
	
})
