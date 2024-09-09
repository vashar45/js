---
marp: true
---

# How to run Django app locally

:information_source: Clone the project into your choice of directory on your computer, then
  
```bash
cd django/webapp
pipenv sync
pipenv shell
python manage.py runserver
```

Additionally you can run if you have made some changes to the model

```bash
python manage.py makemigrations
python manage.py migrate
```

Make migrations will scan and compare the changes against the current version of your migration files, and the migrate command will apply the changes if any changes reported/discovered by the makemigrations. So everytime you make changes to your model you can apply the changes.

:warning: for the complex changes sometimes makemigrations unable to detect changes.

Go to your browser and type

```
http://127.0.0.1:8000/
```

---

## Build and Push images to Azure Container Registry

Make sure you have the Azure account, and you can login to your account.

We are going to use today az acr command instead of docker commands

- Make sure you are logged in
- Create a resource group
- Create a container registry
- Create a container image
- Enable the admin account
- Deploy the image to a container

```bash
az container create --resource-group <NAME> --name <ACI-INSTANCE-NAME> --image $ACR/hello --registry-login-server $ACR --ip-address Public --location eastus --registry-username <admin-username> --registry-password <admin-password>

az container show --resource-group <NAME> --name <ACI-INSTANCE-NAME> --query ipAddress.ip --output table
```
