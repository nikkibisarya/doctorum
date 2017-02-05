import requests
import json
filePath = 'C:/Users/Boltak/Desktop/Doctorum/'
textFileNames = ['q1.txt', 'q2.txt','q3.txt']
    
zipWords = ['90001/', '90023/']
allWords = ["the common cold", "flu", "pneumonia", "food poisoning", "sinusitus"]
    
def text_file_to_vec(filePath, allWords, textFileNames, zipWords):
    
    for i in range(0, len(zipWords)):
        for j in range(0, len(textFileNames)):
            with open(''.join([filePath,zipWords[i],textFileNames[j]]), 'r') as file:

                for line in file:
                    for word in line.split():
                        if word==allWords[0] or word==allWords[2] or word==allWords[3] or word==allWords[4]:
                            index = allWords.index(word)

                            
    
                            feat= {'attributes' : {"OBJECTID" : 60, "FID" : 60, "zipcode" : 90210, word : 1}}
       
                            payload = {'f': 'json'}
    
                            url = 'http://services1.arcgis.com/uRIm5IkWjDXybgFb/arcgis/rest/services/LA_Nhood_Change/FeatureServer/0http://services1.arcgis.com/uRIm5IkWjDXybgFb/arcgis/rest/services/LA_Nhood_Change/FeatureServer/0?f=json'
    
                            print(json.dumps(payload))
        
                            r = requests.get(url)
        
                            print(r.json())  
                             
    return None

def main():
    finalDict = text_file_to_vec(filePath, allWords, textFileNames, zipWords)
    print(finalDict)
main()