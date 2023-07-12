import re
class Phrase:
      def __init__(self,content):
          self.content= str(content)

      def ispalindrome(self):
        # processed_content=self.content.lower()
        return self._processed_content() == reverse(self._processed_content())
      
      def _processed_content(self):
         return self.letters_and_digits().lower()
      def letters_and_digits(self):
        #   the_letters=[]
        #   for character in self.content:
        #       if re.search(r"[a-zA-Z]",character):
        #           the_letters.append(character)
          return "".join(re.findall(r"[a-zA-Z\d]",self.content))
def reverse(string):
     return "".join(reversed(string))