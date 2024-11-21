# TaskManager
## API for task manager using Django Rest framework and allauth for google oauth based user registration.

## Features
  #### Authentication using Google.
  #### Task creation, deletion, updation.
  #### Email sending for invites (only for admin users)
  
## Technologies Used
#### Django
#### Django REST Framework
#### Python
## Prerequisites
#### Python 3.x
#### pip (Python package installer)
#### allauth

## Setup Instructions
#### 1. Clone the Repository
`git clone https://github.com/rahulmakhijasg8/TaskManager.git`

`cd TaskManager(project-directory)`

#### 2. Create a Virtual Environment
`python -m venv venv`

`venv\Scripts\activate` (for windows)

`source venv/bin/activate` (for macos)

#### 3. Install Dependencies
`pip install -r requirements.txt`

#### 4. Run Migrations
`python manage.py makemigrations`

`python manage.py migrate`

#### 5. Create a Superuser (Optional)
To access the Django admin interface, create a superuser:
`python manage.py createsuperuser`

#### 6. Run the Development Server
`python manage.py runserver`

Open your browser and navigate to http://127.0.0.1:8000/api/tasks to access the API metods.

#### API Endpoints
  GET /api/tasks/ - If the user is not authenticated, they will be asked to signin.
  
  
  ![Screenshot 2024-11-21 173317](https://github.com/user-attachments/assets/6bd5e344-f0a5-4f6a-a111-3691127436a4)

  
  
  After Clicking on the login url, the user will have to login with google, providing consent.
  
  
  ![Screenshot 2024-11-21 173408](https://github.com/user-attachments/assets/a647ff1d-e39b-4905-9a35-00c88e7c9cac)

  ![Screenshot 2024-11-21 173426](https://github.com/user-attachments/assets/1c5746f5-2431-44f8-a20b-cc17a78ed6a6)

  After logging in with google, the user will be redirected to the /api/tasks page
  where they can list, create personal tasks
  Also if the user has already signed in before in the current session, they will directly see the tasks page.
  
  
  ![Screenshot 2024-11-21 173505](https://github.com/user-attachments/assets/df503712-a63d-4cec-a0d7-4ca84b959867)

  The session ends when the browser is closed, on restarting the browser the user will have to login again.
    
  
  
  GET /api/tasks/{task_id} - The user can edit or delete a particular task
  
  
  PUT /api/tasks/{task_id} will be used to edit
  
  
  ![Screenshot 2024-11-21 173531](https://github.com/user-attachments/assets/837899d9-7f31-49b9-8f03-d3c5b775f99b)
  
  
  
  POST /api/emailsend/ - Only Admin users can send emails to thers which will provide them with the registration link.
  
  
  ![Screenshot 2024-11-21 173618](https://github.com/user-attachments/assets/7956766f-cf6d-4d09-add4-613621f3607e)
  
  
  
  They will be denied permission if they are not an admin user
  
  
  ![Screenshot 2024-11-21 173703](https://github.com/user-attachments/assets/089c96bf-1d78-454a-bb79-b7537443e968)
  They can send mail if they are admin users by providing email id

  
  Email sent and received example
  
  
  ![Screenshot 2024-11-21 173844](https://github.com/user-attachments/assets/f26d88f2-56a0-461c-b093-aab86d8d2fb4)
