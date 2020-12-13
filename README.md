                                                              Filed Assesment Assignment

1.To Run the project clone it first using the "command git clone <link>"

2.Open it using your prefered ide ,lets suppose pycharm.

3.Check the version of correct python version using the command python3 -V i.e 3.6 if not please switch to it.

4.Create virtual environment using python3 -m venv <virtual environment name > i.e python3 -m venv filed_env

5.Install all the requirements using the command "pip3 install -m requirements.txt"

6.create the database named filedb.

7.Do make migrations and migrate using the command "python manage.py makemigrations" and "python manage.py makemigrations" one after another.

8.Create a superuser if you like using the command python manage.py createsuperuser

9.Now ,in order to test the api ,we can test via different way:
    1.Run the unit testing command i.e " python manage.py test "
        I have written some 13 test cases as per my knowledge in test.py with different status code.
        If you want to test for some other scenario ,please add new test cases as per your requirements
    2.Check manually for all cases in postman :
        The data is : Put it in body form-data and the url is " http://127.0.0.1:8000/payment/ "
        {
        CreditCardNumber:4454233323435433
        CardHolder:Sunny
        ExpirationDate:2021-03-02
        SecurityCode:332
        Amount:10
        }
        And check for different test cases by changing the value, i will be attaching postman collection for your need.


Also some things were not clear from the pdf i got i.e the 3 payment gateway i have to use here is some 3rd party API
or we have to pass of our own ,so i did things as per my knowledge, please let me know if there any changes.
