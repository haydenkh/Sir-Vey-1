class form:
   """ used for creating the forms on webpage"""

   def set_type(self, bool):
       #if false it's MC 
       self.qtype=bool;
       
   def set_question(self,str):
       self.question = str;

   def set_question_length(self,int):
       self.length = int;

   def set_anon(self,bool):
       self.anon = bool;

   
