"use client";

import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import { flightService } from "@/lib/api";
import type { Flight, FlightQuery } from "@/types";
import { FlightCard } from "./FlightCard";
import { ArrowUpDown } from "lucide-react";

type SortKey = "price" | "flight_date";

export function FlightResults() {
  const sp = useSearchParams();
  const [flights, setFlights] = useState<Flight[]>([]);
  const [loading, setLoading] = useState(false);
  const [sortBy, setSortBy] = useState<SortKey>("price");
  const [sortOrder, setSortOrder] = useState<"asc" | "desc">("asc");

  const origin = sp.get("origin") ?? "";
  const dest = sp.get("dest") ?? "";
  const flight_date = sp.get("flight_date") ?? "";
  const ticket_class = sp.get("ticket_class") ?? "";
  const hasQuery = origin || dest || flight_date || ticket_class;

  useEffect(() => {
    if (!hasQuery) {
      // load all flights by default
      fetchFlights({});
      return;
    }
    const q: FlightQuery = {};
    if (origin) q.origin = origin;
    if (dest) q.dest = dest;
    if (flight_date) q.flight_date = flight_date;
    if (ticket_class) q.ticket_class = ticket_class as any;
    fetchFlights(q);
  }, [origin, dest, flight_date, ticket_class]);

  const fetchFlights = async (q: FlightQuery) => {
    setLoading(true);
    try {
      const data = await flightService.list({ ...q, sort_by: sortBy, sort_order: sortOrder });
      setFlights(data);
    } catch {
      setFlights([]);
    } finally {
      setLoading(false);
    }
  };

  const toggleSort = (key: SortKey) => {
    if (sortBy === key) {
      setSortOrder((o) => (o === "asc" ? "desc" : "asc"));
    } else {
      setSortBy(key);
      setSortOrder("asc");
    }
  };

  return (
    <div className="max-w-5xl mx-auto px-6 py-6">
      {/* Sort bar */}
      <div className="flex items-center justify-between mb-4">
        <div>
          <p className="text-lg font-serif">
            {loading ? "Поиск рейсов..." : `Найдено ${flights.length} рейсов`}
          </p>
          {(origin || dest) && (
            <p className="text-sm text-gray-400">
              {[origin, dest].filter(Boolean).join(" → ")}
              {flight_date && ` · ${flight_date}`}
            </p>
          )}
        </div>
        <div className="flex gap-2">
          {(["price", "flight_date"] as const).map((key) => (
            <button
              key={key}
              onClick={() => toggleSort(key)}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs border transition-colors ${
                sortBy === key
                  ? "bg-navy text-white border-navy"
                  : "bg-white text-gray-500 border-gray-200 hover:border-gray-300"
              }`}
            >
              <ArrowUpDown className="w-3 h-3" />
              {key === "price" ? "Цена" : "Дата"}
              {sortBy === key && (sortOrder === "asc" ? " ↑" : " ↓")}
            </button>
          ))}
        </div>
      </div>

      {/* Cards */}
      {loading ? (
        <div className="space-y-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="bg-white rounded-xl border border-gray-200 p-5 animate-pulse">
              <div className="flex items-center gap-4">
                <div className="w-10 h-10 bg-gray-100 rounded-lg" />
                <div className="flex-1 space-y-2">
                  <div className="h-4 bg-gray-100 rounded w-1/3" />
                  <div className="h-3 bg-gray-100 rounded w-1/4" />
                </div>
                <div className="w-20 h-8 bg-gray-100 rounded" />
              </div>
            </div>
          ))}
        </div>
      ) : flights.length > 0 ? (
        <div className="space-y-3">
          {flights.map((flight) => (
            <FlightCard key={flight.flight_id} flight={flight} />
          ))}
        </div>
      ) : (
        <div className="text-center py-16 text-gray-400">
          <p className="text-5xl mb-4">✈️</p>
          <p className="text-lg font-serif text-gray-500">Рейсы не найдены</p>
          <p className="text-sm mt-1">Попробуйте изменить параметры поиска</p>
        </div>
      )}
    </div>
  );
}
