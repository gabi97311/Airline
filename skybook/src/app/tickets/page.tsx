"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth-context";
import { ticketService } from "@/lib/api";
import type { Ticket } from "@/types";
import { Plane, Clock, CheckCircle, XCircle, AlertCircle } from "lucide-react";

const STATUS_CONFIG = {
  paid: { icon: CheckCircle, color: "text-green-500", bg: "bg-green-50", label: "Оплачен" },
  pending: { icon: Clock, color: "text-amber-500", bg: "bg-amber-50", label: "Ожидает оплаты" },
  failed: { icon: XCircle, color: "text-red-500", bg: "bg-red-50", label: "Отменён" },
};

export default function TicketsPage() {
  const { isLoggedIn, isLoading } = useAuth();
  const router = useRouter();
  const [tickets, setTickets] = useState<Ticket[]>([]);

  useEffect(() => {
    if (!isLoading && !isLoggedIn) router.push("/auth");
  }, [isLoggedIn, isLoading]);

  // In real app we'd have GET /ticket/me endpoint; simulate with placeholder
  // The backend has /ticket/{id} but no "my tickets" list
  // Showing empty state with note

  if (isLoading) return null;

  return (
    <div className="max-w-3xl mx-auto px-6 py-8">
      <h1 className="font-serif text-2xl mb-6">Мои билеты</h1>

      {tickets.length === 0 ? (
        <div className="bg-white border border-gray-200 rounded-2xl p-12 text-center">
          <div className="w-14 h-14 bg-sky-ice rounded-2xl flex items-center justify-center mx-auto mb-4">
            <Plane className="w-7 h-7 text-sky-blue" />
          </div>
          <p className="font-serif text-xl text-gray-700 mb-2">Билетов пока нет</p>
          <p className="text-sm text-gray-400 mb-6">
            Найдите рейс и забронируйте ваш первый билет
          </p>
          <button
            onClick={() => router.push("/")}
            className="px-5 py-2.5 bg-navy text-white rounded-xl text-sm font-medium hover:bg-sky-blue transition-colors"
          >
            Найти рейс
          </button>
        </div>
      ) : (
        <div className="space-y-3">
          {tickets.map((ticket) => {
            const config = STATUS_CONFIG[ticket.ticket_status];
            const Icon = config.icon;
            return (
              <div key={ticket.ticket_id} className="bg-white border border-gray-200 rounded-xl p-5">
                <div className="flex items-start justify-between">
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <span className="font-medium">{ticket.origin} → {ticket.dest}</span>
                      <span className={`flex items-center gap-1 text-xs px-2 py-0.5 rounded-full ${config.bg} ${config.color}`}>
                        <Icon className="w-3 h-3" />
                        {config.label}
                      </span>
                    </div>
                    <p className="text-sm text-gray-400">
                      {new Date(ticket.flight_time).toLocaleDateString("ru-RU", {
                        day: "numeric", month: "long", year: "numeric"
                      })}
                    </p>
                    <p className="text-sm text-gray-400">Пассажир: {ticket.passenger_name}</p>
                  </div>
                  <div className="text-right">
                    <p className="text-xl font-light">${ticket.price.toFixed(2)}</p>
                    <p className="text-xs text-gray-400">Место: {ticket.seat_id}</p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
