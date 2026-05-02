"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth-context";
import { flightService } from "@/lib/api";
import type { Flight } from "@/types";
import { Plus, CheckCircle2, AlertTriangle } from "lucide-react";

export default function AdminFlightsPage() {
  const { user, isLoading } = useAuth();
  const router = useRouter();
  const [flights, setFlights] = useState<Flight[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!isLoading && user?.role !== "admin") router.push("/");
  }, [user, isLoading]);

  useEffect(() => {
    flightService.list({}).then(setFlights).finally(() => setLoading(false));
  }, []);

  if (isLoading || user?.role !== "admin") return null;

  return (
    <div className="max-w-6xl mx-auto px-6 py-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="font-serif text-2xl">Управление рейсами</h1>
        <button className="flex items-center gap-2 px-4 py-2 bg-navy text-white rounded-xl text-sm font-medium hover:bg-sky-blue transition-colors">
          <Plus className="w-4 h-4" />
          Добавить рейс
        </button>
      </div>

      <div className="bg-white border border-gray-200 rounded-xl overflow-hidden">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-gray-100 bg-gray-50">
              <th className="text-left px-5 py-3 font-medium text-gray-500 text-xs uppercase tracking-wider">ID</th>
              <th className="text-left px-5 py-3 font-medium text-gray-500 text-xs uppercase tracking-wider">Авиалиния</th>
              <th className="text-left px-5 py-3 font-medium text-gray-500 text-xs uppercase tracking-wider">Маршрут</th>
              <th className="text-left px-5 py-3 font-medium text-gray-500 text-xs uppercase tracking-wider">Дата</th>
              <th className="text-left px-5 py-3 font-medium text-gray-500 text-xs uppercase tracking-wider">Самолёт</th>
              <th className="text-left px-5 py-3 font-medium text-gray-500 text-xs uppercase tracking-wider">Статус</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-50">
            {loading ? (
              Array.from({ length: 5 }).map((_, i) => (
                <tr key={i} className="animate-pulse">
                  {Array.from({ length: 6 }).map((_, j) => (
                    <td key={j} className="px-5 py-3">
                      <div className="h-4 bg-gray-100 rounded w-24" />
                    </td>
                  ))}
                </tr>
              ))
            ) : flights.length > 0 ? (
              flights.map((f) => (
                <tr key={f.flight_id} className="hover:bg-gray-50 transition-colors">
                  <td className="px-5 py-3 text-gray-400 font-mono text-xs">#{f.flight_id}</td>
                  <td className="px-5 py-3 font-medium">{f.reporting_airline}</td>
                  <td className="px-5 py-3">
                    <span className="font-medium">{f.origin}</span>
                    <span className="text-gray-300 mx-1">→</span>
                    <span className="font-medium">{f.dest}</span>
                  </td>
                  <td className="px-5 py-3 text-gray-500">{f.flight_date}</td>
                  <td className="px-5 py-3 text-gray-400 text-xs">{f.airplane_id}</td>
                  <td className="px-5 py-3">
                    {f.is_delay ? (
                      <span className="flex items-center gap-1 text-xs text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full w-fit">
                        <AlertTriangle className="w-3 h-3" />
                        Задержка
                      </span>
                    ) : (
                      <span className="flex items-center gap-1 text-xs text-green-600 bg-green-50 px-2 py-0.5 rounded-full w-fit">
                        <CheckCircle2 className="w-3 h-3" />
                        Вовремя
                      </span>
                    )}
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={6} className="px-5 py-8 text-center text-gray-400">
                  Рейсы не найдены
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
