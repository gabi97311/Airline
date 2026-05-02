// ─── Auth ────────────────────────────────────────────────────────────────────
export interface LoginRequest {
  username: string;
  password: string;
}

export interface RegisterRequest {
  user_name: string;
  user_password: string;
}

export interface TokenInfo {
  access_token: string;
  token_info: string;
}

export interface User {
  id: number;
  user_name: string;
  role: "user" | "admin";
}

// ─── Airplanes ────────────────────────────────────────────────────────────────
export interface Airplane {
  airplane_id: number;
  model_name: string;
  max_seats: number;
  seats_config: string;
}

// ─── Flights ──────────────────────────────────────────────────────────────────
export type SeatClass = "Economy" | "Comfort" | "Business" | "First";

export interface Flight {
  flight_id: number;
  flight_date: string;
  reporting_airline: string;
  origin: string;
  dest: string;
  airplane_id: number;
  is_delay: boolean;
  min_price?: number;
}

export interface FlightQuery {
  flight_date?: string;
  origin?: string;
  dest?: string;
  min_price?: number;
  max_price?: number;
  ticket_class?: SeatClass;
  sort_by?: "price" | "flight_date";
  sort_order?: "asc" | "desc";
  page?: number;
  size?: number;
}

// ─── Seats ────────────────────────────────────────────────────────────────────
export type SeatStatus = "Free" | "Pending" | "Occupied";

export interface Seat {
  seat_id: number;
  flight_id: number;
  seat_code: string;
  seat_class: SeatClass;
  price: number;
  seat_status: SeatStatus;
}

// ─── Tickets ─────────────────────────────────────────────────────────────────
export type TicketStatus = "pending" | "paid" | "failed";

export interface TicketCreate {
  flight_id: number;
  seat_id: number;
  passenger_name: string;
}

export interface Ticket {
  ticket_id: number;
  ticket_status: TicketStatus;
  user_id: number;
  seat_id: number;
  flight_id: number;
  origin: string;
  dest: string;
  passenger_name: string;
  purchase_time: string;
  flight_time: string;
  price: number;
}

// ─── Payment ─────────────────────────────────────────────────────────────────
export interface PaymentCreate {
  ticket_id: number;
}
