fp = open(r"C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\new.html","w")
f2 = open(r"C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\new.txt","r")
p=f2.read()
f2.close()
fp.write('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
  
    <title>HTML 5 Boilerplate</title>
  </head>
  <body background="C:/Users/urvas/OneDrive/Desktop/Arithemania-2.0/songRecommender/data/bg.jpg">
  
	<script src="index.js"></script>
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/'''+p+'''?utm_source=generator" width="75%" height="500" frameBorder="0" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture" loading="lazy"></iframe>

  </body>
</html>''')

fp.close()

import os
os.system(r"C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\new.html")