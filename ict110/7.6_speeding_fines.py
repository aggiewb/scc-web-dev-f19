'''
This is a program that accepts a speed limit and a clocked speed and either
prints a message that indicates the speed was illegal or prints the amount
of the fine if the speed is illegal.

Aggie Wheeler Bateman

11/7/19
'''

#SPEEDING_TICKET_FINE = $50
#ADDITIONAL_FINE_PER_MPH = $5
#ADDITIONAL_FINE_OVER_90_MPH = $200


def determineLegality (speedLimit, clockedSpeed):
    milesOverSpeed = clockedSpeed - speedLimit
    fine = 50 + (5 * milesOverSpeed)
    extremeFine = fine + 200

    if speedLimit < clockedSpeed and clockedSpeed <= 90:
        print("The clocked speed was ILLEGAL. The fine is ${0}.".format(fine))

    elif clockedSpeed > 90:
        print("The clocked speed was VERY ILLEGAL. The fine is ${0}.".format(extremeFine))

    else:
        print("The clocked speed was LEGAL.")
    

determineLegality(50, 50)
    
