"use client";

import { useRouter } from "next/navigation";
import type { Flight } from "@/types";
import { AlertTriangle, CheckCircle2, Plane } from "lucide-react";

const AIRLINE_COLORS: Record<string, string> = {
  KC: "bg-blue-50 text-blue-700",
  SU: "bg-amber-50 text-amber-700",
  S7: "bg-green-50 text-green-700",
  UT: "bg-purple-50 text-purple-700",
};

function airlineCode(airline: string) {
  return airline.slice(0, 2).toUpperCase();
}

// Fake departure/arrival times since backend doesn't expose them directly
function fakeTimes(flightId: number) {
  const deps = [640, 690, 720, 780, 840, 900, 960, 1020, 1080, 1140];
  const dep = deps[flightId % deps.length];
  const dur = 340 + (flightId % 6) * 20;
  const arr = (dep + dur) % 1440;
  const fmt = (m: number) =>
    `${String(Math.floor(m / 60)).padStart(2, "0")}:${String(m % 60).padStart(2, "0")}`;
  const fmtDur = (m: number) => `${Math.floor(m / 60)} ч ${m % 60} м`;
  return { dep: fmt(dep), arr: fmt(arr), dur: fmtDur(dur) };
}

export function FlightCard({ flight }: { flight: Flight }) {
  const router = useRouter();
  const code = airlineCode(flight.reporting_airline);
  const colorClass = AIRLINE_COLORS[code] ?? "bg-gray-100 text-gray-600";
  const { dep, arr, dur } = fakeTimes(flight.flight_id);

  return (
    <div
      onClick={() => router.push(`/flights/${flight.flight_id}/seats`)}
      className="bg-white border border-gray-200 rounded-xl px-5 py-4 grid grid-cols-[160px_1fr_1fr_1fr_auto_auto] items-center gap-4 cursor-pointer hover:shadow-md hover:border-gray-300 transition-all group"
    >
      {/* Airline */}
      <div className="flex items-center gap-3">
        <div className={`w-10 h-10 rounded-lg ${colorClass} flex items-center justify-center text-xs font-semibold flex-shrink-0`}>
          {code}
        </div>
        <div>
          <p className="text-sm font-medium leading-tight truncate max-w-[100px]">
            {flight.reporting_airline}
          </p>
          <p className="text-xs text-gray-400 mt-0.5">#{flight.flight_id}</p>
        </div>
      </div>

      {/* Departure */}
      <div>
        <p className="text-2xl font-light tracking-tight leading-none">{dep}</p>
        <p className="text-xs text-gray-400 uppercase tracking-wide mt-1">{flight.origin}</p>
      </div>

      {/* Duration */}
      <div className="flex flex-col items-center gap-1">
        <div className="flex items-center gap-2 w-full">
          <div className="w-2 h-2 rounded-full bg-gray-300 flex-shrink-0" />
          <div className="flex-1 h-px bg-gray-200 relative">
            <Plane className="w-3 h-3 text-gray-300 absolute top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2" />
          </div>
          <div className="w-2 h-2 rounded-full bg-gray-300 flex-shrink-0" />
        </div>
        <p className="text-xs text-gray-400">{dur} · Прямой</p>
      </div>

      {/* Arrival */}
      <div>
        <p className="text-2xl font-light tracking-tight leading-none">{arr}</p>
        <p className="text-xs text-gray-400 uppercase tracking-wide mt-1">{flight.dest}</p>
      </div>

      {/* Price + status */}
      <div className="text-right">
        <p className="text-xs text-gray-400 mb-0.5">от</p>
        <p className="text-2xl font-light tracking-tight">
          <span className="text-sm text-gray-400 font-normal">$</span>
          {flight.min_price?.toFixed(0) ?? "—"}
        </p>
        <div className="flex items-center gap-1 justify-end mt-1">
          {flight.is_delay ? (
            <>
              <AlertTriangle className="w-3 h-3 text-amber-500" />
              <span className="text-xs text-amber-600">Задержка</span>
            </>
          ) : (
            <>
              <CheckCircle2 className="w-3 h-3 text-green-500" />
              <span className="text-xs text-green-600">Вовремя</span>
            </>
          )}
        </div>
      </div>

      {/* CTA */}
      <button className="px-4 py-2 bg-sky-ice text-sky-blue text-sm font-medium rounded-lg group-hover:bg-sky-blue group-hover:text-white transition-colors whitespace-nowrap">
        Выбрать
      </button>
    </div>
  );
}
