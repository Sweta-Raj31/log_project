<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

<h1>Log Ingestor Project</h1>

<p>This project is a Log Ingestor built with Django, allowing users to capture logs from different APIs and query them based on various criteria.</p>

<h2>Installation</h2>

<p>Follow these steps to download the project and set it up on your local machine:</p>

<ol>
  <li>Clone the repository to your local machine:</li>
  <code>git clone &lt;repository-url&gt;</code>
  
  <li>Navigate to the project directory:</li>
  <code>cd log_ingestor_project</code>
  
  <li>(Optional) Create and activate a virtual environment:</li>
  <code>python -m venv env</code><br>
  <code>source env/bin/activate  # For Unix/Linux</code><br>
  <code>.\env\Scripts\activate    # For Windows</code>
  
  <li>Install the required dependencies using pip:</li>
  <code>pip install -r requirements.txt</code>
</ol>

<h2>Usage</h2>

<p>Once you have set up the project, you can run it locally:</p>

<ol>
  <li>Navigate to the project directory if you haven't already:</li>
  <code>cd log_ingestor_project</code>
  
  <li>Run the Django development server:</li>
  <code>python manage.py runserver</code>
  
  <li>Access the following pages in your web browser:</li>
  <ul>
    <li>Log Page: <a href="http://127.0.0.1:8000/log/">http://127.0.0.1:8000/log/</a> (Requires login)</li>
    <li>Query Interface: <a href="http://127.0.0.1:8000/query_interface/">http://127.0.0.1:8000/query_interface/</a></li>
    <li>Admin Page: <a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a></li>
  </ul>
</ol>

<h2>Admin Credentials</h2>

<p>To access the admin panel, use the following credentials:</p>
<ul>
  <li>Username: <strong>rajsw</strong></li>
  <li>Password: <strong>1234</strong></li>
</ul>

<h2>Live Demo</h2>

<p>A live demo of this project is available at the following URLs:</p>
<ul>
  <li><a href="https://log-project-xj59.onrender.com/log/">Log Page</a></li>
  <li><a href="https://log-project-xj59.onrender.com/query_interface/">Query Interface</a></li>
  <li><a href="https://log-project-xj59.onrender.com/admin/">Admin Page</a></li>
</ul>

<h2>Contributing</h2>

<p>If you'd like to contribute to this project, follow these steps:</p>

<ol>
  <li>Fork the repository on GitHub.</li>
  
  <li>Create a new branch with a descriptive name:</li>
  <code>git checkout -b feature/my-new-feature</code>
  
  <li>Make your changes and commit them to your branch:</li>
  <code>git commit -am 'Add some feature'</code>
  
  <li>Push your changes to your fork:</li>
  <code>git push origin feature/my-new-feature</code>
  
  <li>Create a pull request on the original repository.</li>
</ol>

<h2>License</h2>

<p>This project is licensed under the MIT License.</p>

</body>
</html>
