# 📜 Receipt Processor API

A FastAPI-based web service for processing receipts and calculating points.

## 🚀 Features

- Submit a receipt and receive a unique ID
- Retrieve points awarded based on specific rules
- Fully containerized with Docker support
- Automatic API documentation using Swagger UI

## 📦 Installation & Running

### 🔹 Running Locally (Without Docker)

#### 1️⃣ **Clone the Repository**

```sh
git clone https://github.com/pete-RK/receipt-processor.git
cd receipt-processor
```

#### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

#### 3️⃣ **Install Dependencies**

```sh
pip install -r requirements.txt
```

#### 4️⃣ **Run the FastAPI Server**

```sh
python main.py
```

#### 5️⃣ **Access API Documentation**

Once running, open the Swagger UI:

```
http://localhost:8080/docs
```

You can test the endpoints interactively from here.

---

### 🐳 Running with Docker

#### 1️⃣ **Build the Docker Image**

```sh
docker build -t receipt-processor .
```

#### 2️⃣ **Run the Container**

```sh
docker run -p 8080:8080 receipt-processor
```

#### 3️⃣ **Access API Documentation**

Visit:

```
http://localhost:8080/docs
```

---

## 📡 API Endpoints

| **Method** | **Endpoint**            | **Description**                       |
| ---------- | ----------------------- | ------------------------------------- |
| `POST`     | `/receipts/process`     | Submit a receipt for processing.      |
| `GET`      | `/receipts/{id}/points` | Get the points awarded for a receipt. |

---

## 🛠 Testing the API

### ✅ Using Postman or Curl

#### Submit a Receipt

```sh
curl -X POST "http://localhost:8080/receipts/process" -H "Content-Type: application/json" -d '
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}'
```

#### Get Points for a Receipt

```sh
curl -X GET "http://localhost:8080/receipts/{id}/points"
```

Replace `{id}` with the actual ID from the previous request.

---

### ✅ Running Tests

#### 1️⃣ **Run Tests Using pytest**

```sh
pytest tests/
```

This will validate all API functionality.

---

## 📌 Notes

- Ensure that you have Python 3.8+ installed if running locally.
- When running in Docker, make sure that no other service is using port `8080`.
- The API follows FastAPI’s best practices and utilizes Pydantic for validation.

---

### 🎯 **You're all set!** 🎯

Your FastAPI Receipt Processor is now up and running! 🚀
