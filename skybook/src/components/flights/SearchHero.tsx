"use client";

import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { ArrowLeftRight, Search } from "lucide-react";

export function SearchHero() {
  const router = useRouter();
  const sp = useSearchParams();

  const [origin, setOrigin] = useState(sp.get("origin") ?? "");
  const [dest, setDest] = useState(sp.get("dest") ?? "");
  const [date, setDate] = useState(sp.get("flight_date") ?? "");
  const [ticketClass, setTicketClass] = useState(sp.get("ticket_class") ?? "");
  const [tripType, setTripType] = useState<"one" | "round">("one");

  const swap = () => {
    setOrigin(dest);
    setDest(origin);
  };

  const handleSearch = () => {
    const params = new URLSearchParams();
    if (origin) params.set("origin", origin.toUpperCase());
    if (dest) params.set("dest", dest.toUpperCase());
    if (date) params.set("flight_date", date);
    if (ticketClass) params.set("ticket_class", ticketClass);
    router.push(`/?${params.toString()}`);
  };

  return (
    <div className="bg-navy">
      {/* Grid decoration */}
      <div
        className="absolute inset-0 pointer-events-none opacity-30"
        style={{
          backgroundImage:
            "linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px)",
          backgroundSize: "40px 40px",
        }}
      />

      <div className="relative max-w-5xl mx-auto px-6 pt-10 pb-0">
        {/* Heading */}
        {origin && dest ? (
          <div className="flex items-baseline gap-3 mb-1">
            <h1 className="font-serif text-4xl text-white leading-none">{origin}</h1>
            <span className="text-sky-gold text-2xl">→</span>
            <h1 className="font-serif text-4xl text-white leading-none">{dest}</h1>
          </div>
        ) : (
          <h1 className="font-serif text-4xl text-white mb-1">
            Куда летим?
          </h1>
        )}
        <p className="text-white/40 text-sm tracking-wide uppercase mb-7 font-light">
          Лучшие цены · Мгновенное бронирование · Stripe оплата
        </p>

        {/* Search card */}
        <div className="bg-white rounded-t-2xl px-6 pt-5 pb-6">
          {/* Trip type tabs */}
          <div className="flex gap-0 border-b border-gray-100 mb-5">
            {(["one", "round"] as const).map((t) => (
              <button
                key={t}
                onClick={() => setTripType(t)}
                className={`px-4 py-2 text-sm border-b-2 -mb-px transition-colors ${
                  tripType === t
                    ? "border-sky-blue text-sky-blue font-medium"
                    : "border-transparent text-gray-400 hover:text-gray-600"
                }`}
              >
                {t === "one" ? "В одну сторону" : "Туда-обратно"}
              </button>
            ))}
          </div>

          <div className="grid grid-cols-[1fr_auto_1fr_160px_160px_auto] gap-3 items-end">
            {/* Origin */}
            <div>
              <label className="block text-xs text-gray-400 uppercase tracking-wider mb-1.5 font-medium">
                Откуда
              </label>
              <input
                value={origin}
                onChange={(e) => setOrigin(e.target.value.toUpperCase())}
                placeholder="ALA"
                maxLength={3}
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm text-center font-medium tracking-widest outline-none focus:border-sky-blue"
              />
            </div>

            {/* Swap */}
            <button
              onClick={swap}
              className="w-8 h-8 rounded-full bg-sky-ice border border-gray-200 flex items-center justify-center text-sky-blue hover:bg-sky-blue hover:text-white transition-colors mb-0.5"
            >
              <ArrowLeftRight className="w-3.5 h-3.5" />
            </button>

            {/* Destination */}
            <div>
              <label className="block text-xs text-gray-400 uppercase tracking-wider mb-1.5 font-medium">
                Куда
              </label>
              <input
                value={dest}
                onChange={(e) => setDest(e.target.value.toUpperCase())}
                placeholder="SVO"
                maxLength={3}
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm text-center font-medium tracking-widest outline-none focus:border-sky-blue"
              />
            </div>

            {/* Date */}
            <div>
              <label className="block text-xs text-gray-400 uppercase tracking-wider mb-1.5 font-medium">
                Дата
              </label>
              <input
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm outline-none focus:border-sky-blue"
              />
            </div>

            {/* Class */}
            <div>
              <label className="block text-xs text-gray-400 uppercase tracking-wider mb-1.5 font-medium">
                Класс
              </label>
              <select
                value={ticketClass}
                onChange={(e) => setTicketClass(e.target.value)}
                className="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm outline-none focus:border-sky-blue bg-white"
              >
                <option value="">Любой</option>
                <option value="Economy">Эконом</option>
                <option value="Comfort">Комфорт</option>
                <option value="Business">Бизнес</option>
                <option value="First">Первый</option>
              </select>
            </div>

            {/* Search btn */}
            <button
              onClick={handleSearch}
              className="flex items-center gap-2 bg-navy text-white px-5 py-2.5 rounded-xl text-sm font-medium hover:bg-sky-blue transition-colors whitespace-nowrap"
            >
              <Search className="w-4 h-4" />
              Найти
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
