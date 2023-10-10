# Extracting-Security-Knowledge

## Description
This program was developed to extract security measures from the BSI's IT-Grundschutzkompendium. This was preceded by my bachelor thesis, in which I identified an ontology into which the knowledge from the Grundschutzkompendium 
should be integrated. With this program a first partial step was fulfilled. The program is used to extract the knowledge from the XML version of the IT-Grundschutzkompendium. 
In the next sub-step, which may also be developed, the knowledge should then be fed into the ontology. 

## Installation
You can simply clone the repository. 

# Usage
This program was developed to enable automated knowledge extraction from the IT-Grundschutzkompendium. This knowledge should be available in such a way that it is subsequently possible to integrate the knowledge into an ontology. 
The ontology in question is the ontology of Stefan Fenz and Andreas Ekelhart (https://dl.acm.org/doi/abs/10.1145/1533057.1533084). 
For this it is necessary that the knowledge is present after the extraction in a certain form and/or is described with certain relations. 
Example: A measure mitigates a vulnerability. 
However, there is the problem that the IT-Grundschutzkompendium cannot be adopted 1 to 1 in the ontology. For example, there are no vulnerabilities in the IT-Grundschutzkompendium. 
While these are present in the ontology of Stefan Fenz. Thus, these vulnerabilities had to be created. For this the API of ChatGPT was used. 
It was given the control and the threat as input. From these it should then formulate vulnerabilities. 

# Current State of the Folders 
In the current state the programm was executed for 34 "Bausteine". These can be found in the "Notwendige Bausteine.txt". These are the "Bausteine" which are needed for the "Handwerksprofil".
If you are interested in other "Bausteine" then please follow the "Configuration" Chapter. Else you can have a look in the Sub-Folders of the "Single Excel Files" folder to get an idea of how ChatGPT created new Relations and Vulnerabilities.

# Configuration
Following steps should be taken if you are interested in other "Bausteine" then the ones specified in the "Notwendige Bausteine.txt"
You can also have a look into the "Initialized" Branch. Here I have reset everything. You can follow the below Steps according to your needs. 
## Initialization of data Folder
### API Key:
The program accesses the API of ChatGPT. To enable this, an API key must be present. This must be stored under the directory "data" in a text file with the name api.txt. 
### Notwendige Bausteine.txt:
You might not be interested in all the "Bausteine" in the IT-Grundschutzkompendium. For this reason, those "Bausteine" that are to be extracted are to be inserted line by line in this file. 
The identifier must be specified in combination with the name of the "Baustein". 
### XML Version of the IT-Grundschutzkompendium:
There is an XML version of each IT-Grundschutzkompendium. If you are not interested in the one from 2023, this must also be saved in this folder, as all information is extracted from this file.
### All-Threats.txt and All-Controls.txt: 
This file contains all the threats and their description for the IT-Grundschutzkompendium from 2023. If a newer one is to be used, the threats should be updated manually.
The "All-Controls.txt" File can be either kept or if you use other "Bausteine" then in the "Notwendige Bausteine.txt" you should delete the content. This File is filled automatically by the programm.
### Cross-reference table:
A cross-reference table is also supplied with each IT-Grundschutzkompendium. This contains which threat can be mitigated by which control. This table must also be stored in the data directory. 
## Other Adjustments
### Root-Folder
A root folder must be created in which all sub folders are stored. The sub folders are the individual "Bausteine" that are to be extracted. By default, this Folder is the "Single Excel Files" Folder.
### Adjusting Main.py
In the code directory, the path to all respective files must then be adjusted in the Main.py class.

# Known Problems
It should be noted that the program can run for several hours. For previous test runs, costs of about $2 were incurred for 34 "Bausteine". Furthermore, the expenses on the console should be considered. 
At the beginning of the program, the program may not find the description for some Controls. The console will then indicate that these should be inserted manually. Further it can be that for some "Bausteine" the context size is too large. 
A solution could be to increase the context size of the ChatGPT model. In the default setting a context size of 4k tokens is used. GPT 3.5-turbo is used as the model. 

## Authors and acknowledgment
Fatih Ünal