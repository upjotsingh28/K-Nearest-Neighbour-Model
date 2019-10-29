# K-Nearest Neighbour
(PyCharm Project)
#### Output :

Loading DataSet Of Breast Cancer Analysis...

<img src="https://user-images.githubusercontent.com/46626425/67757859-95e40b00-fa62-11e9-80a9-031db78c33e3.png"/>
[5 rows x 31 columns]
<br>
<br>
Plotting Pair Plots For The DataSet.<br>
Please Wait...

<img src="https://user-images.githubusercontent.com/46626425/67758196-3f2b0100-fa63-11e9-9f9c-fa59821f7a1f.png"/>
<br>
Saved the pair plots extracted from data.
<br>
<br>
Setting Up The Knn Model With K value = 3(No. of neighbours)<br>
We Have Confusion Matrix as :
<br>
<br>
[ [ 53   6]<br>
 [ 11 101] ]<br>
<br> 
And Classification report as :<br>
<img src="https://user-images.githubusercontent.com/46626425/67759311-3cc9a680-fa65-11e9-959f-16e6ff395823.png"/>
<br>
<br>
Let's plot the Elbow Method graph for finding the correct value of K.<br>
Plotting...<br>
<img src="https://user-images.githubusercontent.com/46626425/67758313-77324400-fa63-11e9-8a2f-f0d8dbc95305.png"/>

Saved Elbow Method Graph.<br>
As per graph we can select k = 3,4,8,14,15....<br>
We will go for k=8 and Compare with previous classification reports.
<br>
<br>
So for K=8, Setting Up The Model...<br>
Now We Have Confusion Matrix as :<br>
<br>
 [ [ 52   7]<br>
 [  5 107] ]<br>
<br> 
Classification Report as :
<img src="https://user-images.githubusercontent.com/46626425/67758408-a21c9800-fa63-11e9-91df-180e3f4ca3d9.png"/>

