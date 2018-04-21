

# Project-2018 Programming-and-Scripting

Project to be submitted for the module of Programming and Scripting GMIT  Higher Diploma in Data Analytics

The iris data set was downloaded from the Machine Learning Repository from the Center Machine Learning and Intelligent Systems at UCI (University of California, Irvine) United States https://archive.ics.uci.edu/ml/index.html.

https://en.wikipedia.org/wiki/Iris_flower_data_set Research/Background information into the origins of the Iris flower data set.It is an example of the use  multivariate statistics https://en.wikipedia.org/wiki/Multivariate_statistics which is a subdivision of statistics encompassing the simultaneous observation and analysis of more than one outcome variable. The application of multivariate statistics is multivariate analysis.
Introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. 
Iris flower data set or Fisher's Iris data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

https://gist.github.com/jobliz/2903500 Iris dataset (petal size) scatterplot done in matplotlib source https://github.com/jobliz

Looking for code Research 18/04/2018 https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset

https://github.com/RicardsGraudins/Iris-Flower-Data-Set 

This is a good link https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn and another kaggle link https://www.kaggle.com/gilsousa/prediction-iris-dataset
import matplotlib.pyplot as pl

#setting figure size
pl.rcParams['figure.figsize'] = (16, 8)
#plotting scatter diagram using sepal length and sepal width
pl.scatter(sepalLength, sepalWidth, marker='.')

#setting title and labels
pl.title('Scatter Diagram Representing Sepal Width & Sepal Length', fontsize=20)
pl.xlabel('Sepal Length', fontsize=12)
pl.ylabel('Sepal Width', fontsize=12)

#displaying the diagram
pl.show()
