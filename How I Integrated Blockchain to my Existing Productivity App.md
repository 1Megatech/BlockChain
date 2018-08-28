# How I Integrated Blockchain to my Existing Productivity App (Kanbanote)

## Kanbanote 
kanbanote is a productivity tool for **Gettings Things Done** methodology (GTD) that shows your tasks on a Kanban board. It’s very similar to Trello but it uses Evernote to read/store the tasks.
## Designing the cryptocurrency

Define the identity of the cryptocurrency:
1. Purpose: Get rewarded by doing your own tasks
2. Name: Motive
3. Symbol: MOTIV
4. Future: Give MOTIVs to different productivity products and services so that they can distribute the coins to their users in order to boost their productivity!

## Building a cryptocurrency
There are many ways to build a cryptocurrency:
1. ERC20 Tokens: They run inside Ethereum blockchain. It’s very easy to create them, also there are many existing libraries to interact with Ethereum.
2. “Colored coin”: It’s a coin that runs inside another blockchain. For example with Peerassets you can create your own coin inside the peercoin cryptocurrency.
3. Creating a clone of a Proof of Work cryptocurrency with its own blockchain.
4. Creating a clone of a Proof of Stake cryptocurrency with its own blockchain.
5. Create a cryptocurrency from scratch: the hardest solution, and the longest indeed, and maybe not secured enough if you are not skilled enough.
**The easiest would be to use ERC20 Tokens**

## The integration with Kanbanote
### Defining rules
- Kanbanote’s users choose one column of one board as the reward board
- they give their Motive account address
- every time they mark a task as done (move a card to the reward column) they get 1 MOTIV. 
- With a maximum of 1 MOTIV per task.

## Defining the architecture
- Starting with 2 nodes to keep the blockchain alive
- 1 Lightweight wallet with the Kanbanote account
- Kanbanote’s backend will query the lightweight wallet that has an API in order to send a MOTIV coin every time a task is dropped in the reward column and if it hasn’t been done before.

## Implementing it

- Try API with the command line interface
- create the CURL query
- Update the database in order to track if one note got already its reward and also to save the public MOTIV address and the reward column. Kanbanote does not save your private key! So you are the only owner of it, keep it safe!
- Finally implement the UI, in order to go faster it’s a server side rendered UI with some VanillaJS to query the API






