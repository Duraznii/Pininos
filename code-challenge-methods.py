class Student:
    scores = [65, 75, 85, 95]
   
    def average_score(self):
        return sum(self.scores) / len(self.scores)
    
result = Student().average_score()
print(result)
        
    

