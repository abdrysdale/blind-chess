A few edits to the blind chess repo from https://github.com/rabidmachine9/blind-chess.git/.

The original README is below.

---

This is a small blind chess app made with python, first thing you need to do is download [Stockfish engine](https://stockfishchess.org/)
Place it somewhere in your computer and add the path in this line of the script
```python
#here you need to add the path to stockfish or some other uci engine(that will probably work)
engine = chess.uci.popen_engine("./stockfish-9-64") # <--here
```
Then from terminal just ```cd ``` to the blind chess folder and run:

```console 
foo@bar:path/to/blind-chess $ pipenv install
``` 
That will basically install python-chess that is the only dependency for this project

To start the program just run: 
``` 
python3 index.py
```
Yes, you need Python 3.X.x
You can insert the moves either in a UCI(ex. 'e2e4') format or SAN(ex. 'e4')
There are also a few commands I have added to make life easier type:```help``` while you are in the progran to see your options
For now you can only play as white

Thanks for looking!
