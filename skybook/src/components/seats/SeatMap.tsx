"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { seatService, ticketService, paymentService } from "@/lib/api";
import type { Seat, SeatClass } from "@/types";
import { useAuth } from "@/lib/auth-context";
import toast from "react-hot-toast";
import clsx from "clsx";

const CLASS_ORDER: SeatClass[] = ["First", "Business", "Comfort", "Economy"];
const CLASS_LABELS: Record<SeatClass, string> = {
  First: "Первый",
  Business: "Бизнес",
  Comfort: "Комфорт",
  Economy: "Эконом",
};
const CLASS_COLORS: Record<SeatClass, string> = {
  First: "bg-amber-50 border-amber-200 text-amber-700 hover:bg-amber-100",
  Business: "bg-purple-50 border-purple-200 text-purple-700 hover:bg-purple-100",
  Comfort: "bg-blue-50 border-blue-200 text-sky-blue hover:bg-blue-100",
  Economy: "bg-white border-gray-200 text-gray-600 hover:bg-gray-50",
};

export function SeatMap({ flightId }: { flightId: number }) {
  const router = useRouter();
  const { isLoggedIn } = useAuth();
  const [seats, setSeats] = useState<Seat[]>([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState<Seat | null>(null);
  const [filterClass, setFilterClass] = useState<SeatClass | "all">("all");
  const [passengerName, setPassengerName] = useState("");
  const [booking, setBooking] = useState(false);

  useEffect(() => {
    seatService
      .list(flightId)
      .then(setSeats)
      .catch(() => toast.error("Не удалось загрузить места"))
      .finally(() => setLoading(false));
  }, [flightId]);

  // Group by class
  const classSections = CLASS_ORDER.map((cls) => ({
    cls,
    seats: seats.filter((s) => s.seat_class === cls),
  })).filter(({ seats }) => seats.length > 0);

  const visibleSeats = filterClass === "all"
    ? seats
    : seats.filter((s) => s.seat_class === filterClass);

  const handleSelect = (seat: Seat) => {
    if (seat.seat_status !== "Free") return;
    setSelected(selected?.seat_id === seat.seat_id ? null : seat);
  };

  const handleBook = async () => {
    if (!selected) return;
    if (!isLoggedIn) {
      toast("Войдите, чтобы забронировать", { icon: "🔒" });
      router.push("/auth");
      return;
    }
    if (!passengerName.trim()) {
      toast.error("Введите имя пассажира");
      return;
    }
    setBooking(true);
    try {
      const ticket = await ticketService.create({
        flight_id: flightId,
        seat_id: selected.seat_id,
        passenger_name: passengerName.trim(),
      });
      toast.success("Билет создан! Переходим к оплате...");
      const checkoutUrl = await paymentService.createCheckout(ticket.ticket_id);
      if (typeof checkoutUrl === "string" && checkoutUrl.startsWith("http")) {
        window.location.href = checkoutUrl;
      } else {
        router.push(`/tickets/${ticket.ticket_id}`);
      }
    } catch (err: any) {
      toast.error(err?.response?.data?.detail ?? "Ошибка бронирования");
    } finally {
      setBooking(false);
    }
  };

  // Build seat grid rows (6 seats per row: ABC + DEF)
  const buildRows = (sectionSeats: Seat[]) => {
    const sorted = [...sectionSeats].sort((a, b) => {
      const rowA = parseInt(a.seat_code), rowB = parseInt(b.seat_code);
      if (rowA !== rowB) return rowA - rowB;
      return a.seat_code.localeCompare(b.seat_code);
    });

    const rows: Map<number, Seat[]> = new Map();
    sorted.forEach((s) => {
      const rowNum = parseInt(s.seat_code);
      if (!rows.has(rowNum)) rows.set(rowNum, []);
      rows.get(rowNum)!.push(s);
    });
    return Array.from(rows.entries());
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-20 text-gray-400">
        <div className="animate-spin w-8 h-8 border-2 border-sky-blue border-t-transparent rounded-full" />
      </div>
    );
  }

  return (
    <div className="grid grid-cols-[1fr_280px] gap-6 items-start">
      {/* Left: seat map */}
      <div>
        {/* Class filter */}
        <div className="flex gap-2 flex-wrap mb-5">
          <button
            onClick={() => setFilterClass("all")}
            className={clsx(
              "px-3 py-1.5 rounded-full text-xs border transition-colors",
              filterClass === "all" ? "bg-navy text-white border-navy" : "bg-white text-gray-500 border-gray-200 hover:border-gray-300"
            )}
          >
            Все места
          </button>
          {CLASS_ORDER.map((cls) => {
            const section = classSections.find((s) => s.cls === cls);
            if (!section) return null;
            const minPrice = Math.min(...section.seats.map((s) => s.price));
            return (
              <button
                key={cls}
                onClick={() => setFilterClass(cls)}
                className={clsx(
                  "px-3 py-1.5 rounded-full text-xs border transition-colors",
                  filterClass === cls ? "bg-navy text-white border-navy" : "bg-white text-gray-500 border-gray-200 hover:border-gray-300"
                )}
              >
                {CLASS_LABELS[cls]} — ${minPrice.toFixed(0)}
              </button>
            );
          })}
        </div>

        {/* Plane + seats */}
        <div className="bg-white border border-gray-200 rounded-2xl p-5">
          {/* Nose */}
          <div className="flex justify-center mb-3">
            <div className="w-16 h-6 bg-gray-100 border border-gray-200 rounded-t-full" />
          </div>

          {/* Letter header */}
          <div className="flex items-center gap-1 justify-center mb-2">
            <div className="w-6" />
            {["A", "B", "C", "", "D", "E", "F"].map((l, i) => (
              <div
                key={i}
                className={clsx(
                  "text-center text-xs text-gray-400 font-medium",
                  l === "" ? "w-5" : "w-8"
                )}
              >
                {l}
              </div>
            ))}
          </div>

          {/* Sections */}
          {classSections.map(({ cls, seats: sectionSeats }) => {
            if (filterClass !== "all" && filterClass !== cls) return null;
            const rows = buildRows(sectionSeats);
            return (
              <div key={cls} className="mb-4">
                {/* Class divider */}
                <div className="flex items-center gap-3 my-2">
                  <div className="flex-1 h-px bg-gray-100" />
                  <span className="text-xs text-gray-400 uppercase tracking-wider font-medium">
                    {CLASS_LABELS[cls]}
                  </span>
                  <div className="flex-1 h-px bg-gray-100" />
                </div>

                {rows.map(([rowNum, rowSeats]) => (
                  <div key={rowNum} className="flex items-center gap-1 justify-center mb-1">
                    <div className="w-6 text-center text-xs text-gray-300 font-medium">{rowNum}</div>
                    {["A", "B", "C"].map((l) => {
                      const seat = rowSeats.find((s) => s.seat_code === `${rowNum}${l}`);
                      return (
                        <SeatButton
                          key={l}
                          seat={seat}
                          cls={cls}
                          isSelected={selected?.seat_id === seat?.seat_id}
                          onSelect={handleSelect}
                        />
                      );
                    })}
                    <div className="w-5" />
                    {["D", "E", "F"].map((l) => {
                      const seat = rowSeats.find((s) => s.seat_code === `${rowNum}${l}`);
                      return (
                        <SeatButton
                          key={l}
                          seat={seat}
                          cls={cls}
                          isSelected={selected?.seat_id === seat?.seat_id}
                          onSelect={handleSelect}
                        />
                      );
                    })}
                  </div>
                ))}
              </div>
            );
          })}

          {/* Tail */}
          <div className="flex justify-center mt-3">
            <div className="w-16 h-4 bg-gray-100 border border-gray-200 rounded-b-xl" />
          </div>
        </div>

        {/* Legend */}
        <div className="flex gap-4 mt-3 justify-center">
          {[
            { label: "Свободно", cls: "bg-white border-gray-200" },
            { label: "Занято", cls: "bg-gray-100 border-gray-200" },
            { label: "Выбрано", cls: "bg-sky-blue border-sky-blue" },
            { label: "Первый", cls: "bg-amber-50 border-amber-200" },
          ].map(({ label, cls }) => (
            <div key={label} className="flex items-center gap-1.5">
              <div className={`w-4 h-4 rounded border ${cls}`} />
              <span className="text-xs text-gray-400">{label}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Right: booking panel */}
      <div className="sticky top-20">
        <div className="bg-white border border-gray-200 rounded-xl p-5">
          <h3 className="font-serif text-lg mb-4">Детали заказа</h3>

          {selected ? (
            <div className="space-y-3 mb-5">
              <InfoRow label="Место" value={selected.seat_code} />
              <InfoRow label="Класс" value={CLASS_LABELS[selected.seat_class]} />
              <InfoRow label="Цена" value={`$${selected.price.toFixed(2)}`} highlight />
            </div>
          ) : (
            <p className="text-sm text-gray-400 mb-5 text-center py-4">
              Выберите место на схеме
            </p>
          )}

          {selected && (
            <div className="mb-4">
              <label className="block text-xs text-gray-400 uppercase tracking-wider mb-1.5 font-medium">
                Имя пассажира
              </label>
              <input
                value={passengerName}
                onChange={(e) => setPassengerName(e.target.value)}
                placeholder="Иван Иванов"
                className="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm outline-none focus:border-sky-blue"
              />
            </div>
          )}

          <button
            onClick={handleBook}
            disabled={!selected || booking}
            className={clsx(
              "w-full py-3 rounded-xl text-sm font-medium transition-colors",
              selected
                ? "bg-navy text-white hover:bg-sky-blue"
                : "bg-gray-100 text-gray-300 cursor-not-allowed"
            )}
          >
            {booking ? "Бронирование..." : "Перейти к оплате →"}
          </button>

          {!isLoggedIn && selected && (
            <p className="text-xs text-gray-400 text-center mt-2">
              Необходима авторизация
            </p>
          )}
        </div>
      </div>
    </div>
  );
}

function SeatButton({
  seat,
  cls,
  isSelected,
  onSelect,
}: {
  seat?: Seat;
  cls: SeatClass;
  isSelected: boolean;
  onSelect: (s: Seat) => void;
}) {
  if (!seat) return <div className="w-8 h-8" />;

  const isFree = seat.seat_status === "Free";
  const isOcc = seat.seat_status === "Occupied" || seat.seat_status === "Pending";

  const baseClass = "w-8 h-8 rounded-t-lg rounded-b border text-xs font-medium flex items-center justify-center transition-all";

  let colorClass = "";
  if (isSelected) colorClass = "bg-sky-blue border-sky-blue text-white";
  else if (isOcc) colorClass = "bg-gray-100 border-gray-200 text-gray-300 cursor-not-allowed";
  else colorClass = CLASS_COLORS[cls] + " cursor-pointer";

  return (
    <button
      className={`${baseClass} ${colorClass}`}
      onClick={() => isFree && onSelect(seat)}
      title={`${seat.seat_code} · ${CLASS_LABELS[cls]} · $${seat.price}`}
      disabled={!isFree}
    >
      {seat.seat_code.replace(/^\d+/, "")}
    </button>
  );
}

function InfoRow({ label, value, highlight }: { label: string; value: string; highlight?: boolean }) {
  return (
    <div className="flex justify-between items-center text-sm border-b border-gray-50 pb-2">
      <span className="text-gray-400">{label}</span>
      <span className={highlight ? "font-semibold text-navy" : "font-medium"}>{value}</span>
    </div>
  );
}
