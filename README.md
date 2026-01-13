### Simple Demonstration of Deploying an ML Model
* Deployment here refers to exposing the functionality of a trained ML model so that others can use it.
* In the example provided, the ML model is a very simple RandomForestRegressor from the ```scikit-learn``` library that given a set of ```X``` inputs, returns some predictive outputs ```y```.
* In a more complex application, this model may be a trained PhysicsNeMo model, such as the DoMINO architecture for predicting fields given an input geometry. Given the compute resource needed to 1) train such a complex model and 2) make inference at speed, it is necessary to deploy these models in a way that enables flexible scalability of compute.
* Here we demonstrate building a Docker image and exposing it's functionality via an API endpoint.


### Azure Deployment:
* In this example, I have pushed the built Docker image to the Docker Hub and then pulled this Docker image into my Azure cloud environment.
* Using Azures container app I have been able to host this simple predictive model in the cloud environment. 
* Hosting in the cloud allows me to specify the minimum and maximum number of containers to run at any instance, as well as enabling Azure to manage auto scaling of resource to satisfy demand. 

The live ML model can be accessed by sending a HTTP POST request with:
```curl -X POST https://predict-api.yellowsand-55c50e72.uksouth.azurecontainerapps.io/predict \-H "Content-Type: application/json" \ -d '{"x":[1,2,3]}'```