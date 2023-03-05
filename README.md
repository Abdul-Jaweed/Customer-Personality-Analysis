# Customer Personality Analysis

### Problem Statement

Customer Personality Analysis is a detailed analysis of a company’s ideal customers. It
helps a business to better understand its customers and makes it easier for them to
modify products according to the specific needs, behaviors and concerns of different
types of customers.
Customer personality analysis helps a business to modify its product based on its target
customers from different types of customer segments. For example, instead of spending
money to market a new product to every customer in the company’s database, a
company can analyze which customer segment is most likely to buy the product and then
market the product only on that particular segment.


The main objective here is -
1. What people say about your product: what gives customers’ attitude towards the
product.
2. What people do: which reveals what people are doing rather than what they are
saying about your product.





## Tech Stack Used
Python 
FastAPI 
Machine learning algorithms
Docker
MongoDB


## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions

## How to run?

Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.


## Data Collections
![image](https://github.com/Abdul-Jaweed/Customer-Personality-Analysis/blob/main/flowchart/1.png)



## Project Archietecture
![image](https://github.com/Abdul-Jaweed/Customer-Personality-Analysis/blob/main/flowchart/2.png)


## Deployment Archietecture
![image](https://github.com/Abdul-Jaweed/Customer-Personality-Analysis/blob/main/flowchart/3.png)



### Step 1: Clone the repository
```bash
git clone https://github.com/Abdul-Jaweed/Customer-Personality-Analysis.git
```


### Step 2- Create a conda environment after opening the repository

```bash
conda create -p venv  python=3.8.15 -y
```

```bash
conda activate venv/
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"

```


### Step 5 - Run the application server
```bash
python app.py
```



## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

then run 
```
python main.py
```