# RaspWiegand2
2 reader Wiegand using 4 interrupt pins on Arduino Micro
Most examples of Wiegand reader circuits only allow for one reader to control one door
This is a modified version to allow two readers connected to INT0, INT1, INT2 and INT3 of a Genuino Micro
Modifications also allow returning of reader ID.
Arduino puts values to USB serial which is ready by Raspberry Pi python script which in turn validates cardID with database and drives the relay associated with the reader.


