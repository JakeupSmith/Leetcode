class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0 
        char = "1"
        current_row = 0
        prev_row = 0
        
        #Number of beams in element (1) Gets multiplied by the next element that HAS beams
        
        for i in bank:
            current_row = 0
            for j in i:
                if j == char:
                    current_row += 1
            if current_row == 0:
                continue
            total = total + (current_row * prev_row)
            prev_row = current_row
        return total
                
            