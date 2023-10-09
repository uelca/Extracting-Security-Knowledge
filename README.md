# Extracting-Security-Knowledge

## Description
This program was developed to extract security measures from the BSI's IT-Grundschutzkompendium. This was preceded by my bachelor thesis, in which I identified an ontology into which the knowledge from the Grundschutzkompendium 
should be integrated. With this program a first partial step was fulfilled. The program is used to extract the knowledge from the XML version of the IT-Grundschutzkompendium. 
In the next sub-step, which may also be developed, the knowledge should then be fed into the ontology. 

## Installation
You can simply clone the repository. 

# Usage
This program was developed to enable automated knowledge extraction from the IT-Grundschutzkompendium. This knowledge should be available in such a way that it is subsequently possible to integrate the knowledge into an ontology. 
The ontology in question is the ontology of Stefan Fenz and Andreas Eckelhart (https://dl.acm.org/doi/abs/10.1145/1533057.1533084). 
For this it is necessary that the knowledge is present after the extraction in a certain form and/or is described with certain relations. 
Example: A measure mitigates a vulnerability. 
However, there is the problem that the IT-Grundschutzkompendium cannot be adopted 1 to 1 in the ontology. For example, there are no vulnerabilities in the IT-Grundschutzkompendium. 
While these are present in the ontology of Stefan Fenz. Thus, these vulnerabilities had to be created. For this the API of ChatGPT was used. 
It was given the measure and the threat as input. From these it should then formulate vulnerabilities. 
# Configuration
## Initialization of data Folder
### API Key
The program accesses the API of ChatGPT. To enable this, an API key must be present. This must be stored under the directory "data" in a text file with the name api.txt. 
### Notwenidge Bausteine.txt
We might not be interested in all of the "Bausteine" in the IT-Grundschutzkompendium. For this reason, those "Bausteine" that are to be extracted are to be inserted line by line in this file. 
The identifier must be specified in combination with the name of the "Baustein".
### XML Version of the IT-Grundschutzkompendium
There is an XML version of each IT-Grundschutzkompendium. This must also be saved in this folder, as all information is extracted from this file.
### All-Threats.txt 
This file contains all the threats for the IT-Grundschutzkompendium from 2023. If a newer one is to be used, the threats should be updated. 
### Cross reference table
A cross-reference table is also supplied with each IT-Grundschutzkompendium. This contains which threat can be mitigated by which control. This table must also be stored in the data directory. 
## Root-Folder
A root folder must be created in which all sub folders are stored. The sub folders are the individual "Bausteine" that are to be extracted.
## Adjusting Main.py
In the code directory, the path to all respective files must then be adjusted in the Main.py class. 

# Known Problems
It should be noted that the program can run for several hours. For previous test runs, costs of about $10 were incurred for 35 "Bausteine". Furthermore, the expenses on the console should be considered. 
At the beginning of the program, the program may not find the description for some Controls. The console will then indicate that these should be inserted manually. Further it can be that for some "Bausteine" the context size is too large. 
A solution could be to increase the context size of the ChatGPT model. In the default setting a context size of 4k tokens is used. GPT 3.5-turbo is used as the model. 

## Authors and acknowledgment
Fatih Ünal
