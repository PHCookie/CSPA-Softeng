Required Python Modules:
    pip install numpy
    pip install pandas
    pip install pillow
    pip install graphviz
    pip install pydotplus
    pip install regex

# to avoid sklearn.externals.six incompatibility
    from six import StringIO
    donwload graphviz
then add this line
    import os
    os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz/bin/'

Dataset attribute
1. Loan: "Loan Status" ;1 = Fully Paid & 0 = Charged Off
