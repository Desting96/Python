#
# Complete the timeConversion function below.
#
def timeConversion(s):

    hh = int(s[0:2])
    if (s.find("PM") > 0):
        if hh == 12:
            s = s[0:s.find("PM")]
        else:
            hh += 12
            s = s[0:s.find("PM")]
            s = s.replace(s[0:2], str(hh))
        return s
    elif (s.find("AM") > 0):
        hh += 12
        s = s[0:s.find("AM")]
        if (hh >= 24):
            hh = hh - hh
            s = s.replace(s[0:2], "0" + str(hh))
        return s

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)
