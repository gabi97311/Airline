
# Airline — Booking Backend

Backend for airline ticket booking. Built as a learning project to explore microservices, distributed transactions, and async Python.

Two FastAPI services communicating over HTTP and RabbitMQ, with Stripe handling payments.

## Stack

| | |
|---|---|
| **API** | FastAPI + Uvicorn |
| **Database** | PostgreSQL + SQLAlchemy 2.0 async (`asyncpg`) |
| **Migrations** | Alembic |
| **Message Broker** | RabbitMQ + FastStream |
| **Payments** | Stripe Checkout |
| **Auth** | Stateless JWT (RBAC: `user` / `admin`) |
| **Infrastructure** | Docker, Docker Compose |

---

## Getting Started

```bash
git clone https://github.com/your-username/airline.git
cd airline
cp .env.example .env
docker-compose up -d --build
docker-compose exec flight-auth-app alembic upgrade head
docker-compose exec payment-app alembic upgrade head
```

| Service | URL |
|---|---|
| flight_auth API | http://localhost:8001/docs |
| payment API | http://localhost:8000/docs |
| RabbitMQ | http://localhost:15672 |

> **Note:** after first run, create an `admin` user via `POST /auth/register` and use that token to seed flights and seats. Automated seed script is on the roadmap.

---

## How it works

User books a seat → payment processed via Stripe → result propagated back through RabbitMQ → ticket finalized.

Seats are locked with `SELECT FOR UPDATE` during booking to prevent double reservations. If payment fails or times out, the seat is released automatically.

JWT token carries the user role in its payload — downstream services authorize requests without calling back to `flight_auth`.

---


## ER Diagram

<img width="1511" height="990" alt="{5154765A-1384-4690-89D3-DD44E816010E}" src="https://github.com/user-attachments/assets/e73980a7-66f8-44bf-bb5b-b5d8390819a5" />


## API

### flight_auth `localhost:8001`

| Method | Path | Access |
|---|---|---|
| POST | `/auth/register` | public |
| POST | `/auth/login` | public |
| GET | `/auth/me` | user |
| GET | `/airplanes/` | public |
| POST | `/airplanes/` | admin |
| GET | `/flight/` | public |
| POST | `/flight/` | admin |
| GET | `/flight/{id}` | public |
| GET | `/seat/?flight_id=` | public |
| POST | `/ticket/create_ticket` | user |
| GET | `/ticket/{id}` | user |

### payment `localhost:8000`

| Method | Path |
|---|---|
| POST | `/payment/create_checkout_session` |
| POST | `/payment/webhook` |

---

## Roadmap

- [ ] Seed script
- [ ] Auto-migrations on container start
- [ ] Airflow DAG — cancel stale `pending` tickets after 15 min
- [ ] Analytics service
- [ ] Tests (pytest)
- [ ] CI/CD (GitHub Actions)
