class Time(object):
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_elapsed_time(self):
        return self._hours * 60 * 60 + self._minutes * 60 + self._seconds

    def set_elapsed_time(self, seconds):
        overflow = seconds % (24 * 60 * 60)
        self._hours = overflow / (60 * 60)
        remainder = overflow % (60 * 60)
        self._minutes = remainder / 60
        self._seconds = remainder % 60

    def __str__(self):
        return "Time: %d:%d:%d"%(self._hours, self._minutes, self._seconds)

    elapsed_time=property(get_elapsed_time,set_elapsed_time)

##My anw
class Time(object):
    def __init__(self,hours, minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        
    def get_elapsed_time(self):
        return int(self.hours*3600+self.minutes*60+self.seconds)
        
    def set_elapsed_time(self,elapsed_time):
        h=24*(elapsed_time/3600.0/24-int(elapsed_time/3600.0/24))       
        self.hours=int(h)
        self.minutes=int(((h-int(h))*3600)/60.0)
        self.seconds=round((((h-int(h))*3600.0)/60.0-self.minutes)*60,0)
        
    def __str__(self):
        str='Time: %d:%d:%d'%(self.hours,self.minutes,self.seconds)
        return str
        
    elapsed_time=property(get_elapsed_time,set_elapsed_time)

t = Time (10 , 19, 10)
print t.elapsed_time
t.elapsed_time = 555550
print t.elapsed_time
print t