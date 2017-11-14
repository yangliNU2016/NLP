sentence = "isn't python so much fun?"
tokens = sentence.split()
for token in tokens:
 if token == "isn't":
  print "is"
  print "not" 
 elif token == "fun?":
  print "fun"
  print "?"
 else:
  print token
