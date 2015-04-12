SMS Spam Detection using Support Vector Machine
################################################

Team Members:
**************
Abinaya M (MT2012007)
Vikas Verma (MT2012162)

1. Install Weka using following instructions
	- You can download Weka from "http://www.cs.waikato.ac.nz/ml/weka/downloading.html".
	- Before running the setup install JRE on your machine.
	- Run the setup now to install Weka.

2. How to load file in Weka
	- Weka supports multiple file formats as input like CSV, Arff etc.
	- Go to preprocess step click on "open file" to select your input file.
	- To clean your data you can choose appropriate filter from the "Choose" dropdown list.

3. How to classify
	- Click on "classify" tab.
	- Click on "Choose" to select your classifier from the dropdown (in this case Classifier -> functions ->LibSVM)
	- Click on the textbox in front of "Choose" button, it will open a window from where you can set your parameters.
	- In this case set the "kerneltype" as "linear".
	- Set "seed" to specify number of random points to be selected in the dataset to start learning.
	- Set "cost" parameter to specify the error tolerance.
	- press ok.
	- select "cross-validation" under "Test option" and specify number of folds (in this case 5 to 15).
	- Press start to learn.

Note: while supplying data for classification remember to change the data type of the label row from NUMERIC to NOMINAL

4. How to run the SMSSpamSVM.py file 
	- Download python version 2.7 from the site http://www.python.org/download/releases/2.7/
	- To install the necessar packages (matplotlib, numpy, scipy and scikit-learn), use this link http://scikit-learn.org/stable/install.html
	- Once the installation is complete, open the SMSSpamSVM.py file, change the file paths in the program appropriately and press F5 to run it.


