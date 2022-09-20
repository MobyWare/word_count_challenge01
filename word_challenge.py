#%%
from typing import List, Tuple
words = ['baby', 'allison']
string1 = 'aayyby'

#%%
def get_letter_count_tuple(input_word:str) -> List[Tuple[str,int]]:
  result = []
  if not input_word:
    return result
  sorted_letters = [x for x in input_word]
  if len(sorted_letters) < 1:
    return result
  
  sorted_letters.sort()
  previous_letter = sorted_letters[0]
  current_letter_count = 0
  for letter in sorted_letters:
    if previous_letter != letter:
      result.append((previous_letter,current_letter_count))
      current_letter_count = 0
    current_letter_count+=1
    previous_letter = letter
  
  result.append((previous_letter,current_letter_count))
  return result

#%%
print(get_letter_count_tuple(string1))

