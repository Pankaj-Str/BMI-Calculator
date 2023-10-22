# BMI-Calculator
 This project will help you understand the basics of Django, including form handling and data processing

 -----
## Step 1: Create a Django Project

Start by creating a new Django project. Open your terminal and run the following commands:

```bash
# Create a new Django project (replace "bmi_calculator_project" with your preferred project name)
django-admin startproject bmi_calculator_project

# Change into the project directory
cd bmi_calculator_project
```

## Step 2: Create a Django App

Django projects consist of one or more apps. In this case, we'll create a new app called "calculator." Run the following command:

```bash
# Create a new app
python manage.py startapp calculator
```

## Step 3: Define the BMI Calculation Logic

In your app's `calculator/views.py` file, define a view for calculating BMI. Modify the `views.py` file as follows:

```python
from django.shortcuts import render
from django.http import JsonResponse

def calculate_bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        bmi = weight / (height ** 2)
        return JsonResponse({'bmi': bmi})
    else:
        return render(request, 'calculator/bmi_form.html')
```

## Step 4: Modify the HTML Template

Update the `bmi_form.html` template to include JavaScript code that uses jQuery to make an AJAX request and display the BMI result on the same page. Here's the modified `bmi_form.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>BMI Calculator</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>BMI Calculator</h1>
    <form id="bmi-form" method="post">
        {% csrf_token %}
        <label for="weight">Weight (kg):</label>
        <input type="text" name="weight" id="weight" required>
        <br>
        <label for "height">Height (m):</label>
        <input type="text" name="height" id="height" required>
        <br>
        <input type="submit" value="Calculate BMI">
    </form>
    <div id="bmi-result">
        <!-- BMI result will be displayed here -->
    </div>

    <script>
        $(document).ready(function () {
            $("#bmi-form").submit(function (event) {
                event.preventDefault();
                $.ajax({
                    type: "POST",
                    url: "{% url 'calculate_bmi' %}",
                    data: $(this).serialize(),
                    success: function (data) {
                        $("#bmi-result").html("Your BMI is: " + data.bmi.toFixed(2));
                    },
                });
            });
        });
    </script>
</body>
</html>
```

This modified code includes JavaScript that prevents the form submission, sends an AJAX POST request to the `calculate_bmi` view, and updates the `#bmi-result` element with the BMI result.

## Step 5: Configure URLs

In your app's `calculator/urls.py` file, define URL patterns for the BMI calculator views. Here's how you can do it:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('bmi/', views.calculate_bmi, name='calculate_bmi'),
]
```

## Step 6: Update Project URLs

To make your app's URLs accessible from the main project, include them in the project's `urls.py`:

In `bmi_calculator_project/urls.py`, add the following code:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),
]
```

## Step 7: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit "http://localhost:8000/calculator/bmi/" in your web browser, and you should see the BMI calculator form. Enter the weight and height, click "Calculate BMI," and the BMI result will be displayed on the same page without a page reload.

This approach allows you to provide instant feedback to the user and keep them on the same page, enhancing the user experience.
