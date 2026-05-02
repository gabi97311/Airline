import Link from "next/link";
import { XCircle } from "lucide-react";

export default function PaymentCancelPage() {
  return (
    <div className="min-h-[calc(100vh-56px)] flex items-center justify-center">
      <div className="text-center max-w-sm">
        <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-5">
          <XCircle className="w-8 h-8 text-red-400" />
        </div>
        <h1 className="font-serif text-2xl mb-2">Оплата отменена</h1>
        <p className="text-gray-400 text-sm mb-7">
          Вы отменили оплату. Ваш билет временно зарезервирован.
        </p>
        <div className="flex gap-3 justify-center">
          <Link
            href="/"
            className="px-5 py-2.5 border border-gray-200 rounded-xl text-sm font-medium hover:border-gray-300 transition-colors"
          >
            На главную
          </Link>
          <Link
            href="/tickets"
            className="px-5 py-2.5 bg-navy text-white rounded-xl text-sm font-medium hover:bg-sky-blue transition-colors"
          >
            Мои билеты
          </Link>
        </div>
      </div>
    </div>
  );
}
