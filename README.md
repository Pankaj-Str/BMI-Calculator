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
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</head>
<body>
    <header class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="https://www.codeswithpankaj.com/">Codes With Pankaj</a>
        </div>
    </header>
    <div class="container mt-4">
        <h1 class="text-center">BMI Calculator</h1>
        <div class="row justify-content-center mt-4">
            <form id="bmi-form" class="col-md-6" method="post">
                {% csrf_token %}
                <div class="form-group">
                    <label for="weight">Weight (kg):</label>
                    <input type="text" class="form-control" name="weight" id="weight" required>
                </div>
                <div class="form-group">
                    <label for="height">Height (m):</label>
                    <input type="text" class="form-control" name="height" id="height" required>
                </div>
                <div class="text-center">
                    <button type="submit" class="btn btn-primary">Calculate BMI</button>
                </div>
            </form>
        </div>
        <div class="row justify-content-center mt-4">
            <div id="bmi-result" class="col-md-6 text-center">
                <!-- BMI result will be displayed here -->
            </div>
        </div>
    </div>

    <!-- BMI meter with animation -->
    <div class="bmi-meter">
        <div class="bmi-value" id="bmi-value">BMI: 0</div>
        <div class="bmi-scale">
            <div class="bmi-category">Underweight</div>
            <div class="bmi-category">Normal Weight</div>
            <div class="bmi-category">Overweight</div>
            <div class="bmi-category">Obesity</div>
        </div>
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
                        const bmi = data.bmi.toFixed(2);
                        $("#bmi-result").html("Your BMI is: " + bmi);
                        
                        // Update the BMI meter with animation
                        updateBMIMeter(bmi);
                    },
                });
            });

            // Function to update the BMI meter
            function updateBMIMeter(bmi) {
                const meterValue = $("#bmi-value");
                meterValue.text("BMI: " + bmi);
                const scale = $(".bmi-scale");
                scale.children().removeClass("active");
                if (bmi < 18.5) {
                    scale.children().eq(0).addClass("active");
                } else if (bmi < 24.9) {
                    scale.children().eq(1).addClass("active");
                } else if (bmi < 29.9) {
                    scale.children().eq(2).addClass("active");
                } else {
                    scale.children().eq(3).addClass("active");
                }
            }
        });
    </script>
</body>
</html>
<style>
    /* Additional styles for the BMI meter */
.bmi-meter {
    text-align: center;
    margin-top: 40px;
}

.bmi-value {
    font-size: 24px;
    animation: pulse 2s infinite;
}

.bmi-scale {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
}

.bmi-category {
    flex: 1;
    text-align: center;
    font-weight: bold;
    opacity: 0.5;
    transition: all 0.2s;
}

.bmi-category.active {
    font-weight: bold;
    color: #007bff;
    opacity: 1;
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
    100% {
        transform: scale(1);
    }
}

</style>
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
