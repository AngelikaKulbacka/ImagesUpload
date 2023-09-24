# Image Upload API
## Overview
This is a Django REST Framework-based API that allows users to upload images in PNG or JPG format. It also provides features based on different account tiers, including generating thumbnails, providing links to original images, and expiring links. Admins can configure custom account tiers with various options.

## Setup
1. Clone the repository to your local machine
2. Install project dependencies:
   - pip install Django
   - pip install djangorestframework
3. Apply database migrations:
   - python manage.py makemigrations
   - python manage.py migrate
4. Create a superuser account (admin) to manage users and tiers:
   - python manage.py createsuperuser
5. Start the development server:
   - python manage.py runserver
6. Open your web browser and navigate to http://localhost:8000/admin/. Log in using the superuser account created in step 4.
7. Use the admin interface to manage users, account tiers, and options.

## Usage
1. To upload an image, send a POST request to /image-upload/upload/.
2. To list uploaded images, send a GET request to /image-upload/list-images/.
3. Account tiers provide additional features:
   - "Basic" tier: Get a link to a 200px thumbnail.
   - "Premium" tier: Get links to a 200px thumbnail, a 400px thumbnail, and the original image.
   - "Enterprise" tier: Get links to a 200px thumbnail, a 400px thumbnail, the original image, and an expiring link (customizable).

## Customization
Admins can create custom account tiers with configurable options, including thumbnail sizes, the presence of links to original files, and the ability to generate expiring links.

## Tests
To run tests, execute the following command:
python manage.py test

## Note
The time it took me to perform the task: 5 days.
