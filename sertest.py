import serial
import datetime
import MySQLdb



from gpiozero import LED
from time import sleep

door0 = LED(17)
door1 = LED(27)









# Open database connection
db = MySQLdb.connect("localhost","username","password","database" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor2 = db.cursor()



ser = serial.Serial('/dev/ttyACM0',9600)


while 1 :
	a=ser.readline()
	b=a.split(",")
	print "card",b[0]
	
	try :
		query="SELECT * FROM members where memberCard = '%s'" % b[0]
		print query
		cursor.execute(query)
		results = cursor.rowcount
		
                print "Rowcount:",results
		print "exists"
	except :            
            print "db error"

        if results ==1:
                query2="INSERT INTO doorevents (cardid,doorid,detail) values ('%s','%s','%s')" % (b[0],b[1],'Auth')
                try:
                        print query2
                        cursor2.execute(query2)
                        db.commit()
                        print "door:",b[1]
                        if int(float(b[1]))==0 :
                                sleep(0.5)
                                door0.on()
                                sleep(3)
                                door0.off()
                                
                        if int(float(b[1]))==1 :
                                sleep(0.5)
                                door1.off()
                                sleep(1)
                                door1.on()
				sleep(1)

				
                        
                                        
                except :
                        print "db error 2"
                        db.rollback()
        else :
                query3="INSERT INTO doorevents (cardid,doorid,detail) values ('%s','%s','%s')" % (b[0],b[1],'Deny')
                try:
                        print query3
                        cursor2.execute(query3)
                        db.commit()
                except :
                        print "db error 3"
                        db.rollback()
