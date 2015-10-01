import hashlib
c = 'a'
while c != 'x':
    file_name = 'x64' + c + '.rpf'
    print(file_name)
    output = open(file_name, 'w')
    c = chr(ord(c)+1)
    
original_md5 = ['683610e269ba60c5fcc7a9f6d1a8bfd5', '70af24cd4fe2c8ee58edb902f018a558', '2a0f6f1c35ad567fe8e56b9c9cc4e4c6',
                'c8757b052ab5079c7749bcce02538b2e', 'e5416c0b0000dad4014e0c5e9b878ff9', '5c6fc965d56ae6d422cd6cbe5a65a3a5',
                '1d8a64b337c3e07dffec0f53530cdb8e', 'fe657d9282df303b080c3a2f6771c9ea', 'bb271d313467465d62c75e208236487b',
                '143deee4c7699b9f07ef21d43ae0915b', 'da2c88b4ca69c99a86868a9433084a9d', 'f4307b005a3e90192f235959621781d1',
                'a1304d84875747aa7405465d37d3c6fb', 'c48a14fe1c301360a16e8b0c5472fd1d', '6715a4eabbbc8868f15630bf917db49a',
                '6ad56befada1db7cccd9cea7834c825b', 'ff6d09527d7fdc005d3fa78435e09c8a', '1465c9da5cc17b68f14915b6c1d815bc',
                '2c6e61201eb4f60d5c3c1e9ae6d67a32', '4c15a54a4c9573d7a0bcfa4689d9d1ed', '2c9cff0cc5f99ad2218e4c4de39881b7',
                'db647120263d0282b6f6c555f6112a1c', '46a4abe50bfc78c30c0173d888cf2c4a']

print(original_md5[2])
print(len(original_md5))

output.write('File corrotti: \n')
for i in original_md5:
    print(i)
    output.write(i + '\n')

print('md5 del file a')
with open('x64a.rpf') as file_to_check:
    # read contents of the file
    data = file_to_check.read().encode('utf-8')
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()
       
    # Finally compare original MD5 with freshly calculated
    print(md5_returned)
    

