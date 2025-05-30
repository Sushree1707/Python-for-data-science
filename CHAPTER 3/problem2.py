#replacing name and date

letter = ''' Dear <|Name|>, You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", " Suraj").replace("<|Date|>", "28th January"))