# SkyBook Frontend

Next.js 15 фронтенд для системы бронирования авиабилетов.

## Стек

- **Next.js 15** (App Router, Turbopack)
- **TypeScript**
- **Tailwind CSS** с кастомной темой
- **DM Sans + DM Serif Display** — типографика
- **Axios** — HTTP клиент
- **react-hot-toast** — уведомления
- **lucide-react** — иконки

## Быстрый старт

```bash
cd skybook
npm install
npm run dev
```

Приложение запустится на http://localhost:3000

## Конфигурация API

Настройте в `next.config.ts`:

| Путь | Сервис |
|------|--------|
| `/api/auth/*` | Auth сервис (порт 8001) |
| `/api/*` | Flight сервис (порт 8002) |
| `/api/payment/*` | Payment сервис (порт 8000) |

## Переменные окружения

Создайте `.env.local`:

```
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

## Структура

```
src/
├── app/
│   ├── page.tsx              # Главная — поиск рейсов
│   ├── auth/page.tsx         # Вход / регистрация
│   ├── tickets/page.tsx      # Мои билеты
│   ├── flights/[flightId]/
│   │   └── seats/page.tsx    # Схема мест
│   ├── payment/
│   │   ├── success/page.tsx  # Успешная оплата
│   │   └── cancel/page.tsx   # Отменённая оплата
│   └── admin/
│       └── flights/page.tsx  # Управление рейсами (admin)
│
├── components/
│   ├── layout/Navbar.tsx
│   ├── flights/
│   │   ├── SearchHero.tsx    # Форма поиска + hero
│   │   ├── FlightResults.tsx # Список рейсов
│   │   └── FlightCard.tsx    # Карточка рейса
│   └── seats/
│       ├── FlightHeader.tsx
│       └── SeatMap.tsx       # Схема мест + бронирование
│
├── lib/
│   ├── api.ts               # API клиенты
│   └── auth-context.tsx     # Auth провайдер
│
└── types/index.ts           # TypeScript типы
```

## API эндпоинты (соответствие бэкенду)

### Auth сервис
- `POST /auth/register` — регистрация
- `POST /auth/login` — вход (cookie)
- `GET /auth/me` — текущий пользователь

### Flight сервис
- `GET /flight` — список рейсов (фильтры: origin, dest, flight_date, ticket_class, sort_by)
- `GET /flight/{id}` — рейс по ID
- `GET /seats?flight_id=` — места рейса
- `POST /ticket/create_ticket` — создать билет

### Payment сервис
- `POST /payment/create_checkout_session` — Stripe checkout URL

## Stripe

После успешной оплаты Stripe редиректит на:
- `/payment/success` — успех
- `/payment/cancel` — отмена

Webhook автоматически обновляет статус билета через payment микросервис.
