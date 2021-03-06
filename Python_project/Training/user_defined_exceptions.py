class SpeedLimitError(Exception):
    """
        Base Class for UserDefined Exception
    """
    
    def __init__(self, speed):
        self.speed = speed
        
    def __str__(self):
        """
            Invoked when : print e where e is of type SpeedLimitError
        """
        
        return "Vehicle Speed is " + str(self.speed)
    
class SpeedBelowLimit(SpeedLimitError):
    """
        Speed Below limit Exception
    """
    
    def __init__(self, speed):
        SpeedLimitError.__init__(self, speed)
        
class SpeedAboveLimit(SpeedLimitError):
    """
        Speed Above limit Exception
    """
    
    def __init__(self, speed):
        SpeedLimitError.__init__(self, speed)
        
if __name__ == "__main__":
    while True:
        try:
            speed = eval(input("Enter Speed: "))
            
            if speed < 20:
                raise SpeedBelowLimit(speed)
            elif speed > 80:
                raise SpeedAboveLimit(speed)
            else:
                print("Speed In Limit")
                break
            
        except SpeedBelowLimit as e:
            print("Speed Below limit " + str(e))
        
        except SpeedAboveLimit as e:
            print("Speed Above limit " + str(e))