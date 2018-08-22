# Working with databses

## Persistence
- Open a DB file.
- Check if there’s a blockchain stored in it.
- If there’s a blockchain:
-- Create a new Blockchain instance.
-- Set the tip of the Blockchain instance to the last block hash stored in the DB.
- If there’s no existing blockchain:
-- Create the genesis block.
-- Store in the DB.
-- Save the genesis block’s hash as the last block hash.
-- Create a new Blockchain instance with its tip pointing at the genesis block.

Here we are first opening a database. If there are no blocks in it then we will create a Genesis block and if required then we will add some blocks.
But if there are blocks already in the database then we will collect the information about the last block and we use that data to generate further blocks and store in the same database.
This process continues...
Below is the code to perform the above mentioned task



```sh
import hashlib as hasher
import datetime as date
import sys
import sqlite3


conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS blockchain')
#cur.execute('CREATE TABLE blockchain(block INTEGER PRIMARY KEY, data TEXT, hash TEXT, prevhash TEXT, nonce INTEGER)')
cur.execute('select count(*) from blockchain')
total = cur.fetchone()[0]

nonce = 0
blockchain = []



class Block:
  def __init__(self, index, timestamp, data, previous_hash, nonce):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.nonce = nonce  
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + 
               str(self.data) + 
               str(self.previous_hash)+
               str(self.timestamp) + 
               hex(nonce))
    return sha.hexdigest()

#creating genesis Block
def create_genesis_block():
# Manually construct a block with
# index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0", 0) #last parameter is nonce


#adding blocks one-by-one
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash
  this_nonce = last_block.nonce
  return Block(this_index, this_timestamp, this_data, this_hash, this_nonce)


# Create the blockchain and add the genesis block
if(total == 0):
  target_bits = 24
  target = 2 ** (256-target_bits)

  nonce = 0
  while nonce < sys.maxint:
    first_block = create_genesis_block()
    if(long(first_block.hash, 16) < target):
      blockchain.append(first_block)
      previous_block = blockchain[0]
      break
    else:
      nonce = nonce + 1


  print("Genesis Block  has been added to the blockchain!")
  print("Previous Hash: 0")
  print("Hash: {}".format(first_block.hash)) 
  print("data: {}\n".format(first_block.data))
  print("nonce value for block #{}".format(nonce))

  cur.execute('INSERT INTO blockchain (data, hash, prevhash, nonce) VALUES (?,?,?,?)', (first_block.data, first_block.hash, first_block.previous_hash, nonce))
  conn.commit()


    #blockchain = [create_genesis_block()]
    #previous_block = blockchain[0]



# How many blocks should we add to the chain
#  after the genesis block
num_of_blocks_to_add = input("how many blocks would you like to add to the chain")


timestamp = date.datetime.now()
cur.execute('SELECT * from blockchain ORDER BY block DESC limit 1')
last_block_index = cur.fetchone()[0]
print(last_block_index)

cur.execute('SELECT * from blockchain ORDER BY block DESC limit 1')
data = cur.fetchone()[1]
print(data)

cur.execute('SELECT * from blockchain ORDER BY block DESC limit 1')
hash = cur.fetchone()[2]
print(hash)

cur.execute('SELECT * from blockchain ORDER BY block DESC limit 1')
previous_hash = cur.fetchone()[3]
print(previous_hash)

cur.execute('SELECT * from blockchain ORDER BY block DESC limit 1')
nonce = cur.fetchone()[4]
print(nonce)




previous_block = Block(last_block_index, timestamp, data, previous_hash, nonce)


# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  if(i < num_of_blocks_to_add):
    target_bits = 24
    target = 2 ** (256-target_bits)

    nonce = 0

    #we iterate it till the max int value of python
    while nonce < sys.maxint:
      block_to_add = next_block(previous_block)    

      #proof-of-work is calculated here
      #that is if hash value is less than target value, then we add it to the blockchain 
      #since it satisfied the requirements.
      #that is we require 3 bytes of zeros(000000) 6 zeros
      if(long(block_to_add.hash, 16) < target):
        blockchain.append(block_to_add)
        previous_block = block_to_add
        break
      else:
        nonce = nonce + 1
  

  


    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Previous Hash: {}".format(block_to_add.previous_hash))
    print("Hash: {}".format(block_to_add.hash)) 
    print("data: {}\n".format(block_to_add.data))
    print("nonce value for block #{}".format(nonce))

    cur.execute('INSERT INTO blockchain (data, hash, prevhash, nonce) VALUES (?,?,?,?)', (block_to_add.data, block_to_add.hash, block_to_add.previous_hash, nonce))
    conn.commit()

  else:
    cur.close()
    break

```



# New Features!

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)


You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| Github | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version}
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
