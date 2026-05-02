"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import { flightService } from "@/lib/api";
import type { Flight } from "@/types";

export function FlightHeader({ flightId }: { flightId: number }) {
  const router = useRouter();
  const [flight, setFlight] = useState<Flight | null>(null);

  useEffect(() => {
    flightService.getById(flightId).then(setFlight).catch(() => null);
  }, [flightId]);

  return (
    <div className="mb-6">
      <button
        onClick={() => router.back()}
        className="flex items-center gap-2 text-sm text-gray-400 hover:text-navy transition-colors mb-4"
      >
        <ArrowLeft className="w-4 h-4" />
        Назад к рейсам
      </button>
      <div className="flex items-baseline gap-3">
        <h1 className="font-serif text-2xl">Выбор места</h1>
        {flight && (
          <span className="text-gray-400 text-sm">
            {flight.reporting_airline} · {flight.origin} → {flight.dest} · {flight.flight_date}
          </span>
        )}
      </div>
    </div>
  );
}
