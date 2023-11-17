# FetchExercise
Repo for a Fetch screening exercise where I use machine learning to predict the number of scanned receipts from a year of data.

## Running the app
You can run the app by pulling the docker image here: https://hub.docker.com/r/lcvetko/luke_fetch_exercise.
When you've pulled it, you can run it with the command "docker run -ti lcvetko/luke_fetch_exercise".
It will ask you for a file path for the location of the data you want to predict from. If the file is in the same folder as the
 program, you can just enter the file name, "filename.csv" (without the quotation marks). Otherwise, you can give the path to 
the file. For example, "C:\Users\cvetk\Downloads\filename.csv", again without the quotation marks.

