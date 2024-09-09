---
marp: true
---

# Deploying multi-containers to Azure container instance (ACI)

- Deploy multi container to ACI
- Explain the deployment YAML file
- Demo the deployment

```bash
az group create --name techwithfoyzur --location eastus

az container create --resource-group techwithfoyzur --file deploy-multicontainer-aci.yaml

az container show --resource-group techwithfoyzur --name techwithfoyzur --output table


az container logs --resource-group techwithfoyzur --name techwithfoyzur --container-name techwithfoyzur-main


az container logs --resource-group techwithfoyzur --name techwithfoyzur --container-name techwithfoyzur-sidecar
```

---

## Azure container apps

Today we are going to learn the followings:

- What is Azure container apps?
- How to deploy an application to Azure container Apps?

In the next video, we will run some performance tests to show you how auto scaling works. I plan to make 3/4 videos on Azure container apps this month. Please subscribe to my channel. Thank you

---

## What is azure container apps?

Azure Container Apps is a serverless platform that allows you to maintain less infrastructure and save costs while running containerized applications. 

- No server to manage
- No server configuration
- Saves cost since you only pay for the runtime that you consume
- **Container** Apps provides all the up-to-date server resources required to keep your applications stable and secure
- You do not need to manage any containers or whatsoever

---

## What are the common use cases?

- Deploying API endpoints
- Hosting background processing jobs
- Handling event-driven processing
- Running microservices

Additionally, applications built on Azure Container Apps can dynamically scale based on the following characteristics:

- HTTP traffic
- Event-driven processing
- CPU or memory load
- Any KEDA-supported scaler

---

## How to authenticate with Azure Container Registry(ACR) using ACR TOKEN

I am going to show you the followings:

- What is a TOKEN?
- How to create an ACR token?
- How to grant access?
- Demo

---

## How to login to ACR exposing a TOKEN

- Show the demo

---

## How to authenticate to Azure Container Registry (ACR) using Service Principal (SP)

- What is service principal?
- Why do we need one?
- Demo (SP to authenticate to ACR)

---

## What is SP?

Microsoft Entra ID service principals provide access to Azure resources within your subscription. You can think of a service principal as a user identity for a service, where "service" is any application, service, or platform that needs to access the resources.

You can configure a service principal with access rights scoped only to those resources you specify. Then, configure your application or service to use the service principal's credentials to access those resources.

---

## Why use a service principal?

By using a Microsoft Entra service principal, you can provide scoped access to your private container registry. Create different service principals for each of your applications or services, each with tailored access rights to your registry. And, because you can avoid sharing credentials between services and applications, you can rotate credentials or revoke access for only the service principal (and thus the application) you choose.
