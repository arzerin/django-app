<h3>how to Install </h3>

<h4>Make sure you run the below command to install necessary library</h4>
<h5>pip install -r requirements.txt</h5>
<table width="100%" style="width: 100%">
    <tr>
        <th></th>
        <th width="95%">Title/Information</th>
    </tr>
    <tr>
        <td>1</td>
        <td>
             pip install requirements.txt
        </td>
    </tr>
    <tr>
        <td>2</td>
        <td>
             django-admin --version
        </td>
    </tr>
    <tr>
        <td>3</td>
        <td>
             django-admin startproject myproject <br/>
             cd myproject
        </td>
    </tr>
    <tr>
        <td>4</td>
        <td>
             python manage.py runserver
        </td>
    </tr>

    <tr>
        <td>4</td>
        <td>
             python manage.py startapp firstapp
        </td>
    </tr>

    <tr>
        <td>4</td>
        <td>
             in root urls.py, add  <br/>

             from firstapp.views import home  <br/>

             add also  <br/>
             urlpatterns = [
                    path('app/', include('firstapp.urls')),
                ]

        </td>
    </tr>

     <tr>
        <td>1</td>
        <td>
             in firstapp folder, models.py
             <pre>
             <code>
             from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


             </code>
             </pre>

        </td>
    </tr>

    <tr>
        <td>1</td>
        <td>
            Run the migration command to add the above models in db.sqlite3 <br/>
             python manage.py makemigrations
            python manage.py migrate

        </td>
    </tr>
    <tr>
        <td>1</td>
        <td>
             django-admin --version
        </td>
    </tr>

    

</table>
