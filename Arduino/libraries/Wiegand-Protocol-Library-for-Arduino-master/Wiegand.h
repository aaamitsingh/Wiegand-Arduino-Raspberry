#ifndef _WIEGAND_H
#define _WIEGAND_H

#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif

class WIEGAND {

public:
	WIEGAND();
	void begin();
	void begin(int pinD0, int pinIntD0, int pinD1, int pinIntD1, int pinD2, int pinIntD2, int pinD3, int pinIntD3);
	bool available();
	unsigned long getCode();
	unsigned long getReaderID();
	int getWiegandType();

	
private:
	static void ReadD0();
	static void ReadD1();
	static void ReadD2();
	static void ReadD3();
	static bool DoWiegandConversion ();
	static unsigned long GetCardId (volatile unsigned long *codehigh, volatile unsigned long *codelow, char bitlength);
	
	static volatile unsigned long 	_cardTempHigh;
	static volatile unsigned long 	_cardTemp;
	static volatile unsigned long 	_lastWiegand;
	static volatile int				_bitCount;	
	static int				_wiegandType;
	static unsigned long	_code;
	static unsigned int	_readerID;
};

#endif
