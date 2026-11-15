class Solution(object):
    def scoreOfString(self, s):
        total_score = 0
        prev_ascii = None
        
        for char in s:
            current_ascii = ord(char)
            
            if prev_ascii is not None:
                diff = current_ascii - prev_ascii
                if diff < 0:
                    diff = -diff
                total_score += diff
                
            prev_ascii = current_ascii
            
        return total_score