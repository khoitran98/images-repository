# Django-Image-Repository App

<h1>Getting Started</h1>
An Image Repository that you can login and search for similar images.

<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. However, access to AWS S3, AWS RDS, or MySQL is not available in the public repository. Testers have to provide their own access keys for this project to run in the desired manner locally</p>

<h2>Prerequisites</h2>
<code>python== 3.7</code>

<h2>Install packages after clonning </h2>
<code>pip install requirements.txt </code><br>

<h2>Migrate the database</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>To run the project</h2>
<code>python manage.py runserver</code>

## Tech Stack
* Django/Python3
* MySQL, hosted on AWS RDS
* AWS S3
* ImageHash 4.2.0
## Functionalities
* Users can sign up, login, and logout.
* Users who are authenticated can upload image to the repository, or search for similar images in the repository (using an uploaded image).
* Users can see all of their uploaded images.
* Search results for similar images can be from any user. However, users have no option to see the entire repository.
## Architecture description
* Users authentication is managed via Django and a MySQL database (hosted on AWS RDS).
* Images are processed using ImageHash 4.2.0 Perceptual Hashing, which creates an hexadecimal hash number for each image.
* Uploaded image is stored in the AWS S3.
* Each image has an user_id as a foreign key; its AWS S3 url reference, title, hash(int) is stored in a MySQL database (hosted on AWS RDS).
* Search is implemented by using MySQL's BIT_COUNT to compare the hash between the search image's hash and those of the database's images. A BIT_COUNT < 5 is considered a match.

