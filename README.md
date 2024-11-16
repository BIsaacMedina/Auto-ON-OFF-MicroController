# Auto-ON-OFF-MicroController
MicroPython code that turns PC ON and OFF when properly wired.

GPIO pin 15 outputs 3.3v to keep power to the motherboard pin. When power is breafly turned off it results in power being switched either off or on. If pc is on the power needs to be turned off for 5 seconds. If pc is off power needs to be switched off for 1 second. The light (Pin 25) blinks to show the board is running the program. GPIO pin 16 takes input and monitors if the pc is giving output. If it is, it's on.

## Notes

connect to pc via motherboard pins. you need to measure the length you'll need from mounting it under the PSU.

### Time is printed for testing purposes. Remove before release.
