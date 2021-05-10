# Django-Image-Repository App

<h1>Getting Started</h1>
An Image Repository that you can add, delete, and search for similar images.

<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

<h2>Prerequisites</h2>
<code>python== 3.7 </code>

<h2>Setup after clonning </h2>

<h2>To migrate the database do this in the terminal</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>To run the project</h2>
<code>python manage.py runserver</code>

## Tech Stack
* Django/Python3
* MySQL
* Google Cloud Storage
* ImageHash 4.2.0

## Description
* Images are processed using ImageHash 4.2.0 Perceptual Hashing.
* Uploaded image is stored in the Google Cloud Storage, its Google Cloud url and hash data is stored in MySQL database.
* Search is implemented by comparing hash between the search image's hash and those of the database images.
