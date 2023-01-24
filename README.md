### Count Reps

A customizable computer vision application that helps you track and count the reps during the exercises like sit-ups, push-ups, dumble presses, and other exercises. With the support of a database, you can even keep a track of your data. 

### Tech stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Project Setup
+ Clone the repository
```bash
https://github.com/nikhil25803/count-reps.git
```

+ Create and activate a virtual environment
```bash
python -m venv env
```

```bash
env\scripts\activate
```

+ Install the dependencies
```
pip install -r requirements.txt
```

### Folder Structure
```
count-reps
│   
└───📂database
│   │   database.py   
│   │   functions.py  
│   │   models.py 
│   │ 
📄.gitignore
📄LICENCE
📄main.py
📄README.md
📄pose_detection.py
📄helpers.py
📄requirements.txt
```

By default, the application is programmed to count the number of knee bends, useful in ortho exercise. 

### Run the program
```bash
python main.py
```
A window will appear at first as a test, close that for now by pressing `q`, and then the database will automatically get connected (you'll notice, a `database db` file is now created in the root directory of the project) which is responsible for storing a user's data. It will keep counting your reps and will store them in the database once it quits.


Example ...


![image](https://user-images.githubusercontent.com/93156825/214383344-fc1a251f-17d1-450f-a849-bc1ca0cb2ad6.png)

-----

### Want to customize it? 👀
Here's how you can do it ...
