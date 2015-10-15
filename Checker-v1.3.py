#===============================================================================
# Author: Tecchia Dario
# Date: 2015/09/26 16:01
# Original Idea: http://stackoverflow.com/questions/16874598/how-do-i-calculate-the-md5-checksum-of-a-file-in-python
# Copyright policy: Make it what you want,remember to quote author and original idea.
# How to use: Put this file in the GTA V main directory and run.
# How it works: Examines the md5 code of the .rpf files to check the integrity, corrupted files will be referred to
#               a text file called corrupted_files.txt
# P.S.: Sorry for my bad english :)
#===============================================================================
# Autore: Tecchia Dario
# Data: 2015/09/26 16:01
# Idea Originale: http://stackoverflow.com/questions/16874598/how-do-i-calculate-the-md5-checksum-of-a-file-in-python
# Politica di copyright: Fatene cio' che volete, ricordare di citare autore e idea originale.
# Come funziona: Esamina il codice md5 dei file .rpf per verificarne l'integritï¿½, i file corrotti verranno
#                indicati su un file di testo chiamato corrupted_files.txt
# Come usare: Inserire questo file nella main directory di GTA V ed eseguirlo.
#===============================================================================

# Import hashlib library (md5 method is part of it)
import hashlib
# Import time library (time method is part of it)
import time
# The char after x64
c = 'a'
# List with corrupted file
corrupted_file = []
# A txtfile where corrupted files are listed
output = open('Corrupted_files.txt', 'w')

# List of original md5 goes here
original_md5 = ['683610e269ba60c5fcc7a9f6d1a8bfd5', '70af24cd4fe2c8ee58edb902f018a558', '2a0f6f1c35ad567fe8e56b9c9cc4e4c6',
                'c8757b052ab5079c7749bcce02538b2e', 'e5416c0b0000dad4014e0c5e9b878ff9', '5c6fc965d56ae6d422cd6cbe5a65a3a5',
                '1d8a64b337c3e07dffec0f53530cdb8e', 'fe657d9282df303b080c3a2f6771c9ea', 'bb271d313467465d62c75e208236487b',
                '143deee4c7699b9f07ef21d43ae0915b', 'da2c88b4ca69c99a86868a9433084a9d', 'f4307b005a3e90192f235959621781d1',
                'a1304d84875747aa7405465d37d3c6fb', 'c48a14fe1c301360a16e8b0c5472fd1d', '6715a4eabbbc8868f15630bf917db49a',
                '6ad56befada1db7cccd9cea7834c825b', 'ff6d09527d7fdc005d3fa78435e09c8a', '1465c9da5cc17b68f14915b6c1d815bc',
                '2c6e61201eb4f60d5c3c1e9ae6d67a32', '4c15a54a4c9573d7a0bcfa4689d9d1ed', '2c9cff0cc5f99ad2218e4c4de39881b7',
                'db647120263d0282b6f6c555f6112a1c', '46a4abe50bfc78c30c0173d888cf2c4a']

#Start the timer
start_time = time.time()

# Open, close, read file and calculate MD5 on its contents
for i in original_md5:
    # File to check
    file_name = 'x64' + c + '.rpf'
    with open(file_name, 'rb') as file_to_check:
        # read contents of the file
        data = file_to_check.read()
        # pipe contents of the file through
        md5_returned = hashlib.md5(data).hexdigest()
        
        # Finally compare original MD5 with freshly calculated
        print('Checking ' + file_name + "\nCorrect md5: " + i + "\nFile md5: " + md5_returned)
        if i == md5_returned:
            print ('MD5 verified.')
            c = chr(ord(c)+1) # Increment c, like c++ or (c=c+1)
        elif i != md5_returned:
            print ("MD5 verification failed!.")
            # Add the corrupted file name to the list
            corrupted_file.append(file_name)
            c = chr(ord(c)+1) # Increment c, like c++ or (c=c+1)
#   print(file_name, c)

# Print the number of the corrupted files
print(len(corrupted_file) + "Errors!")
# Print the execution time
print("--- %s seconds ---" % (time.time() - start_time))

# Print and write in a txtfiles the corrupted files
output.write('Corrupted files: \nTo be sure, check with another program! \n')
for c in corrupted_file:
    output.write(c + '\n')
    print(c)
