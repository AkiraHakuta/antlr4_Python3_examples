class Interval(object):
    """
    Represents an interval. 
    Defined as half-open interval [start,end), which includes the start position but not the end.
    Start and end do not have to be numeric types. 
    """
    
    
    def __init__(self, tokens):
        self.start = tokens[0].tokenIndex
        self.stop = tokens[-1].tokenIndex
        self.member_list = [tokens[0], tokens[-1]]
        
    def __getitem__(self, i):
        return self.member_list[i]
        
        
    
        
         
    
         
