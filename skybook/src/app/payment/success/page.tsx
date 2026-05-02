import Link from "next/link";
import { CheckCircle2 } from "lucide-react";

export default function PaymentSuccessPage() {
  return (
    <div className="min-h-[calc(100vh-56px)] flex items-center justify-center">
      <div className="text-center max-w-sm">
        <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-5">
          <CheckCircle2 className="w-8 h-8 text-green-500" />
        </div>
        <h1 className="font-serif text-2xl mb-2">Оплата прошла успешно!</h1>
        <p className="text-gray-400 text-sm mb-7">
          Ваш билет оплачен и забронирован. Проверьте раздел «Мои билеты».
        </p>
        <Link
          href="/tickets"
          className="inline-block px-6 py-2.5 bg-navy text-white rounded-xl text-sm font-medium hover:bg-sky-blue transition-colors"
        >
          Мои билеты
        </Link>
      </div>
    </div>
  );
}
