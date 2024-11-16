# Auto-ON-OFF-MicroController
MicroPython code that turns PC ON and OFF when properly wired.

![pico](https://github.com/user-attachments/assets/382c9f28-7702-44bd-893c-0421ab5e37b3)

GPIO pin 15 (marked red) outputs 3.3v to keep power to the motherboard pin. When power is breafly turned off it results in power being switched either off or on. If pc is on the power needs to be turned off for 5 seconds. If pc is off power needs to be switched off for 1 second. The built in LED (Pin 25) blinks to show the board is running the program. GPIO pin 16 (marked green) takes input and monitors if the pc is giving output. If it is, the pc is on. The VSYS pin (marked blue) provides power to the board from the standby (Purple) line on the PSU. Ground pin (marked black) grounds the power recieved from the PSU. 

#### Set up instructions
Blue line will be soldered or spliced into the pruple standby line from the PSU, black will be soldered or taped to the side of the case, green and red will have the female connector on the end attached to the motherboard and male soldered into the hole on the pico. 

## Notes

connect to pc via motherboard pins. you need to measure the length you'll need from mounting it under the PSU.

### Time is printed for testing purposes. Remove before release.
