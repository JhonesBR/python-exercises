# Access the value of key ‘history’ from the below dict
# Solution: https://github.com/JhonesBR

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict["class"]["student"]["marks"]["history"])