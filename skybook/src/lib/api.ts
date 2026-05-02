import axios from "axios";
import type {
  Flight, FlightQuery, Seat, Ticket, TicketCreate,
  LoginRequest, RegisterRequest
} from "@/types";

const api = axios.create({
  baseURL: "/api",
  withCredentials: true,
});

const authApi = axios.create({
  baseURL: "/api/auth",
  withCredentials: true,
});

// ─── Auth ─────────────────────────────────────────────────────────────────────
export const authService = {
  login: async (data: LoginRequest) => {
    const form = new FormData();
    form.append("user_name", data.username);
    form.append("user_password", data.password);
    return authApi.post("/login", form);
  },
  register: async (data: RegisterRequest) => {
    return authApi.post("/register", data);
  },
  me: async (): Promise<{ id: number; user_name: string; role: string }> => {
    const res = await authApi.get("/me");
    return res.data;
  },
};

// ─── Flights ──────────────────────────────────────────────────────────────────
export const flightService = {
  list: async (query: FlightQuery = {}): Promise<Flight[]> => {
    const params = new URLSearchParams();
    Object.entries(query).forEach(([k, v]) => {
      if (v !== undefined && v !== "") params.append(k, String(v));
    });
    const res = await api.get(`/flight?${params}`);
    return res.data;
  },
  getById: async (id: number): Promise<Flight> => {
    const res = await api.get(`/flight/${id}`);
    return res.data;
  },
};

// ─── Seats ────────────────────────────────────────────────────────────────────
export const seatService = {
  list: async (flightId: number): Promise<Seat[]> => {
    const res = await api.get(`/seats?flight_id=${flightId}`);
    return res.data;
  },
  getById: async (flightId: number, seatId: number): Promise<Seat> => {
    const res = await api.get(`/seats/${seatId}?flight_id=${flightId}`);
    return res.data;
  },
};

// ─── Tickets ─────────────────────────────────────────────────────────────────
export const ticketService = {
  create: async (data: TicketCreate): Promise<Ticket> => {
    const res = await api.post("/ticket/create_ticket", null, { params: data });
    return res.data;
  },
  getById: async (id: number): Promise<Ticket> => {
    const res = await api.get(`/ticket/${id}`);
    return res.data;
  },
};

// ─── Payment ─────────────────────────────────────────────────────────────────
export const paymentService = {
  createCheckout: async (ticketId: number): Promise<string> => {
    const res = await api.post("/payment/create_checkout_session", { ticket_id: ticketId });
    return res.data;
  },
};
