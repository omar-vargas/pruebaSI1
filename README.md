# pruebaSI1
![servinformacion_logo](https://github.com/omar-vargas/pruebaSI1/assets/69634983/a2d9e201-6500-4473-add5-65355a94477f)
# Django API Routes

Below are the details of the Django API routes along with their associated views.

### Create User

Endpoint to create a new user.

- Method: `POST`
- Route: `/create/`
- Name: `create_user`

### List Users

Endpoint to list all users.

- Method: `GET`
- Route: `/list/`
- Name: `list_users`

### View User

Endpoint to view details of a specific user.

- Method: `GET`
- Route: `/user/<int:user_id>/`
- Name: `view_user`

### Delete User

Endpoint to delete a specific user.

- Method: `DELETE`
- Route: `/delete/<int:user_id>/`
- Name: `delete_user`

### Geocode Database

Endpoint to geocode the database.

- Method: `POST`
- Route: `/geocode_database/`
- Name: `geocode_database`
## Example of GET list of users

![image](https://github.com/omar-vargas/pruebaSI1/assets/69634983/d9613e1a-3fe8-4d50-933e-6c2c7305280d)

## to run execute command py manage.py runserver



